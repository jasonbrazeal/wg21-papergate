- If `P` evaluates to a null pointer value and `J` evaluates to 0, the result is a null pointer value.
- Otherwise, if `P` points to a (possibly-hypothetical) array element *i* of an array object `x` with *n* elements (9.3.4.5[dcl.array]),`58` the expressions `P` `+` `J` and `J` `+` `P` (where `J` has the value *j*) point to the (possibly-hypothetical) array element *i* + *j* of `x` if 0 *≤**i* + *j* *≤**n* and the expression `P` `-` `J` points to the (possibly-hypothetical) array element *i* *−**j* of `x` if 0 *≤**i* *−**j* *≤**n*.
- Otherwise, the behavior is undefined (F.3.31[ubx:expr.add.out.of.bounds]).*∗*

[*Note*: Adding a value other than 0 or 1 to a pointer to a base class subobject, a member subobject, or a complete object results in undefined behavior. *— end* *note*]

#### Note

*∗***ubdef:** expr.add.out.of.bounds **summary:** forming a pointer beyond an array’s one-past-the-end bound. **runtime-checkable:** Yes **locally-checkable:** Only if the array bound is statically known **checking:** Track pointer provenance, insert bounds check **replacement:** None **implementations:** `.known` fully checked by the P3850 bounds check (all semantics, both compilers) and rejected during constant evaluation on both compilers; `.unknown` only heuristically by AddressSanitizer, and also rejected during constant evaluation on both compilers; `.pointer.arithmetic` by UBSan’s `pointer-overflow` check on both compilers.

`58` As specified in 6.9.5[basic.compound], an object that is not an array element is considered to belong to a single-element array for this purpose and a pointer past the last element of an array of *n* elements is considered to be equivalent to a pointer to a hypothetical array element *n* for this purpose.

5 The result of subtracting two pointer expressions `P` and `Q` is a prvalue of type `std::ptrdiff_t` (17.2.4[support.types.layout]).

:::wording

— (5.1) If P and Q both evaluate to null pointer values, the value is 0. — (5.2) Otherwise, if P and Q point to, respectively, array elements i and j of the same array object x, the expression P - Q has the value i −j. If the value i −j is not in the range of representable values of type `std::ptrdiff_t`, the <del>behavior</del><ins>result</ins> is <del>undefined</del><ins>an unspecified erroneous value and there is an implicit precondition that</ins> this does not occur (F.3.32[ubx:expr.sub.pointers.representable]).∗

:::

— (5.3) Otherwise, the behavior is undefined (F.3.33[ubx:expr.add.sub.diff.pointers]).*†*

#### Note

*∗***ubdef:** expr.sub.pointers.representable **summary:** subtracting two pointers into the same array when the index difference overflows `std::ptrdiff_t`. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Verify that overflow does not occur when converting to `std::ptrdiff_t` **replacement:** Coerce into erroneous value **implementations:** None

#### Note

*†* **ubdef:** expr.add.sub.diff.pointers **summary:** subtracting pointers into two different, unrelated arrays. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track pointer provenance, verify both operands point into the same array object **replacement:** None **implementations:** caught at run time by AddressSanitizer’s `pointer-subtract` check (stock and integrated) on both compilers, and rejected during constant evaluation on both GCC and Clang.

6 For addition or subtraction, if the expressions `P` or `Q` have type “pointer to *cv* `T`”, where `T` and the array element type are not similar (7.3.6[conv.qual]), the behavior is undefined (F.3.34[ubx:expr.add.not.similar]).*∗*

[*Example*:

```cpp
unsigned int *p = reinterpret_cast<unsigned int*>(arr + 1);
unsigned int k = *p;  // OK, value of k is 2 (7.3.2[conv.lval])
unsigned int *q = p + 1;  // undefined behavior: p points to an int, not an unsigned int object
```

*— end* *example*]

#### Note

*∗***ubdef:** expr.add.not.similar **summary:** pointer arithmetic advancing by the wrong per-element size (dissimilar pointer/array types). **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type **replacement:** None **implementations:** Rejected during constant evaluation on both compilers.

#### 7*.*6*.*7 Shift operators [expr.shift]

Modify section 7.6.7[expr.shift], paragraph 1:

1 The shift operators `<<` and `>>` group left-to-right.

*shift-expression*: *additive-expression* *shift-expression* `<<` *additive-expression* *shift-expression* `>>` *additive-expression*

:::wording

The operands shall be prvalues of integral or unscoped enumeration type and integral promotions are performed. The type of the result is that of the promoted left operand. <del>The behavior</del><ins>There</ins> is <del>undefined (F.3.35[ubx:expr.shift.neg.and.width]) if</del><ins>an</ins> <ins>implicit precondition that</ins> the right operand is <del>negative, or greater</del><ins>nonnegative and</ins> <ins>less</ins> than <del>or equal to</del> the width of the promoted left operand <ins>(6.11.2+a[basic.contract.</ins> <ins>implicit]) (F.3.35[ubx:expr.shift.neg.and.width]); if not, an unspecified erroneous value</ins> <ins>is produced</ins>.

:::

#### Note

#### ubdef:

expr.shift.neg.and.width **summary:** shifting by a negative amount or by the type’s bit width or more. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert check whether right operand is valid **replacement:** Coerce into erroneous value **implementations:** exhaustively caught by UBSan’s `shift` check, constant evaluation, and the P3850 prototype (both compilers, all semantics).

#### 7*.*6*.*19 Assignment and compound assignment operators [expr.assign]

Notes regarding 7.6.19[expr.assign], paragraph 8:

8 If the value being stored in an object is read via another object that overlaps in any way the storage of the first object, then the overlap shall be exact and the two objects shall have the same type, otherwise the behavior is undefined *(F.3.36[ubx:expr.assign.overlap]).∗*

[*Note*: This restriction applies to the relationship between the left and right sides of the assignment operation; it is not a statement about how the target of the assignment can be aliased in general. See 7.2.1[basic.lval]. *— end* *note*]

#### Note

*∗***ubdef:** expr.assign.overlap **summary:** an assignment whose source and destination overlap in storage. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Check overlap of the two address ranges **replacement:** None **implementations:** None

8 **Statements** **[stmt]**

### 8*.*8 Jump statements [stmt.jump]

#### 8*.*8*.*4 The `return` statement [stmt.return]

Modify section 8.8.4[stmt.return], paragraph 4:

:::wording

4 Flowing off the end of a constructor, a destructor, or a non-coroutine function with a cv void return type is equivalent to a return with no operand. Otherwise, flowing off the end of a function that is neither main (6.10.3.1[basic.start.main]) nor a coroutine (9.6.4[dcl. fct.def.coroutine]) <del>results in undefined behavior</del><ins>initializes the storage of the return value</ins> <ins>with unspecified erroneous values, with an implicit precondition assertion that this does</ins> <ins>not occur (6.11.2+a[basic.contract.implicit])</ins> (F.4.1[ubx:stmt.return.flow.off]).

:::

#### Note

#### ubdef:

stmt.return.flow.off **summary:** a value-returning function flowing off its end without a `return`. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Equivalent to implicitly inserting a `contract_assert(false)` at end of the *function-body*. **replacement:** As with automatic variables, we can initialize the storage for the return value with erroneous values. **implementations:** exhaustively caught by UBSan’s `return` check, constant evaluation, and the P3850 prototype (all available semantics, both compilers).

#### 8*.*8*.*5 The `co_return` statement [stmt.return.coroutine]

Notes regarding 8.8.5[stmt.return.coroutine], paragraph 4:

4 If overload resolution for *p*`.return_void()` succeeds, flowing off the end of a coroutine’s *function-body* is equivalent to a `co_return` with no operand; otherwise flowing off the end of a coroutine’s *function-body* results in undefined behavior (F.4.2[ubx:stmt.return. coroutine.flow.off]).

#### Note

#### ubdef:

stmt.return.coroutine.flow.off **summary:** a value-returning coroutine flowing off its body without a `co_return`. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert `contract_assert(false)` at end of *function-body* if no `return_void` function is provided **replacement:** No, we cannot fabricate an argument of a type suitable to invoke one of possibly many overloads of `return_value` on the promise type. **implementations:** Caught by the P3850 prototype.

### 8*.*10 Declaration statement [stmt.dcl]

Notes regarding 8.10[stmt.dcl], paragraph 4:

4 Dynamic initialization of a block variable with static storage duration (6.8.6.2[basic.stc. static]) or thread storage duration (6.8.6.3[basic.stc.thread]) is performed the first time control passes through its declaration; such a variable is considered initialized upon the completion of its initialization. If the initialization exits by throwing an exception, the initialization is not complete, so it will be tried again the next time control enters the declaration. If control enters the declaration concurrently while the variable is being initialized, the concurrent execution shall wait for completion of the initialization.

[*Note*: A conforming implementation cannot introduce any deadlock around execution of the initializer. Deadlocks might still be caused by the program logic; the implementation need only avoid deadlocks due to its own synchronization operations. *— end* *note*]

If control re-enters the declaration recursively while the variable is being initialized, the behavior is undefined (F.4.3[ubx:stmt.dcl.local.static.init.recursive]).*∗*

[*Example*:

```cpp
  static int s = foo(2*i);  // undefined behavior: recursive call
  return i+1;
}
```

*— end* *example*]

### Note

*∗***ubdef:** stmt.dcl.local.static.init.recursive **summary:** recursively re-entering a block-scope `static` variable’s initializer. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Insert a recursion counter into a guard for static and thread-local object construction **replacement:** None **implementations:** None

9 **Declarations** **[dcl]**

### 9*.*2 Specifiers [dcl.spec]

#### 9*.*2*.*9 Type specifiers [dcl.type]

##### 9*.*2*.*9*.*2 The *cv-qualifier*s [dcl.type.cv]

Notes regarding 9.2.9.2[dcl.type.cv], paragraphs 5-6:

5 Any attempt to modify (7.6.19[expr.assign], 7.6.1.6[expr.post.incr], 7.6.2.3[expr.pre.incr]) a const object (6.9.6[basic.type.qualifier]) during its lifetime (6.8.4[basic.life]) results in undefined behavior (F.5.1[ubx:dcl.type.cv.modify.const.obj]).*∗*

[*Example*:

```cpp
ci = 4;  // error: attempt to modify const
int i = 2;  // not cv-qualified
const int* cip;  // pointer to const int
cip = &i;  // OK, cv-qualified access path to unqualified
*cip = 4;  // error: attempt to modify through ptr to const
int* ip;
ip = const_cast<int*>(cip);  // cast needed to convert const int* to int*
*ip = 4;  // defined: *ip points to i, a non-const object
const int* ciq = new const int(3);  // initialized as required
int* iq = const_cast<int*>(ciq);  // cast required
*iq = 4;  // undefined behavior: modifies a const object
```

For another example,

```cpp
  mutable int i;
  int j;
};
struct Y {
  X x;
  Y();
};
const Y y;
y.x.i++;  // well-formed: mutable member can be modified
y.x.j++;  // error: const-qualified member modified
Y* p = const_cast<Y*>(&y);  // cast away const-ness of y
p->x.i = 99;  // well-formed: mutable member can be modified
p->x.j = 99;  // undefined behavior: modifies a const subobject
```

*— end* *example*]

##### Note

*∗***ubdef:** dcl.type.cv.modify.const.obj **summary:** modifying a `const` object, even via a `const_cast`-obtained pointer. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with a `const` object **replacement:** None **implementations:** Rejected during constant evaluation on both compilers.

6 The semantics of an access through a volatile glvalue are implementation-defined. If an attempt is made to access an object defined with a volatile-qualified type through the use of a non-volatile glvalue, the behavior is undefined (F.5.2[ubx:dcl.type.cv.access.volatile]).

##### Note

##### ubdef:

dcl.type.cv.access.volatile **summary:** accessing a `volatile`-qualified object through a non- `volatile` glvalue. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with a `volatile` object **replacement:** None **implementations:** Rejected during constant evaluation on Clang.

### 9*.*3 Declarators [dcl.decl]

#### 9*.*3*.*4 Meaning of declarators [dcl.meaning]

##### 9*.*3*.*4*.*3 References [dcl.ref]

Notes regarding 9.3.4.3[dcl.ref], paragraph 7:

7 Attempting to bind a reference to a function where the converted initializer is a glvalue whose type is not call-compatible (7.6.1.3[expr.call]) with the type of the function’s definition results in undefined behavior (F.5.3[ubx:dcl.ref.incompatible.function]).*∗*Attempting to bind a reference to an object where the converted initializer is a glvalue through which the object is not type-accessible (7.2.1[basic.lval]) results in undefined behavior (F.5.4[ubx:dcl.ref.incompatible.type]).*†*

[*Note*: The object designated by such a glvalue can be outside its lifetime (6.8.4[basic.life]). Because a null pointer value or a pointer past the end of an object does not point to an object, a reference in a well-defined program cannot refer to such things; see 7.6.2.2[expr.unary.op]. As described in 11.4.10[class.bit], a reference cannot be bound directly to a bit-field. *— end* *note*]

The behavior of an evaluation of a reference (7.5.5[expr.prim.id], 7.6.1.5[expr.ref]) that does not happen after (6.10.2.2[intro.races]) the initialization of the reference is undefined (F.5.5[ubx:dcl.ref.uninitialized.reference]).*‡*

[*Example*:

```cpp
int &g();
extern int &ir3;
int *ip = 0;
int &ir1 = *ip;  // undefined behavior: null pointer
int &ir2 = f(ir3);  // undefined behavior: ir3 not yet initialized
int &ir3 = g();
int &ir4 = f(ir4);  // undefined behavior: ir4 used in its own initializer
char x alignas(int);
int &ir5 = *reinterpret_cast<int *>(&x);  // undefined behavior: initializer refers to char object
```

*— end* *example*]

##### Note

*∗***ubdef:** dcl.ref.incompatible.function **summary:** binding a reference to a function of a call-incompatible type. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track the types of all functions based on their addresses **replacement:** None **implementations:** UBSan’s `function` (part of `undefined`) check catches it on Clang.

##### Note

*†* **ubdef:** dcl.ref.incompatible.type **summary:** binding a reference to an object via a type-incompatible (strict-aliasing) access. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type **replacement:** None **implementations:** None

##### Note

*‡* **ubdef:** dcl.ref.uninitialized.reference **summary:** evaluating a reference before it has actually been initialized. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether references have been initialised **replacement:** None **implementations:** None

### 9*.*6 Function definitions [dcl.fct.def]

#### 9*.*6*.*4 Coroutine definitions [dcl.fct.def.coroutine]

Notes regarding 9.6.4[dcl.fct.def.coroutine], paragraphs 9-12:

9 A suspended coroutine can be resumed to continue execution by invoking a re- sumption member function (17.13.4.6[coroutine.handle.resumption]) of a coroutine handle (17.13.4[coroutine.handle]) that refers to the coroutine. The evaluation that invoked a resumption member function is called the *resumer*. Invoking a resumption member function for a coroutine that is not suspended results in undefined behavior (F.5.6[ubx:dcl.fct.def.coroutine.resume.not.suspended]).

#### Note

#### ubdef:

dcl.fct.def.coroutine.resume.not.suspended **summary:** calling `resume()` on a coroutine handle that is not suspended. **runtime-checkable:** Yes **locally-checkable:** No, requires additional instrumentation **checking:** Track (in a thread-safe fashion) the suspension state associated with every coroutine handle **replacement:** None **implementations:** AddressSanitizer will catch many cases as a use-after-free.

12 The coroutine state is destroyed when control flows off the end of the coroutine or the `destroy` member function (17.13.4.6[coroutine.handle.resumption]) of a coroutine handle (17.13.4[coroutine.handle]) that refers to the coroutine is invoked. In the latter case, control in the coroutine is considered to be transferred out of the function (8.10[stmt. dcl]). The storage for the coroutine state is released by calling a non-array deallocation function (6.8.6.5.3[basic.stc.dynamic.deallocation]). If `destroy` is called for a coroutine that is not suspended, the program has undefined behavior (F.5.7[ubx:dcl.fct.def.coroutine. destroy.not.suspended]).

#### Note

#### ubdef:

dcl.fct.def.coroutine.destroy.not.suspended **summary:** calling `destroy()` on a coroutine handle that is not suspended. **runtime-checkable:** Yes **locally-checkable:** No, requires additional instrumentation **checking:** Track (in a thread-safe fashion) the suspension state associated with every coroutine handle **replacement:** None **implementations:** AddressSanitizer (use-after-free/double-free) catches it on both compilers.

### 9*.*13 Attributes [dcl.attr]

#### 9*.*13*.*3 Assumption attribute [dcl.attr.assume]

Modify section 9.13.3[dcl.attr.assume], paragraphs 1-3:

1 The *attribute-token* `assume` may be applied to a null statement; such a statement is an *assumption*. An *attribute-argument-clause* shall be present and shall have the form:

`(` *conditional-expression* `)`

:::wording

The expression is contextually converted to bool (7.3.1[conv.general]). The expression is not evaluated <ins>and the assumption has no effect</ins>. <del>If</del><ins>There is an implicit</ins> <ins>precondition assertion that</ins> the converted expression would evaluate to`true` <del>at the point</del> <del>where the assumption appears, the assumption has no effect.</del> <del>Otherwise, evaluation</del> <del>of the assumption has runtime-undefined behavior</del> <ins>(6.11.2+a[basic.contract.implicit])</ins> (F.5.8[ubx:dcl.attr.assume.false]).

:::

#### Note

#### ubdef:

dcl.attr.assume.false **summary:** reaching an `[[assume(expr)]]` attribute while `expr` is false. **runtime-checkable:** Not in general, UB is based on the hypothetical result of an arbitrary expression that cannot be evaluated if it might have side effects. **locally-checkable:** Yes, if checkable at all.

**checking:** No automatic checking strategy is possible because the predicate cannot be, in general, proven to be free of side effects; instead, the user has to change `[[assume(x)]]` to `contract_assert<may_be_assumed>(x)` and select an appropriate evaluation semantic **replacement:** Ignore the assumption **implementations:** P3850-native check covers the side-effect-free `.pure` sub- group with every semantic on both compilers, plus a `constexpr` catch on both compilers; the opaque `.nonpure` subgroup supports only *assume* and *ignore*.

2 [*Note*: The expression is potentially evaluated (6.3[basic.def.odr]). The use of assumptions is intended to allow implementations to analyze the form of the expression and deduce information used to optimize the program. Implementations are not required to deduce any information from any particular assumption. It is expected that the value of a *has-attribute-expression* for the `assume` attribute is `0` if an implementation does not attempt to deduce any such information from assumptions. *— end* *note*]

3 [*Example* *1*:

:::wording

int divide_by_32(int x) { [[assume(x &gt;= 0)]]; <ins>// Implicit precondition that x &gt;= 0</ins> `return` `x/32;`<del>␣␣␣␣</del> // <del>The instructions produced for the division</del><ins>If assumed, may omit handling of</ins> <del>␣␣␣␣</del> // <del>may omit handling of</del> negative values<del>.</del> } int f(int y) { `[[assume(++y` `==` `43)]];`<del>␣␣␣␣</del> // y is not incremented `return` `y;`<del>␣␣␣␣</del> // <del>statement</del><ins>If assumed,</ins> may <del>be replaced with return 42;</del><ins>return 42</ins> }

:::

*— end* *example*]

#### 9*.*13*.*10 Noreturn attribute [dcl.attr.noreturn]

Notes regarding 9.13.10[dcl.attr.noreturn], paragraph 3:

3 If a function `f` is invoked where `f` was previously declared with the `noreturn` attribute and that invocation eventually returns, the behavior is runtime-undefined (F.5.9[ubx:dcl. attr.noreturn.eventually.returns]).*∗*

[*Note*: The function can terminate by throwing an exception. *— end* *note*]

#### Note

*∗***ubdef:** dcl.attr.noreturn.eventually.returns **summary:** a `[[noreturn]]`-declared function returns to its caller anyway. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert `post(false)` **replacement:** Return normally. This would require both the caller and callee translation unit to ignore instead of assume that the function does not return. **implementations:** UBSan’s `unreachable` check (own diagnostic) catches it on both Clang and GCC.

11 **Classes** **[class]**

### 11*.*4 Class members [class.mem]

#### 11*.*4*.*7 Destructors [class.dtor]

Notes regarding 11.4.7[class.dtor], paragraph 19:

19 Once a destructor is invoked for an object, the object’s lifetime ends; the behavior is undefined (F.6.1[ubx:class.dtor.no.longer.exists]) if the destructor is invoked*∗*for an object whose lifetime has ended (6.8.4[basic.life]).

[*Example*: If the destructor for an object with automatic storage duration is explicitly invoked, and the block is subsequently left in a manner that would ordinarily invoke implicit destruction of the object, the behavior is undefined. *— end* *example*]

#### Note

*∗***ubdef:** class.dtor.no.longer.exists **summary:** invoking a destructor on an object whose lifetime has already ended. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** `.nonpolymorphic` caught only by constant evaluation (both compilers); `.polymorphic` caught at runtime by UBSan’s `vptr` check on GCC only.

### 11*.*7 Derived classes [class.derived]

#### 11*.*7*.*4 Abstract classes [class.abstract]

Notes regarding 11.7.4[class.abstract], paragraph 7:

7 Member functions can be called from a constructor (or destructor) of an abstract class; the effect of making a virtual call (11.7.3[class.virtual]) to a pure virtual function directly or indirectly for the object being created (or destroyed) from such a constructor (or destructor) is undefined (F.6.2[ubx:class.abstract.pure.virtual]).

#### Note

#### ubdef:

class.abstract.pure.virtual **summary:** calling a pure virtual function from a constructor or destructor. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a `pre(false)` into the pure virtual stub pointed to from the base-class vtable **replacement:** None **implementations:** rejected during constant evaluation on both compilers; and, in the P3850 prototype, checkable at run time on both compilers.

### 11*.*9 Initialization [class.init]

#### 11*.*9*.*3 Initializing bases and members [class.base.init]

Notes regarding 11.9.3[class.base.init], paragraph 19:

19 Member functions (including virtual member functions, 11.7.3[class.virtual]) can be called for an object under construction or destruction. Similarly, an object under construction or destruction can be the operand of the `typeid` operator (7.6.1.8[expr.typeid]) or of a `dynamic_cast` (7.6.1.7[expr.dynamic.cast]). However, if these operations are performed during evaluation of

- a *ctor-initializer* (or in a function called directly or indirectly from a *ctor-initializer*) before all the *mem-initializer*s for base classes have completed,
- a precondition assertion of a constructor, or
- a postcondition assertion of a destructor (9.4.1[dcl.contract.func]), the program has undefined behavior (F.6.3[ubx:class.base.init.mem.fun]).*∗*

[*Example*:

```cpp
public:
  A(int);
};
class B : public A {
  int j;
public:
  int f();
  B() : A(f()),  // undefined behavior: calls member function but base A not yet initialized
  j(f()) { }  // well-defined: bases are all initialized
};
class C {
public:
  C(int);
};
class D : public B, C {
  int i;
public:
  D() : C(f()),  // undefined behavior: calls member function but base C not yet initialized
  i(f()) { }  // well-defined: bases are all initialized
};
```

*— end* *example*]

#### Note

*∗***ubdef:** class.base.init.mem.fun **summary:** calling a member function outside the base classes’ constructed lifetime. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** For polymorphic types, this can be caught by UBSan’s `vptr`, generally consistently for GCC when nothing else has written to the object’s storage.

#### 11*.*9*.*5 Construction and destruction [class.cdtor]

Notes regarding 11.9.5[class.cdtor], paragraphs 2-7:

2 For an object with a non-trivial constructor, referring to any non-static member or base class of the object before the constructor begins execution results in undefined behavior (F.6.4[ubx:class.cdtor.before.ctor]).*∗*For an object with a non-trivial destructor, referring to any non-static member or base class of the object after the destructor finishes execution results in undefined behavior (F.6.5[ubx:class.cdtor.after.dtor]).*†*

[*Example*:

```cpp
struct Y : X { Y(); };  // non-trivial
struct A { int a; };
struct B : public A { int j; Y y; };  // non-trivial
extern B bobj;
B* pb = &bobj;  // OK
int* p1 = &bobj.a;  // undefined behavior: refers to base class member
int* p2 = &bobj.y.i;  // undefined behavior: refers to member’s member
```

```cpp
A* pa = &bobj;  // undefined behavior: upcast to a base class type
B bobj;  // definition of bobj
extern X xobj;
int* p3 = &xobj.i;  // OK, all constructors of X are trivial
X xobj;
```

For another example,

```cpp
struct X : public virtual W { };
struct Y {
  int* p;
  X x;
  Y() : p(&x.j) {  // undefined, x is not yet constructed
    }
};
```

*— end* *example*]

#### Note

*∗***ubdef:** class.cdtor.before.ctor **summary:** referring to a member or base of an object before its constructor has begun. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** Accesses in non-polymorphic objects are not generally caught. Accesses in polymorphic types are caught, heuristically, by UBSan’s `vptr` check on both compilers. GCC accepts non-polymorphic cases at compile time while Clang does not.

#### Note

*†* **ubdef:** class.cdtor.after.dtor **summary:** referring to a member or base of an object after its destructor has run. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** split by polymorphism – `.polymorphic` caught by UBSan’s `vptr` check on GCC only; `.nonpolymorphic` rejected during constant evaluation on both compilers.

4 To explicitly or implicitly convert a pointer (a glvalue) referring to an object of class `X` to a pointer (reference) to a direct or indirect base class `B` of `X`, the construction of `X` and the construction of all of its direct or indirect bases that directly or indirectly derive from `B` shall have started and the destruction of these classes shall not have completed, otherwise the conversion results in undefined behavior (F.6.6[ubx:class.cdtor.convert.pointer]).*∗*To form a pointer to (or access the value of) a direct non-static member of an object `obj`, the construction of `obj` shall have started and its destruction shall not have completed, otherwise the computation of the pointer value (or accessing the member value) results in undefined behavior (F.6.7[ubx:class.cdtor.form.pointer]).*†*

[*Example*:

```cpp
struct B : virtual A { };
struct C : B { };
struct D : virtual A { D(A*); };
struct X { X(A*); };
struct E : C, D, X {
  E() : D(this),  // undefined behavior: upcast from E* to A* might use path E* →D* →A*
                    // but D is not constructed
```

```cpp
                    // “D((C*)this)” would be defined: E* →C* is defined because E() has started,
                    // and C* →A* is defined because C is fully constructed
  X(this) {}  // defined: upon construction of X, C/B/D/A sublattice is fully constructed
};
```

*— end* *example*]

#### Note

*∗***ubdef:** class.cdtor.convert.pointer **summary:** converting a pointer to a base class during that base’s not-yet-constructed or already-destroyed window. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** None

#### Note
