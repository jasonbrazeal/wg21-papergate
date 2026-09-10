## 3 Analysis

### 3.1 Enumeration

#### 3.1.1 Methodology

We manually inspected all occurrences of the words “undefined” and “assume” in revision [N5054] of the C++ working paper. We then constructed a list of all cases of explicitly specified core language UB. We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” (“...the behaviour is undefined”, “...has undefined behaviour”, “...results in undefined behaviour”, etc.) and one instance of explicit language UB introduced with a phrase containing the word “assume” (“the implementation may assume...”).1 We thus obtained a list with 82 cases of explicit language UB; it can be found in Appendix A of this paper.

Originally, we constructed our list independently from another effort to enumerate core language UB led by Shafik Yaghmour (see [P1705R1], [P3075R0]). The current list in Appendix A represents a merger of the lists produced by both efforts, further increasing confidence that we in fact exhaustively covered all core language UB explicitly specified in the current C++ working paper.

Each individual case of UB in our list has a stable identifier. Separately from this paper, [P3596R3], which was adopted in Brno, added a UB and IFNDR annex to the C++ Standard. Various fixes and updates to that Annex have been proposed in [P4284R0]. The enumeration of core language UB in that annex, and the stable identifiers used therein, are in sync with Appendix A of this paper. However, in this paper, we place those identifiers between {curly braces} to visually distinguish them from the C++ working paper’s clause identifiers, which we place between [square brackets].

#### 3.1.2 Granularity

The granularity of our enumeration — i.e., when a piece of core language specification is considered a distinct case of UB — is somewhat arbitrary. As a general rule, we consider a single sentence in the C++ working paper that specifies a condition under which a core language operation has UB to be one case of UB; if such a sentence contains a bulleted list where each item specifies such a condition (e.g., [basic.life]/7), we consider each item to be a separate case of UB.

We could consider dividing up the cases of UB in different ways and with greater granularity. In particular, we could more closely align the enumeration with possible mitigation strategies, rather than with the lexical appearance of the word “undefined” in the C++ working paper.

For example, for [basic.life]/7, instead of considering each bullet to be a separate case of UB, we could consider each different way in which a pointer can be invalid (lifetime of the object not started yet, lifetime of the object ended already, pointer is null, etc.) to be a separate case of UB.

As another example, instead of considering flowing off the end of a function ([stmt.return]/4) as a single case of UB, we could introduce separate cases for flowing off the end of an assignment operator (which has a proposed mitigation, see [P2973R0]), flowing off the end of a function that returns a built-in type (which could be mitigated via returning an erroneous value, see Section 3.4), and flowing off the end of any other non-`main` function that returns a non-`void` type.

However, such alternative approaches would make the enumeration more difficult to map to existing wording, which in turn would make it more difficult to track changes and reason about whether the enumeration is exhaustive. Further, keeping the enumeration of cases of UB separate from the enumeration of possible mitigation strategies reduces interdependencies and complexity. Instead, whenever a mitigation strategy does not fully align with a case of UB, we point this out explicitly (for example, inserting an implicit null pointer check is considered only a *partial* mitigation for dereferencing an invalid pointer).

#### 3.1.3 Scope

In this paper, we consider only explicit UB, not implicit UB — that is, UB that exists by omission because the C++ working paper failed to specify the behaviour of a well-formed operation. We consider all cases of implicit UB that may be discovered in the future to be wording bugs that should be addressed via Core issues, and then subsequently become explicit UB that can be addressed via

1Except for this one occurrence, which is in [intro.progress]/1, the verb “assume” in core wording does not imply that there may be undefined behaviour, but instead means things like “this case will be treated as the default” or “other cases will be ignored”. To remove ambiguity, [CWG2816] proposes to change the wording in [intro.progress]/1 to use the phrase “the behaviour is undefined” instead of “the implementation may assume”.

the framework proposed here. Importantly, while explicit UB can be enumerated exhaustively, and we do so in Appendix A of this paper, enumerating all implicit UB is impossible in principle as we can never be sure we found all wording bugs in the C++ working paper.

We exclude one case of explicit UB from our enumeration that does not actually represent a separate case of UB. The current wording in this case2 normatively states that “the program has undefined behaviour” but merely refers to cases of UB already specified elsewhere in the Standard, rather than specifying any new such cases. The relevant wording should instead be a non-normative note; this issue is currently being addressed by Core issue [CWG3022].

Further, in this paper we consider only *runtime* UB, not compile-time or link-time issues. We therefore exclude all cases of IFNDR listed in [P3596R3] from our analysis. Although the effects of IFNDR can manifest at run time, whether a program is IFNDR is (unlike UB) fundamentally not a runtime property. We also exclude the case of infinite recursion during template instantiation, listed as {temp.inst.inf.recursion} in [P3596R3]. The current wording3 for this case can be interpreted to mean that such infinite recursion could cause runtime UB; however, this interpretation makes little sense as failure during template instantiation is fundamentally a compile-time issue. We therefore consider this case a wording bug rather than an instance of UB; this issue is currently being addressed by Core issue [CWG3034].

Finally, we exclude *library* *undefined* *behaviour*. The natural mitigation approach for library UB is to make use of contract assertions (`pre`, `post`, and `contract_assert`) in library implementations and, where sensible, mandate such assertions through library hardening [P3471R4], both of which are out of scope for this paper. We, therefore, consider only UB that is specified in the core language part of the C++ working paper (Clauses 1–15). Further, we found one case of UB that is specified in the core language part of [N5054], listed as {basic.start.term.signal.handler} in [P3596R3], but actually represents a precondition on Standard Library functions;4 that case is, therefore, also excluded from our list.

### 3.2 Classification

#### 3.2.1 Categories

We found that all identified cases of core language UB can be classified into ten basic categories:

I. **Initialisation** — 1 case. Evaluating an expression that produces an indeterminate value.

II. **Bounds** — 5 cases. Using a pointer in a way that fails to respect the range of the pointed-to object or array. Examples: incrementing a pointer beyond the past-the-end position; performing single-object delete on an operand obtained from an array-new expression; dereferencing a pointer returned from a request for zero size.

III. **Type** **and** **Lifetime** — 52 cases. Operations that access storage and/or use pointers or references to storage in an inappropriate way that is not already covered by Initialisation and

2[class.dtor]/16: The invocation of a destructor is subject to the usual rules for member functions ([class.mfct]); that is, if the object is not of the destructor’s class type and not of a class derived from the destructor’s class type (including when the destructor is invoked via a null pointer value), the program has undefined behavior. 3[temp.inst]/16: There is an implementation-defined quantity that specifies the limit on the total depth of recursive instantiations ([implimits]), which could involve more than one template. The result of an infinite recursion in instantiation is undefined. 4[basic.start.term]/6: If there is a use of a standard library object or function not permitted within signal handlers ([support.runtime]) that does not happen before ([intro.multithread]) completion of destruction of objects with static storage duration and execution of `std::atexit` registered functions ([support.start.term]), the program has undefined behavior.

Bounds. Examples: attempting to access a value of one type through a pointer of a different, incompatible type; attempting to access the value of an object after its lifetime has ended.

IV. **Arithmetic** — 10 cases. Executing an arithmetic operation whose operands fail to meet certain preconditions. Examples: division by zero; conversion of a value to a different arithmetic type that cannot represent that value.

V. **Threading** — 2 cases. Data races; non-trivial infinite loops with no side effects.

VI. **Sequencing** — 1 case. Performing two concurrent accesses, at least one of which is modifying, to the same memory location from the same thread where neither access is sequenced before the other.

VII. **Assumptions** — 1 case. Reaching an `[[assume]]` declaration whose operand would not evaluate to `true`.

VIII. **Control** **Flow** — 5 cases. Errors in control flow. Examples: flowing off the end of a function; re-entering the same declaration recursively when initialising a static variable.

IX. **Replacement** **Functions** — 2 cases. Executing a user-defined replacement function (`operator` `new`/`delete`) that fails to meet the specified requirements. Examples: returning `null` from a user-defined placement `new`.

X. **Coroutines** — 3 cases. Misusing coroutine machinery. Examples: destroying a coroutine that is not suspended; failing to provide a `return_void` function for a coroutine that does not return a value.

Figure 1 shows the distribution of the 82 identified cases of explicit core language UB across these ten basic categories.

The categories of Initialisation, Bounds, and Type and Lifetime correspond to the common terms *initialisation* *safety*, *bounds* *safety*, *type* *safety*, and *lifetime* *safety*, respectively, and collectively represent UB that is commonly referred to with the umbrella term *memory* *safety*. Much of the ongoing work around how to “make C++ safe” is focused on these categories (see [P3081R2], [P3700R0], and references therein).

Because unambiguously categorising a particular case of UB into either *type* *safety* or *lifetime* *safety* is often impossible since it concerns both, we grouped them into a single combined category, Type

> **[Figure: Flow Diagram]**
> 1. 1
> 2. 2 3
> 3. I. Initialisation
> 4. 5
> 5. 5
> 6. II. Bounds
> 7. 211
> 8. III. Type and Lifetime
> 9. 10

IV. Arithmetic V. Threading VI. Sequencing VII. Assumptions

> **[Figure: Concept Chain]**
> 52

VIII. Control Flow IX. Replacement Functions

X. Coroutines

Figure 1: Distribution of identified cases of explicit language UB across specified categories and Lifetime. While some cases of UB are primarily caused by type aliasing and others are primarily caused by out-of-lifetime accesses, they form a spectrum, and many common operations in C++ (e.g., using a reference) rely on *both* type and lifetime constraints to be satisfied.

Remarkably, these three categories related to memory safety account for 58 cases of UB, or 70.7% of all identified cases; the Type and Lifetime category alone accounts for 52 cases of UB, or 63.4% of all identified cases.

The next two categories, Arithmetic and Threading, correspond to the common terms *arithmetic* *safety* and *thread* *safety*, respectively. Note that the term thread safety is often used to refer to data races specifically and does not include the other case of UB we placed in the Threading category (infinite loops with no side effects).

The following category, Sequencing, contains just one case of UB: unsequenced operations, such as `i++` `+` `++i`. Classifying UB due to data races and unsequenced operations into two separate categories might seem surprising at first since they have a very similar shape (except that one is inter-thread and the other is intra-thread), but as we will see in Section 4, these two categories actually require very different approaches to mitigation.

The next category, Assumptions, also contains just one case of UB: reaching an `[[assume]]` declaration whose operand would not evaluate to `true`. As we will see later, this case of UB is of a different nature than the others and warrants its own category.

The final three categories (Control Flow, Replacement Functions, and Coroutines) contain a handful of cases of UB that are less frequently discussed in the current “safe C++” discourse.

#### 3.2.2 Relevance for security

[P3656R1] asks which cases of UB are security related. The paper suggests having security experts indicate which cases of UB have security impact and use “always”, “never”, and “sometimes” tags. We are not security experts, so we do not attempt to do this here. However, we note that cases of UB commonly associated with security vulnerabilities (see, for example, the CWE list at `https://cwe.mitre.org/`) fall into the Initialisation, Bounds, and Type and Lifetime categories.

UB in other categories is not commonly exploited by malicious attackers to our knowledge. Nevertheless, some of these cases, for example those in categories Arithmetic and Threading, are a common source of program defects that do sizeable damage to existing software.

In principle, with aggressive optimising compilers any form of UB can lead to unpredictable defects and vulnerabilities. Mitigating cases of UB currently considered to be the most critical security concern will simply remove the easiest routes of attack from the table, and any UB not yet addressed may become the new major candidate for attackers to leverage for nefarious purposes. Therefore, prioritising implementation based on current trends amongst malicious actors, though helpful, should not be used to limit the scope of our work on improving the C++ language specification (see [Sutter2024], [P3500R1], and [P3578R0]).

### 3.3 Diagnosability

The second question [P3656R1] asks is which cases of UB are “efficiently locally diagnosable”. In this paper, we split this question into three separate questions: whether diagnosis can happen statically or whether it needs to happen dynamically (i.e., at run time), whether such diagnosis can be performed locally, and the runtime cost of such diagnosis (whether performed locally or not).

#### 3.3.1 Static vs. dynamic diagnosis

A commonly asked question is “why does the committee not simply make all the UB ill-formed instead”? The answer is that in order for that to happen, it would be necessary to determine statically — i.e., at compile time — whether a given operation in a C++ program would lead to UB when executed at run time. However, whether a C++ program will have UB when executed is fundamentally a *runtime* property, i.e., the answer depends on runtime values unknown at compile time (for example, the runtime value of a pointer or an integer). Therefore, in the vast majority of cases, such a compile-time determination cannot be made. In fact, in our entire list of 82 cases of UB, we cannot identify *any* cases that can unconditionally be diagnosed at compile time.

Of course, static analysis is still useful and widely used in the field. There are many situations where static analysis *can* detect a bug that would lead to UB when executed, because the relevant values or conditions happen to be known at compile time in the particular program at hand. However, given an existing C++ program, any approach based on static analysis fundamentally has to choose between *false* *positives* (rejecting code for which no proof can be constructed one way or another, even if that code happens to be correct) and *false* *negatives* (accepting incorrect code that will lead to UB when executed).

Crucially, whether a pointer or reference refers to a valid object of the correct type within its lifetime at a given point in time (“memory safety”), the relevant property for addressing UB in the Initialisation, Bounds, and Type and Lifetime categories, seems to be fundamentally unprovable at compile time in the general case (see [Baxter2024]).

As we will see in Section 4, despite these fundamental limitations there are things we can (and should) do in the C++ Standard to enable static analysis to construct a proof in more cases, such as subsetting the language (4.3.5), providing replacement features (4.3.7), and adding annotations (4.3.6). However, for existing C++ programs, reliably detecting cases of UB without rejecting correct code will inevitably have to leverage *runtime* detection, i.e., the insertion of additional runtime checks when compiling the program. We therefore focus on such runtime detection for the remainder of this analysis.

#### 3.3.2 Locality of diagnosis

An important property for diagnosis of UB is whether such diagnosis (whether static or dynamic) can be performed *locally*, i.e. without keeping track of additional information across the entire program that is not available within the C++ abstract machine (achievable with additional instrumentation of the kind that is implemented in sanitisers, such as ASan and UBSan) and without analysing code in other branches (which is limited by the Halting problem) or on the other side of a function call boundary (which might be located in another TU and therefore inaccessible).

Most cases of UB in the Initialisation, Bounds, and Type and Lifetime categories are, in the *general* case, *not* locally diagnosable — and this is an inherent limitation of the C++ object model, see [Baxter2024] — but require instrumentation applied across the entire program to be reliably diagnosed.

Of course, “not locally diagnosable in general” does not mean “*never* locally diagnosable”: under special circumstances, such cases of UB can be locally diagnosable — for example, if an array bound happens to be statically known, if a pointer happens to be null and not otherwise invalid/dangling, or if additional information about control flow and object values can be inferred from local analysis — and existing static analysis tools diagnose such cases today. This set of special cases could be further enlarged in the future with the introduction of novel features such as lifetime annotations [P2771R1] or “ghost data” [Lippincott2025], which are the subject of ongoing research. We discuss some of these approaches in Section 4; here, we focus on the status quo in Standard C++.

In the Initialisation category, no cases of UB are generally locally diagnosable, as C++ does not enforce initialisation and uninitialised objects can be passed around arbitrarily. In the Bounds category, no cases of UB are generally locally diagnosable because array bounds are generally not known.

In the Type and Lifetime category, {expr.mptr.oper.member.func.null} is locally diagnosable because this case requires *only* a null pointer check. {basic.align.object.alignment} is locally diagnosable by checking the alignment of storage when creating an object at run time. {expr.assign.overlap} is locally diagnosable by checking the overlap of the two address ranges. (The ranges are known because the address and `sizeof` are known at run time for both the source and the destination object.) {class.abstract.pure.virtual} is locally diagnosable by adding a runtime check to the pure virtual function stub to which the base class vtable points. {conv.lval.valid.representation} is locally diagnosable by validating the bits in the value representation of the object against its type. None of the other cases of UB in the Type and Lifetime category are locally diagnosable in general. Two recently introduced cases, {basic.compound.pointer.before.storage.duration} and {expr.reinterpret.cast.invalid.pointer.value}, depend on identifying numeric pointer values that cannot represent any possible object in or out of its lifetime, and due to the angelic nature of the undefined behaviour being removed it is challenging or impossible to identify diagnostic strategies for these.

However, all 10 cases of UB in the Arithmetic category are locally diagnosable since they are all cases of an arithmetic operation producing a value that is somehow inappropriate (mathematically invalid, not representable in the target type, etc.) and that value can be inspected at run time.

UB in the Threading category is either not locally diagnosable ({intro.races.data}) or not diagnosable at all ({intro.progress.stops}). However, UB in the Sequencing category ({intro.execution. unsequenced.modification}) is locally diagnosable.

UB in the Assumption category ({dcl.attr.assume.false}) is, in principle, locally diagnosable by evaluating the operand of the assumption and verifying that the resulting value, contextually converted to `bool`, equals `true`. However, if that evaluation has any side effects, such a check could alter the observable state of the program. Therefore, even if the given assumption holds and no UB occurs, the check itself might render the program invalid by altering its state. Thus, this case of UB is meaningfully diagnosable in any automated fashion only if the operand has no side effects when evaluated. However, proving that the operand has no side effects is generally impossible to do efficiently and is outright impossible in the presence of an opaque function call. We therefore consider this case not diagnosable at all.

Two cases of UB in the Control Flow category are locally diagnosable. {stmt.return.flow.off} can be diagnosed by inserting a check at the end of every function body that does not end with a `return` statement. {dcl.attr.noreturn.eventually.returns} can be diagnosed by inserting a check into every function declared `[[noreturn]]`. The remaining three cases of UB in that category are not locally diagnosable.

In the Replacement Function category, {expr.new.non.allocating.null} is locally diagnosable because we can check locally that a function does not exit via an exception, or that it does not return null. However, the more complex set of constraints specified in {basic.stc.alloc.dealloc.constraint} is not fully diagnosable (locally or at all).

Finally, one case of UB in the Coroutine category, {stmt.return.coroutine.flow.off}, is locally diagnosable in a way analogous to {stmt.return.flow.off} by inserting a check at the end of a coroutine for which no `return_void` function is provided. The remaining two cases of UB in that category are not locally diagnosable since being so would require tracking runtime state information that is not currently maintained within the coroutine handle in most implementations.

Overall, as shown in Figure 2, only 20 cases of UB (24.4% of all cases) are unconditionally locally diagnosable at run time, while 57 cases of UB (69.5%) are not locally diagnosable in the general case,

> **[Figure: Flow Diagram]**
> 1. 5
> 2. 20

Checkable locally Requires global instrumentation

Not checkable

> **[Figure: Concept Chain]**
> 57

Figure 2: Runtime diagnosability of explicit core language UB for the general case requiring instrumentation of the code in order to be diagnosed at run time. We will discuss these requirements in more detail in Section 3.3.4. In addition, 5 cases of UB (6.1%) are not diagnosable at all in the general case, even with additional instrumentation.

#### 3.3.3 Cost of local diagnosis

Considering locally checkable cases of UB separately from non-locally checkable ones is useful to estimate the cost of diagnosis. For locally diagnosable cases, some kind of runtime check — an *assertion* — could be inserted by the implementation and then evaluated at run time. The total cost of diagnosis can, therefore, be approximated by the cost of evaluating that check multiplied by the number of times the check needs to be evaluated.

Note that in this paper, we study the theoretical, relative cost based on the current specification of the C++ language. We do not, however, measure the actual cost in existing tooling that implements such checks, nor do we present benchmarks in this paper; such studies are left for future work.

That said, the cheapest kind of check — and the only one that has (almost) no overhead for the happy path — is the “fail if you get here” check, equivalent to a `pre`/`post`/`contract_assert(false)`. This kind of check is sufficient to diagnose {class.abstract.pure.virtual}, {stmt.return.flow.off}, {stmt.return.coroutine.flow.off}, and {dcl.attr.noreturn.eventually.returns}.

A slightly more expensive but still cheap and optimiser-friendly kind of check is a null check, required to diagnose the null pointer cases ({expr.static.cast.downcast.wrong.derived.type}, {expr.unary. dereference}, {conv.ptr.virtual.base}, {expr.dynamic.cast.pointer.lifetime}, {expr.mptr.oper.member. func.null}, and {expr.new.non.allocating.null}) as well as division by zero ({expr.mul.div.by.zero}).

Integer comparisons are similarly cheap and optimiser-friendly and are required for bounds checks with statically known array bounds, i.e. a subset of ({expr.add.out.of.bounds} and {expr.add.sub.diff. pointers}), as well as {expr.shift.neg.and.width} and {intro.execution.unsequenced.modification}.

Beyond this, a number of UB cases can still be checked by a straightforward arithmetic expression but with increasingly expensive expressions: {expr.assign.overlap} requires computing whether two integer ranges overlap, and {basic.align.object.alignment} requires computing an integer modulo.

At the expensive end of the locally diagnosable UB spectrum are runtime checks for which there is no corresponding C++ expression; instead, the compiler would have to generate more complex “magic” checks based on knowledge unavailable in the C++ abstract machine. In particular, this case applies to all arithmetic UB except {expr.add.out.of.bounds} and {expr.add.sub.diff.pointers}.

The compiler would have to validate the bit patterns of values of arithmetic types according to knowledge it has about how values of such types are represented on the targeted platform. Such checks can be done locally, but they can slow operations involving built-in types and, in particular, floating-point types.

In addition to the cost of the check itself, we need to consider the frequency with which these checks would need to be done. Checks that would need to happen once when a function is called or when a function returns are likely to be acceptable in most scenarios. Extensive checks for arithmetic UB will probably be acceptable in fewer scenarios because such checks have the potential to significantly slow arithmetic operations, which are performance sensitive in many contexts. On the extreme end, if we wanted to diagnose {intro.execution.unsequenced.modification} via a runtime check, the check itself would be fairly inexpensive, but the compiler would have to identify all potential read operations that are not sequenced with respect to each given write operation and then insert checks to identify if those operations are actually going to reference the same address.

#### 3.3.4 Cost of non-local diagnosis

For UB that is not locally diagnosable (which is most of the UB in C++), we need to consider the cost of the required additional instrumentation. To get an idea of that cost, we must nail down exactly which additional properties that are not normally known from within the C++ abstract machine would need to be tracked by such instrumentation. This tracking would need to happen at run time throughout the *entire* program; checks relying on the tracked information would have to be inserted for *every* runtime operation that may be affected by such UB. The full list is available in Appendix A; we provide an overview below.

To diagnose *all* cases of UB in the memory safety categories of Initialisation, Bounds, and Type and Lifetime, instrumentation would have to track all the following properties:

- Provenance of all pointers and pointers-to-member

- For all storage, whether it has been allocated or freed

- For all storage, whether it has been initialised

- For all storage, whether it has been created such that it can hold implicit lifetime objects

— For all storage, the type of the object associated with it (if any), including whether it is `const` or `volatile`

- For all objects, whether their lifetime has been started or ended

- For all objects, whether they are currently being constructed or destroyed

- The dynamic type of all *non*-polymorphic objects of class type

- For all references, whether they have been initialised

- For all addresses that point to functions, the type of the function

To diagnose UB in the Threading category, instrumentation would have to track, for *all* memory accesses, from which threads that memory is accessed and when these accesses synchronise with each other. Doing this exhaustively is not practically possible; however, instrumentation that is capable of diagnosing a subset of cases exists in the form of sanitisers (TSan).

The non-locally-diagnosable UB in the Control Flow category concerns operations that are not allowed during construction and destruction of objects with static or thread-local storage duration
