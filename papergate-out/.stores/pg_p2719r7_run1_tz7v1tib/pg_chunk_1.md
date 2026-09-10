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
