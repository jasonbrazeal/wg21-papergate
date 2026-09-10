## 6 Proposed wording

After the adoption of [P3596R3], and with the followups proposed by [P4284R0], each instance of undefined behaviour in the wording is annotated with a link to the annex. Wherever these occur, we have included notes containing our description and summary of how we are handling each particular instance of undefined behaviour. Those notes are called out with markers in this text (like *∗*, *†*, or *‡*, or multiples when we have particularly dense commentary on a section) along with explanations that follow in larger purple boxes.

In general when there is no fallback behaviour being introduced there is also no actual wording change, as the implicit contract assertion that is needed is introduced in basic.contract.implicit. This extra wording context and the corresponding purple boxes are to facilitate wording review by both EWG and CWG so that we can verify that the desired changes to existing undefined behaviour have been properly captured.

The wording in this document has been based off the changes in [P4284R0], which include the latest updates to the UB and IFNDR annexes on top of [P3596R3]. A companion paper, [P4277R0], contains significant additional commentary on all of the wording changes, along with details on the implementation experience with introducing runtime checks for each of these undefined behaviours.

These wording changes are relative to the C++29 draft sources with git hash [cfa21fec](https://github.com/cplusplus/draft/tree/cfa21fecf8d3610de0601cac858c2edbc39f64f0), last modified on Thu, 13 Aug 2026 13:55:07 -0400.

3 **Terms** **and** **definitions** **[intro.defs]**

### 3*.65* + *a* unconstrained behavior [defns.unconstrained]

:::wording-add

Add a new definition <ins>3.65+a</ins>[defns.unconstrained] after 3.65[defns.unblock]

:::

### 3*.65* + *a* [defns.unconstrained]

**unconstrained** **behavior** behavior for which this document imposes no requirements

:::wording-add

[Note to entry 1: Unconstrained behavior is expected whenever a contract assertion with the assume semantic (6.11.2[basic.contract.eval]) is violated or control continues after the guarding contract assertion (6.11.2+a[basic.contract.implicit]) of undefined behavior. — end note]

:::

:::wording-add

[Note to entry 2: Permissible unconstrained behavior ranges from ignoring the situation completely with unpredictable results, to behaving during translation or program execution in a documented manner characteristic of the environment (with or without the issuance of a diagnostic message (defns.diagnostic)), to terminating a translation or execution (with the issuance of a diagnostic message). — end note]

:::

### 3*.*66 undefined behavior [defns.undefined]

Modify definition 3.66[defns.undefined]:

:::wording

3.66 [defns.undefined] undefined behavior behavior <del>for which this document</del><ins>that begins with an implicit contract assertion</ins> <del>imposes</del> <del>no requirements</del><ins>that the behavior cannot occur (6.11.2+a[basic.contract.implicit]) and,</ins> <ins>if control continues after the contract assertion, has unconstrained behavior.</ins>

:::

:::wording

[Note to entry 1: Undefined behavior may be expected when this document omits any explicit definition of behavior or when a program uses an incorrect construct or invalid data. <del>Permissible</del> <del>undefined behavior ranges from ignoring the situation completely with unpredictable results,</del> <del>to behaving during translation or program execution in a documented manner characteristic</del> <del>of the environment (with or without the issuance of a diagnostic message (defns.diagnostic)),</del> <del>to terminating a translation or execution (with the issuance of a diagnostic message).</del> Many incorrect program constructs do not engender undefined behavior; they are required to be diagnosed. <ins>There is no requirement that any particular semantic choice be available for the</ins> <ins>implicit contract assertion. — end note]</ins>

:::

[*Note* *to* *entry* *1+a*: Evaluation of a constant expression (7.7.2[expr.const.core]) never exhibits behavior explicitly specified as undefined in Clause 4[intro] through Clause 15[cpp]. *— end* *note*]

4 **General** **principles** **[intro]**

### 4*.*1 Implementation compliance [intro.compliance]

#### 4*.*1*.*1 General [intro.compliance.general]

Modify section 4.1.1[intro.compliance.general], paragraphs 1-2:

:::wording

1 The set of diagnosable rules consists of all syntactic and semantic rules in this document except for those rules containing an explicit notation that “no diagnostic is required” or which are described as resulting in “<del>undefined</del><ins>unconstrained</ins> behavior”.

:::

#### Note

Many behaviors are described as resulting in undefined behavior, and when control continues past the guarding contract assertion of that behavior they then result in undefined behavior.

2 Although this document states only requirements on C++ implementations, those requirements are often easier to understand if they are phrased as requirements on programs, parts of programs, or execution of programs. Such requirements have the following meaning:

- (2.1) If a program contains no violations of the rules in Clause 5[lex] through Clause 33[exec] as well as those specified in Annex D[depr], a conforming implementation shall accept and correctly execute`3` that program, except when the implementation’s limitations (see below) are exceeded.
- (2.2) If a program contains a violation of a rule for which no diagnostic is required, this document places no requirement on implementations with respect to that program.
- (2.3) Otherwise, if a program contains

- a violation of any diagnosable rule,
- a preprocessing translation unit with a `#warning` preprocessing directive (15.9[cpp.error]),
- an occurrence of a construct described in this document as “conditionallysupported” when the implementation does not support that construct, or
- a contract assertion (6.11.2[basic.contract.eval]) evaluated with a checking semantic in a manifestly constant-evaluated context (7.7.7[expr.const.defns]) resulting in a contract violation, a conforming implementation shall issue at least one diagnostic message.

[*Note* *1*: During template argument deduction and substitution, certain constructs that in other contexts require a diagnostic are treated differently; see 13.10.3[temp.deduct]. *— end* *note*]

Furthermore, a conforming implementation shall not accept

- (2.1) a preprocessing translation unit containing a `#error` preprocessing directive (15.9[cpp.error]),
- (2.2) a translation unit with a *static_assert-declaration* that fails (9.1[dcl.pre]), or
- (2.3) a contract assertion evaluated with a terminating semantic (6.11.2[basic.contract.eval]) in a manifestly constant-evaluated context (7.7.7[expr.const.defns]) resulting in a contract violation.

3 “Correct execution” can include undefined behavior, unconstrained behavior, and erroneous behavior, depending on the data being processed; see Clause 3[intro.defs] and 6.10.1[intro.execution].

#### 4*.*1*.*2 Abstract machine [intro.abstract]

Add a paragraph to and modify section 4.1.2[intro.abstract], paragraphs 4-6:

:::wording-add

3+a Certain operations are described in this document as undefined behavior (for example, the effect of attempting to modify a const object). Such operations evaluate a guarding contract assertion, which is an implicit contract assertion that they do not occur (6.11.2+a[basic.contract.implicit]). If control continues normally after a guarding contract assertion, the behavior is unconstrained.

:::

:::wording

4 Certain <del>other</del> operations are described in this document as <del>undefined</del><ins>unconstrained</ins> behavior (for example, <ins>control continuing after evaluating</ins> the <del>effect of</del><ins>guarding contract</ins> <ins>assertion</ins> <del>attempting to modify a const object</del><ins>associated with an instance of undefined</ins> <ins>behavior (6.11.2+a[basic.contract.implicit])</ins>).

:::

5 Certain events in the execution of a program are termed *observable* *checkpoints*.

[*Note* *1*: A call to `std::observable_checkpoint` (22.2.9[utility.undefined]) is an observable checkpoint, as are certain parts of the evaluation of contract assertions (6.11[basic.contract]). *— end* *note*]

:::wording-add

[Note 1+a: Undefined behavior whose guarding contract assertion is evaluated with the ignore or assume semantic does not imply an observable checkpoint. — end note]

:::

:::wording

6 The defined prefix of an execution comprises the operations O for which for every <del>undefined</del><ins>unconstrained</ins> operation U there is an observable checkpoint C such that O happens before C and C happens before U.

:::

[*Note* *2*: The undefined behavior that arises from a data race (6.10.2.2[intro.races]) occurs on all participating threads. *— end* *note*]

:::wording

A conforming implementation executing a well-formed program shall produce the observable behavior of the defined prefix of one of the possible executions of the corresponding instance of the abstract machine with the same program and the same input. If the selected execution contains an <del>undefined</del><ins>unconstrained</ins> operation, the implementation executing that program with that input may produce arbitrary additional observable behavior afterwards. If the execution of an operation is specified as having erroneous behavior, the implementation is permitted to issue a diagnostic and is permitted to terminate the execution of the program.

:::

6 **Basics** **[basic]**

### 6*.*8 Memory and objects [basic.memobj]

#### 6*.*8*.*2 Object model [intro.object]

Notes regarding 6.8.2[intro.object], paragraphs 13-14:

13 Some operations are described as *implicitly* *creating* *objects* within a specified region of storage. For each operation that is specified as implicitly creating objects, that operation implicitly creates and starts the lifetime of zero or more objects of implicit-lifetime types (6.9.1[term.implicit.lifetime.type]) in its specified region of storage if doing so would result in the program having defined behavior. If no such set of objects would give the program defined behavior (F.2.1[ubx:intro.object.implicit.create]),*∗*the behavior of the program is undefined. If multiple such sets of objects would give the program defined behavior, it is unspecified which such set of objects is created.

[*Note*: Such operations do not start the lifetimes of subobjects of such objects that are not themselves of implicit-lifetime types. *— end* *note*]

#### Note

*∗***ubdef:** intro.object.implicit.create **summary:** using storage in a way no choice of implicitly-created object could make well-defined. **runtime-checkable:** Not generally, requires predicting whether the object will be used correctly as a given type **locally-checkable:** No **checking:** None **replacement:** None **implementations:** None

14 Further, after implicitly creating objects within a specified region of storage, some operations are described as producing a pointer to a *suitable* *created* *object*. These operations select one of the implicitly-created objects whose address is the address of the start of the region of storage, and produce a pointer value that points to that object, if that value would result in the program having defined behavior. If no such pointer value would give the program defined behavior, the behavior of the program is undefined (F.2.2[ubx:intro.object.implicit.pointer]).*∗*If multiple such pointer values would give the program defined behavior, it is unspecified which such pointer value is produced.

#### Note

*∗***ubdef:** intro.object.implicit.pointer **summary:** producing a pointer to an implicitly-created object when no pointer value into that storage is well-defined. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage can hold implicit lifetime objects **replacement:** None **implementations:** None

#### 6*.*8*.*3 Alignment [basic.align]

Notes regarding 6.8.3[basic.align], paragraph 1:

1 Object types have *alignment* *requirements* (6.9.3[basic.fundamental], 6.9.5[basic. compound]) which place restrictions on the addresses at which an object of that type may be allocated. An *alignment* is an implementation-defined integer value representing the number of bytes between successive addresses at which a given object can be allocated. An object type imposes an alignment requirement on every object of that type; stricter alignment can be requested using the *alignment-specifier* (9.13.2[dcl.align]). Attempting to create an object (6.8.2[intro.object]) in storage that does not meet the alignment requirements of the object’s type is undefined behavior (F.2.3[ubx:basic.align.object.alignment]).

#### Note

#### ubdef:

basic.align.object.alignment **summary:** placing an object at a storage address misaligned for its type. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert alignment check when creating or reading objects. **replacement:** None **implementations:** UBSan’s `alignment` check (stock and routed through the handler); and, in the P3850 prototype, a native middle-end check on both compilers.

#### 6*.*8*.*4 Lifetime [basic.life]

Notes regarding 6.8.4[basic.life], paragraphs 7-12:

7 Before the lifetime of an object has started but after the storage which the object will occupy has been allocated`16` or after the lifetime of an object has ended and before the storage which the object occupied is reused or released, any pointer that represents the address of the storage location where the object will be or was located may be used but only in limited ways. For an object under construction or destruction, see 11.9.5[class. cdtor]. Otherwise, such a pointer refers to allocated storage (6.8.6.5.2[basic.stc.dynamic. allocation]), and using the pointer as if the pointer were of type `void*` is well-defined. Indirection through such a pointer is permitted but the resulting lvalue may only be used in limited ways, as described below. The program has undefined behavior if:

— the pointer is used as the operand of a *delete-expression* (F.2.4[ubx:lifetime.outside. pointer.delete]),*∗*

— the pointer is used to access a non-static data member or call a non-static member function of the object (F.2.5[ubx:lifetime.outside.pointer.member]), or*†*

- the pointer is converted (7.3.12[conv.ptr], 7.6.1.9[expr.static.cast]) to a pointer to a virtual base class (F.2.6[ubx:lifetime.outside.pointer.virtual]) or*‡* to a base class thereof, or
- the pointer is used as the operand of a `dynamic_cast` (7.6.1.7[expr.dynamic.cast]) (F.2.7[ubx:lifetime.outside.pointer.dynamic.cast]).*∗∗*

[*Example*:

```cpp
struct B {
  virtual void f();
  void mutate();
  virtual ~B();
};
struct D1 : B { void f(); };
struct D2 : B { void f(); };
void B::mutate() {
  new (this) D2;  // reuses storage — ends the lifetime of *this
  f();  // undefined behavior
  ... = this;  // OK, this points to valid memory
}
void g() {
  void* p = std::malloc(sizeof(D1) + sizeof(D2));
  B* pb = new (p) D1;
  pb->mutate();
  *pb;  // OK, pb points to valid memory
  void* q = pb;  // OK, pb points to valid memory
  pb->f();  // undefined behavior: lifetime of *pb has ended
}
```

*— end* *example*]

`16` For example, before the dynamic initialization of an object with static storage duration (6.10.3.3[basic.

start.dynamic]).

#### Note

*∗***ubdef:** lifetime.outside.pointer.delete **summary:** `delete`-ing a pointer to an object whose lifetime has already ended. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** caught by constant evaluation on Clang.

#### Note

*†* **ubdef:** lifetime.outside.pointer.member **summary:** accessing a member through a pointer to an object outside its lifetime. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** caught by constant evaluation on both GCC and Clang.

#### Note

*‡* **ubdef:** lifetime.outside.pointer.virtual **summary:** converting a pointer outside its lifetime into a virtual base class pointer. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** heuristically caught by UBSan’s `vptr` check (detection relies on the ended object’s vtable still being recognizably invalid) and exhaustively caught by constant evaluation, on both GCC and Clang.

#### Note

*∗∗***ubdef:** lifetime.outside.pointer.dynamic.cast **summary:** `dynamic_cast` through a pointer to an object outside its lifetime. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** heuristically caught by UBSan’s `vptr` check on Clang (detection relies on the ended object’s vtable) and rejected in constant evaluation on Clang; GCC has no detection channel (it does not instrument `dynamic_cast` for `vptr`, and its constant evaluator accepts the cast).

8 Similarly, before the lifetime of an object has started but after the storage which the object will occupy has been allocated or after the lifetime of an object has ended and before the storage which the object occupied is reused or released, any glvalue that refers to the original object may be used but only in limited ways. For an object under construction or destruction, see 11.9.5[class.cdtor]. Otherwise, such a glvalue refers to allocated storage (6.8.6.5.2[basic.stc.dynamic.allocation]), and using the properties of the glvalue that do not depend on its value is well-defined. The program has undefined behavior if:

— the glvalue is used to access the object (F.2.8[ubx:lifetime.outside.glvalue.access]), or*∗*

— the glvalue is used to call a non-static member function of the object (F.2.9[ubx:lifetime.outside.glvalue.member]), or*†*

— the glvalue is bound to a reference to a virtual base class (9.5.4[dcl.init.ref]) (F.2.10[ubx:lifetime.outside.glvalue.virtual]), or*‡*

— the glvalue is used as the operand of a `dynamic_cast` (7.6.1.7[expr.dynamic.cast]) or as the operand of `typeid` (F.2.11[ubx:lifetime.outside.glvalue.dynamic.cast]).*∗∗*

[*Note*: Therefore, undefined behavior results if an object that is being constructed in one thread is referenced from another thread without adequate synchronization. *— end* *note*]

#### Note

*∗***ubdef:** lifetime.outside.glvalue.access **summary:** using a glvalue to read or write an object outside its lifetime (before construction completes or after it ends). **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** heuristically caught by AddressSanitizer on both compilers (default heap-use-after-free; extra flags for stack/overflow variants) and exhaustively caught by constant evaluation.

#### Note

*†* **ubdef:** lifetime.outside.glvalue.member **summary:** calling a non-static member function through a glvalue outside its lifetime. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** caught by constant evaluation on both GCC and Clang.

#### Note

*‡* **ubdef:** lifetime.outside.glvalue.virtual **summary:** binding a glvalue outside its lifetime to a virtual base class reference. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** heuristically caught by UBSan’s `vptr` check (detection relies on the ended object’s vtable still being recognizably invalid) and exhaustively caught by constant evaluation, on both GCC and Clang.

#### Note

*∗∗***ubdef:** lifetime.outside.glvalue.dynamic.cast **summary:** using a glvalue to a dead object as the operand of `dynamic_cast` or `typeid`. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** Clang heuristically catches it at run time via UBSan’s `vptr` check (both `noexcept`-enforce and `noexcept`-observe; detection relies on the ended object’s vtable); GCC has no run-time channel. Both compilers reject it in constant evaluation, though only incidentally – the virtual base makes the class ineligible for a constexpr constructor/destructor, so evaluation fails before the offending `dynamic_cast` is reached.

11 If a program ends the lifetime of an object of type `T` with static (6.8.6.2[basic.stc.static]), thread (6.8.6.3[basic.stc.thread]), or automatic (6.8.6.4[basic.stc.auto]) storage duration and if `T` has a non-trivial destructor,`17` and another object of the original type does not occupy that same storage location when the implicit destructor call takes place, the behavior of the program is undefined (F.2.12[ubx:original.type.implicit.destructor]). This is true*∗*even if the block is exited with an exception.

[*Example*:

```cpp
struct B {
  ~B();
};
void h() {
  B b;
  new (&b) T;
}  // undefined behavior at block exit
```

*— end* *example*]

`17` That is, an object for which a destructor will be called implicitly—upon exit from the block for an object with automatic storage duration, upon exit from the thread for an object with thread storage duration, or upon exit from the program for an object with static storage duration.

#### Note

*∗***ubdef:** original.type.implicit.destructor **summary:** an implicit destructor at scope exit running on storage reused for a different type. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Checking this would require maintaining type and lifetime information across an entire program. **replacement:** None **implementations:** None

12 Creating a new object within the storage that a const, complete object with static, thread, or automatic storage duration occupies, or within the storage that such a const object used to occupy before its lifetime ended, results in undefined behavior (F.2.13[ubx:creating. within.const.complete.obj]).*∗*

[*Example*:

```cpp
  B();
  ~B();
};
const B b;
void h() {
  b.~B();
  new (const_cast<B*>(&b)) const B;  // undefined behavior
}
```

*— end* *example*]

#### Note

*∗***ubdef:** creating.within.const.complete.obj **summary:** creating a new object in storage a `const` complete object occupies or used to occupy. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with a `const` object **replacement:** None **implementations:** Clang’s constant evaluation catches both `.live` and `.reuse` subsets.

#### 6*.*8*.*5 Indeterminate and erroneous values [basic.indet]

Modify section 6.8.5[basic.indet], paragraph 2:

:::wording

2 If any operand of a built-in operator that produces a prvalue is evaluated, is not a discardedvalue expression (7.2.3[expr.context]), and produces an erroneous or indeterminate value, then the value produced by that operator is erroneous or indeterminate respectively. Except in the following cases, <del>if</del><ins>all evaluations have</ins> an <ins>implicit precondition assertion</ins> <ins>that they will not produce an</ins> indeterminate value <del>is produced by an evaluation, the</del> <del>behavior is undefined</del> (F.2.14[ubx:basic.indet.value]),∗and <ins>if they do then the result of the</ins> evaluation is an indeterminate value; if an erroneous value is produced by an evaluation, the behavior is erroneous and the result of the evaluation is that erroneous value:

:::

— (2.1) If an indeterminate or erroneous value of unsigned ordinary character type (6.9.3[basic. fundamental]) or `std::byte` type (17.2.1[cstddef.syn]) is produced by the evaluation of:

- the second or third operand of a conditional expression (7.6.16[expr.cond]),
- the right operand of a comma expression (7.6.20[expr.comma]),
- the operand of a cast or conversion (conv.integral, expr.type.conv, expr.static.cast, expr.cast) to an unsigned ordinary character type or `std::byte` type (17.2.1[cstddef.syn]), or
- a discarded-value expression (7.2.3[expr.context]), then the result of the operation is an indeterminate value or that erroneous value, respectively.
- (2.2) If an indeterminate or erroneous value of unsigned ordinary character type or `std::byte` type is produced by the evaluation of the right operand of a simple assignment operator (7.6.19[expr.assign]) whose first operand is an lvalue of unsigned ordinary character type or `std::byte` type, an indeterminate value or that erroneous value, respectively, replaces the value of the object referred to by the left operand.
- (2.3) If an indeterminate or erroneous value of unsigned ordinary character type is produced by the evaluation of the initialization expression when initializing an object of unsigned ordinary character type, that object is initialized to an indeterminate value or that erroneous value, respectively.
- (2.4) If an indeterminate value of unsigned ordinary character type or `std::byte` type is produced by the evaluation of the initialization expression when initializing an object of `std::byte` type, that object is initialized to an indeterminate value or that erroneous value, respectively.

Converting an indeterminate or erroneous value of unsigned ordinary character type or `std::byte` type produces an indeterminate or erroneous value, respectively. In the latter case, the result of the conversion is the value of the converted operand.

[*Example* *1*:

```cpp
int f(bool b) {
  unsigned char *c = new unsigned char;
  unsigned char d = *c;  // OK, d has an indeterminate value
  int e = d;  // undefined behavior
  return b ? d : 0;  // undefined behavior if b is true
}
int g(bool b) {
  unsigned char c;
  unsigned char d = c;  // no erroneous behavior, but d has an erroneous value
  assert(c == d);  // holds, both integral promotions have erroneous behavior
  int e = d;  // erroneous behavior
  return b ? d : 0;  // erroneous behavior if b is true
}
void h() {
  int d1, d2;
  int e1 = d1;  // erroneous behavior
  int e2 = d1;  // erroneous behavior
  assert(e1 == e2);  // holds
  assert(e1 == d1);  // holds, erroneous behavior
  assert(e2 == d1);  // holds, erroneous behavior
  std::memcpy(&d2, &d1, sizeof(int));  // no erroneous behavior, but d2 has an erroneous value
  assert(e1 == d2);  // holds, erroneous behavior
  assert(e2 == d2);  // holds, erroneous behavior
}
```

*— end* *example*]

##### Note

*∗***ubdef:** basic.indet.value **summary:** reading an uninitialized (indeterminate) value. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage has been initialized **replacement:** Only for built-in types: initialise default-initialised variables with erroneous value **implementations:** caught by MemorySanitizer on Clang; also rejected during constant evaluation.

#### 6*.*8*.*6 Storage duration [basic.stc]

##### 6*.*8*.*6*.*5 Dynamic storage duration [basic.stc.dynamic]

###### 6*.*8*.*6*.*5*.*1 General [basic.stc.dynamic.general]

Notes regarding 6.8.6.5.1[basic.stc.dynamic.general], paragraph 4:

4 If the behavior of an allocation or deallocation function does not satisfy the semantic constraints specified in 6.8.6.5.2[basic.stc.dynamic.allocation] and 6.8.6.5.3[basic.stc.dynamic. deallocation], the behavior is undefined (F.2.15[ubx:basic.stc.alloc.dealloc.constraint]).

###### Note

###### ubdef:

basic.stc.alloc.dealloc.constraint **summary:** a user-replaced allocation or deallocation function violating its semantic constraints. **runtime-checkable:** Partially **locally-checkable:** No **checking:** Add postcondition assertions to allocation functions, evaluate them. Some constraints can be expressed this way, some (such as global distinctness) are not locally verifiable. **replacement:** None **implementations:** Some caught by UBSan’s `undefined` check on Clang.

###### 6*.*8*.*6*.*5*.*2 Allocation functions [basic.stc.dynamic.allocation]

Notes regarding 6.8.6.5.2[basic.stc.dynamic.allocation], paragraph 2:

2 An allocation function attempts to allocate the requested amount of storage. If it is successful, it returns the address of the start of a block of storage whose length in bytes is at least as large as the requested size. The order, contiguity, and initial value of storage allocated by successive calls to an allocation function are unspecified. Even if the size of the space requested is zero, the request can fail. If the request succeeds, the value returned by a replaceable allocation function is a non-null pointer value (6.9.5[basic.compound]) `p0` different from any previously returned value `p1`, unless that value `p1` was subsequently passed to a replaceable deallocation function. Furthermore, for the library allocation functions in 17.6.3.2[new.delete.single] and 17.6.3.3[new.delete.array], `p0` represents the address of a block of storage disjoint from the storage for any other object accessible to the caller. The effect of indirecting through a pointer returned from a request for zero size is undefined (F.2.16[ubx:basic.stc.alloc.zero.dereference]).*∗*`18`
