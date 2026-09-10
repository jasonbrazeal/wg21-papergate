---
title: "Type-aware allocation and deallocation functions"
document: P2719R7
date: 2026-07-15
audience: CWG
reply-to:
  - "Louis Dionne <ldionne@apple.com>"
  - "Oliver Hunt <oliver@apple.com>"
  - "Vlad Serebrennikov <serebrennikov.vladislav@gmail.com>"
---

## 1 Introduction

C++ currently provides two ways of customizing the creation of objects in new expressions. First, `operator new` can be provided as a static member function of a class, like `void* T::operator new`. If such a declaration is provided, an expression like `new T(...)` will use that allocation function. Otherwise, the global version of `operator new` can be replaced by users in a type-agnostic way, by implementing `void* operator new(size_t)` and its variants. A similar mechanism exists for *delete-expressions*.

This paper proposes an extension to *new-expressions* and *delete-expressions* to provide the concrete type being [de]allocated to the allocation functions. This is achieved via the use of an additional `std::type_identity<T>` tag argument that allows the provision of the concrete type to `operator new` and `operator delete`. In addition to providing valuable information to the allocator, this allows the creation of type-specific `operator new` and `operator delete` for types that cannot have intrusive class-scoped operators specified.

At a high level, this allows defining allocation and deallocation functions like:

```cpp
void* operator new(std::type_identity<mylib::Foo>, std::size_t n, std::align_val_t align) {
  ...
}
void operator delete(std::type_identity<mylib::Foo>, void* ptr, std::size_t n, std::align_val_t align) {
  ...
}
```

However, it also allows providing these functions for a family of types, which is where this feature becomes interesting:

```cpp
template <class T>
  requires use_special_allocation_scheme<T>
void* operator new(std::type_identity<T>, std::size_t n, std::align_val_t align) { ... }

template <class T>
  requires use_special_allocation_scheme<T>
void operator delete(std::type_identity<T>, void* ptr, std::size_t n, std::align_val_t align) { ... }
```

## 2 Revision history

- R0 (St-Louis): Initial version
- R1 (pre-Wroclaw):
  - Simplified the lookup mechanism by removing the need to perform ADL (based on implementation experience)
  - Allowed `std::type_identity` parameter for in-class `T::operator new` for consistency
  - Made `std::type_identity` as the first parameter
  - Documented design choices and changes based on feedback and implementation experience
- R2 (Wroclaw):
  - Added the initial wording
- R3 (pre-Hagenberg):
  - Added design choices for EWG review:
    - On constant expression evaluation
    - On stripping qualifiers
    - On enforcing matched declaration scopes
  - Mention interactions with coroutines
  - More comprehensive wording
    - Include feature detection macro
    - Better explain the content of the type-identity parameter in `[expr.new]` and `[expr.delete]`
    - Make it explicit that a type aware operator delete cannot be a destroying delete
    - Include language to allow type-aware `operator new` in constant expressions
  - Incorporated wording feedback from Brian, Corentin, and Richard (thanks!)
- R4 (EWG in Hagenberg):
  - Added design choice for EWG review on mandatory implicit parameters
- R5 (post-Hagenberg):
  - Updated wording to reflect EWG guidance:
    - Strip qualifiers from types when constructing type-identity type
    - Treat globally scoped type aware allocation functions as if they were replaceable global allocation functions during consteval
    - Ensure cross scope selection of type aware new/new[] and delete/delete[] is ill formed
    - Make all currently implicit parameters mandatory
  - Updated introduction examples to adopt correct signature following Hagenberg
  - Updated overload resolutions examples in [[expr.new]](https://wg21.link/expr.new)
    - Existing examples were updated to include the type aware operator
    - Added new examples to show behavior of placement parameters of type `std::align_val_t`
  - Updated wording changes to use `std::type_identity<U>` rather than `std::type_identity<T>` as that has caused repeated confusion with `std::type_identity_t<>` during discussions
  - Updated examples to reflect wording changes
- R6 (EWG and CWG Brno26):
  - Vlad Serebrennikov joins as a co-author.
  - Relax the requirements of class scope new and delete.
  - Proposed wording has been largely re-written to be clearer, unambiguous, and correct with respect to standard terminology and wording requirements. Minor additional editorial changes:
    - Merged with changes in base wording from P3769, and general terminology from C++26.
    - Ensured sufficient context around changes to make it possible to understand the diffs.
  - Update the proposal language itself to reflect the outcome of prior meetings and EWG polls.
  - Added design choice note on effect of type-aware placement delete in delete expression
- R7 (post-Brno26):
  - Address CWG feedback.
    - The biggest change is that overload resolution-y parts of [[expr.new]](https://wg21.link/expr.new) and [[expr.delete]](https://wg21.link/expr.delete) were moved to new subclauses [[over.match.new]](https://wg21.link/over.match.new) and [[over.match.delete]](https://wg21.link/over.match.delete).
  - Rebase on top of the papers voted into the draft during 2026 Brno meeting.
  - The wording was made clearer on accessibility checks for deallocation functions.

## 3 Motivation

Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function. However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated. This results in developers various creative (often macro-based) mechanisms to define these allocation functions manually, or circumventing the language-provided allocation mechanisms entirely in order to track the allocated types.

However, in addition to these intrusive mechanisms being cumbersome and error-prone, they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.

Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism and running into problems because they really only intended for their custom `operator new` to be used within their own code, not by all the code in their process. For example, we’ve seen scenarios where multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time – not very user friendly. By providing the concrete type information to allocators at compile time, it becomes possible for users to override `operator new` for a family of types that they control without overriding it for the whole process, which is what they *actually* want.

### 3.1 A concrete use case

A few years ago, Apple published [a blog post](https://security.apple.com/blog/towards-the-next-generation-of-xnu-memory-safety) explaining a technique used inside its kernel (XNU) to mitigate various exploits. At its core, the technique roughly consists in allocating objects of each type in a different bucket. By collocating all objects of the same type into the same region of memory, it becomes much harder for an attacker to exploit a type confusion vulnerability. Since its introduction in the kernel, this technique alone has been by far the most effective at mitigating type confusion vulnerabilities.

In a world where security is increasingly important, it may make sense for some code bases to adopt mitigation techniques such as this one. However, these techniques require a large-scale and *almost* system-wide customization of how allocation is performed while retaining type information, which is not supported by C++ today. While not sufficient in itself to make C++ safer, the change proposed in this paper is a necessary building block for technology such as the above which can greatly improve the security of C++ applications.

## 4 Current behavior recap

Today, the compiler performs [a lookup](https://timsong-cpp.github.io/cppwp/n4950/expr.new#12) in the allocated type’s class scope (for `T::operator new`), and then a lookup in the global scope (for `::operator new`) if the previous one failed. Once the name lookup has been done and the compiler has decided whether it was looking for `T::operator new` or `::operator new`, name lookup will not be done again even if the steps that follow were to fail. From here on, let’s denote by `NEW` the set of candidates found by the name lookup process.

The compiler then performs [overload resolution](https://timsong-cpp.github.io/cppwp/n4950/expr.new#19) on that set of candidates using the language-specified optional implicit parameters, and if present any developer-provided placement arguments. It does so by assembling an argument list that depends on whether `T` has a new-extended alignment or not. For the sake of simplicity, assume that `T` does not have a new-extended alignment. The compiler starts by performing overload resolution as-if the following expression were used:

```cpp
NEW(sizeof(T), args...)
```

If that succeeds, the compiler selects the overload that won. If it does not, the compiler performs overload resolution again as-if the following expression were used:

```cpp
NEW(sizeof(T), std::align_val_t(alignof(T)), args...)
```

If that succeeds, the compiler selects the overload that won. If it does not, the program is ill-formed. For a type `T` that has new-extended alignment, the order of the two overload resolutions performed above is simply reversed.

Delete-expressions behave similarly, with lookup being performed in the context of the static type of the expression. The overload resolution process then works by preferring a destroying delete, followed by an aligned delete (if the type has new-extended alignment), followed by the usual `operator delete` (with or without a `size_t` parameter depending on whether the considered `operator delete` is a member function or not).

## 5 Proposal

This proposal adds a new implicit tag argument of type `std::type_identity<T>` to `operator new` and `operator delete` that is incorporated into the existing overload resolution logic with a higher priority than existing implicit parameters. To avoid conficts with existing code, this parameter is placed as the first argument to the operator, preceding the size or subject pointer. To avoid the complexities of ADL, this proposal does not change any of the *name lookup* rules associated to *new* and *delete* expressions: it only changes the overload resolution that happens once a name has been found.

For the declaration of a type-aware [de]allocation operator to be valid, we explicitly require that the parameter be a (potentially dependent) specialization of `std::type_identity`, but not a fully dependent type. In other words, the compiler must be able to tell that the first parameter is of the form `std::type_identity<T>` at the time of parsing the declaration, but before the declaration has been instantiated in the case of a template. This is analogous to the current behavior where we require specific concrete types in the parameter list even in dependent contexts.

Once a set of candidate declarations has been found we perform the same prioritized overload resolution steps, only with the addition of `std::type_identity<T>`, with a higher priority than the existing size and alignment parameters. For illustration, here is how overload resolution changes (`NEW` is the set of candidates found by name lookup for `operator new`, and `DELETE` is the equivalent for `operator delete`).

If the user writes `new T(...)`, the compiler checks (in order):

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Before</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">After</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T not overaligned
NEW(sizeof(T))
NEW(sizeof(T), align_val_t{alignof(T)})</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T not overaligned
NEW(type_identity&lt;T&gt;{}, sizeof(T), align_val_t{alignof(T)})
NEW(sizeof(T))
NEW(sizeof(T), align_val_t{alignof(T)})</code></pre></td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T overaligned
NEW(sizeof(T), align_val_t{alignof(T)})
NEW(sizeof(T))</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T overaligned
NEW(type_identity&lt;T&gt;{}, sizeof(T), align_val_t{alignof(T)})
NEW(sizeof(T), align_val_t{alignof(T)})
NEW(sizeof(T))</code></pre></td>
</tr>
</table>

If the user writes `delete ptr`, the compiler checks (in order):

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Before</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">After</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T not overaligned
DELETE(T-or-Base*, destroying_delete_t{}, ...)
DELETE((void*)ptr, sizeof(*ptr))
DELETE((void*)ptr)</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T not overaligned
DELETE(T-or-Base*, destroying_delete_t{}, ...)
DELETE(type_identity&lt;T&gt;{}, (void*)ptr, sizeof(T), align_val_t{alignof(T)})
DELETE((void*)ptr, sizeof(T))
DELETE((void*)ptr)</code></pre></td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T overaligned
DELETE(T-or-Base*, destroying_delete_t{}, ...)
DELETE((void*)ptr, sizeof(T), align_val_t{alignof(T)})
DELETE((void*)ptr, align_val_t{alignof(T)})
DELETE((void*)ptr)</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>// T overaligned
DELETE(T-or-Base*, destroying_delete_t{}, ...)
DELETE(type_identity&lt;T&gt;{}, (void*)ptr, sizeof(T), align_val_t{alignof(T)})
DELETE((void*)ptr, sizeof(T), align_val_t{alignof(T)})
DELETE((void*)ptr, align_val_t{alignof(T)})
DELETE((void*)ptr)</code></pre></td>
</tr>
</table>

If multiple candidates match a given set of parameters, candidate prioritisation and selection is performed according to usual rules for overload resolution.

When a constructor throws an exception, a call to `operator delete` is made to clean up. Overload resolution for this call remains essentially the same, the only difference being that the selected `operator delete` must have the same type-awareness as the preceding `operator new` or the program is considered ill-formed.

For clarity, in types with virtual destructors, `operator delete` is resolved using the destructor’s class as the type being deallocated (this matches the existing semantics of being equivalent to performing `delete this` in the context of the class’s non virtual destructor).

### 5.1 Free function example

```cpp
struct SingleClass { };
struct UnrelatedClass { };
struct BaseClass { };
struct SubClass1 : BaseClass { };
struct SubClass2 : BaseClass { };
struct SubClass3 : BaseClass { };
void* operator new(std::type_identity<SingleClass>, std::size_t, std::align_val_t); // (1)
template <typename T> void* operator new(std::type_identity<T>, std::size_t, std::align_val_t); // (2)

template <std::derived_from<BaseClass> T>
void* operator new(std::type_identity<T>, std::size_t, std::align_val_t); // (3)
void* operator new(std::type_identity<SubClass2>, std::size_t, std::align_val_t); // (4)
void* operator new(std::type_identity<SubClass3>, std::size_t, std::align_val_t) = delete; // (5)

struct SubClass4 : BaseClass {
  void *operator new(size_t); // (6)
};

void f() {
  new SingleClass();     // calls (1)
  new UnrelatedClass();  // calls (2)
  new BaseClass();       // calls (3) with T=BaseClass
  new SubClass1();       // calls (3) with T=SubClass1
  new SubClass2();       // calls (4)
  new SubClass3();       // resolves (5) reports error due to deleted operator
  new SubClass4();       // calls (6) as the class scoped operator wins
  new int();             // calls (2) with T=int
}
```

[*Note:* The above is for illustrative purposes only: it is a bad idea to provide a fully unconstrained type-aware `operator new`. — *end note* ]

### 5.2 In-class example

```cpp
// In-class operator
class SubClass1;
struct BaseClass {
  template <typename T>
  void* operator new(std::type_identity<T>, std::size_t, std::align_val_t); // (1)
  void* operator new(std::type_identity<SubClass1>, std::size_t, std::align_val_t); // (2)
};

struct SubClass1 : BaseClass { };
struct SubClass2 : BaseClass { };
struct SubClass3 : BaseClass {
  void *operator new(std::size_t); // (3)
};
struct SubClass4 : BaseClass {
  template <typename T>
  void *operator new(std::type_identity<T>, std::size_t, std::align_val_t); // (4)
};

void f() {
  new BaseClass;         // calls (1) with T=BaseClass
  new SubClass1();       // calls (2)
  new SubClass2();       // calls (1) with T=SubClass2
  new SubClass3();       // calls (3)
  new SubClass4();       // calls (4) with T=SubClass4
  ::new BaseClass();     // ignores in-class operators and uses appropriate global operator
}
```

### 5.3 Operator suppression example

There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators. Doing so today requires injecting operators into the relevant types, which often results in extensive use of macros. This proposal allows constraint based selection of target types, and as such can be leveraged to specify deleted operators, and so automatically prevent their use e.g.

```cpp
template <typename T> concept SelectionConstraint = ...;
template <SelectionConstraint T> void *operator new(std::type_identity<T>, std::size_t, std::align_val_t) = delete;
[. . .]
template <SelectionConstraint T> void operator delete(std::type_identity<T>, void *, std::size_t, std::align_val_t) = delete;
[. . .]
```

### 5.4 Template type allocation example

The template arguments to a type aware operator new or delete are not required to be directly applied to `std::type_identity`, but are simply available for usual template deduction, so a type aware allocation function can be defined to operate over a template type, e.g.

```cpp
template <typename T, int N>
struct MyArrayType {
  // …
};
template <typename T, int N>
void *operator new(std::type_identity<MyArrayType<T, N>>, size_t, std::align_val_t, ...) {
  // …
}
// …
// calls the above operator new<int, 5>(std::type_identity<MyArrayType<int, 5>>, ...)
auto A = new MyArrayType<int, 5>;
```

### 5.5 Allocation and deallocation function declarations

Like basic allocation and deallocation functions, type-aware functions can only be declared in a class scope or the global scope. One additional constraint that is placed on type-aware declarations is that any scope that contains a type-aware `operator new` or `operator new[]` must also contain a corresponding `operator delete` or `operator delete[]`, and vice versa. It is not required that both be type-aware, but if either is, then both allocation and deallocation functions must belong to the same scope. This reduces the chance of unintentional use of operator `delete` and `new` from mismatching allocation interfaces.

Declarations of type-aware allocation functions require the declarations of both operator `new` and `delete` to include all existing optional allocation function parameters, e.g. a type-aware `operator new` or `new[]` must have at least three parameters: `std::type_identity<U>`, `std::size_t`, and `std::align_val_t`. Similarly, an `operator delete` or `delete[]` has at least four parameters: `std::type_identity<U>`, `void *`, `std::size_t`, and `std::align_val_t`.

Placement parameters are permitted for type-aware allocation functions, and behave identically to those of basic allocation functions with two contained behavioral changes. The first is concerned with how the allocation function is selected for a given new-expression. If the first placement argument is of type `std::align_val_t`, then the implicit alignment argument is suppressed.

The second change removes the leak hazard present in the existing allocation logic. Currently, when a matching deallocation function is selected to release the allocated memory in a case constructor throws an exception, it is not an error to find more than one deallocation function or to find none. In such case no deallocation function is selected, and the memory is leaked. Now, if the object was allocated with a type-aware allocation function, the program is ill-formed if a matching deallocation function cannot be selected.

## 6 Design choices and notes

### 6.1 Design choice: Allowing type aware allocation functions in constant expressions

In the current specification it is not possible for a user to specify a constexpr `operator new` or `operator delete`. Instead, using a *new-expression* or a *delete-expression* in a `constexpr` context requires that the resolved operator be `::operator new` / `::operator delete`, and the compiler elides the call entirely. In particular, if an in-class `T::operator new` is defined and the *new-expression* resolves to it, the *new-expression* is not `constexpr`-friendly. That seems to be an arbitrary limitation.

We clearly don’t want or need such a limitation for typed `operator new`. Our solution to that is to treat a global typed `operator new` (without placement parameters) just like an untyped `::operator new`, i.e. as a *replaceable global allocation function*. While that does mean the compiler will assume the behaviour of typed `operator new`, that seems like a reasonable assumption inside `constexpr`. We apply the same rationale to `operator new[]`, `operator delete`, and `operator delete[]` in order to fully support type aware allocators where existing global allocators are supported.

### 6.2 Design choice: Stripping qualifiers from the type

There is a question as to whether the type-identity should include qualifiers. In previous drafts this was not addressed, and retaining the qualifiers was implied. After consideration we have realised that this would be surprising, is inconsistent with how the type being allocated is presented to the developer throughout the process of allocation and deallocation, and results in the type-identity trivially diverging between such allocation and deallocation e.g.

```cpp
const T *t = new T;
...
delete t;
```

### 6.3 Design choice: Safety restriction on mismatched declaration scopes

There is currently no language mechanism to enforce that `operator new` and `operator delete` are defined as a pair. That is a potential source of confusion and bugs. However, since we are introducing a new form of `operator new` and `operator delete`, we are free to change these rules, and it would be simple to do so. In [[expr.new]](https://wg21.link/expr.new) we suggest adding the follow paragraph to force the selected `operator delete` to be in the same scope as its matching `operator new`. We believe that the vast majority of use cases will already assume that’s the case, and this would only catch a potentially common misuse.

### 6.4 Design choice: All implicit parameters are mandatory

The proposal currently continues to consider optional implicit parameters to be optional. During edge case testing we found that the non-universality of sized deallocation creates a hazard where a less constrained sized deallocation may be selected over a more constrained unsized deallocation function. We believe it is actually reasonable to update the language to make all currently optional implicit parameters mandatory for type aware allocators.

We believe this is a reasonable step to take, as in the future any type-oriented implicit parameters can be based on the `std::type_identity` parameter, which would reduce the exponential increase in new allocation and deallocation APIs.

In addition to resolving the hazard derived from compiler mode flag changes this also simplifies lookup semantics for the operators, and resolves the problem of sized deallocation for exception cleanup in the context of type aware allocation and deallocation (P3492 addresses this problem for environments where type aware allocation may not be an option).

The following wording changes are necessary:

- In [[basic.stc.dynamic.allocation]](https://wg21.link/basic.stc.dynamic.allocation) paragraph 1 and [[basic.stc.dynamic.deallocation]](https://wg21.link/basic.stc.dynamic.deallocation) paragraph 3

  > If a type-identity parameter is provided, the otherwise optional parameters are required to be present and specified with non-dependent types.
- [[expr.new]](https://wg21.link/expr.new) paragraph 29 is modified:

  > 29 <ins>A declaration of a type aware placement deallocation function matches the declaration of a type aware placement deallocation function if the types of the type-identity parameter, and each parameter after the mandatory parameters are the same.</ins> Otherwise, a declaration of a placement deallocation function matches the declaration of a placement allocation function if it has the same number of parameters and, after parameter transformations ([[dcl.fct]](https://wg21.link/dcl.fct)).
  > 
  > …
  > 
  > 30 If a new-expression calls a deallocation function, it passes the value returned from the allocation function call as the argument of type `void*` <ins>as the address parameter</ins>. <ins>If the deallocation operator has a type-identity parameter, the allocation size is passed as the third parameter of type size_t.</ins>…

### 6.5 Design choice: `std::type_identity<T>` vs “raw” template argument

In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism. Instead of using `std::type_identity<T>` as a tag, the compiler would search as per the following expression:

```cpp
operator new<T>(sizeof(T), args...)
```

The only difference here is that we’re passing the type being allocated directly as a template argument instead of using a `std::type_identity<T>` tag parameter. Unfortunately, this has a number of problems, the most significant being that it’s not possible to distinguish the newly-introduced type-aware operator from existing template `operator new` and `operator delete` declarations.

For example, a valid `operator new` declaration today would be:

```cpp
template <class ...Args>
void* operator new(std::size_t, Args...);
```

Hence, an expression like `new (42) int(3)` which would result in a call like `operator new<int>(sizeof(int), 42)` could result in this operator being called with a meaning that isn’t clear – is it a type-aware (placement) operator or a type-unaware placement operator? This also means that existing and legal operators could start being called in code bases that don’t expect it, which is problematic.

Beyond that being confusing for users, this also creates a legitimate problem for the compiler since the resolution of new and delete expressions is based on checking various forms of the operators using different priorities. In order for this to make sense, the compiler has to be able to know exactly what “category” of operator a declaration falls in, so it can perform overload resolution at each priority on the right candidates.

Finally, when a constructor in a *new-expression* throws an exception, an `operator delete` that must be a *usual deallocation function* gets called to clean up. If there is no matching usual deallocation function, no cleanup is performed. Using a template parameter instead of a tag argument could lead to code where no cleanup happened to now find a valid usual deallocation function and perform a cleanup.

Taken together we believe these issues warrant the use of an explicit tag parameter.

### 6.6 Design choice: `std::type_identity<T>` vs `T*`

This proposal uses `std::type_identity<T>` as a tag argument rather than passing a first argument of type `T*`. At first sight, passing `T*` as a first tag argument seems to simplify the proposal and decouple the compiler from the standard library.

However, this approach hides an array of subtle problems that are avoided through the use of `std::type_identity`.

#### 6.6.1 Problems with the value being passed

The first problem is the value being passed as the tag parameter. Given operator signatures of the form

```cpp
template <class T> void *operator new(T*, size_t);
template <class T> void operator delete(T*, void*);
```

Under the hood, the compiler could perform calls like

```cpp
// T* ptr = new T(…)
operator new<T>((T*)nullptr, sizeof(T));

// delete ptr
operator delete<T>((T*)nullptr, ptr);
```

A developer could reasonably be assumed to know that the tag parameter to `operator new` can’t be anything but a null pointer. However, for `operator delete` we can be assured that people will be confused about receiving two pointer parameters, where the explicitly typed parameter is `nullptr`. Also note that we cannot pass the object pointer through that parameter as `operator delete` is called after the object has been destroyed. Passing the memory to be deallocated through a typed pointer is an incitation to use that memory as a `T` object, which would be undefined behavior.

#### 6.6.2 Silent conversions to base types

A scenario we have discussed is developers wishing to provide custom [de]allocation operators for a whole class hierarchy. When using a typed pointer as the tag, this would be written as:

```cpp
struct Base { };
void* operator new(Base*, std::size_t);
void operator delete(Base*, void*);
```

This operator would then also match any derived types of `Base`, which may or may not be intended. If not intended, the conversion from `Derived*` to `Base*` would be entirely silent and may not be noticed. Furthermore, this would basically defeat the purpose of providing type knowledge to the allocator, since only the type of the base class would be known. We believe that the correct way of implementing an operator for a hierarchy is this:

```cpp
struct Base {
  template <class T>
  void* operator new(std::type_identity<T>, std::size_t); // T is the actual type being allocated

  template <class T>
  void operator delete(std::type_identity<T>, void*);
};
```

Or alternatively, in the global namespace:

```cpp
template <std::derived_from<Base> T>
void* operator new(std::type_identity<T>, std::size_t);

template <std::derived_from<Base> T>
void operator delete(std::type_identity<T>, void*);
```

For these reasons, we believe that a tag type like `std::type_identity` is the right design choice.

### 6.7 Design choice: Location of `std::type_identity<T>`

When writing this paper, we went back and forth of the order of arguments. This version of the paper proposes:

```cpp
operator new(std::type_identity<T>, std::size_t, placement-args...)
operator new(std::type_identity<T>, std::size_t, std::align_val_t, placement-args...)

operator delete(std::type_identity<T>, void*)
operator delete(std::type_identity<T>, void*, std::size_t)
operator delete(std::type_identity<T>, void*, std::size_t, std::align_val_t)
```

Another approach would be:

```cpp
operator new(std::size_t, std::type_identity<T>, placement-args...)
operator new(std::size_t, std::align_val_t, std::type_identity<T>, placement-args...)

operator delete(void*, std::type_identity<T>)
operator delete(void*, std::size_t, std::type_identity<T>)
operator delete(void*, std::size_t, std::align_val_t, std::type_identity<T>)
```

The existing specification allows for the existence of template (including variadic template) declarations of operator new and delete, and this functionality is used in existing code bases. This leads to problems compiling real world code where overload resolution will allow selection of a non-SFINAE-safe declaration and subsequently break during compilation.

Placing the tag argument first ensures that no existing operator definition can match, and so we are guaranteed to be free from conflicts.

### 6.8 Design choice: Templated type-aware `operator delete` is a usual deallocation function

Allowing type-aware `operator delete` does require changes to the definition of usual deallocation functions, but the changes are conceptually simple and the cost of not supporting this case is extremely high.

In the current specification, we place very tight requirements on what an `operator delete` declaration can look like in order to be considered a *usual deallocation function*. The reason this definition previously disallowed function templates is that all of the implicit parameters are monomorphic types. That restriction made sense previously.

However, this proposal introduces a new form of the operators for which it is correct (even expected) to be a function template. To that end, we allow a templated `operator delete` to be considered a usual deallocation function, as long as the only dependently-typed parameter is the first `std::type_identity<T>` parameter. To our minds, these semantics match the “intent” of the restrictions already in place for the other implicit parameters like `std::align_val_t`.

The cost of not allowing a templated type-aware `operator delete` as a usual deallocation function is very high, as it functionally prohibits the use of type-aware allocation operators in any environment that requires the ability to clean up after a constructor has thrown an exception.

### 6.9 Design choice: No support for type-aware destroying delete

We have decided not to support type-aware destroying delete as we believe it creates a user hazard. At a technical level there is no additional complexity in supporting type-aware destroying delete, but the resulting semantics seem likely to cause a lot of confusion. For example, given this hypothetical declaration:

```cpp
struct Foo {
  // …
  template <class T>
  void operator delete(std::type_identity<T>, Foo*, std::destroying_delete_t);
};

struct Bar : Foo { };

void f(Foo* foo) {
  delete foo; // calls Foo::operator delete<Foo>
}

void g(Bar *bar) {
  delete bar; // calls Foo::operator delete<Bar>
}
```

To a user this appears to be doing what they expect. However, consider the following:

```cpp
struct Oops : Bar { };

void h(Oops *oops) {
  g(oops); // calls Foo::operator delete<Bar> from within g
}
```

By design, destroying delete does not perform any polymorphic dispatch, and as a result the type being passed to the operator is not be the dynamic type of the object being destroyed, but rather its static type. As a result, basic functionality will appear to work correctly from the user’s point of view when in reality the rules are much subtler than they seem.

Given that the design intent of destroying delete is for users to manage destruction and dispatching manually, we believe that adding type-awareness to destroying delete will add little value while creating the potential for confusion, so we decided not to do it.

### 6.10 Design choice: Dropped support for ADL

The initial proposal allowed the specification of type-aware operators in namespaces that would then be resolved via ADL. Upon further consideration, this introduces a number of challenges that are difficult to resolve robustly. As a result, we have dropped support for namespace-scope operator declarations and removed the use of ADL from the proposal.

The first problem is that ADL would be based on the type of all arguments passed to `operator new`, including placement arguments. While this is not a problem for `operator new` itself, `operator delete` does not get the same placement arguments, which would potentially change the set of associated namespaces used to resolve `new` and `delete`.

One of our original motivations for allowing namespace-scoped operators was to simplify the task of providing operators for a whole library. However, since ADL is so viral, the set of associated namespaces can easily grow unintentionally (e.g. `new lib1::Foo<lib2::Bar>(...)`), which means that developers would have to appropriately constrain their type-aware operators anyway. In other words, we believe that a declaration like this would never have been a good idea in the first place:

```cpp
namespace lib {
  // intent: override for all types in this namespace
  template <class T>
  void* operator new(std::type_identity<T>, std::size_t);
}
```

There are too many ways in which an unconstrained declaration like this can break, including an unexpected set of associated namespaces or even a mere `using namespace lib;`.

Given the need to constrain a type-aware operator anyway, we believe that allowing namespace-scoped operators is merely a nice-to-have but not something that we need fundamentally. Furthermore, adding this capability to the language could always be pursued as a separate proposal since that concern can be tackled orthogonally. For example, a special ADL lookup could be done based solely on the dynamic type being [de]allocated.

Since this adds complexity to the proposal and implementation and doesn’t provide great value, we are not pursuing it as part of this proposal.

### 6.11 Design choice: Supporting manual alignment override

Non-type-aware allocation calls are evaluated by trial overload resolution using the concatenation of a set of implicit arguments with the arguments passed with the placement-new syntax. Developers make use of this to support manually allocating overaligned storage for a non-alignment-extended type, e.g

```cpp
new (std::align_val_t(512)) int; // allocate storage for a single int, aligned to 512 bytes
```

This is a useful and *used* feature, which we have found needs to be supported in practice, but the wording changes post-Hagenberg require this function to be explicitly described rather than as an implicit consequence of the existing trial based `operator new` lookup.

Type-aware allocation function support this use case by discarding the implicit alignment argument if the first placement argument is of type `std::align_val_t` when calling the allocation function.

### 6.12 Design choice: Allow non-type aware `delete` even if type-aware placement delete exists

This proposal initially intended to make deleting an object ill-formed if, when deleting an object of type `U`, there are no usual type-aware deallocation functions with a type-identity parameter of type `std::type_identity<U>`, but there are placement type-aware deallocation functions that *do* have a type-identity parameter of type `std::type_identity<U>`.

> [*Example:* 
> 
> ```cpp
> struct S {
>   S();
>   void *operator new(std::type_identity<S>, size_t, std::align_val_t, placement_t); // #1
>   void operator delete(std::type_identity<S>, void *, size_t, std::align_val_t, placement_t); // #2
>   void operator delete(void *); // #3
> };
> 
> ...
>   S* obj = new (placement{}) S;
>   delete obj;
> ...
> ```
> 
>   — *end example* ]

The new expression resolves `operator new` at #1 to perform the allocation, and resolves the `operator delete` at #2 to clean up if the constructor throws an exception. But when delete is called we produce an error: Both `operator delete` declarations are found, the only candidate that can be used for a delete expression is the non-type aware declaration at line #3, however because we found the placement type-aware `operator delete` and it accepts a type-identity argument of type `std::type_identity<S>`.

The fix for this error is to introduce a usual type-aware deallocator

```cpp
struct S {
  . . .
  void operator delete(std::type_identity<S>, void *, size_t, std::align_val_t);
};
```

The original intention was to reject this as a hazard reduction: preventing errors in which a developer incorrectly specified a type-aware deallocation function, e.g. the *size* and *alignment* parameters of developer specified sized and aligned `operator delete` are frequently reversed.

Following Hagenberg these optional parameters became mandatory for type-aware allocation and deallocation functions, making errors of this kind impossible.

At the same time, relaxing this requirement provides a much more ergonomic path for the common case where object type is not considered important during deallocation, as the non-type aware operator delete is a valid deallocation function for such types. e.g the common case for such a deallocator is simply

```cpp
template <class T> void operator delete(std::type_identity<T>, void *ptr, size_t, std::align_val_t) {
  untyped_free(ptr);
}
```

Lifting this restriction does not remove the requirement that both allocation and deallocation functions are declared in the same scope.

### 6.13 Design clarification: disallow alias templates as wrappers for `std::type_identity`

The proposal disallows the use of a dependent type to reference `std::type_identity`, by design this prevents the use of alias templates, as there is no functional difference between an alias template and any other template for the purpose of declaration site validation. This restriction is consistent with existing specification’s definition for the `size` and `address` parameters, and the return type.

### 6.14 Interactions with `std::allocator<T>`

Today, `std::allocator<T>::allocate` is specified to call `::operator new(std::size_t)` explicitly. Even if `T::operator new` exists, `std::allocator<T>` will not attempt to call it. We view this as a defect in the current standard since `std::allocator<T>` could instead select the same operator that would be called in an expression like `new T(...)` (without the constructor call, obviously).

This doesn’t have an interaction with our proposal, except for making `std::allocator<T>`’s behavior a bit more unfortunate than it already is today. Indeed, users may rightly expect that `std::allocator<T>` will call their type-aware `operator new` when in reality that won’t be the case.

Since this deception already exists for `T::operator new`, we do not attempt to change `std::allocator<T>`’s behavior in this proposal. However, the authors are willing to investigate fixing this issue as a separate proposal, which will certainly present its own set of challenges (e.g. constant evaluation).

### 6.15 ODR implications and mismatched `operator new` / `operator delete`

A concern that was raised in St-Louis was that this proposal would increase the likelihood of ODR violation caused by different declarations of `operator new`/`operator delete` being used in different TUs. For example, one TU would get `lib1::operator new` and another TU would use `lib2::operator delete` due to e.g. a different set of headers being included. Note that the exact same issue also applies to every other operator that is commonly used via ADL (like `operator+`), except that many such ODR violations may end up being more benign than a mismatched `new`/`delete`.

First, we believe that the only way to avoid this issue (in general) is to properly constrain templated declarations, and nothing can prevent users from doing that incorrectly. However, since this proposal has dropped the ADL lookup, declarations of type-aware operators must now be in-class or global. This greatly simplifies the selection of an operator, which should make it harder for users to unexpectedly define an insufficiently constrained operator without immediately getting a compilation error.

Furthermore, without ADL lookup, the ODR implications of this proposal are exactly the same as the existing ODR implications of user-defined placement new operators, which can be templates.

### 6.16 Impact on the library

This proposal does not have any impact on the library, since this only tweaks the search process performed by the compiler when it evaluates a new-expression and a delete-expression. In particular, we do not propose adding new type-aware free function `operator new` variants in the standard library at this time, althought this could be investigated in the future.

### 6.17 Interactions with coroutines

Coroutines currently allow using a custom `operator new` and `operator delete` for allocating the coroutine frame. That is done by looking up in the coroutine’s promise type for `Promise::operator new`. However, there is no mechanism to communicate the type being allocated, since that type is only something known by the compiler (and fairly late during translation). This paper does not propose changing how allocation for coroutine frames is customized. In the future, the coroutine specification could be updated to make the type being allocated more visible and to use a typed allocation function, but there is significant enough design space to avoid doing that here.

## 7 Overview of the wording

The tables below serves as an index of specification for various stages of allocation and deallocation function selection in the following scenarios:

- selection of an allocation function,
- selection of a matching deallocation function for a placement allocation function,
- selection of a matching deallocation function for a non-placement allocation function, and
- selection of a deallocation function (for a delete-expression).

<!-- tomd:lossy-table -->
|  | Allocation | Matching deallocation (placement) | Matching deallocation (placement) |
| --- | --- | --- | --- |
|  | **Allocation** | **Type-unaware** | **Type-aware** |
| Name lookup | [over.match.new]/1 | [expr.new]/30 defers to [over.match.new/1] | [over.match.new]/1 |
| Candidate restrictions | None | [over.match.new]/1 | [over.match.new]/1 |
| Argument list | [over.match.new]/2 | [expr.new]/30 derives from [expr.new]/20 | [over.match.new]/4 derives from [expr.new]/20 |
| Selection | [expr.new]/20 defers to [over.match.new] | [expr.new]/30 | [expr.new]/29a defers to [over.match.new] |
| Selected function restrictions | Overload resolution | [expr.new]/30 | [expr.new]/29a |
| Call arguments | [expr.new]/20 derives from [over.match.new]/2 | [expr.new]/30 | [expr.new]/29a derives from [expr.new]/20 |

<!-- tomd:lossy-table -->
|  | Deallocation | Deallocation | Matching deallocation (non-placement) | Matching deallocation (non-placement) |
| --- | --- | --- | --- | --- |
|  | **Type-unaware** | **Type-aware** | **Type-unaware** | **Type-aware** |
| Name lookup | [over.match.delete]/1 | [over.match.delete]/1 | [over.match.new]/1 ⚠️ | [over.match.new]/1 ⚠️ \| |
| Candidate restrictions | [over.match.delete]/1, [over.match.delete]/3 | [over.match.delete]/1, [over.match.delete]/3 | [over.match.new]/1 ⚠️ [over.match.delete]/3 | [over.match.new]/1 ⚠️ \| [over.match.delete]/3 |
| Argument list | Not needed | [over.match.delete]/4 | Not needed | [over.match.delete]/4 |
| Selection | [expr.delete]/8a can defer to [expr.delete]/9 | [expr.delete]/8a can defer to [expr.delete]/9, which defers to [over.match.delete], which falls back to [expr.delete]/9 | [expr.delete]/8a can defer to [expr.delete]/9 | [expr.delete]/8a can defer to [expr.delete]/9, which defers to [over.match.delete], which falls back to [expr.delete]/9 |
| Selected function restrictions | [expr.delete]/9 | Overload resolution, [expr.delete]/8a, [expr.delete]/9 | [expr.delete]/9 | Overload resolution, [expr.delete]/8a, [expr.delete]/9 |
| Call arguments | [expr.delete]/10b.2 | [expr.delete]/10b.1 defers to [over.match.delete]/4 | [expr.delete]/10b.2 | [expr.delete]/10b.1 defers to [over.match.delete]/4 |

## 8 Proposed wording

Hide removals

Strikethrough

Readers who feel overwhelmed by the variety of scenarios of allocation and deallocation function selection are advised to consult the previous section, which provides a frame of reference.

### 8.1 General [[basic.stc.dynamic.general]](https://wg21.link/basic.stc.dynamic.general)

> 1 Objects can be created dynamically during program execution, using new-expressions ([[expr.new]](https://wg21.link/expr.new)), and destroyed using delete-expressions ([[expr.delete]](https://wg21.link/expr.delete)). <ins>An *allocation operator* is a function or function template named `operator new` or `operator new[]`.</ins> <ins>An *allocation function* is an allocation operator that is not a function template.</ins> <ins>A *deallocation operator* is a function or function template named `operator delete` or `operator delete[]`.</ins> <ins>A *deallocation function* is a deallocation operator that is not a function template.</ins> A C++ implementation provides access to, and management of, dynamic storage via the global <del>*allocation functions* `operator new` and `operator new[]`</del> <ins>allocation</ins> and <del>the global *deallocation functions* `operator delete` and `operator delete[]`</del> <ins>deallocation functions</ins>.
> 
> 2 The library provides default definitions for the global allocation and deallocation functions. Some global allocation and deallocation functions are replaceable ([[dcl.fct.def.replace]](https://wg21.link/dcl.fct.def.replace)). The following allocation and deallocation functions ([[support.dynamic]](https://wg21.link/support.dynamic)) are implicitly declared in global scope in each translation unit of a program.
> 
> [. . .]
> 
> These implicit declarations introduce only the function names `operator new`, `operator new[]`, `operator delete`, and `operator delete[]`.
> 
> > [*Note:* [. . .] — *end note* ]
> 
> Allocation and/or deallocation functions may also be declared and defined for any class ([[class.free]](https://wg21.link/class.free)).
> 
> 2a The first parameter *P* of an allocation or deallocation operator is a *type-identity parameter* if the type *U* of *P* is a specialization of `std::type_identity` ([[meta.trans.other]](https://wg21.link/meta.trans.other)) and, if *U* is dependent, *U* is the same as ([[temp.over.link]](https://wg21.link/temp.over.link)) `std::type_identity<V>` for some (potentially dependent) type *V*. An allocation operator that has a type-identity parameter is a *type-aware allocation operator*. A deallocation operator that has a type-identity parameter is a *type-aware deallocation operator*.
> 
> > [*Example:* 
> > 
> > ```cpp
> > template <typename T>
> > using A = std::type_identity<T>;
> > 
> > template <typename U>
> > void* operator new(A<U>, std::size_t, std::align_val_t);    // not a type-aware allocation operator
> > 
> > template<typename V>
> > struct B {
> >   using C = std::type_identity<T>;
> > };
> > 
> > template <typename W>
> > void* operator new(B<W>::C, std::size_t, std::align_val_t); // not a type-aware allocation operator
> > 
> > template <typename X>
> > class D {
> >   using E = std::type_identity<D>;
> >   void* operator new(E, std::size_t, std::align_val_t);     // a type-aware allocation operator
> > };
> > 
> > template <typename Y>
> > void* D<Y>::operator new(std::type_identity<D<Y>>, std::size_t, std::align_val_t) { return {}; };    // a type-aware allocation operator
> > ```
> > 
> >   — *end example* ]
> 
> 3 If the behavior of an allocation or deallocation function does not satisfy the semantic constraints specified in [[basic.stc.dynamic.allocation]](https://wg21.link/basic.stc.dynamic.allocation) and [[basic.stc.dynamic.deallocation]](https://wg21.link/basic.stc.dynamic.deallocation), the behavior is undefined.

### 8.2 Allocation Functions [[basic.stc.dynamic.allocation]](https://wg21.link/basic.stc.dynamic.allocation)

> 1 An allocation <del>function</del> <ins>operator</ins> that is not a class member <del>function</del> shall belong to the global scope and not have a name with internal linkage.
> 
> 1a The <ins>declared</ins> return type <ins>of an allocation operator *F*</ins> shall be <ins>the same as ([[temp.over.link]](https://wg21.link/temp.over.link))</ins> “pointer to `void`”. <ins>The minimum number of parameters of *F* is determined as follows:</ins>
> 
> - <ins>(1a.1) If *F* is a type-aware allocation operator, then *F* shall have at least three parameters, where the second parameter is termed the size parameter and the third parameter is termed the *alignment parameter*.</ins>
> - <ins>(1a.2) Otherwise, if *F* is a function template, then *F* shall have at least two parameters, where the first parameter is termed the size parameter.</ins>
> - <ins>(1a.3) Otherwise *F* shall be a function that has at least one parameter, where the first parameter is termed the size parameter.</ins>
> 
> <ins>The following restrictions apply to the parameters of *F*:</ins>
> 
> - <ins>(1a.4) The type-identity parameter (if present) shall not have a default argument.</ins>
> - (1a.5) The <del>first</del> <ins>size</ins> parameter shall have type <ins>that is the same as</ins> `std::size_t` ([[support.types]](https://wg21.link/support.types))<del>. The first parameter</del> <ins>and</ins> shall not have a default argument.
> - <ins>(1a.6) The alignment parameter (if present) shall have the type that is the same as `std::align_val_t` ([[support.dynamic]](https://wg21.link/support.dynamic)) and shall not have a default argument.</ins>
> 
> The value of the first parameter is interpreted as the requested size of the allocation. An allocation function can be a function template. Such a template shall declare its return type and first parameter as specified above (that is, template parameter types shall not be used in the return type and first parameter type). Allocation function templates shall have two or more parameters.
> 
> > [*Note:* An allocation operator can have additional parameters that are not specified in this document. — *end note* ]
> 
> 2 An allocation function attempts to allocate the <del>requested</del> amount of storage <ins>specified by the size parameter</ins>. If it is successful, it returns the address of the start of a block of storage whose length in bytes is at least as large as the <del>requested</del> size <ins>specified by the size parameter</ins>. The order, contiguity, and initial value of storage allocated by successive calls to an allocation function are unspecified. Even if the size of the space requested is zero, the request can fail. If the request succeeds, the value returned by a replaceable allocation function is a non-null pointer value ([[basic.compound]](https://wg21.link/basic.compound)) `p0` different from any previously returned value `p1`, unless that value `p1` was subsequently passed to a replaceable deallocation function. Furthermore, for the library allocation functions in [[new.delete.single]](https://wg21.link/new.delete.single) and [[new.delete.array]](https://wg21.link/new.delete.array), `p0` represents the address of a block of storage disjoint from the storage for any other object accessible to the caller. The effect of indirecting through a pointer returned from a request for zero size is undefined.<sup>18</sup>

[ Drafting note: The new wording for the return type of allocation and deallocation operators should resolve [CWG1676](https://cplusplus.github.io/CWG/issues/1676.html) “`auto` return type for allocation and deallocation functions”, as it follows the approach in [CWG1669](https://cplusplus.github.io/CWG/issues/1669.html) “`auto` return type for `main`”. ]

[ Drafting note: (CWG) Is it fine to italicize “alignment parameter” but not “size parameter” and “address parameter” (the latter two are “defined” three times)? ]

### 8.3 Deallocation functions [[basic.stc.dynamic.deallocation]](https://wg21.link/basic.stc.dynamic.deallocation)

> 1 A deallocation <del>function</del> <ins>operator</ins> that is not a class member <del>function</del> shall belong to the global scope and not have a name with internal linkage.

Apply the following changes to paragraph 2 and move it after the existing paragraph 3:

> 2 A <ins>usual</ins> deallocation <del>function</del> <ins>operator</ins> is a *destroying operator delete* if <del>it has at least two parameters</del> <ins>its first parameter is of type “pointer to `C`”, where `C` is a class type,</ins> and its second parameter is of type `std::destroying_delete_t` <ins>([[new.syn]](https://wg21.link/new.syn)); a destroying operator delete shall be a direct member of `C`</ins>. <del>A destroying operator delete shall be a class member function named `operator delete`.</del>
> 
> > [*Note:* Array deletion cannot use a destroying operator delete. — *end note* ]
> 
> > [*Note:* The requirements placed on the parameters of a destroying operator delete prevent it from being a function template or a type-aware deallocation function. — *end note* ]

Insert a new paragraph before the existing paragraph 3 and apply the following changes to the existing paragraph 3:

> 2a The declared return type of a deallocation operator *F* shall be the same as ([[temp.over.link]](https://wg21.link/temp.over.link)) `void`. The following restrictions apply to the parameters of *F*:
> 
> - (2a.1) If *F* is a type-aware deallocation function, then *F* shall have at least four parameters, where
>   - (2a.1.1) the second parameter is termed the address parameter,
>   - (2a.1.2) the third parameter shall have a type that is the same as `std::size_t` ([[support.types]](https://wg21.link/support.types)), and
>   - (2a.1.3) the fourth parameter shall have a type that is the same as `std::align_val_t` ([[support.dynamic]](https://wg21.link/support.dynamic)).
> - (2a.2) Otherwise, if *F* is a function template, then *F* shall have at least two parameters, where the first parameter is termed the address parameter.
> - (2a.3) Otherwise, *F* shall be a function that has at least one parameter, where the first parameter is termed the address parameter.
> 
> The address parameter of a deallocation operator that is not a destroying operator delete (see below) shall have a type that is the same as “pointer to `void`”. A deallocation operator shall not have a potentially throwing exception specification ([[except.spec]](https://wg21.link/except.spec)).
> 
> > [*Note:* A deallocation operator can have additional parameters that are not specified in this document. — *end note* ]
> 
> 3 <del>Each deallocation function shall return `void`.</del> <del>A deallocation function shall not have a potentially throwing exception specification ([[except.spec]](https://wg21.link/except.spec)).</del> <del>If the function is a destroying operator delete declared in class type `C`, the type of its first parameter shall be “pointer to `C`”; otherwise, the type of its first parameter shall be “pointer to `void`”.</del> <del>A deallocation function may have more than one parameter.</del> A *usual deallocation <del>function</del> <ins>operator</ins>* is
> 
> - (3.1) <ins>a type-aware deallocation operator with four parameters or</ins>
> - (3.2) a deallocation function <ins>which is not a function template specialization and</ins> whose parameters after the <del>first</del> <ins>address parameter</ins> are
>   - (3.2.1) optionally, a parameter of type `std::destroying_delete_t`, then
>   - (3.2.2) optionally, a parameter of type `std::size_t`<sup>19</sup>, then
>   - (3.2.3) optionally, a parameter of type `std::align_val_t`.
> 
> <del>A destroying operator delete shall be a usual deallocation function.</del> <del>A deallocation function may be an instance of a function template.</del> <del>Neither the first parameter nor the return type shall depend on a template parameter.</del> <del>A deallocation function template shall have two or more function parameters.</del> <del>A template instance is never a usual deallocation function, regardless of its signature.</del> <ins>A *usual deallocation function* is a usual deallocation operator that is not a function template.</ins>

[ Drafting note: The new wording for the return type of deallocation operators should resolve [CWG3025](https://cplusplus.github.io/CWG/issues/3025.html) “Deallocation functions returning `void`”. ]

[ Drafting note: (CWG) are we fine with “address parameter”, or we want something with the word “storage”? ]

### 8.4 New [[expr.new]](https://wg21.link/expr.new)

> 12 A new-expression may obtain storage for the object by calling an allocation function ([[basic.stc.dynamic.allocation]](https://wg21.link/basic.stc.dynamic.allocation)). If the new-expression terminates by throwing an exception, it may release storage by calling a deallocation function. If the allocated type is a non-array type, the allocation function’s name is `operator new` and the deallocation function’s name is `operator delete`. If the allocated type is an array type, the allocation function’s name is `operator new[]` and the deallocation function’s name is `operator delete[]`.
> 
> > [*Note:* [. . .] — *end note* ]
> 
> 13 <del>If the new-expression does not begin with a unary `::` operator and the allocated type is a class type `T` or array thereof, a search is performed for the allocation function’s name in the scope of `T` ([[class.member.lookup]](https://wg21.link/class.member.lookup)). Otherwise, or if nothing is found, the allocation function’s name is looked up by searching for it in the global scope.</del>
> 
> 14 [. . .]
> 
> 17 When a new-expression calls an allocation function and that allocation has not been extended, the <del>new-expression passes the amount of space requested to the allocation function as the first argument of type `std::size_t`. That argument shall be</del> <ins>*allocation size* is a value</ins> no less than the size of the object being created; it may be greater than the size of the object being created only if the object is an array and the allocation function is not a non-allocating form ([[new.delete.placement]](https://wg21.link/new.delete.placement)). <del>For</del> <ins>When the allocated type is an</ins> array<del>s</del> of `char`, `unsigned char`, <del>and</del> <ins>or</ins> `std::byte`, the difference between the result of the new-expression and the address returned by the allocation function shall be an integral multiple of the strictest fundamental alignment requirement of any object type whose size is no greater than the size of the array being created. <ins>The *allocation alignment* is a value equal to the alignment requirement of the allocated type.</ins>
> 
> > [*Note:* Because allocation functions are assumed to return pointers to storage that is appropriately aligned for objects of any type with fundamental alignment, this constraint on array allocation overhead permits the common idiom of allocating character arrays into which objects of other types will later be placed. — *end note* ]
> 
> 18 When a new-expression calls an allocation function and that allocation has been extended, the <del>size argument to the allocation call shall be</del> <ins>allocation size is a value</ins> no greater than the sum of the sizes for the omitted calls as specified above, plus the size for the extended call had it not been extended, plus any padding necessary to align the allocated objects within the allocated memory. <ins>The allocation alignment is a value equal to the strictest allocation alignment for the omitted calls as specified above.</ins>
> 
> 19 The new-placement syntax is used to supply additional arguments to an allocation function; such an expression is called a *placement new-expression*.
> 
> 20 <del>Overload resolution is performed on a function call created by assembling an argument list. The first argument is the amount of space requested, and has type `std::size_t`. If the type of the allocated object has new-extended alignment, the next argument is the type’s alignment, and has type `std::align_val_t`. If the new-placement syntax is used, the initializer-clauses in its expression-list are the succeeding arguments. If no matching function is found then</del>
> 
> - (20.1) <del>if the allocated object type has new-extended alignment, the alignment argument is removed from the argument list;</del>
> - (20.2) <del>otherwise, an argument that is the type’s alignment and has type `std::align_val_t` is added into the argument list immediately after the first argument;</del>
> 
> <del>and then overload resolution is performed again.</del>
> 
> The allocation function is selected by overload resolution using the argument list termed *K* as specified in [[over.match.new]](https://wg21.link/over.match.new). The selected allocation function is called with arguments in *K*. If there are parameters that do not have a corresponding argument in *K*, their default arguments are used instead. The resulting list of arguments to call the selected allocation function is termed *L*.
> 
> > [*Example:* 
> > 
> > ```cpp
> > struct S1 {
> >   S1() noexcept;
> >   void* operator new(std::type_identity<S1>, std::size_t, std::align_val_t, int = 42);
> >   void operator delete(std::type_identity<S1>, void*, std::size_t, std::align_val_t, int);
> > };
> > 
> > struct S2 {
> >   S2() noexcept;
> >   void* operator new(std::type_identity<S2>, std::size_t, std::align_val_t, int = 42);
> >   void operator delete(std::type_identity<S2>, void*, std::size_t, std::align_val_t);
> > };
> > 
> > void f() {
> >   new S1(); // OK
> >   new S2(); // error: no matching deallocation function
> > }
> > ```
> > 
> >   — *end example* ]
> 
> 21
> 
> > [*Example:* 
> > 
> > - (3.1) `new T` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new(sizeof(T))
> >   operator new(sizeof(T), std::align_val_t(alignof(T)))
> >   ```
> > - (3.2) `new(2,f) T` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new(sizeof(T), 2, f)
> >   operator new(sizeof(T), std::align_val_t(alignof(T)), 2, f)
> >   ```
> > - (3.3) `new T[5]` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new[](sizeof(T) * 5 + x)
> >   operator new[](sizeof(T) * 5 + x, std::align_val_t(alignof(T)))
> >   ```
> > - (3.4) `new(2,f) T[5]` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new[](sizeof(T) * 5 + x, 2, f)
> >   operator new[](sizeof(T) * 5 + x, std::align_val_t(alignof(T)), 2, f)
> >   ```
> > 
> >   — *end example* ]
> 
> 22 [. . .]
> 
> 27 If any part of the object initialization described above<sup>55</sup> terminates by throwing an exception <del>and a suitable deallocation function can be found</del>, the <ins>matching</ins> deallocation function <ins>(if any)</ins> is called to free the memory in which the object was being constructed, <del>after which</del> the exception continues to propagate in the context of the new-expression. If no unambiguous matching deallocation function can be found, propagating the exception does not cause the object’s memory to be freed.
> 
> > [*Note:* This is appropriate when the called allocation function does not allocate memory; otherwise, it is likely to result in a memory leak. — *end note* ]
> 
> 28 <del>If the new-expression does not begin with a unary `::` operator and the allocated type is a class type `T` or an array thereof, a search is performed for the deallocation function’s name in the scope of `T`. Otherwise, or if nothing is found, the deallocation function’s name is looked up by searching for it in the global scope.</del>
> 
> 29 <del>For a non-placement allocation function, the normal deallocation function lookup is used to find the matching deallocation function ([[expr.delete]](https://wg21.link/expr.delete)). For a placement allocation function, the selection process is described below. In any case, the matching deallocation function (if any) shall be non-deleted and accessible from the point where the new-expression appears.</del> <ins>If the selected allocation function is not a placement allocation function, [[expr.delete]](https://wg21.link/expr.delete) specifies how the matching deallocation function is selected and which arguments are used to call it.</ins>
> 
> 29a <ins>Otherwise, if the selected allocation function is type-aware, the matching deallocation function *F* is selected by overload resolution using the argument list termed *M* as specified in [[over.match.new]](https://wg21.link/over.match.new). The parameter-type-list of *F* shall be identical to that of the allocation function, when considering parameters after their respective alignment parameters. *F* is called with arguments in *M*.</ins>
> 
> 30 <del>For a placement allocation function</del> <ins>Otherwise, let</ins>
> 
> - (30.a) <ins>*S* be a set of candidate functions as specified in [[over.match.new]](https://wg21.link/over.match.new), and</ins>
> - (30.b) <ins>*N* be an argument list that is same as *L*, except that the value returned from the call to the selected allocation function is inserted before the first argument.</ins>
> 
> <del>the</del> <ins>The</ins> matching deallocation function is selected <ins>from *S*</ins> as follows:
> 
> - (30.1) Each candidate that is a function template is replaced by the function template specializations (if any) generated using template argument deduction ([[temp.over]](https://wg21.link/temp.over), [[temp.deduct.call]](https://wg21.link/temp.deduct.call)) <del>with arguments as specified below</del> <ins>using *N* as the argument list</ins>.
> - (30.2) Each candidate whose associated constraints (if any) are not satisfied ([[temp.constr.constr]](https://wg21.link/temp.constr.constr)) is removed from the set of candidates.
> - (30.3) Each candidate whose parameter-type-list is not identical to that of the allocation function, ignoring their respective first parameters, is removed from the set of candidates.
> - (30.4) If exactly one function remains, that function is selected.
> - (30.5) Otherwise, no deallocation function is selected.
> 
> <del>If</del> <ins>The selected deallocation function (if any) shall not be deleted, shall not be</ins> a usual deallocation function <del>is selected, the program is ill-formed</del><ins>, and shall be accessible from the point where the new-expression appears</ins>. <ins>The selected allocation function is called with arguments in *N*.</ins>
> 
> 31
> 
> > [*Example:* [. . .] — *end example* ]
> 
> 32 <del>If a new-expression calls a deallocation function, it passes the value returned from the allocation function call as the first argument of type `void*`. If a placement deallocation function is called, it is passed the same additional arguments as were passed to the placement allocation function, that is, the same arguments as those specified with the new-placement syntax.</del> If the implementation is allowed to introduce a temporary object or make a copy of any argument as part of the call to the allocation function, it is unspecified whether the same object is used in the call to both the <ins>selected</ins> allocation <ins>function</ins> and <ins>the matching</ins> deallocation function<del>s</del>.
> 
> > [*Note:* This does not affect matching deallocation functions selected in [[expr.delete]](https://wg21.link/expr.delete), because they are usual dealloaction functions, therefore they do not accept additional arguments. — *end note* ]

[ Drafting note: The part of paragraph 20 that speaks about default arguments should resolve the second half of [CWG1628](https://cplusplus.github.io/CWG/issues/1628.html) “Deallocation function templates”. ]

[ Drafting note: (CWG) [CWG2592](https://cplusplus.github.io/CWG/issues/2592.html) “Missing definition for placement allocation/deallocation function” needs to be considered, so that we know what “placement (de)allocation functions” are. ]

[ Drafting note: (CWG) In p32, “if the implementation is allowed” sounds awkward. Is there wording somewhere else allowing or disallowing copying the placement arguments? ]

### 8.5 Delete [[expr.delete]](https://wg21.link/expr.delete)

> 7 <del>If a deallocation function is called, it is `operator delete` for a single-object delete expression or `operator delete[]` for an array delete expression.</del> <ins>The deallocation function’s name of a delete-expression *E* is `operator delete` if *E* is a single-object delete expression, and `operator delete[]` otherwise.</ins>
> 
> > [*Note:* An implementation provides default definitions of the global deallocation functions ([[new.delete.single]](https://wg21.link/new.delete.single), [[new.delete.array]](https://wg21.link/new.delete.array)). A C++ program can provide alternative definitions of these functions ([[replacement.functions]](https://wg21.link/replacement.functions)), and/or class-specific versions ([[class.free]](https://wg21.link/class.free)). — *end note* ]
> 
> 8 If the keyword `delete` in a delete-expression is not preceded by the unary `::` operator and the type of the operand is a pointer to a (possibly cv-qualified) class type `T` or (possibly multidimensional) array thereof:
> 
> - (8.1) For a single-object delete expression, if the operand is a pointer to *cv* `T` and `T` has a virtual destructor, the deallocation function is the one selected at the point of definition of the dynamic type’s virtual destructor ([[class.dtor]](https://wg21.link/class.dtor)).
> - (8.2) Otherwise, a search is performed for the deallocation function’s name in the scope of `T`.
> 
> Otherwise, or if nothing is found, the deallocation function’s name is looked up by searching for it in the global scope. In any case, any declarations other than of usual deallocation functions ([[basic.stc.dynamic.deallocation]](https://wg21.link/basic.stc.dynamic.deallocation)) are discarded.
> 
> > [*Note:* If only a placement deallocation function is found in a class, the program is ill-formed because the lookup set is empty ([[basic.lookup]](https://wg21.link/basic.lookup)). — *end note* ]
> 
> 8a The selected deallocation function is the static deallocation function as specified below, unless the following holds when selecting a deallocation function for a delete-expression *E*:
> 
> - (8a.1) the keyword `delete` in *E* is not preceded by the unary `::` operator,
> - (8a.2) the operand of *E* is a pointer to *cv* `T`, where `T` is a class type or (possibly multidimensional) array thereof, and
> - (8a.3) `T` has a virtual destructor,
> 
> in which case the selected deallocation function is the dynamic deallocation function ([[class.dtor]](https://wg21.link/class.dtor)) of the virtual destructor of the dynamic type of the operand of *E*.
> 
> > [*Note:* The dynamic deallocation function is never a matching deallocation function for a new-expression. — *end note* ]
> 
> 8b The static deallocation function is selected for every delete-expression.
> 
> > [*Note:* The static deallocation function is selected and its semantic constraints are checked even if it does not become the selected deallocation function. — *end note* ]
> 
> 9 <ins>Overload resolution tries to select the static deallocation function using the set of candidate functions termed *S* and the argument list termed *L* as specified in [[over.match.delete]](https://wg21.link/over.match.delete).</ins> <del>The</del> <ins>If overload resolution fails or was not performed, the static</ins> deallocation function <del>to be called</del> is selected <ins>from *S*</ins> as follows:
> 
> - (9.1) <del>If any of the deallocation functions is a destroying operator delete, all deallocation functions that are not destroying operator deletes are eliminated from further consideration.</del>
> - (9.1a) <ins>Each candidate that is a type-aware deallocation operator is eliminated from further consideration.</ins>
> - (9.2) If the type has new-extended alignment, a <del>function</del> <ins>candidate</ins> with a parameter of type `std::align_val_t` is preferred; otherwise a <del>function</del> <ins>candidate</ins> without such a parameter is preferred. If any preferred <del>functions</del> <ins>candidates</ins> are found, all non-preferred <del>functions</del> <ins>candidates</ins> are eliminated from further consideration.
> - (9.3) If exactly one <del>function</del> <ins>candidate</ins> remains, that <del>function</del> <ins>candidate</ins> is selected and the selection process terminates.
> - (9.4) If the <del>deallocation functions</del> <ins>candidates</ins> belong to a class scope, the one without a parameter of type `std::size_t` is selected.
> - (9.5) If the type is complete and if, for an array delete expression only, the operand is a pointer to a class type with a non-trivial destructor or a (possibly multidimensional) array thereof, the <del>function</del> <ins>candidate</ins> with a parameter of type `std::size_t` is selected.
> - (9.6) Otherwise, it is unspecified whether a <del>deallocation function</del> <ins>candidate</ins> with a parameter of type `std::size_t` is selected.
> 
> <del>Unless the deallocation function is selected at the point of definition of the dynamic type’s virtual destructor, the</del> <ins>The</ins> selected <ins>static</ins> deallocation function shall be accessible from the point where the delete-expression appears.

Move the third note in paragraph 10 after the paragraph 10b, and apply the following changes:

> 10 For a single-object delete expression, the deleted object is the object *A* pointed to by the operand if the static type of *A* does not have a virtual destructor, and the most-derived object of *A* otherwise.
> 
> > [*Note:* If the deallocation function is not a destroying operator delete and the deleted object is not the most derived object in the former case, the behavior is undefined, as stated above. — *end note* ]
> 
> For an array delete expression, the deleted object is the array object. <ins>When selecting a matching deallocation function for a new-expression, the deleted object is a hypothetical object of the allocated type ([[expr.new]](https://wg21.link/expr.new)).</ins> <del>When a delete-expression is executed, the selected deallocation function shall be called with the address of the deleted object in a single-object delete expression, or the address of the deleted object suitably adjusted for the array allocation overhead ([[expr.new]](https://wg21.link/expr.new)) in an array delete expression, as its first argument.</del>
> 
> > [*Note:* Any cv-qualifiers in the type of the deleted object are ignored when forming this argument. — *end note* ]
> 
> > [*Note:* Because a matching deallocation function is called only when a constructor throws, the lifetime of the deleted object does not start, but its type is known. — *end note* ]
> 
> 10a The *deallocation address* is:
> 
> - (10a.1) the address of the deleted object, if the delete-expression is a single-object delete expression, or
> - (10a.2) the address of the deleted object adjusted for the array allocation overhead, if the delete-expression is an array delete expression, or
> - (10a.3) the value returned by the call to the allocation function, if *F* is a matching deallocation function for a new-expression.
> 
> <del>If a destroying operator delete is used, an unspecified value is passed as the argument corresponding to the parameter of type `std::destroying_delete_t`.</del> <ins>The *deallocation size* is the sum of the size of the deleted object and of the array allocation overhead in the case of array delete expression, and the size of the deleted object otherwise.</ins> <del>If a deallocation function with a parameter of type `std::align_val_t` is used, the</del> <ins>The *deallocation alignment* is the</ins> alignment <ins>requirement</ins> of the type of the deleted object <del>is passed as the corresponding argument</del>. <del>If a deallocation function with a parameter of type `std::size_t` is used, the size of the deleted object in a single-object delete expression, or of the array plus allocation overhead in an array delete expression, is passed as the corresponding argument.</del>
> 
> 10b When a selected deallocation function *F* is called, the arguments for the call are:
> 
> - (10b.1) If *F* is a type-aware deallocation function, that of *L*.
> - (10b.2) Otherwise:
>   - (10b.2.1) A pointer value that represents the deallocation address and has the type:
>     - (10b.2.1.1) “pointer to `C`” if *F* is a destroying operator delete, where `C` is the cv-unqualified version of type of the deleted object, and
>     - (10b.2.1.2) “pointer to `void`” otherwise.
>   - (10b.2.2) If *F* is a destroying operator delete, then an unspecified value of type `std::destroying_delete_t` ([[new.syn]](https://wg21.link/new.syn)).
>   - (10b.2.3) If *F* has a parameter of type `std::size_t` ([[support.types]](https://wg21.link/support.types)), then a value of type `std::size_t` equal to the deallocation size.
>   - (10b.2.4) If *F* has a parameter of type `std::align_val_t` ([[support.dynamic]](https://wg21.link/support.dynamic)), then a value of type `std::align_val_t` equal to the deallocation alignment.
> 
> > [*Note:* If <del>this results in a call to</del> <ins>the selected deallocation function is</ins> a replaceable deallocation function, and either the first argument was not the result of a prior call to a replaceable allocation function or the second or third argument was not the corresponding argument in said call, the behavior is undefined ([[new.delete.single]](https://wg21.link/new.delete.single), [[new.delete.array]](https://wg21.link/new.delete.array)). — *end note* ]

[ Drafting note: (CWG) Should “(de)alloaction function’s name” be renamed to “(de)allocation operator’s name”? Do we want “the name of the deallocation operator”? ]

[ Drafting note: Should we try to move the note after p7 somewhere? Its contents feel rather close to [basic.stс.dynamic.general]/2. ]

[ Drafting note: We need to make sure that the correct alignment is passed to the deallocation function if there was a placement argument of type `std::align_val_t`. ]

[ Drafting note: (CWG) Should we make the deleted object to have a cv-unqualified type, as opposed to stripping the qualifiers when forming an argument for destroying operator delete? ]

### 8.6 The `constexpr` and `consteval` specifiers [[dcl.constexpr]](https://wg21.link/dcl.constexpr)

> 2 A `constexpr` or `consteval` specifier used in the declaration of a function declares that function to be a *constexpr function*.
> 
> > [*Note:* A function declared with the `consteval` specifier is an immediate function ([[expr.const.imm]](https://wg21.link/expr.const.imm)). — *end note* ]
> 
> A destructor, an allocation <del>function</del> <ins>operator</ins>, or a deallocation <del>function</del> <ins>operator</ins> shall not be declared with the `consteval` specifier.

### 8.7 Coroutine definitions [[dcl.fct.def.coroutine]](https://wg21.link/dcl.fct.def.coroutine)

> 13 The deallocation function’s name is looked up by searching for it in the scope of the promise type. If nothing is found, a search is performed in the global scope. If both a usual deallocation function with only <del>a pointer</del> <ins>the address</ins> parameter and a usual deallocation function with both <del>a pointer</del> <ins>the address</ins> parameter and a <del>size</del> parameter <ins>of the type `std::size_t`</ins> are found, then the selected deallocation function shall be the one with two parameters. Otherwise, the selected deallocation function shall be the function with one parameter. If no usual deallocation function is found, the program is ill-formed. The selected deallocation function shall be called with the address of the block of storage to be reclaimed as its first argument. If a deallocation function with a parameter of type `std::size_t` is used, the size of the block is passed as the corresponding argument.

### 8.8 Destructors [[class.dtor]](https://wg21.link/class.dtor)

> 15 At the point of definition of a virtual destructor (including an implicit definition), <del>the non-array deallocation function is determined as if for the</del> <ins>its *dynamic deallocation function* *F* is determined, which is the static deallocation function ([[expr.delete]](https://wg21.link/expr.delete)) selected for a hypothetical</ins> expression `delete this` appearing <del>in a non-virtual destructor of the destructor’s class (see [[expr.delete]](https://wg21.link/expr.delete))</del> <ins>at some point in the definition of the destructor</ins>. If <del>the lookup fails or if the deallocation function</del> <ins>no deallocation function was selected or *F*</ins> has a deleted definition ([[dcl.fct.def]](https://wg21.link/dcl.fct.def)), the program is ill-formed.
> 
> > [*Note:* This assures that a deallocation function corresponding to the dynamic type of an object is available for the delete-expression ([[class.free]](https://wg21.link/class.free)). — *end note* ]

### 8.9 Allocation and deallocation functions [[class.free]](https://wg21.link/class.free)

> 1 Any allocation <del>function</del> <ins>operator</ins> for a class `T` is a static member (even if not explicitly declared `static`).
> 
> 2 [*Example:* [. . .] — *end example* ]
> 
> 3 Any deallocation <del>function</del> <ins>operator</ins> for a class `X` is a static member (even if not explicitly declared `static`).
> 
> [*Example:* [. . .] — *end example* ]
> 
> 4 Since member allocation and deallocation <del>functions</del> <ins>operators</ins> are `static` they cannot be virtual.
> 
> > [*Note:* However, when the cast-expression of a delete-expression refers to an object of class type with a virtual destructor, because the deallocation function is chosen by the destructor of the dynamic type of the object, the effect is the same in that case.
> > 
> > > [*Example:* 
> > > 
> > > ```cpp
> > > struct B {
> > >   virtual ~B();
> > >   void operator delete(void*, std::size_t);
> > > };
> > > 
> > > struct D : B {
> > >   void operator delete(void*);
> > > };
> > > 
> > > struct E : B {
> > >   void log_deletion();
> > >   void operator delete(E *p, std::destroying_delete_t) {
> > >     p->log_deletion();
> > >     p->~E();
> > >     ::operator delete(p);
> > >   }
> > > };
> > > 
> > > void f() {
> > >   B* bp = new D;
> > >   delete bp;        // 1: uses D​::​operator delete(void*)
> > >   bp = new E;
> > >   delete bp;        // 2: uses E​::​operator delete(E*, std​::​destroying_delete_t)
> > > }
> > > ```
> > > 
> > > Here, storage for the object of class `D` is deallocated by `D::operator delete()`, and the object of class `E` is destroyed and its storage is deallocated by `E::operator delete()`, due to the virtual destructor. — *end example* ]
> > 
> >   — *end note* ]
> 
> > [*Note:* Virtual destructors have no effect on the deallocation function actually called when the cast-expression of a delete-expression refers to an array of objects of class type.
> > 
> > > [*Example:* 
> > > 
> > > ```cpp
> > > struct B {
> > >   virtual ~B();
> > >   void operator delete[](void*, std::size_t);
> > > };
> > > 
> > > struct D : B {
> > >   void operator delete[](void*, std::size_t);
> > > };
> > > 
> > > void f(int i) {
> > >   D* dp = new D[i];
> > >   delete [] dp;     // uses D​::​operator delete[](void*, std​::​size_t)
> > >   B* bp = new D[i];
> > >   delete[] bp;      // undefined behavior
> > > }
> > > ```
> > > 
> > >   — *end example* ]
> > 
> >   — *end note* ]
> 
> 4a If a class scope *S* is the target scope of a type-aware allocation or deallocation operator *F*, then
> 
> - (4a.1) if the name of *F* is `operator new` or `operator delete`, *S* shall be the target scope of an allocation operator named `operator new` and a deallocation operator named `operator delete`, or
> - (4a.2) if the name of *F* is `operator new[]` or `operator delete[]`, *S* shall be the target scope of an allocation operator named `operator new[]` and a deallocation operator named `operator delete[]`.
> 
> 5
> 
> > <ins>[*Note:* </ins>Access to the deallocation function is checked statically, even if a different one is actually <del>executed</del> <ins>called ([[expr.delete]](https://wg21.link/expr.delete))</ins>.<ins> — *end note* ]</ins>
> 
> > [*Example:* For the call on line “// 1” above, if `B::operator delete()` had been private, the delete expression would have been ill-formed. — *end example* ]
> 
> 6
> 
> > [*Note:* If a deallocation <del>function</del> <ins>operator</ins> has no explicit noexcept-specifier, it has a non-throwing exception specification ([[except.spec]](https://wg21.link/except.spec)). — *end note* ]

### 8.10 Candidate functions and argument lists [[over.match.funcs.general]](https://wg21.link/over.match.funcs.general)

> 2 The set of candidate functions can contain both member and non-member functions to be resolved against the same argument list. If a member function is
> 
> - (2.1) an implicit object member function that is not a constructor, or
> - (2.2) a static member function and the argument list includes an implied object argument,
> 
> it is considered to have an extra first parameter, called the implicit object parameter, which represents the object for which the member function has been called.
> 
> 3 Similarly, when appropriate, the context can construct an argument list that contains an implied object argument as the first argument in the list to denote the object to be operated on.
> 
> 4 [. . .]
> 
> 8 In each case where a candidate is a function template <ins>and the argument list is known</ins>, candidate function template specializations are generated using template argument deduction ([[temp.over]](https://wg21.link/temp.over), [[temp.deduct]](https://wg21.link/temp.deduct)). If a constructor template or conversion function template has an explicit-specifier whose constant-expression is value-dependent ([[temp.dep]](https://wg21.link/temp.dep)), template argument deduction is performed first and then, if the context admits only candidates that are not explicit and the generated specialization is explicit ([[dcl.fct.spec]](https://wg21.link/dcl.fct.spec)), it will be removed from the candidate set. Those candidates are then handled as candidate functions in the usual way.<sup>93</sup> A given name can refer to, or a conversion can consider, one or more function templates as well as a set of non-template functions. In such a case, the candidate functions generated from each function template are combined with the set of non-template candidate functions.
> 
> > [*Note:* When selecting the matching deallocation function for an allocation function, the argument list might not be known ([[over.match.new]](https://wg21.link/over.match.new), [[over.match.delete]](https://wg21.link/over.match.delete)). In such cases the candidates that are function templates are left as is, and a matching deallocation function is selected among the set of candidates by means other than overload resolution ([[expr.new]](https://wg21.link/expr.new), [[expr.delete]](https://wg21.link/expr.delete)). — *end note* ]

Footnote 93:

> 93 The process of argument deduction fully determines the parameter types of the function template specializations, i.e., the parameters of function template specializations contain no template parameter types. Therefore, except where specified otherwise, function template specializations and non-template functions ([[dcl.fct]](https://wg21.link/dcl.fct)) are treated equivalently for the remainder of overload resolution.

### 8.11 New expression [[over.match.new]](https://wg21.link/over.match.new)

Add a new subclause after [[over.match.class.deduct]](https://wg21.link/over.match.class.deduct):

> 1 When selecting an allocation function or a matching deallocation function for a new-expression *E* whose allocated type is `U`, the set of candidate functions consists of the results of a search for the allocation or deallocation function’s name ([[expr.new]](https://wg21.link/expr.new), [[expr.delete]](https://wg21.link/expr.delete)), respectively, in the following scopes:
> 
> - (1.1) If *E* does not begin with `::` and `U` is a class type or array thereof, in the scope associated with `U`.
> - (1.2) Otherwise, or if no declarations were found, in the global scope.
> 
> Each candidate that is a destroying operator delete ([[basic.std.dynamic.deallocation]](https://wg21.link/basic.std.dynamic.deallocation)) is removed from the set of candidate functions.
> 
> 2 Let
> 
> - (2.1) *T* be a value of type `std::type_identity<V>` ([[meta.trans.other]](https://wg21.link/meta.trans.other)), where `V` is a cv-unqualified version of the array element type of `U` if `U` is an array type, and a cv-unqualified version of `U` otherwise,
> - (2.2) *S* be a value of type `std::size_t` ([[support.types]](https://wg21.link/support.types)) equal to the allocation size,
> - (2.3) *A* be a value of type `std::align_val_t` ([[support.dynamic]](https://wg21.link/support.dynamic)) equal to the allocation alignment, and
> - (2.4) *P* be the initializer-clauses in the expression-list of *E* if the new-placement syntax is used, and an empty set otherwise.
> 
> Overload resolution selects an allocation function in multiple phases using different argument lists. The argument list for an allocation function consists of
> 
> - (2.5) (*T*, *S*, *P*) if the first initializer-clause in *P* (if any) has the type `std::align_val_t` after parameter transformations ([[dcl.fct]](https://wg21.link/dcl.fct)), and (*T*, *S*, *A*, *P*) otherwise, or, if overload resolution fails,
> - (2.6) (*S*, *A*, *P*) if the type of the allocated object has new-extended alignment, and (*S*, *P*) otherwise, or, if overload resolution fails,
> - (2.7) (*S*, *P*) if the type of the allocated object has new-extended alignment, and (*S*, *A*, *P*) otherwise.

Move [[expr.new]](https://wg21.link/expr.new) paragraph 21 after paragraph 2 and apply the following changes:

> 3
> 
> > [*Example:* <ins>In the following examples `T` is a non-array type that does not have new-extended alignment:</ins>
> > 
> > - (3.1) `new T` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new(std::type_identity<std::remove_cv_t<T>>(), sizeof(T), std::align_val_t(alignof(T)))
> >   operator new(sizeof(T))
> >   operator new(sizeof(T), std::align_val_t(alignof(T)))
> >   ```
> > - (3.2) `new(2,f) T` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new(std::type_identity<std::remove_cv_t<T>>(), sizeof(T), std::align_val_t(alignof(T)), 2, f)
> >   operator new(sizeof(T), 2, f)
> >   operator new(sizeof(T), std::align_val_t(alignof(T)), 2, f)
> >   ```
> > - (3.3) `new T[5]` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new[](std::type_identity<std::remove_cv_t<T>>(), sizeof(T) * 5 + x, std::align_val_t(alignof(T)))
> >   operator new[](sizeof(T) * 5 + x)
> >   operator new[](sizeof(T) * 5 + x, std::align_val_t(alignof(T)))
> >   ```
> > - (3.4) `new(2,f) T[5]` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new[](std::type_identity<std::remove_cv_t<T>>(), sizeof(T) * 5 + x, std::align_val_t(alignof(T)), 2, f)
> >   operator new[](sizeof(T) * 5 + x, 2, f)
> >   operator new[](sizeof(T) * 5 + x, std::align_val_t(alignof(T)), 2, f)
> >   ```
> > 
> > In the following example `T` has new-extended alignment and is not an array type:
> > 
> > - (3.5) `new(std::align_val_t(7), f) T` results in one of the following calls:
> > 
> >   ```cpp
> >   operator new(std::type_identity<std::remove_cv_t<T>>(), sizeof(T), std::align_val_t(7), f)
> >   operator new(sizeof(T), std::align_val_t(alignof(T)), std::align_val_t(7), f)
> >   operator new(sizeof(T), std::align_val_t(7), f)
> >   ```
> > 
> > Here, each instance of `x` is a non-negative unspecified value representing array allocation overhead; the result of the *new-expression* will be offset by this amount from the value returned by `operator new[]`. This overhead may be applied in all array *new-expressions*, including those referencing a placement allocation function, except when referencing the library function `operator new[](std::size_t, void*)`. The amount of overhead may vary from one invocation of new to another. — *end example* ]
> 
> 4 If there is a candidate that is a type-aware deallocation function and the selected allocation function *F* is not a placement allocation function, then overload resolution selects a matching deallocation function for *E*. The argument list consists of the arguments used to call *F* ([[expr.new]](https://wg21.link/expr.new)), except that the value returned from the call to *F* is inserted after the first argument.
> 
> > [*Note:* If a call to the selected allocation function uses default arguments, they can influence the selection of a matching deallocation function. The parameter-type-list of the selected matching deallocation function has to satisfy additional criteria for a program to be well-formed ([[expr.new]](https://wg21.link/expr.new)). — *end note* ]
> 
> 5
> 
> > [*Note:* Otherwise, the matching deallocation function is selected as specified in [[expr.new]](https://wg21.link/expr.new). — *end note* ]

[ Drafting note: (CWG) How clear it is that the sets of arguments in p2 are ordered? ]

[ Drafting note: (CWG) Discarding candidates that are destroying operators delete should resolve CWG2623 “Invoking destroying `operator delete` for constructor failure”. ]

[ Drafting note: (CWG) does p4 needs to be predicated on the presence of a type-aware candidate and on the fact that the selected allocation function is a placement one? More broadly, this is a question how independent [[over.match.new]](https://wg21.link/over.match.new) is from [[expr.new]](https://wg21.link/expr.new), which specifies the same predicates before referring to overload resolution. ]

### 8.12 Delete expression [[over.match.delete]](https://wg21.link/over.match.delete)

Add a new subclause after [[over.match.new]](https://wg21.link/over.match.new):

> 1 When selecting a deallocation function for a delete-expression *E* whose operand is of type “pointer to *cv* `U`”, the set of candidate functions consists of the results of a search for the deallocation function’s name ([[expr.delete]](https://wg21.link/expr.delete)) in the following scopes:
> 
> - (1.1) If *E* does not begin with `::` and `U` is a class type, in the scope associated with `U`.
> - (1.2) Otherwise, or if no declarations were found, in the global scope.
> 
> If any of the candidates is a destroying operator delete, each candidate that is not a destroying operator delete is removed from the set of candidate functions.
> 
> 2
> 
> > [*Note:* When selecting a matching deallocation function for an allocation function that is not a placement allocation function ([[expr.new]](https://wg21.link/expr.new)), the set of candidate functions is as specified in [[over.match.new]](https://wg21.link/over.match.new). — *end note* ]

Move the note that follows [[expr.delete]](https://wg21.link/expr.delete) paragraph 8 after paragraph 3 and apply the following changes:

> 3 When selecting a deallocation function for a delete-expression or a matching deallocation function for an allocation function that is not a placement allocation function, each candidate that is not a usual deallocation operator ([[basic.stc.dynamic.deallocation]](https://wg21.link/basic.stc.dynamic.deallocation)) is removed from the set of candidate functions.
> 
> > [*Note:* If only a placement deallocation function <del>is</del> <ins>was</ins> found in a class <ins>scope</ins>, the program is ill-formed because the lookup set is empty ([[basic.lookup]](https://wg21.link/basic.lookup)). — *end note* ]
> 
> 4 When selecting a deallocation function for a delete-expression or a matching deallocation function for an allocation function that is not a placement allocation function, if one of the candidates is a type-aware deallocation operator, overload resolution selects a deallocation function using an argument list that consists of, in order:
> 
> - (3.1) a value of type `std::type_identity<U>` ([[meta.trans.other]](https://wg21.link/meta.trans.other)),
> - (3.2) a value of type “pointer to `void`” that represents the deallocation address,
> - (3.3) a value of type `std::size_t` ([[support.types]](https://wg21.link/support.types)) equal to the deallocation size, and
> - (3.4) a value of type `std::align_val_t` ([[support.dynamic]](https://wg21.link/support.dynamic)) equal to the deallocation alignment.
> 
> 5
> 
> > [*Note:* Otherwise, or if overload resolution fails, a deallocation function is selected as specified in [[expr.delete]](https://wg21.link/expr.delete). — *end note* ]

### 8.13 General [[over.oper.general]](https://wg21.link/over.oper.general)

> 5 The allocation and deallocation <del>functions</del> <ins>operators</ins>, `operator new`, `operator new[]`, `operator delete`, and `operator delete[]`, are described completely in [[basic.stc.dynamic]](https://wg21.link/basic.stc.dynamic). The attributes and restrictions found in the rest of [[over.oper]](https://wg21.link/over.oper) do not apply to them unless explicitly stated in [[basic.stc.dynamic]](https://wg21.link/basic.stc.dynamic).

[ Drafting note: (CWG) Additional places where we might need “function” → “operator” replacement: [[temp.func.order]](https://wg21.link/temp.func.order), [[temp.deduct.decl]](https://wg21.link/temp.deduct.decl), [[except.spec]](https://wg21.link/except.spec). ]

### 8.14 Predefined macro names [[cpp.predefined]](https://wg21.link/cpp.predefined)

Add a feature-test macro `__cpp_typed_allocation` with an appropriate value.

> ```cpp
> #define __cpp_typed_allocation 202XXXL
> ```

## 9 Acknowledgments

We’d like to acknowledge the time spent by Jens Maurer, Brian Bi, Corentin Jabot, Richard Smith, Hana Dusikova, Lauri Vasama, and others to help us develop the wording in this proposal.
