---
title: "Expression Aliases"
document: P2826R4
date: 2026-06-08
audience: EWG
reply-to:
  - "Gašper Ažman <gasper.azman@gmail.com>"
---


## 1 Introduction

This paper introduces a way to rewrite a function call to a different expression without a forwarding layer.

Example:

```cpp
int g(int) { return 42; }
int f(long) { return 43; }

using g(unsigned x) = (f(x)); // handle unsigned int with f(long)

int main() {
    g(1); // 42
    g(1u); // 43
}
```

One might think that declaring

```cpp
int g(unsigned x) { return f(x); }
```

is equivalent; this is far from the case in general, which is exactly why we need this capability. See the motivation section for the full list of issues this capability solves.


## 2 Status

Currently in EWG.


## 3 Proposal

We propose a new kind of entity, called an **expression alias**, of the form:

*alias-declaration*: `using` *declarator* `=` `(` *expression* `)` `;`

The *declarator* must be a function declarator. The parameters of the function declarator are in scope within the *expression*.

We call the expression evaluated the **target expression*.

Such a definition has to be the first declaration of the declarator.

A call expression that resolves to an expression alias instead resolves to the evaluation of the target expression. The parameter names in the target expression refer directly to the expressions bound as arguments, without any interceding conversions that might have been synthesized in order to perform overload resolution.

This is a **hygienic** substitution: even if a parameter name is used multiple times in the target expression (e.g., `using f(Widget w) = g(w, w)`), the argument expression is only evaluated once, retaining its value category. Multiple uses of a parameter behave identically to multiple uses of a named variable, and standard diagnostics (like use-after-move) apply.

**Notes:**

- **Lookup:** Expression aliases participate in overload resolution the standard way. No new lookup rules are introduced.
- **Linkage:** Expression aliases have **no linkage** (they don’t survive past the frontend).
- **AST Transformation:** The model is an AST transformation performed after selection.
- **SFINAE behavior:** The alias must first “win” overload resolution based on its signature and any `requires` clauses. Once selected, the substituted target expression is SFINAE-able at the call site. If substitution fails in a SFINAE-able context (like a concept), it yields a SFINAE failure rather than a hard error. To conditionally disable an alias from its own overload set, use a `requires` clause.
- **Lifetime:** Temporaries created within the target expression have their lifetime extended to the end of the full-expression containing the alias call.
- **Recursion:** Direct recursion is generally not supported, as eager AST substitution must terminate. A recursive definition would typically lead to an infinite substitution loop during compilation. However, recursion is possible if the recursive call is guarded by a compile-time evaluated branch, such as an `if consteval` or `if constexpr` statement, that guarantees the substitution will terminate.

### 3.1 Access Control

Expression aliases respect access control. If an expression alias is a friend or member of a class, the target expression is evaluated with those access rights, allowing it to call private functions or access private data members.

### 3.2 Examples

#### 3.2.1 Example 1: simple free function aliases

We could implement overload sets from the C library without indirection:

```cpp
// <cmath>
using exp(float x)       = (::expf(x)); // no duplication 
double exp(double)      { /* normal definition */ }
using exp(long double x) = (::expl(x)); // no duplication
```

This capability would make wrapping C APIs much easier, since we could just make overload sets out of individually-named functions.

#### 3.2.2 Example 2: simple member function aliases

```cpp
template <typename T>
struct Container {
  auto cbegin() const -> const_iterator;
  auto begin() -> iterator;
  using begin() const = (cbegin()); // saves on template instantiations
};
```

#### 3.2.3 Example 3: avoiding template bloat

`fmt::format` goes through great lengths to validate format string compatibility at compile time, but *really* does not want to generate code for every different kind of string.

This is extremely simple to do with this extension - just funnel all instantiations to a `string_view` overload.

```cpp
template <typename FmtString, typename... Args>
using format(std::format_string<Args...> fmt, Args const&... args) 
    = (vformat(std::string_view(fmt), std::make_format_args(args...)));
```

Contrast with the best we can realistically do presently:

```cpp
template <typename FmtString, typename... Args>
auto format(format_string<Args...> fmt, Args const&... args) -> std::string {
    return vformat(fmt.get(), std::make_format_args(args...));
}
```

The second example results in a separate function for each format string (which is, say, one per log statement). The expression alias provably never instantiates different function bodies for different format strings.

#### 3.2.4 Example 4: deduce-to-baseclass

Imagine we inherited from `std::optional`, and we wanted to forward `operator*`, but have it be treated the same as `value()`. This becomes trivial:

```cpp
template <typename T>
struct my_optional : std::optional<T> {
    using operator*(this auto&& self)
      = (*static_cast<copy_cvref_t<decltype(self), std::optional<T>>>(self));
};
```

#### 3.2.5 Example 5: immovable argument types

Consider having an argument type that must be in-place constructed:

```cpp
#include <type_traits>
#include <utility>

template <typename T>
struct pin {
    T value;

    pin(auto&&... vs) 
        requires(requires { T(std::forward<decltype(vs)>(vs)...); })
        : value(std::forward<decltype(vs)>(vs)...) {}
    pin(pin&&) = delete;
};

template <typename T>
void takes_pinned(pin<T> x) {}

template <typename T>
void takes_pinned_adapter(pin<T> x) { // oops
    takes_pinned(std::forward<decltype(x)>(x));
}

template <typename T>
using takes_pinned_alias(T&& x) = (takes_pinned<std::decay_t<T>>(std::forward<T>(x)));

int main() {
    takes_pinned<int>(3); // (A) OK; what we have to write
    takes_pinned(3);      // Error, but what we want to write
    takes_pinned(pin<int>{3}); // OK, but verbose
    takes_pinned_adapter(pin<int>{3}); // Error, can't forward pin<T>
    takes_pinned_alias(3); // OK with this paper, same as (A)
}
```

#### 3.2.6 Example 6: Customization Point Objects (CPOs)

Expression Aliases make CPOs behave seamlessly without overhead. For example, `std::ranges::begin` could simply be an alias:

```cpp
namespace __adl_protected {
  template <typename T>
  concept adl_test_begin = requires (T t) { begin(t); };
  template <typename T>
  using adl_begin(T&& t) = (begin(t));
}
namespace std::ranges {
struct begin_t {
  // objects that support x.begin(); omitting the "and that's an iterator" clause
  template <typename T>
  using operator()(this begin_t, T&& t) const
    requires /* requires clause for "any one of the rules work" */
    // using [P2806R3]; do-expressions
    = do {
      if constexpr(enable_borrowed_range<remove_cv_t<T>>) {
        // If E is an rvalue and enable_borrowed_range<remove_cv_t<T>>
        // is false, ranges::begin(E) is ill-formed.
        static_assert(false, "T does not enable borrowing");
      } else if constexpr (is_array_v<remove_cv_t<T>>) {
        if constexpr(__is_complete(remove_all_extents<remove_cv_t<T>)) {
          // Otherwise, if T is an array type (9.3.4.5) and remove_all_extents_t<T> is an incomplete type,
          // ranges::begin(E) is ill-formed with no diagnostic required.
          static_assert(false, "Can't begin() over arrays of incomplete types");
        } else {
          // Otherwise, if T is an array type, ranges::begin(E) is expression-equivalent to t + 0
          do_return t + 0;
        }
      } else if constexpr(requires { t.begin(); } &&
                          requires { input_or_output_iterator<decltype(t.begin())>}) {
        //Otherwise, if auto(t.begin()) is a valid expression whose type models
        // input_or_output_iterator, ranges::begin(E) is expression-equivalent to auto(t.begin())
        do_return auto(t.begin());
      } else if constexpr(requires { __adl_protected::adl_begin(t); } &&
                          requires { input_or_output_iterator<decltype(__adl_protected::adl_begin(t))>}) {
        //Otherwise, if T is a class or enumeration type and auto(begin(t)) is a valid expression whose type
        // models input_or_output_iterator where the meaning of begin is established as-if by performing
        // argument-dependent lookup only (6.5.4), then ranges::begin(E) is expression-equivalent to that
        // expression.
        do_return auto(__adl_protected::adl_begin(t));
      } else {
        // Otherwise, ranges::begin(E) is ill-formed.
        static_assert(false, "Can't begin()");
      }
    };
};
inline constexpr begin = begin_t{};
} // end namespace
```

#### 3.2.7 Example 8: Literal checking on strings

By using a `requires` clause with built-ins like `__builtin_constant_p`, we can detect if an argument is a constant expression and allow the alias to be selected only in those cases.

```cpp
struct cstring_view {
  // ..
  template <size_t N> 
  using cstring_view(const char (&in)[N]) requires (__builtin_constant_p(in)) 
      = (cstring_view(in, N - 1));
  // ...
};
```

#### 3.2.8 Example 9: Constant evaluation verification constraint

Similarly, we can constrain an alias to only match constant expressions by using a `requires` clause. This allows the alias to drop out of overload resolution if the expression is not a constant, rather than resulting in a hard error after being selected.

```cpp
template <auto V> constexpr auto constant = V;
using as_constant(auto X) requires requires { constant<X>; } = (constant<X>);
```

#### 3.2.9 Example 10: Trivial Library Extensions for Safety

The standard library replaced `operator>>(istream&, char*)` with `operator>>(istream&, char(&)[N])` for obvious safety reasons. Adding support for `std::array` or `std::span` to benefit from the same safety would be trivial and avoid new instantiations of the actual I/O logic.

For instance, we can forward `std::array` directly to the safe C-array overload by aliasing the underlying array member:

```cpp
namespace std {
  template <class charT, class traits, size_t N>
  using operator>>(basic_istream<charT, traits>& is, array<charT, N>& arr) 
      = (is >> arr._M_elems); // dispatches directly to the safe C-array overload
}
```

Alternatively, we can use an alias to transparently bridge contiguous containers to a `std::span` implementation. If we define the actual I/O logic for a span of a specific size, an alias can perform the conversion without introducing an intermediate function frame. The key benefit here is that `std::span`’s constructor deduces the `N` parameter from the container, naturally and efficiently routing the call to the correctly-sized template overload:

```cpp
// 1. The actual implementation:
template <size_t N> 
std::istream& operator>>(std::istream& is, std::span<char, N> spn) { /* ... */ }

// 2. An alias that accepts containers (like std::array) and forwards to the span overload:
using operator>>(std::istream& is, auto&& range) 
    requires requires { std::span(std::forward<decltype(range)>(range)); } 
    = (is >> std::span(std::forward<decltype(range)>(range)));

void test() {
    std::array<char, 42> buffer;
    std::cin >> buffer; // Picks the alias, converts to span, and invokes (1)
}
```

#### 3.2.10 Example 11: String-like Types and `string_view`

A similar situation arises with all string-like types and `std::basic_string_view`. The standard library implements `operator<<` for `std::basic_string_view` by deducing `CharT` and `Traits`.

Currently, if you implement a custom string type (such as a compile-time `fixed_string`), you often must write a wrapper `operator<<` that explicitly converts your type to `std::string_view` and then delegates the call to avoid ambiguity or missing overloads. Expression aliases eliminate this boilerplate:

```cpp
template <class CharT, size_t N>
struct fixed_string {
    /* ... */
    constexpr operator std::basic_string_view<CharT>() const;
};

// A single expression alias transparently bridges any string-like type 
// to the basic_string_view implementation:
using operator<<(std::ostream& os, auto const& str) 
    requires requires { std::basic_string_view(str); }
    = (os << std::basic_string_view(str));
```


## 4 Why this syntax

- The `using` syntax aligns with type aliases.
- The function declarator naturally introduces names for bound expressions and their substitution.
- It seamlessly represents the pure forwarding nature without instantiating extra template scopes.


## 5 Nice-to-have properties

- **Copy Elision & Programmable Dispatch**: Enables programmable dispatch without actual argument binding, allowing the compiler to cleanly preserve copy elision (conversions are thrown away and recalculated within the expression)
- **Removal of library-defined dispatch from callstacks**: the library defines many customization point objects as “expression-equivalent to *list-of-cases*”. This feature should be able to make all of them truly act that way.
- **Optimizers have to work way less hard**: the extra inline-ing contexts are hard on optimizers; inlining depth is a valuable resource, and the intermediate symbols still get emitted, optimized, and then sometimes garbage-collected.
- **Major debug symbol reduction**: expression aliases don’t need cross-TU mangling and have no linkage.
- **No extra work for overload resolution** - this feature interacts as-if it were a normal function for the purposes of overload resolution. No new rules required.


## 6 Related Work

Roughly related were Parametric Expressions [P1221R1], but they didn’t interact with overload sets very well.

This paper is strictly orthogonal, as it doesn’t give you a way to rewire the arguments at the language level in a new way, just substitute the expression that’s actually invoked.

#### 6.0.1 Example 12: deduce-to-type (Deducing This)

The problem of template-bloat when all we wanted to do was deduce the type qualifiers gets much worse with the introduction of (Deducing This) [P0847R7] into the language.

This topic is explored in Barry Revzin’s [P2481R1].

Observe how easy it is to forward with an explicit-object member function using expression aliases:

```cpp
struct C {
  void f(this std::same_as<C> auto&& x) {} // implementation
  template <typename T>
  using f(this T&& x) = (static_cast<copy_cvref_t<T, C>&&>(x).f());
};
struct D : C {};

void use_member() {
  D d;
  d.f();                // OK, calls C::f(C&)
  std::move(d).f();     // OK, calls C::f(C&&)
  std::as_const(d).f(); // OK, calls C::f(C const&)
}
```

##### 6.0.1.1 Don’t lambdas make this shorter?

While one could use an inline lambda, lambdas still depend on `T`, since one can use it in the lambda body, leading to more instantiations. Expression aliases sidestep this by just rewriting the call.

#### 6.0.2 Example 13: The “Rename Overload Set” / “Rename Function” refactoring

In C++, “rename function” or “rename overload set” are not refactorings that are physically possible for large codebases without at least temporarily risking overload resolution breakage.

However, with this paper, one can disentangle overload sets by leaving removed overloads where they are, and redirecting them to the new implementations, until they are ready to be removed.

(*Reminder:* conversions to reference can lose fidelity, so trampolines in general do not work).

One can also just define

```cpp
using new_name(auto&&...args) 
    requires requires { old_name(std::forward<decltype(args)>(args)...); }
    = (old_name(std::forward<decltype(args)>(args)...));
```

and have a new name for an old overload set. This refactoring also becomes ABI stable, as we basically gain true function aliases.

#### 6.0.3 Example 14: Emulating Language Rewrites

The SFINAE-at-call-site model allows us to express existing language rewrites as expression aliases. For example, the rewrite of `a < b` to `(a <=> b) < 0` can be expressed as:

```cpp
template <typename T>
auto operator<(T const& a, T const& b) = ((a <=> b) < 0);
```

While this alias will be selected if it wins overload resolution based on its signature, the resulting substitution is SFINAE-able. This means that a concept checking for the existence of `operator<` will correctly return `false` if `(a <=> b) < 0` is ill-formed, rather than resulting in a hard error. If one desires the alias to drop out of its own selection process (for example, to allow a different overload to be picked), a `requires` clause on the declaration is still necessary.

#### 6.0.4 Example 15: Recursion via `if consteval`

While direct recursion leads to infinite expansion, we can use `if consteval` (or `if constexpr`) to terminate the substitution in contexts where the compiler can statically determine the branch.

```cpp
using fact(int n) = (n <= 1 ? 1 : n * fact(n - 1)); // Error: infinite expansion

// But with a compile-time guard (requires [P2806R3] do-expressions):
using fact(int n) = do {
    if consteval {
        if (n <= 1) do_return 1;
        do_return n * fact(n - 1);
    } else {
        do_return runtime_fact(n);
    }
};
```


## 7 Future Directions

The following features are NOT part of the current proposal P2826R3, but represent potential future extensions or related work being explored in other papers.

### 7.1 Constant Evaluation Check

We are considering the possibility of allowing `consteval` or `constexpr` on parameters (e.g., `using fn(consteval int a) = (expr);`). This would act as a requirement that any expression bound to such a parameter must be a constant expression.

This is distinct from “constexpr parameters” as proposed in [P1045R1] (and reated [P3334R0]) which imply a template-like behavior or constant-template-parameter-equivalent. For expression aliases, it is simply a constraint on the argument expression itself. This capability is particularly useful for enabling overload resolution based on whether an argument is a constant, which is a key requirement for libraries like `ctre` to provide a seamless interface.

Example:

```cpp
// A ctre match that requires a compile-time pattern
using match(consteval std::string_view pattern, auto&& text)  // instead of requires __builtin_constant_p(pattern)
    = (ctre::match<pattern>(text));
```


## 8 FAQ

### 8.1 What if the chosen expression alias has a failing requires clause or the target expression is ill-formed?

If a `requires` clause on the declaration fails, the alias drops out of overload resolution gracefully. If it wins overload resolution but the substituted target expression is ill-formed, it results in a SFINAE failure if the call is in a SFINAE context (like a `requires` clause or `decltype`), or a hard error otherwise. This follows the “SFINAE-at-call-site” model where the validity of the resulting expression determines the outcome.


## 9 Acknowledgements

- Hana Dusíková for implementing the paper and many discussions, comments, and collaboration.
- Barry Revzin for his comments and work on reflection and code injection.
- Daveed Vandevoorde for lots of early guidance.
- Oliver Rosten and Andrei Zissu for their feedback on the draft.
- Tomasz Kamiński for his feedback on SFINAE and the rewrite model.
- Lénárd Szolnoki for his feedback on value categories, lifetimes, and recursion.


## 10 References

[P0847R7] Deducing this.

https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p0847r7.html

[P1045R1] David Stone. 2019-09-27. constexpr Function Parameters.

https://wg21.link/p1045r1

[P1221R1] Parametric Expressions.

https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1221r1.html

[P2481R1] Forwarding reference to specific type/template.

https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2481r1.html

[P3334R0] Coral Kashri, Andrei Zissu, Tal Yaakovi, Inbal Levi.
2024-10-15. Cross Static Variables.

https://wg21.link/p3334r0
