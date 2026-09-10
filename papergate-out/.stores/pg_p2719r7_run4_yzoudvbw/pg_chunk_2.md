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
