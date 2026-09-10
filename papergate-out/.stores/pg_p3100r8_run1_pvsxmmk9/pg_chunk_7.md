`18` The intent is to have `operator` `new()` implementable by calling `std::malloc()` or `std::calloc()`, so the rules are substantially the same. C++ differs from C in requiring a zero request to return a non-null pointer.

###### Note

*∗***ubdef:** basic.stc.alloc.zero.dereference **summary:** dereferencing the non-null pointer returned by a zero-size allocation **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track pointer provenance, insert bounds check **replacement:** None **implementations:** caught by AddressSanitizer on both compilers.

### 6*.*9 Types [basic.types]

#### 6*.*9*.*5 Compound types [basic.compound]

Notes regarding 6.9.5[basic.compound], paragraphs 5-6:

5 If an evaluation produces or causes an object to have (6.9.2[basic.types.trivial]) a pointer value to or past the end of an object *O* and happens before the beginning of the duration of the region of storage for *O*, the behavior is undefined (F.2.17[ubx:basic.compound. pointer.before.storage.duration]).*∗*

[*Note*: Relaxed atomic operations (32.5.4[atomics.order]) can produce such values. Conversions from integers avoid producing them (7.6.1.10[expr.reinterpret.cast]). *— end* *note*]

#### Note

*∗***ubdef:** basic.compound.pointer.before.storage.duration **summary:** forming a pointer to an object before its storage duration begins. **runtime-checkable:** No, requires knowing that undefined behavior will or will not be encountered with any potential value a pointer might have. **locally-checkable:** No **checking:** Would require properly identifying when angelic provenance is unable to apply. **replacement:** None **implementations:** None

6 A pointer value *P* is *valid* *in* *the* *context* *of* an evaluation *E* if *P* is a pointer to function or a null pointer value, or if it is a pointer to or past the end of an object *O* and *E* happens after the beginning and happens before the end of the duration of the region of storage for *O*. If a pointer value *P* is used in an evaluation *E* and *P* is not valid in the context of *E*:

— If *E* is an indirection (7.6.2.2[expr.unary.op]), the behavior is undefined (F.2.18[ubx:basic.compound.invalid.pointer]).*∗*

- If *E* either

- is a boolean conversion (7.3.15[conv.bool]) or
- is performed by a unary `+`, additive, three-way comparison, relational, or equality operator (7.6[expr.compound]), the behavior is implementation-defined.

[*Note*: *P* can be valid in the context of *E* even if it points to a type unrelated to that of *O* or if *O* is not within its lifetime, although further restrictions apply to such pointer values (6.8.4[basic.life], 7.2.1[basic.lval], 7.6.6[expr.add]). *— end* *note*]

#### Note

*∗***ubdef:** basic.compound.invalid.pointer **summary:** dereferencing a pointer to storage that has already been freed. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track object lifetimes across the entire program **replacement:** None **implementations:** heuristically caught by AddressSanitizer, on both compilers; also rejected during constant evaluation on both compilers.

### 6*.*10 Program execution [basic.exec]

#### 6*.*10*.*1 Sequential execution [intro.execution]

Notes regarding 6.10.1[intro.execution], paragraph 10:

10 Except where noted, evaluations of operands of individual operators and of subexpressions of individual expressions are unsequenced.

[*Note*: In an expression that is evaluated more than once during the execution of a program, unsequenced and indeterminately sequenced evaluations of its subexpressions need not be performed consistently in different evaluations. *— end* *note*]

The value computations of the operands of an operator are sequenced before the value computation of the result of the operator. The behavior is undefined (6.10.2[intro. multithread]) (F.2.19[ubx:intro.execution.unsequenced.modification]) if*∗*

- a side effect on a memory location (6.8.1[intro.memory]) or
- starting or ending the lifetime of an object in a memory location is unsequenced relative to

- another side effect on the same memory location,
- starting or ending the lifetime of an object occupying storage that overlaps with the memory location, or
- a value computation using the value of any object in the same memory location, and the two evaluations are not potentially concurrent (6.10.2[intro.multithread]).

[*Note*: Starting the lifetime of an object in a memory location can end the lifetime of objects in other memory locations (6.8.4[basic.life]). *— end* *note*]

[*Note*: The next subclause imposes similar, but more complex restrictions on potentially concurrent computations. *— end* *note*]

[*Example*:

```cpp
  i = 7, i++, i++;  // i becomes 9
  i = i++ + 1;  // the value of i is incremented
  i = i++ + i;  // undefined behavior
  i = i + 1;  // the value of i is incremented
  union U { int x, y; } u;
  (u.x = 1, 0) + (u.y = 2, 0);  // undefined behavior
}
```

*— end* *example*]

#### Note

*∗***ubdef:** intro.execution.unsequenced.modification **summary:** unsequenced side effects (or a side effect and a read) on the same scalar object, single-threaded. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Identify all potential read operations that are not sequenced with respect to each given write operation; insert checks to identify if those operations are referencing the same address **replacement:** Sequence operations in some unspecified order **note:** Needs more careful specification work, defer to future paper. **implementations:** None

#### 6*.*10*.*2 Multi-threaded executions and data races [intro.multithread]

##### 6*.*10*.*2*.*2 Data races [intro.races]

Notes regarding 6.10.2.2[intro.races], paragraph 17:

17 Two actions are *potentially* *concurrent* if

- they are performed by different threads, or
- they are unsequenced, at least one is performed by a signal handler, and they are not both performed by the same signal handler invocation.

The execution of a program contains a *data* *race* if it contains two potentially concurrent conflicting actions, at least one of which is not atomic, and neither happens before the other, except for the special case for signal handlers described below. Any such data race results in undefined behavior (F.2.20[ubx:intro.races.data]).*∗*

[*Note*: It can be shown that programs that correctly use mutexes and `memory_order::seq_cst` operations to prevent all data races and use no other synchronization operations behave as if the operations executed by their constituent threads were simply interleaved, with each value computation of an object being taken from the last side effect on that object in that interleaving. This is normally referred to as “sequential consistency”. However, this applies only to data-race-free programs, and data-race-free programs cannot observe most program transformations that do not change single-threaded program semantics. In fact, most single-threaded program transformations remain possible, since any program that behaves differently as a result has undefined behavior. *— end* *note*]

##### Note

*∗***ubdef:** intro.races.data **summary:** unsynchronized, potentially concurrent accesses to the same memory location, at least one a write. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track from which threads memory is accessed and when accesses synchronize with each other; only practical for a subset of cases **replacement:** Could possibly make all primitive memory accesses implicitly atomic, but that is neither specified nor ready to propose **implementations:** heuristically detected by ThreadSanitizer on both compilers.

##### 6*.*10*.*2*.*3 Forward progress [intro.progress]

Notes regarding 6.10.2.3[intro.progress], paragraph 1:

1 The implementation may assume (F.2.21[ubx:intro.progress.stops]) that any thread*∗*will eventually do one of the following:

- terminate,
- invoke the function `std::this_thread::yield` (32.4.5[thread.thread.this]),
- make a call to a library I/O function,
- perform an access through a volatile glvalue,
- perform an atomic or synchronization operation other than an atomic modify-write operation (32.5.4[atomics.order]), or
- continue execution of a trivial infinite loop (8.6.1[stmt.iter.general]).

[*Note*: This is intended to allow compiler transformations such as removal, merging, and reordering of empty loops, even when termination cannot be proven. An affordance is made for trivial infinite loops, which cannot be removed nor reordered. *— end* *note*]

##### Note

*∗***ubdef:** intro.progress.stops **summary:** a non-terminated thread stops making progress – e.g., a busy-wait whose loop condition is not a constant expression (a trivial infinite loop is not undefined). **runtime-checkable:** No, requires (quite literally) solving the halting problem **locally-checkable:** No **checking:** No checking strategy exists as whether a thread will make progress is undecidable **replacement:** None **implementations:** None

#### 6*.*10*.*3 Start and termination [basic.start]

##### 6*.*10*.*3*.*1 `main` function [basic.start.main]

Notes regarding 6.10.3.1[basic.start.main], paragraph 4:

4 Terminating the program without leaving the current block (e.g., by calling the function `std::exit(int)` (17.5[support.start.term])) does not destroy any objects with automatic storage duration (11.4.7[class.dtor]). If `std::exit` is invoked during the destruction of an object with static or thread storage duration, the program has undefined behavior (F.2.22[ubx:basic.start.main.exit.during.destruction]).

##### Note

##### ubdef:

basic.start.main.exit.during.destruction **summary:** calling `std::exit` recursively during the destruction sequence it would restart. **runtime-checkable:** Yes **locally-checkable:** No, needs new instrumentation of existing functionality **checking:** Track whether static or thread-local objects are currently being destroyed **replacement:** None **implementations:** None

##### 6*.*10*.*3*.*4 Termination [basic.start.term]

Notes regarding 6.10.3.4[basic.start.term], paragraph 5:

5 If a function contains a block variable of static or thread storage duration that has been destroyed and the function is called during the destruction of an object with static or thread storage duration, the program has undefined behavior (F.2.23[ubx:basic.start.term. use.after.destruction]) if the flow of *control∗passes* through the definition of the previously destroyed block variable.

[*Note*: Likewise, the behavior is undefined if the block variable is used indirectly (e.g., through a pointer) after its destruction. *— end* *note*]

##### Note

*∗***ubdef:** basic.start.term.use.after.destruction **summary:** using a static-storage-duration object after its destructor has run. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track the lifetime of static objects **replacement:** None **implementations:** None

### 6*.*11 Contract assertions [basic.contract]

#### 6*.*11*.*1 General [basic.contract.general]

Add a paragraph to and modify section 6.11.1[basic.contract.general], paragraphs 1-2:

:::wording

1 Contract assertions <del>allow</del> <del>the</del> <del>programmer</del> <del>to</del> specify properties of the state of the program that are expected to hold at certain points during execution. <del>Contract assertions</del><ins>Explicit contract assertions</ins> are introduced by precondition-specifiers, postcondition-specifiers (9.4.1[dcl.contract.func]), and assertion-statements (8.9[stmt. contract.assert]). <ins>Implicit contract assertions are introduced as parts of other language</ins> <ins>constructs.</ins>

:::

2 Each explicit contract assertion has a *contract-assertion* *predicate*, which is an expression of type `bool`.

:::wording-remove

[Note 1: The value of the predicate is used to identify program states that are expected. — end note]

:::

:::wording-add

2+a Each implicit contract assertion has a contract-assertion condition under which it is considered satisfied.

:::

:::wording-add

[Note a: If it is determined during program execution that the predicate does not evaluate to true, or that the condition of an implicit contract assertion indicates that the contract assertion is not satisfied, a contract violation occurs. — end note]

:::

#### 6*.*11*.*2 Evaluation [basic.contract.eval]

Add paragraphs to and modify section 6.11.2[basic.contract.eval], paragraphs 1-7:

:::wording

1 An evaluation of a contract assertion uses one of the following <del>four</del><ins>five</ins> evaluation semantics : ignore, observe, enforce, <del>or</del> quick-enforce<ins>, or assume</ins>. Observe, enforce, and quick-enforce are checking semantics; enforce and quick-enforce are terminating semantics.

:::

:::wording

2 <del>It</del><ins>Except that explicit contract assertions are never evaluated with the assume semantic,</ins> it is implementation-defined which evaluation semantic is used for any given evaluation of a contract assertion.

:::

:::wording

[Note 1: The range and flexibility of available choices of evaluation semantics depends on the implementation and need not allow all <del>four</del><ins>five</ins> evaluation semantics as possibilities. The evaluation semantics can differ for different evaluations of the same contract assertion, including evaluations during constant evaluation. — end note]

:::

3 *Recommended* *practice*: An implementation should provide the option to translate a program such that all evaluations of contract assertions use the ignore semantic as well as the option to translate a program such that all evaluations of contract assertions use the enforce semantic. By default, evaluations of contract assertions should use the enforce semantic.

:::wording-remove

4 The evaluation of a contract assertion using the ignore semantic has no effect. <del>[Note 2: The</del> <del>predicate is potentially evaluated (6.3[basic.def.odr]), but not evaluated. — end note]</del>

:::

:::wording-add

4+a If the predicate of a contract assertion evaluated with the assume semantic would not evaluate to true, or the condition of such a contract assertion is not satisfied, the evaluation has unconstrained behavior (4.1.2[intro.abstract]); otherwise the evaluation has no effect.

:::

:::wording-add

4+b [Note 1+a: If a contract assertion has a predicate, and that contract assertion is evaluated with the ignore or assume semantic, the predicate is potentially evaluated (6.3[basic.def.odr]), but not evaluated. — end note]

:::

5 The evaluation *A* of a contract assertion with a predicate using a checking semantic determines the value of the predicate. It is unspecified whether the predicate is evaluated. Let *B* be the value that would result from evaluating the predicate.

[*Note* *2*: To determine whether a predicate would evaluate to `true` or `false`, an alternative evaluation that produces the same value as the predicate but has no side effects can occur.

[*Example* *1*:

```cpp
struct S {
  mutable int g = 5;
} s;
void f()
  pre(( s.g++, false ));  // #1
void g()
{
  f();  // Increment of s.g might not occur, even if #1 uses a checking semantic.
}
```

*— end* *example*]

*— end* *note*]

6 There is an observable checkpoint (4.1.2[intro.abstract]) *C* that happens before *A* such that any other evaluation that happens before *A* also happens before *C*.

7 A *contract* *violation* occurs when

:::wording-add

<ins>—</ins> (<ins>7.a</ins>) <ins>the contract assertion has a condition that is not satisfied,</ins> — (7.1) B is false, — (7.2) the evaluation of the predicate exits via an exception, or — (7.3) the evaluation of the predicate is performed in a context that is manifestly constantevaluated (7.7.7[expr.const.defns]) and the predicate is not a core constant expression.

:::

:::wording-add

[Note 4: If B is `true`, <ins>or the contract assertion has a condition that is satisfied,</ins> no contract violation occurs and control flow continues normally after the point of evaluation of the contract assertion. The evaluation of the predicate can fail to produce a value without causing a contract violation, for example, by calling longjmp (17.14.3[csetjmp.syn]) or terminating the program. — end note]

:::

#### 6*.*11*.2* + *a* Implicit contract assertions [basic.contract.implicit]

:::wording-add

Add a new section <ins>6.11.2+a</ins>[basic.contract.implicit] after 6.11.2[basic.contract.eval]

:::

#### 6.11.2+a Implicit contract assertions [basic.contract.implicit]

:::wording-add

1 A built-in operation O may have an implicit precondition assertion C applied to it. If so, the evaluation in sequence of C is sequenced before the evaluation of O and after the evaluation of all operands of O.

:::

:::wording-add

2 All undefined behavior has a guarding contract assertion that is an implicit contract assertion whose condition is never satisfied.

:::

:::wording-add

3 [Note 1: If the guarding contract assertion of undefined behavior is

:::

:::wording-add

— (3.1) evaluated with the ignore semantic, — (3.2) evaluated with the assume semantic, or — (3.3) evaluated with the observe semantic and the contract-violation handler returns normally then the behavior is unconstrained (4.1.2[intro.abstract]). — end note]

:::

:::wording-add

4 [Note 2: Behavior with an implicit precondition assertion that it does not occur results in unconstrained behavior when that assertion is evaluated with the assume semantic (6.11.2[basic. contract.eval]) but in all other cases has specified behavior. — end note]

:::

##### Note

The above note’s purpose is to make it clear that the places where we have replaced what was previously undefined behavior with erroneous behavior that has an implicit precondition can be implemented in a conforming manner by current compilers by dictating that the associated guarding contract assertion is evaluated with the assume semantic.

7 **Expressions** **[expr]**

### 7*.*1 Preamble [expr.pre]

Modify subclause 7.1[expr.pre], paragraph 4:

4 An *arithmetic* *expression* is

- (4.1) a unary plus or minus (7.6.2.2[expr.unary.op]),
- (4.2) an addition (7.6.6[expr.add]),
- (4.3) a subtraction (7.6.1.2[expr.sub]), or
- (4.4) a multiplication, division, or remainder (7.6.5[expr.mul]) expression where every (possibly converted) operand is of arithmetic type.

[Note 3: There exist non-arithmetic expressions such as compound assignment (7.6.19[expr.assign]) which are defined in terms of arithmetic expressions. *— end* *note*]

:::wording

<del>The behavior</del><ins>If the mathematical result</ins> of evaluating an arithmetic expression is <del>undefined</del> <del>(F.3.1[ubx:expr.expr.eval]) if the mathematical result is</del> neither

:::

:::wording

— (4.1) in the range of representable values for its type nor — (4.2) a negative infinity, positive infinity, or NaN that is among the values of the type<del>.</del><ins>,</ins> <ins>then the result is an unspecified erroneous value with an implicit precondition assertion that it</ins> <ins>does not occur (6.11.2+a[basic.contract.implicit])</ins> <ins>(F.3.1[ubx:expr.expr.eval]).</ins>∗

:::

[*Note* *4*: If the operands are of a type that adheres to ISO/IEC 60559, division by zero is the only case where an arithmetic expression has undefined behavior (7.6.5[expr.mul]). However, some well-defined arithmetic expressions are not core constant expressions (7.7.2[expr.const.core]).

[*Example* *1*: The following example assumes that `std::float32_t` is supported (6.9.4[basic. extended.fp]).

```cpp
constexpr std::float32_t min = std::numeric_limits<std::float32_t>::min();  // OK
constexpr std::float32_t max = std::numeric_limits<std::float32_t>::max();  // OK
constexpr std::float32_t inf = std::numeric_limits<std::float32_t>::infinity();  // OK
constexpr std::float32_t nan = std::numeric_limits<std::float32_t>::quiet_NaN();  // OK
```

```cpp
// Furthermore, if arithmetic expressions with operands of type std::float32_t
// behave as specified in ISO/IEC 60559 for binary32:
constexpr std::float32_t inf2 = inf * 2;  // OK, also positive infinity
constexpr std::float32_t zero = min / max;  // OK, result cannot be represented, and is rounded to zero
constexpr std::float32_t oflo = max * 2;  // error: non-finite result but operands are finite (7.7.2[expr.const.
core])
constexpr std::float32_t nan2 = nan * 2;  // OK, propagating a NaN
constexpr std::float32_t udef = inf * 0;  // error: result is NaN but neither operand is NaN (7.7.2[expr.const.
core])
constexpr std::float32_t div0 = max / 0;  // error: division by zero is undefined (7.6.5[expr.mul], 7.7.2[expr.
const.core])
```

*— end* *example*]

*— end* *note*]

[*Note* *5*: Treatment of division by zero, forming a remainder using a zero divisor, and all floatingpoint exceptions varies among machines, and is sometimes adjustable by a library function. *— end* *note*]

#### Note

*∗***ubdef:** expr.expr.eval **summary:** signed integer `+`, `-`, `*`, and unary negation overflow (a subset of the general expression-evaluation rule). **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the given arguments will produce a valid value **replacement:** Coerce into erroneous value, either explicitly or by using the result of the underlying instruction as-is **implementations:** exhaustively caught by UBSan’s `signed-integer-overflow`, constant evaluation, and the P3850 prototype (GCC nonthrowing-only, Clang all semantics).

### 7*.*2 Properties of expressions [expr.prop]

#### 7*.*2*.*1 Value category [basic.lval]

Notes regarding 7.2.1[basic.lval], paragraph 11:

11 An object of dynamic type `T`obj is *type-accessible* through a glvalue of type `T`ref if `T`ref is similar (7.3.6[conv.qual]) to:

- `T`obj,
- a type that is the signed or unsigned type corresponding to `T`obj, or
- a `char`, `unsigned` `char`, or `std::byte` type.

If a program attempts to access (3.1[defns.access]) the stored value of an object through a glvalue through which it is not type-accessible, the behavior is undefined (F.3.2[ubx:expr. basic.lvalue.strict.aliasing.violation]).*∗*`36` If a program invokes a defaulted copy/move constructor or copy/move assignment operator for a union of type `U` with a glvalue argument that does not denote an object of type *cv* `U` within its lifetime, the behavior is undefined (F.3.3[ubx:expr.basic.lvalue.union.initialization]).*†*

[*Note*: In C, an entire object of structure type can be accessed, e.g., using assignment. By contrast, C`++` has no notion of accessing an object of class type through an lvalue of class type. *— end* *note*]

`36` The intent of this list is to specify those circumstances in which an object can or cannot be aliased.

#### Note

*∗***ubdef:** expr.basic.lvalue.strict.aliasing.violation **summary:** accessing an object through a glvalue of a dissimilar type (strict-aliasing violation). **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track the dynamic type of the object in storage and verify the access glvalue’s type is similar to it **replacement:** None **implementations:** None

#### Note

*†* **ubdef:** expr.basic.lvalue.union.initialization **summary:** defaulted union copy/move construction whose argument isn’t a live similar-type object. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether storage is associated with an object of correct type within its lifetime **replacement:** None **implementations:** rejected during constant evaluation on both GCC and Clang.

#### 7*.*2*.*2 Type [expr.type]

Notes regarding 7.2.2[expr.type], paragraph 1:

1 If an expression initially has the type “reference to `T`” (9.3.4.3[dcl.ref], 9.5.4[dcl.init. ref]), the type is adjusted to `T` prior to any further analysis; the value category of the expression is not altered. Let *X* be the object or function denoted by the reference. If a pointer to *X* would be valid in the context of the evaluation of the expression (6.9.3[basic.fundamental]), the result designates *X*; otherwise, the behavior is undefined (F.3.4[ubx:expr.type.reference.lifetime]).*∗*

[*Note*: Before the lifetime of the reference has started or after it has ended, the behavior is undefined (see 6.8.4[basic.life]). *— end* *note*]

#### Note

*∗***ubdef:** expr.type.reference.lifetime **summary:** evaluating (naming) a reference to an object whose lifetime has ended. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track object and storage lifetimes **replacement:** None **implementations:** None

### 7*.*3 Standard conversions [conv]

#### 7*.*3*.*2 Lvalue-to-rvalue conversion [conv.lval]

Modify section 7.3.2[conv.lval], paragraph 3:

3 The result of the conversion is determined according to the following rules:

:::wording

— (3.1) If T is cv std::nullptr_t, the result is a null pointer constant (7.3.12[conv.ptr]). [Note: Since the conversion does not access the object to which the glvalue refers, there is no side effect even if T is volatile-qualified (6.10.1[intro.execution]), and the glvalue can refer to an inactive member of a union (11.5[class.union]). — end note] — (3.2) Otherwise, if T has a class type, the conversion copy-initializes the result object from the glvalue. — (3.3) Otherwise, if the bits in the value representation of the object to which the glvalue refers are not valid for the object’s type, the <del>behavior</del><ins>prvalue result</ins> is <del>undefined</del><ins>an</ins> <ins>unspecified erroneous value, and there is an implicit precondition that this does not</ins> occur (6.11.2+a[basic.contract.implicit]) (F.3.5[ubx:conv.lval.valid.representation]).∗

:::

[*Example* *2*:

```cpp
bool f() {
  bool b = true;
  char c = 42;
  memcpy(&b, &c, 1);
  return b;  // undefined behavior if 42 is not a valid value representation for bool
}
```

*— end* *example*] — (3.4) Otherwise, the object indicated by the glvalue is read (3.1[defns.access]). Let `V` be the value contained in the object. The prvalue result is

- the value of type `T` congruent (6.9.3[basic.fundamental]) to `V` if `T` is an integer type,
- the result of `reinterpret_cast<T>(reinterpret_cast<std::uintptr_t>(V))` if `T` is volatile-qualified and `V` is a pointer value that is not valid in the context of the evaluation (6.9.5[basic.compound]), and
- `V` otherwise.

#### Note

*∗***ubdef:** conv.lval.valid.representation **summary:** lvalue-to-rvalue conversion of an invalid bit pattern for an object of non-class type **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is a valid value representation for the object’s type **replacement:** Coerce invalid value representations into erroneous values **implementations:** the `bool` and `enum` subgroups are caught natively by the P3850 prototype. With GCC potentially-throwing semantics are not supported while with Clang they are supported. UBSan’s `bool`/`enum` checks (both in the `undefined` group) check both categories. The `int` and `float` subgroups have no invalid representation on commonly available platforms.

#### 7*.*3*.*10 Floating-point conversions [conv.double]

Modify section 7.3.10[conv.double], paragraph 2:

:::wording

2 If the source value can be exactly represented in the destination type, the result of the conversion is that exact representation. If the source value is between two adjacent destination values, the result of the conversion is an implementation-defined choice of either of those values. Otherwise, the <del>behavior</del><ins>result</ins> is <del>undefined</del><ins>an unspecified erroneous</ins> <ins>value with an implicit precondition that this does not occur</ins> (F.3.6[ubx:conv.double.out. of.range]).

:::

#### Note

#### ubdef:

conv.double.out.of.range **summary:** converting a floating-point value to a type that cannot represent it. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is one that can be converted **replacement:** Coerce into erroneous value **implementations:** None

#### 7*.*3*.*11 Floating-integral conversions [conv.fpint]

Modify section 7.3.11[conv.fpint], paragraphs 1-2:

:::wording

1 A prvalue of a floating-point type can be converted to a prvalue of an integer type. The conversion truncates; that is, the fractional part is discarded. <del>The behavior</del><ins>An unspecified</ins> <ins>erroneous value</ins> is <del>undefined (F.3.7[ubx:conv.fpint.float.not.represented])</del> <ins>produced</ins> if the truncated value cannot be represented in the destination type, with an implicit <ins>precondition that this does not occur (6.11.2+a[basic.contract.implicit]) (F.3.7[ubx:conv.</ins> <ins>fpint.float.not.represented])</ins>.∗

:::

[*Note* *1*: If the destination type is `bool`, see 7.3.15[conv.bool]. *— end* *note*]

##### Note

*∗***ubdef:** conv.fpint.float.not.represented **summary:** float-to-integer conversion whose truncated value isn’t representable in the destination type. **runtime-checkable:** Yes **locally-checkable:** Yes **checking:** Insert a check of whether the value is valid **replacement:** Coerce into erroneous value **implementations:** Checked by UBSan’s `float-cast-overflow`, in constant evaluation, and implemented natively by the P3850 prototype.

2 A prvalue of an integer type or of an unscoped enumeration type can be converted to a prvalue of a floating-point type. The result is exact if possible. If the value being converted is in the range of values that can be represented but the value cannot be represented exactly, it is an implementation-defined choice of either the next lower or higher representable value.
