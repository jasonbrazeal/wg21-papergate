*†* **ubdef:** class.cdtor.form.pointer **summary:** forming a pointer to a member before construction starts or after destruction finishes. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** For polymorphic objects, caught by UBSan’s `vptr` check on Clang.

5 Member functions, including virtual functions (11.7.3[class.virtual]), can be called during construction or destruction (11.9.3[class.base.init]). When a virtual function is called directly or indirectly from a constructor or from a destructor, including during the construction or destruction of the class’s non-static data members, or during the evaluation of a postcondition assertion of a constructor or a precondition assertion of a destructor (9.4.1[dcl.contract.func]), and the object to which the call applies is the object (call it `x`) under construction or destruction, the function called is the final overrider in the constructor’s or destructor’s class and not one overriding it in a more-derived class. If the virtual function call uses an explicit class member access (7.6.1.5[expr.ref]) and the object expression refers to the complete object of `x` or one of that object’s base class subobjects but not `x` or one of its base class subobjects, the behavior is undefined (F.6.8[ubx:class.cdtor.virtual.not.x]).*∗*

[*Example*:

```cpp
  virtual void f();
  virtual void g();
};
struct A : virtual V {
  virtual void f();
};
struct B : virtual V {
  virtual void g();
  B(V*, A*);
};
struct D : A, B {
  virtual void f();
  virtual void g();
  D() : B((A*)this, this) { }
};
```

```cpp
B::B(V* v, A* a) {
  f();  // calls V::f, not A::f
  g();  // calls B::g, not D::g
  v->g();  // v is base of B, the call is well-defined, calls B::g
  a->f();  // undefined behavior: a’s type not a base of B
}
```

*— end* *example*]

#### Note

*∗***ubdef:** class.cdtor.virtual.not.x **summary:** explicit-member-access virtual call during construction or destruction, outside the executing class or its bases. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** None

6 The `typeid` operator (7.6.1.8[expr.typeid]) can be used during construction or destruction (11.9.3[class.base.init]). When `typeid` is used in a constructor (including the *mem-initializer* or default member initializer (11.4[class.mem]) for a non-static data member) or in a destructor, or used in a function called (directly or indirectly) from a constructor or destructor, if the operand of `typeid` refers to the object under construction or destruction, `typeid` yields the `std::type_info` object representing the constructor or destructor’s class. If the operand of `typeid` refers to the object under construction or destruction and the static type of the operand is neither the constructor or destructor’s class nor one of its bases, the behavior is undefined (F.6.9[ubx:class.cdtor.typeid]).

#### Note

#### ubdef:

class.cdtor.typeid **summary:** `typeid` on an object under construction or destruction, outside its own class or bases. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** None

7 `dynamic_cast`s (7.6.1.7[expr.dynamic.cast]) can be used during construction or destruction (11.9.3[class.base.init]). When a `dynamic_cast` is used in a constructor (including the *mem-initializer* or default member initializer for a non-static data member) or in a destructor, or used in a function called (directly or indirectly) from a constructor or destructor, if the operand of the `dynamic_cast` refers to the object under construction or destruction, this object is considered to be a most derived object that has the type of the constructor or destructor’s class. If the operand of the `dynamic_cast` refers to the object under construction or destruction and the static type of the operand is not a pointer to or object of the constructor or destructor’s own class or one of its bases, the `dynamic_cast` results in undefined behavior (F.6.10[ubx:class.cdtor.dynamic.cast]).*∗*

[*Example*:

```cpp
  virtual void f();
};
struct A : virtual V { };
struct B : virtual V {
  B(V*, A*);
};
struct D : A, B {
  D() : B((A*)this, this) { }
};
B::B(V* v, A* a) {
  typeid(*this);
```

```cpp
                                // type_info for B
  typeid(*v);  // well-defined: *v has type V, a base of B yields type_info for B
  typeid(*a);  // undefined behavior: type A not a base of B
  dynamic_cast<B*>(v);  // well-defined: v of type V*, V base of B results in B*
  dynamic_cast<B*>(a);  // undefined behavior: a has type A*, A not a base of B
}
```

*— end* *example*]

#### Note

*∗***ubdef:** class.cdtor.dynamic.cast **summary:** `dynamic_cast` on an object under construction or destruction, outside its own class or bases. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** None

13 **Templates** **[temp]**

### 13*.*9 Template instantiation and specialization [temp.spec]

#### 13*.*9*.*2 Implicit instantiation [temp.inst]

Notes regarding 13.9.2[temp.inst], paragraph 18:

18 There is an implementation-defined quantity that specifies the limit on the total depth of recursive instantiations (Annex B[implimits]), which could involve more than one template. The result of an infinite recursion in instantiation is undefined (F.7.1[ubx:temp. inst.inf.recursion]).*∗*

[*Example*:

```cpp
  X<T>* p;  // OK
  X<T*> a;  // implicit generation of X<T> requires
                    // the implicit instantiation of X<T*> which requires
                    // the implicit instantiation of X<T**> which . . .
};
```

*— end* *example*]

#### Note

*∗***ubdef:** temp.inst.inf.recursion **summary:** infinite recursive template instantiation with no base case.

14 **Exception** **handling** **[except]**

### 14*.*4 Handling an exception [except.handle]

Notes regarding 14.4[except.handle], paragraph 12:

12 Referring to any non-static member or base class of an object in the handler for a *function-try-block* of a constructor or destructor for that object results in undefined behavior (F.8.1[ubx:except.handle.handler.ctor.dtor]).

### Note

### ubdef:

except.handle.handler.ctor.dtor **summary:** referring to a member/base of an object from its ctor/dtor function-try-block handler. **runtime-checkable:** Yes **locally-checkable:** No **checking:** Track whether objects are currently being constructed or destroyed **replacement:** None **implementations:** Clang emits a compile-time warning for direct references in the handler, GCC does not, and there is no run-time or constant-evaluation detection.

### 14*.*5 Exception specifications [except.spec]

Modify subclause 14.5[except.spec], paragraph 6:

6 An expression *E* is *potentially-throwing* if

:::wording-add

— (6.1) E is a function call (7.6.1.3[expr.call]) whose postfix-expression has a function type, or a pointer-to-function type, with a potentially-throwing exception specification, or — (6.2) E implicitly invokes a function (such as an overloaded operator, an allocation function in a new-expression, a constructor for a function argument, or a destructor) that has a potentially-throwing exception specification, or — (6.3) E is a throw-expression (7.6.18[expr.throw]), or — (6.4) E is a dynamic_cast expression that casts to a reference type and requires a runtime check (7.6.1.7[expr.dynamic.cast]), or — (6.5) E is a typeid expression applied to a (possibly parenthesized) built-in unary * operator applied to a pointer to a polymorphic class type (7.6.1.8[expr.typeid]), or — (6.6) any of the immediate subexpressions (6.10.1[intro.execution]) of E that is not an unevaluated operand is potentially-throwing. <ins>[Note 1:</ins> <ins>The</ins> <ins>evaluation</ins> <ins>of</ins> <ins>an</ins> <ins>expression</ins> <ins>that</ins> <ins>is</ins> <ins>not</ins> <ins>potentially-throwing</ins> <ins>can</ins> <ins>nevertheless</ins> <ins>exit</ins> <ins>via</ins> <ins>an</ins> <ins>exception</ins> <ins>if,</ins> <ins>as</ins> <ins>part</ins> <ins>of</ins> <ins>that</ins> <ins>evaluation,</ins> <ins>the</ins> <ins>violation</ins> <ins>of an implicit contract assertion (6.11.1[basic.contract.general]) causes a call to the</ins> <ins>contract-violation handler (6.11.3[basic.contract.handler]) and that handler exits via an</ins> <ins>exception. — end note]</ins>

:::

17 **Language** **support** **library** **[support]**

### 17*.*10 Contract-violation handling [support.contract]

#### 17*.*10*.*1 Header `<contracts>` synopsis [contracts.syn]

Modify section 17.10.1[contracts.syn], paragraph 1:

1 The header `<contracts>` defines types for reporting information about contract violations (6.11.2[basic.contract.eval]).

:::wording

```cpp
// all freestanding
namespace std::contracts {
  enum class assertion_kind : unspecified {
    pre = 1,
    post = 2,
    assert = 3,
    <ins>implicit = 4←�</ins>
  };
  enum class evaluation_semantic : unspecified {
    ignore = 1,
    observe = 2,
    enforce = 3,
    quick_enforce = 4
  };
  enum class detection_mode : unspecified {
    predicate_false = 1,
    evaluation_exception = 2
  };
  class contract_violation {
    // no user-accessible constructor
  public:
    contract_violation(const contract_violation&) = delete;
    contract_violation& operator=(const contract_violation&) = delete;
    see below ~contract_violation();
    const char* comment() const noexcept;
    contracts::detection_mode detection_mode() const noexcept;
    bool is_terminating() const noexcept;
    assertion_kind kind() const noexcept;
    source_location location() const noexcept;
    evaluation_semantic semantic() const noexcept;
  };
  void invoke_default_contract_violation_handler(const contract_violation&);
}
```

:::

#### 17*.*10*.*2 Enumerations [support.contract.enum]

Modify section 17.10.2[support.contract.enum], Table 44 [support.contract.enum.kind]:

#### Table 44 — Enum `assertion_kind` [tab:support.contract.enum.kind]

| Name | Meaning |
| --- | --- |
| `pre` | A precondition assertion |
| `post` | A postcondition assertion |
| `assert` | An *assertion-statement* |
| `implicit` | An implicit contract assertion |

#### 17*.*10*.*3 Class `contract_violation` [support.contract.violation]

Modify section 17.10.3[support.contract.violation], paragraph 3:

3 *Recommended* *practice*: The string returned should contain a textual representation of the predicate of the violated contract assertion, a description of the condition that was detected by the assertion, or an empty string if storing a textual representation is undesired.

[*Note* *1*: The string can represent a truncated, reformatted, or summarized rendering of the predicate, before or after preprocessing. *— end* *note*]

*F* **Core** **undefined** **behavior** **[ub]**

*F.*1 **General** **[ub.general]**

Modify subclause F.1[ub.general], paragraph 1:

1 This Annex documents undefined behavior explicitly called out in Clause 4[intro] through Clause 15[cpp] using the following phrases:

:::wording-add

— (1.1) is undefined — (1.2) the behavior is undefined — (1.3) the behavior of the program is undefined — (1.4) has undefined behavior — (1.5) have undefined behavior — (1.6) result has undefined behavior — (1.7) results in undefined behavior <ins>—</ins> (<ins>1.7+a</ins>) <ins>an implicit precondition (6.11.2+a[basic.contract.implicit])</ins>

:::

Undefined behavior that is implicit is not covered by this annex. Each entry contains a title, a cross-reference, a summary of the circumstances, and code examples. The code examples are not intended to exhaustively cover all possible ways of invoking that case.
