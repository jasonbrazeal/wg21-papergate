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