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
