[*Note* *2*: Loss of precision occurs if the integral value cannot be represented exactly as a value of the floating-point type. *— end* *note*]

:::wording

If the value being converted is outside the range of values that can be represented, <del>the behavior</del><ins>an</ins> <ins>unspecified erroneous value</ins> is <del>undefined</del><ins>produced with an implicit precondition that this does</ins> not occur (F.3.8[ubx:conv.fpint.int.not.represented]).∗If the source type is bool, the value false is converted to zero and the value true is converted to one.

:::

##### Note

*∗***ubdef:** conv.fpint.int.not.represented **summary:** integer/unscoped-enum to floating-point conversion whose value isn’t representable. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is valid **replacement:** Coerce into erroneous value **implementations:** None

#### 7*.*3*.*12 Pointer conversions [conv.ptr]

Notes regarding 7.3.12[conv.ptr], paragraph 3:

3 A prvalue `v` of type “pointer to *cv* `D`”, where `D` is a complete class type, can be converted to a prvalue of type “pointer to *cv* `B`”, where `B` is a base class (11.7[class.derived]) of `D`. If `B` is an inaccessible (11.8[class.access]) or ambiguous (6.5.2[class.member.lookup]) base class of `D`, a program that necessitates this conversion is ill-formed. If `v` is a null pointer value, the result is a null pointer value. Otherwise, if `B` is a virtual base class of `D` or is a base class of a virtual base class of `D` and `v` does not point to an object whose type is similar (7.3.6[conv.qual]) to `D` and that is within its lifetime or within its period of construction or destruction (11.9.5[class.cdtor]), the behavior is undefined *(F.3.9[ubx:conv.ptr.virtual.base]).∗*Otherwise, the result is a pointer to the base class subobject of the derived class object.

#### Note

*∗***ubdef:** conv.ptr.virtual.base **summary:** converting a derived-class pointer to a virtual base when the source isn’t a valid, in-lifetime object. **runtime-checkable:** Yes **locally-checkable:** Only for the null pointer case **checking:** Track whether storage is associated with an object of correct type within its lifetime or an object currently being constructed or destroyed; insert null pointer check **replacement:** None **implementations:** Many cases caught by UBSan’s `vptr` check on both compilers.

#### 7*.*3*.*13 Pointer-to-member conversions [conv.mem]

Notes regarding 7.3.13[conv.mem], paragraph 2:

2 A prvalue of type “pointer to member of `B` of type *cv* `T`”, where `B` is a class type, can be converted to a prvalue of type “pointer to member of `D` of type *cv* `T`”, where `D` is a complete class derived (11.7[class.derived]) from `B`. If `B` is an inaccessible (11.8[class. access]), ambiguous (6.5.2[class.member.lookup]), or virtual (11.7.2[class.mi]) base class of `D`, or a base class of a virtual base class of `D`, a program that necessitates this conversion is ill-formed. If class `D` does not contain the original member and is not a base class of the class containing the original member, the behavior is undefined (F.3.10[ubx:conv. member.missing.member]).*∗*Otherwise, the result of the conversion refers to the same member as the pointer to member before the conversion took place, but it refers to the base class member as if it were a member of the derived class. The result refers to the member in `D`’s instance of `B`. Since the result has type “pointer to member of `D` of type *cv* `T`”, indirection through it with a `D` object is valid. The result is the same as if indirecting through the pointer to member of `B` with the `B` subobject of `D`. The null member pointer value is converted to the null member pointer value of the destination type.`40`

`40` The rule for conversion of pointers to members (from pointer to member of base to pointer to member of derived) appears inverted compared to the rule for pointers to objects (from pointer to derived to pointer to base) (7.3.12[conv.ptr], 11.7[class.derived]). This inversion is necessary to ensure type safety.

Note that a pointer to member is not an object pointer or a function pointer and the rules for conversions of such pointers do not apply to pointers to members. In particular, a pointer to member cannot be converted to a `void*`.

#### Note

*∗***ubdef:** conv.member.missing.member **summary:** converting a base pointer-to-member to a derived one that could not actually contain that member. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track which type the pointer to member originated from. **replacement:** None **implementations:** GCC’s `object-size` check flags some cases (heuristic; stock and integrated); constant evaluation exhaustive on both compilers.

### 7*.*6 Compound expressions [expr.compound]

#### 7*.*6*.*1 Postfix expressions [expr.post]

##### 7*.*6*.*1*.*3 Function call [expr.call]

Notes regarding 7.6.1.3[expr.call], paragraph 6:

6 A type `T`call is *call-compatible* with a function type `T`func if `T`call is the same type as `T`func or if the type “pointer to `T`func” can be converted to type “pointer to `T`call” via a function pointer conversion (7.3.14[conv.fctptr]). Calling a function through an expression whose function type is not call-compatible with the type of the called function’s definition results in undefined behavior (F.3.11[ubx:expr.call.different.type]).*∗*

[*Note*: This requirement allows the case when the expression has the type of a potentially-throwing function, but the called function has a non-throwing exception specification, and the function types are otherwise the same. *— end* *note*]

##### Note

*∗***ubdef:** expr.call.different.type **summary:** calling a function through a pointer/reference type incompatible with its actual definition. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track type information of function based on address **replacement:** None **implementations:** caught by Clang’s UBSan `function`/`undefined` check; re- jected during constant evaluation on both GCC and Clang.

##### 7*.*6*.*1*.*5 Class member access [expr.ref]

Notes regarding 7.6.1.5[expr.ref], paragraph 10:

10 If `E2` designates a non-static member (possibly after overload resolution) or direct base class relationship and the result of `E1` is an object whose type is not similar (7.3.6[conv. qual]) to the type of `E1`, the behavior is undefined (F.3.12[ubx:expr.ref.member.not. similar]).*∗*

[*Example*:

```cpp
struct B { int j; };
struct D : A, B {};
void f() {
  D d;
  static_cast<B&>(d).j;  // OK, object expression designates the B subobject of d
  reinterpret_cast<B&>(d).j;  // undefined behavior
}
```

*— end* *example*]

##### Note

*∗***ubdef:** expr.ref.member.not.similar **summary:** accessing a member through a glvalue not similar to the object’s actual type. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** caught by both compilers’ constant evaluators.

##### 7*.*6*.*1*.*7 Dynamic cast [expr.dynamic.cast]

Notes regarding 7.6.1.7[expr.dynamic.cast], paragraph 7:

7 If `v` has type “pointer to *cv* `U`” and `v` does not point to an object whose type is similar (7.3.6[conv.qual]) to `U` and that is within its lifetime or within its period of construction or destruction (11.9.5[class.cdtor]), the behavior is undefined (F.3.13[ubx:expr. dynamic.cast.pointer.lifetime]).*∗*If `v` is a glvalue of type `U` and `v` does not refer to an object whose type is similar to `U` and that is within its lifetime or within its period of construction or destruction, the behavior is undefined (F.3.14[ubx:expr.dynamic.cast.glvalue.lifetime]).

##### Note

*∗***ubdef:** expr.dynamic.cast.pointer.lifetime **summary:** `dynamic_cast` on a non-null pointer to the wrong type or outside any object’s lifetime. **runtime-checkable:** Yes **locally-checkable:** Only for the null pointer case **checking:** Track whether storage is associated with an object of correct type within its lifetime or an object currently being constructed or destroyed; insert null pointer check **replacement:** None **implementations:** None

##### Note

##### ubdef:

expr.dynamic.cast.glvalue.lifetime **summary:** `dynamic_cast<T&>` on an object of the wrong type or outside its lifetime. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime or an object currently being constructed or destroyed **replacement:** None **implementations:** rejected during constant evaluation on Clang.

##### 7*.*6*.*1*.*9 Static cast [expr.static.cast]

Notes regarding 7.6.1.9[expr.static.cast], paragraph 2:

2 An lvalue of type “*cv1* `B`”, where `B` is a class type, can be cast to type “reference to *cv2* `D`”, where `D` is a complete class derived (11.7[class.derived]) from `B`, if *cv2* is the same cv-qualification as, or greater cv-qualification than, *cv1*. If `B` is a virtual base class of `D` or a base class of a virtual base class of `D`, or if no valid standard conversion from “pointer to `D`” to “pointer to `B`” exists (7.3.12[conv.ptr]), the program is ill-formed. An xvalue of type “*cv1* `B`” can be cast to type “rvalue reference to *cv2* `D`” with the same constraints as for an lvalue of type “*cv1* `B`”. If the object of type “*cv1* `B`” is actually a base class subobject of an object of type `D`, the result refers to the enclosing object of type `D`. Otherwise, the behavior is undefined (F.3.15[ubx:expr.static.cast.base.class]).*∗*

[*Example*:

```cpp
struct D : public B { };
D d;
B &br = d;
static_cast<D&>(br);  // produces lvalue denoting the original d object
```

*— end* *example*]

##### Note

*∗***ubdef:** expr.static.cast.base.class **summary:** `static_cast`-ing a base glvalue to a reference of the wrong sibling type. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** polymorphic subset caught by UBSan’s `vptr` check (Clang, integrated, both `noexcept`-enforce and `noexcept`-observe) and constant evaluation (Clang); nonpolymorphic subset caught by constant evaluation (Clang).

Modify and note section 7.6.1.9[expr.static.cast], paragraphs 8-11:

:::wording

8 A value of integral or enumeration type can be explicitly converted to a complete enumeration type. If the enumeration type has a fixed underlying type, the value is first converted to that type by integral promotion (7.3.7[conv.prom]) or integral conversion (7.3.9[conv.integral]), if necessary, and then to the enumeration type. If the enumeration type does not have a fixed underlying type, the value is unchanged if the original value is within the range of the enumeration values (9.8.1[dcl.enum]), and otherwise, <del>the behavior</del><ins>an unspecified erroneous value</ins> is <del>undefined</del><ins>produced with an implicit</ins> <ins>precondition that this does not occur (6.11.2+a[basic.contract.implicit])</ins> (F.3.16[ubx:expr. static.cast.enum.outside.range]).∗A value of floating-point type can also be explicitly converted to an enumeration type. The resulting value is the same as converting the original value to the underlying type of the enumeration (7.3.11[conv.fpint]), and subsequently to the enumeration type.

:::

##### Note

*∗***ubdef:** expr.static.cast.enum.outside.range **summary:** `static_cast`-ing an out-of-range integer into an unscoped enum without a fixed underlying type. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is in the valid range **replacement:** Coerce into erroneous value **implementations:** caught by Clang via constant evaluation and UBSan’s `enum` check (`-fsanitize=enum`) on the load; and, in the P3850 prototype, by a front-end check at the cast site on both compilers (all available semantics) – closing GCC’s coverage gap.

:::wording

9 A prvalue of floating-point type can be explicitly converted to any other floatingpoint type. If the source value can be exactly represented in the destination type, the result of the conversion has that exact representation. If the source value is between two adjacent destination values, the result of the conversion is an implementation-defined choice of either of those values. Otherwise, <del>the behavior</del><ins>an unspecified</ins> <ins>erroneous value</ins> is <del>undefined</del><ins>produced with an implicit precondition that this does not</ins> occur (6.11.2+a[basic.contract.implicit]) (F.3.17[ubx:expr.static.cast.fp.outside.range]).

:::

##### Note

##### ubdef:

expr.static.cast.fp.outside.range **summary:** an explicit `static_cast` of a floating-point value outside the target type’s representable range. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is valid **replacement:** Coerce into erroneous value **implementations:** None

10 A prvalue of type “pointer to *cv1* `B`”, where `B` is a class type, can be converted to a prvalue of type “pointer to *cv2* `D`”, where `D` is a complete class derived (11.7[class.derived]) from `B`, if *cv2* is the same cv-qualification as, or greater cv-qualification than, *cv1*. If `B` is a virtual base class of `D` or a base class of a virtual base class of `D`, or if no valid standard conversion from “pointer to `D`” to “pointer to `B`” exists (7.3.12[conv.ptr]), the program is ill-formed. The null pointer value (6.9.5[basic.compound]) is converted to the null pointer value of the destination type. If the prvalue of type “pointer to *cv1* `B`” points to a `B` that is actually a base class subobject of an object of type `D`, the resulting pointer points to the enclosing object of type `D`. Otherwise, the behavior is undefined (F.3.18[ubx:expr.static.cast.downcast.wrong.derived.type]).

##### Note

##### ubdef:

expr.static.cast.downcast.wrong.derived.type **summary:** `static_cast`-ing a base pointer to a pointer of the wrong sibling type. **runtime-checkable:** Yes **locally-checkable:** Only for the null pointer case **checking:** Track whether storage is associated with an object of correct type within its lifetime or an object currently being constructed or destroyed; insert a null pointer check **replacement:** None **implementations:** polymorphic subset caught by UBSan’s `vptr` check (both compilers, integrated, both `noexcept`-enforce and `noexcept`-observe) and constant evaluation (Clang); non- polymorphic subset caught by constant evaluation (Clang).

11 A prvalue of type “pointer to member of `D` of type *cv1* `T`” can be converted to a prvalue of type “pointer to member of `B` of type *cv2* `T`”, where `D` is a complete class type and `B` is a base class (11.7[class.derived]) of `D`, if *cv2* is the same cv-qualification as, or greater cv-qualification than, *cv1*.

[*Note*: Function types (including those used in pointer-to-member-function types) are never cv-qualified (9.3.4.6[dcl.fct]). *— end* *note*]

If no valid standard conversion from “pointer to member of `B` of type `T`” to “pointer to member of `D` of type `T`” exists (7.3.13[conv.mem]), the program is ill-formed. The null member pointer value (7.3.13[conv.mem]) is converted to the null member pointer value of the destination type. If class `B` contains the original member, or is a base class of the class containing the original member, the resulting pointer to member points to the original member. Otherwise, the behavior is undefined (F.3.19[ubx:expr.static.cast.does. not.contain.original.member]).*∗*

[*Note*: Although class `B` need not contain the original member, the dynamic type of the object with which indirection through the pointer to member is performed must contain the original member; see 7.6.4[expr.mptr.oper]. *— end* *note*]

##### Note

*∗***ubdef:** expr.static.cast.does.not.contain.original.member **summary:** `static_cast`-ing a pointer-to-member to a base lacking the original member. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track which type the pointer to member originated from **replacement:** None **implementations:** caught by Clang’s constant evaluator.

##### 7*.*6*.*1*.*10 Reinterpret cast [expr.reinterpret.cast]

Notes regarding 7.6.1.10[expr.reinterpret.cast], paragraph 5:

5 A value of integral type or enumeration type can be explicitly converted to a pointer. If the value is one that can be produced by converting one or more pointer values (6.9.5[basic. compound]) to an integral type, the result is an unspecified choice among all such values that would result in the program having defined behavior. If no such value exists, the behavior is undefined (F.3.20[ubx:expr.reinterpret.cast.invalid.pointer.value]).*∗*

[*Note*: It is possible for the result to be an invalid pointer value or to not be valid in the context of the conversion (6.9.5[basic.compound]) because it points to an object in a region of storage whose duration has ended or has not yet begun. *— end* *note*]

Otherwise, the result is implementation-defined.

[*Note*: It can be an invalid pointer value. *— end* *note*]

##### Note

*∗***ubdef:** expr.reinterpret.cast.invalid.pointer.value **summary:** forming a pointer via `reinterpret_cast` with no real provenance. **runtime-checkable:** No, requires predicting whether any potential value will encounter undefined behavior **locally-checkable:** No **checking:** Would require properly identifying when angelic provenance does not apply **replacement:** None **implementations:** None

#### 7*.*6*.*2 Unary expressions [expr.unary]

##### 7*.*6*.*2*.*2 Unary operators [expr.unary.op]

Notes regarding 7.6.2.2[expr.unary.op], paragraph 1:

1 The unary `*` operator performs *indirection*. Its operand shall be a prvalue of type “pointer to `T`”, where `T` is an object or function type. The operator yields an lvalue of type `T`. If the operand points to an object or function, the result denotes that object or function; otherwise, the behavior is undefined except as specified in 7.6.1.8[expr. typeid] (F.3.21[ubx:expr.unary.dereference]).*∗*

[*Note*: Indirection through a pointer to an out-of-lifetime object is valid (6.8.4[basic.life]). *— end* *note*]

[*Note*: Indirection through a pointer to an incomplete type (other than *cv* `void`) is valid. The lvalue thus obtained can be used in limited ways (to initialize a reference, for example); this lvalue must not be converted to a prvalue, see 7.3.2[conv.lval]. *— end* *note*]

##### Note

*∗***ubdef:** expr.unary.dereference **summary:** dereferencing a pointer that is null or otherwise does not point to a live object or function. **runtime-checkable:** Yes **locally-checkable:** Only for the null pointer case **checking:** Track whether storage is associated with an object of correct type within its lifetime; track whether the address is associated with a function; insert a null pointer check **replacement:** None **implementations:** `.nullptr` caught by a native P3850 check (all available semantics on Clang; four non-throwing semantics on GCC) and constant evaluation, both compilers; `.invalid` caught heuristically by AddressSanitizer and by constant evaluation, both compilers.

##### 7*.*6*.*2*.*8 New [expr.new]

Notes regarding 7.6.2.8[expr.new], paragraph 22:

22 [*Note*: Unless an allocation function has a non-throwing exception specification (14.5[except.spec]), it indicates failure to allocate storage by throwing a `std::bad_alloc` exception (6.8.6.5.2[basic. stc.dynamic.allocation], 14.2[except.throw], 17.6.4.1[bad.alloc]); it returns a non-null pointer otherwise. If the allocation function has a non-throwing exception specification, it returns null to indicate failure to allocate storage and a non-null pointer otherwise. *— end* *note*]

If the allocation function is a non-allocating form (17.6.3.4[new.delete.placement]) that re- turns null, the behavior is undefined *(F.3.22[ubx:expr.new.non.allocating.null]).∗*Otherwise, if the allocation function returns null, initialization shall not be done, the deallocation function shall not be called, and the value of the *new-expression* shall be null.

##### Note

*∗***ubdef:** expr.new.non.allocating.null **summary:** a user-replaced non-allocating placement-`new` returning null. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert `post(r:` `r)` **replacement:** None **implementations:** caught by UBSan’s `null` check (part of the `undefined` group), which flags the null pointer returned by the non- allocating placement `new`, and by both compilers’ constant evaluators.

##### 7*.*6*.*2*.*9 Delete [expr.delete]

Notes regarding 7.6.2.9[expr.delete], paragraphs 2-3:

2 In a single-object delete expression, the value of the operand of `delete` may be a null pointer value, a pointer value that resulted from a previous non-array *new-expression*, or a pointer to a base class subobject of an object created by such a *new-expression*. If not, the behavior is undefined (F.3.23[ubx:expr.delete.mismatch]).*∗*In an array delete expression, the value of the operand of `delete` may be a null pointer value or a pointer value that resulted from a previous array *new-expression* whose allocation function was not a non-allocating form (17.6.3.4[new.delete.placement]).`56` If not, the behavior is undefined (F.3.24[ubx:expr.delete.array.mismatch]).*†*

[*Note*: This means that the syntax of the *delete-expression* must match the type of the object allocated by `new`, not the syntax of the *new-expression*. *— end* *note*]

[*Note*: A pointer to a `const` type can be the operand of a *delete-expression*; it is not necessary to cast away the constness (7.6.1.11[expr.const.cast]) of the pointer expression before it is used as the operand of the *delete-expression*. *— end* *note*]

`56` For nonzero-length arrays, this is the same as a pointer to the first element of the array created by that *new-expression*. Zero-length arrays do not have a first element.

##### Note

*∗***ubdef:** expr.delete.mismatch **summary:** using `delete[]` on a pointer from single-object `new`. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track pointer provenance, verify the delete form matches the allocation form (single-object versus array) **replacement:** None **implementations:** exhaustively caught by ASan’s `alloc_dealloc_mismatch` on both compilers; rejected during constant evaluation on both GCC and Clang.

##### Note

*†* **ubdef:** expr.delete.array.mismatch **summary:** applying single-object `delete` to a pointer from array `new[]`. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track pointer provenance, verify the delete form matches the allocation form (single-object versus array) **replacement:** None **implementations:** exhaustively caught by ASan’s `alloc_dealloc_mismatch` on both compilers; rejected during constant evaluation on both GCC and Clang.

3 In a single-object delete expression, if the static type of the object to be deleted is not similar (7.3.6[conv.qual]) to its dynamic type and the selected deallocation function (see below) is not a destroying operator delete, the static type shall be a base class of the dynamic type of the object to be deleted and the static type shall have a virtual destructor or the behavior is undefined (F.3.25[ubx:expr.delete.dynamic.type.differ]). In an array delete*∗*expression, if the dynamic type of the object to be deleted is not similar to its static type, the behavior is undefined (F.3.26[ubx:expr.delete.dynamic.array.dynamic. type.differ]).

##### Note

*∗***ubdef:** expr.delete.dynamic.type.differ **summary:** `delete` through a pointer whose static type differs from its dynamic type, with no virtual destructor. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track dynamic type of non-polymorphic objects **replacement:** None **implementations:** caught by ASan’s `new-delete-type-mismatch` on both compilers via allocation-size mismatch; rejected during constant evaluation on Clang.

##### Note

##### ubdef:

expr.delete.dynamic.array.dynamic.type.differ **summary:** `delete[]` whose static type differs from the array’s dynamic type. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track dynamic type of non-polymorphic objects **replacement:** None **implementations:** Partially caught by ASan’s `new-delete-type-mismatch` on both compilers when element sizes differ; rejected during constant evaluation on both GCC and Clang.

#### 7*.*6*.*4 Pointer-to-member operators [expr.mptr.oper]

Notes regarding 7.6.4[expr.mptr.oper], paragraphs 4-6:

4 Abbreviating *pm-expression*`.*`*cast-expression* as `E1.*E2`, `E1` is called the *object* *expression*. If the result of `E1` is an object whose type is not similar to the type of `E1`, or whose most derived object does not contain the member to which `E2` refers, the behavior is undefined (F.3.27[ubx:expr.mptr.oper.not.contain.member]).*∗*The expression `E1` is sequenced before the expression `E2`.

#### Note

*∗***ubdef:** expr.mptr.oper.not.contain.member **summary:** accessing a pointer-to-member whose target object lacks that member. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track which type the pointer to member originated from and the dynamic type of non-polymorphic objects **replacement:** None **implementations:** caught heuristically by AddressSanitizer (both compilers) and by both compilers’ constant evaluators.

6 If the result of `.*` or `->*` is a function, then that result can be used only as the operand for the function call operator `()`.

[*Example*:

calls the member function denoted by `ptr_to_mfct` for the object pointed to by `ptr_to_obj`. *— end* *example*]

In a `.*` expression whose object expression is an rvalue, the program is ill-formed if the second operand is a pointer to member function whose *ref-qualifier* is `&`, unless its *cv-qualifier-seq* is `const`. In a `.*` expression whose object expression is an lvalue, the program is ill-formed if the second operand is a pointer to member function whose *ref-qualifier* is `&&`. The result of a `.*` expression whose second operand is a pointer to a data member is an lvalue if the first operand is an lvalue and an xvalue otherwise. The result of a `.*` expression whose second operand is a pointer to a member function is a prvalue. If the second operand is the null member pointer value (7.3.13[conv.mem]), the behavior is undefined (F.3.28[ubx:expr.mptr.oper.member.func.null]).

#### Note

#### ubdef:

expr.mptr.oper.member.func.null **summary:** calling through a null pointer-to-member-function. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert null pointer check **replacement:** None **implementations:** Caught by both compilers’ constant evaluators.

#### 7*.*6*.*5 Multiplicative operators [expr.mul]

Modify section 7.6.5[expr.mul], paragraph 4:

:::wording

4 The binary / operator yields the quotient, and the binary % operator yields the re- mainder from the division of the first expression by the second. If the second operand of `/` or `%` is zero, <ins>then</ins> the <del>behavior</del><ins>operator yields an unspecified erroneous value and</ins> <ins>there</ins> is <ins>an implicit precondition that</ins> <del>undefined</del><ins>this does not occur</ins> (F.3.29[ubx:expr. mul.div.by.zero]).∗For integral operands, the / operator yields the algebraic quotient with any fractional part discarded;57 if the quotient a/b is representable in the type of the result, `(a/b)*b` `+` `a%b` is equal to `a`; otherwise, the <del>behavior of both</del> <del>a/b</del><ins>operator yields an unspecified erroneous value</ins> and <del>a%b</del><ins>there</ins> is <del>undefined</del><ins>an implicit</ins> <ins>precondition that this does not occur (6.11.2+a[basic.contract.implicit])</ins> (F.3.30[ubx:expr. mul.representable.type.result]).

:::

#### Note

*∗***ubdef:** expr.mul.div.by.zero **summary:** integer division/remainder and floating-point division by zero. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the second operand is zero **replacement:** Produce an erroneous result after checking the second operand **implementations:** the integer cases are caught by UBSan’s `integer-divide-by-zero` check, constant evaluation, and the P3850 prototype (both compilers, all semantics); floating-point division by zero is caught by UBSan’s `float-divide-by-zero` check, which is not part of the `undefined` group, and constant evaluation.

#### Note

#### ubdef:

expr.mul.representable.type.result **summary:** integer division or remainder whose quotient overflows, e.g., `INT_MIN` `/` `-1` or the paired `INT_MIN` `%` `-1`. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is valid **replacement:** Coerce into erroneous value **implementations:** exhaustively caught by UBSan’s `signed-integer-overflow` check, constant evaluation, and the P3850 prototype (both compilers, all semantics).

`57` This is often called truncation towards zero.

#### 7*.*6*.*6 Additive operators [expr.add]

Modify and note section 7.6.6[expr.add], paragraphs 4-6:

4 When an expression `J` that has integral type is added to or subtracted from an expression `P` of pointer type, the result has the type of `P`.
