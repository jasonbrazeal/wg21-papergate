## 7 Future extensions

We already briefly touched upon Labels in earlier sections of this paper. Here, we explore other extensions that rely on Labels as proposed in [P3400R4] and provide important additional functionality for implicit contract assertions not proposed in this paper.

### 7.1 Identifying the UB category

[P3400R4] proposes the addition of *identification* *labels* to contract assertions. These identification labels can be used to identify groups of contract assertions by name. For explicit contract assertions, we must introduce these identification labels manually; however, for implicit contract assertions, we can define and assign such identification labels directly in the C++ Standard (see [P3400R4] Section 3.3.5). Such implicitly defined identification labels would make possible programmatically identifying, in the contract-violation handler, whether the violated implicit contract assertion is related to an out-of-bounds issue, an arithmetic issue, and so forth; for example:

```cpp
void handle_contract_violation(const std::contracts::contract_violation& violation)
{
  if (auto* bounds_label =
      violation.query(bounds_label_tag)) {
      // handle violation of assertion labelled with the bounds label
  }
}
```

Notably, the [P3400R4] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R2] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups. We identified cases of UB, such as {expr.dynamic.cast.glvalue.lifetime}, that are simultaneously type and lifetime issues.

In addition, users (and, more importantly, libraries) can use such labels to annotate their own explicit contract assertions, enabling the same policies to guide handling of core language bounds violations and violations of higher-level functions. For example, the indexing operator of a userdefined container (such as the one shown in Section 5.1) can have an explicit precondition labelled to belong to the same Bounds category as bounds checks defined by the C++ Standard itself. The same identification labels can be defined for hardened preconditions in the C++ Standard Library.

### 7.2 Granular control of the evaluation semantic

Another important feature enabled by Labels is the possibility to control and constrain the evaluation semantic in code. This possibility also extends to implicit contract assertions (see [P3400R4] Section 4.2). Any possible label, such as “always enforce”, “never enforce”, etc., can be applied to any group of implicit contract assertions at any granularity: per file, per TU, per module, per namespace, per function, or per code block:

```cpp
int f(int a, int b) {
  contract_control core arithmetic |= always_enforce;
  return a + b;
}
```

In addition to labels that specify or constrain the evaluation semantics directly, there are labels that give the user higher-level control of the evaluation semantics based on meaningful decisions, for example an “audit” label to identify expensive checks.

Labels used in this way provide granular control when needed, allow the Standard to specify useful groupings of different sources of program defects, and give developers the freedom they need to control mitigations for those defects based on exactly the criteria needed for their environments.

Such a control mechanism for runtime checks (or for other tools in our toolbox such as language subsetting) needs to be designed carefully and take into account the overall strategy (Figure 4). In particular, we need to make it clear which feature is responsible for providing the user-facing configuration mechanism for which tool, and avoid ending up in a situation where the same functionality is provided simultaneously by different features in incompatible ways.

For granular, in-source control of the evaluation semantics of implicit contract assertions, we need to agree whether this happens via directives such as the ones proposed in [P3400R4] and shown here, or by using the syntax proposed in the Profiles framework as proposed in [P3589R2]. If we want to have both, we need to specify one in terms of the other to avoid an incoherent and messy design.

If we follow the idea in Section 4.4 and consider Profiles to be a higher-level feature defined in terms of the seven basic tools (the low-level features), then a Profile that enables or disables runtime checks can be defined as essentially a declaration that expands to [P3400R4] directives as the one shown above. Alternatively, we could design Profiles as an auditing feature rather than a configuration feature: instead of actively enabling certain configuration options, the effect of a Profile would be that the program is ill-formed if the configuration options chosen via [P3400R4] directives or other mechanisms are not compatible with the guarantees that that Profile ensures.

### 7.3 Integrating assertions and assumptions

In Section 5.4, we introduced the *assume* semantic as a backwards-compatibility escape hatch for newly introduced erroneous behaviour; as such, it can only apply to implicit contract assertions, not to explicit ones.

Allowing the *assume* semantic on explicit contract assertions has met sustained opposition in EWG due to the possibility of inadvertently *adding* new UB to a C++ program instead of removing it. The presence of the *assume* semantic in the C++2a Contracts proposal [P0542R5] contributed to that proposal being removed from the C++20 Working Draft. In response to this opposition, no *assume* semantic was included in C++26 Contracts [P2900R14]. Assumptions were instead standardised as a separate feature in the form of the `[[assume]]` attribute [P1774R8] to enable the required functionality.

However, Labels, as proposed in [P3400R4], open up the possibility of introducing an explicit label that would allow the *assume* semantic to apply to an explicit contract assertion as well. Consider the limiter example from [P1774R8]:

```cpp
void limiter(float* data, size_t size) {
  [[assume(size > 0)]];
  [[assume(size % 32 == 0)]];
  // implementation
}
```

With a `may_be_assumed` label, we could instead write:

```cpp
void limiter(float* data, size_t size)
  pre<may_be_assumed> (size > 0)
  pre<may_be_assumed> (size % 32 == 0);
```

Now, the assumptions are not only visible on the *declaration* of the function, but also benefit from all other features of explicit precondition assertions, such as the ability to select evaluation semantics other than *assume*.

To avoid the possibility of introducing an assumption by accident, the *assume* semantic would be allowed on explicit contract assertions only when the `may_be_assumed` label is present; further, a “safe C++” profile could make such a label ill-formed. Thus, contract assertions without the explicit label would be no less “safe” than they are in C++26.

Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle. The `[[assume]]` attribute — a temporary solution that was introduced as a reaction to that failure — could then be deprecated.


## Acknowledgements

Thanks to Gašper Ažman, Herb Sutter, Oliver Rosten, Andrzej Krzemieński, Roger Orr, Phil Nash, Peter Bindels, Jens Maurer, and Bengt Gustafsson for their helpful feedback on previous revisions of this paper.

Thanks to Lori Hughes for reviewing a previous revision of this paper and providing editorial feedback.

Claude (Anthropic) was used for editorial assistance during the preparation of this paper, as well as significant parts of the prototype implementations.


## References

[Baxter2024] Sean Baxter. Why Safety Profiles Failed. `https://www.circle-lang.org/` `draft-profiles.html`, 2024-10-24.

[CWG2816] Jiang An. Core Issue 2816: Unclear phrasing “may assume ... eventually”. `https:` `//www.open-std.org/jtc1/sc22/wg21/docs/cwg_active.html#2816`, 2023-04-26.

[CWG3022] Timur Doumler. Core Issue 3022: Redundant specification of explicit destructor calls.

`https://cplusplus.github.io/CWG/issues/3022.html`, 2025-04-13.

[CWG3034] Timur Doumler. Core Issue 3034: Infinite recursion should hit an implementation limit.

`https://cplusplus.github.io/CWG/issues/3034.html`, 2025-07-26.

[Lippincott2025] Lisa Lippincott. Balancing the Books. C++Now talk, 2025-04-30.

[N5054] Thomas Köppe. Working Draft, Standard for Programming Language C++. `https:` `//wg21.link/n5054`, 2026-07-16.

[P0542R5] G. Dos Reis, J. D. Garcia, J. Lakos, A. Meredith, N. Myers, and B. Stroustrup. Support for contract based programming in C++. `https://wg21.link/p0542r5`, 2018-06-08.

[P0543R3] Jens Maurer. Saturation arithmetic. `https://wg21.link/p0543r3`, 2023-07-19.

[P0593R6] Richard Smith. Implicit creation of objects for low-level object manipulation. `https:` `//www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p0593r6.html`, 2020-02-14.

[P1705R1] Shafik Yaghmour. Enumerating Core Undefined Behavior. `https://www.open-std.` `org/jtc1/sc22/wg21/docs/papers/2019/p1705r1.html`, 2019-09-28.

[P1774R8] Timur Doumler. Portable assumptions. `https://wg21.link/p1774r8`, 2022-06-14.

[P1995R1] Joshua Berne, Timur Doumler, Andrzej Krzemieński, Ryan McDougall, and Herb Sutter. Contracts – Use Cases. `https://www.open-std.org/jtc1/sc22/wg21/docs/papers/` `2020/p1995r1.html`, 2020-03-02.

[P2064R0] Herb Sutter. Assumptions. `http://www.open-std.org/jtc1/sc22/wg21/docs/` `papers/2020/p2064r0.pdf`, 2020-01-13.

[P2644R1] Nicolai Josuttis, Herb Sutter, Titus Winter, Hana Dusíková, Fabio Fracassi, Victor Zverovich, Bryce Adelstein Lelbach, and Peter Sommerlad. Final Fix of Broken Rangebased for Loop, Rev 1. `https://wg21.link/p2644r1`, 2022-11-11.

[P2680R1] Gabriel Dos Reis. Contracts for C++: Prioritizing Safety. `https://wg21.link/p2680r1`, 2022-12-15.

[P2723R1] JF Bastien. Zero-initialize objects of automatic storage duration. `https://wg21.link/` `p2723r1`, 2023-01-15.

[P2754R0] Jake Fevold. Deconstructing the Avoidance of Uninitialized Reads of Auto Variables.

`https://wg21.link/p2754r0`, 2023-01-24.

[P2771R1] Thomas Neumann. Towards memory safety in C++. `https://wg21.link/p2771r1`, 2023-05-17.

[P2795R5] Thomas Köppe. Erroneous behaviour for uninitialized reads. `https://wg21.link/` `p2795r5`, 2024-03-22.

[P2843R3] Alisdair Meredith. Preprocessing is never undefined. `https://wg21.link/p2843r3`, 2025-06-20.

[P2899R1] Joshua Berne, Timur Doumler, Rostislav Khlebnikov, and Andrzej Krzemieński. Contracts for C++ — Rationale. `https://wg21.link/p2899r1`, 2025-03-14.

[P2900R14] Joshua Berne, Timur Doumler, and Andrzej Krzemieński. Contracts for C++. `https:` `//wg21.link/p2900r14`, 2025-02-13.

[P2973R0] Jonathan Wakely and Thomas Köppe. Erroneous behaviour for missing return from assignment. `https://wg21.link/p2973r0`, 2023-09-15.

[P3038R0] . . `https://wg21.link/p3038r0`, 202.

### [P3045R6] Mateusz Pusz, Dominik Berner, Johel Ernesto Guerrero Pe~na, Chip Hogg, Nicolas

Holthaus, Roth Michaels, and Vincent Reverdy. Quantities and units library. `https:` `//wg21.link/p3045r6`, 2025-06-19.

[P3075R0] Shafik Yaghmour. Adding an Undefined Behavior and IFNDR Annex. `https://wg21.` `link/p3075r0`, 2023-12-15.

[P3081R2] Herb Sutter. Core safety profiles for C++26. `https://wg21.link/p3081r2`, 2025-02-04.

[P3173R0] Gabriel Dos Reis. P2900R6 May Be Minimal, but It Is Not Viable. `https://wg21.` `link/p3173r0`, 2024-02-15.

[P3227R0] Gašper Ažman and Timur Doumler. Fixing the library API for contract violation handling. `https://wg21.link/p3227r0`, 2024-10-15.

[P3285R0] Gabriel Dos Reis. Contracts: Protecting The Protector. `https://wg21.link/p3285r0`, 2024-05-15.

[P3318R0] Ville Voutilainen. Throwing violation handlers, from an application programming perspective. `https://wg21.link/p3318r0`, 2024-05-22.

[P3362R0] Ville Voutilainen and Richard Corden. Static analysis and ‘safety’ of Contracts, P2900 vs. P2680/P3285. `https://wg21.link/p3362r0`, 2024-08-11.

[P3376R0] Andrzej Krzemieński. Contract assertions versus static analysis and ‘safety’. `https:` `//wg21.link/p3376r0`, 2024-10-14.

[P3386R0] Joshua Berne. Static Analysis of Contracts with P2900. `https://wg21.link/p3386r0`, 2024-10-15.

[P3390R0] Sean Baxter and Christian Mazakas. Safe C++. `https://wg21.link/p3390r0`, 2024- 09-11.

[P3400R4] Joshua Berne. Controlling Contract-Assertion Properties. `https://wg21.link/p3400r4`, 2026-07-15.

[P3402R3] Marc-André Laverdière, Christopher Lapkowski, and Charles-Henri Gros. A Safety Profile Verifying Initialization. `https://wg21.link/p3402r3`, 2025-05-16.

[P3424R0] Alisdair Meredith. Define Delete With Throwing Exception Specification. `https:` `//wg21.link/p3424r0`, 2024-12-17.

[P3446R0] Bjarne Stroustrup. Profile invalidation – eliminating dangling pointers. `https://wg21.` `link/p3446r0`, 2024-10-14.

[P3471R4] Konstantin Varlamov and Louis Dionne. Standard library hardening. `https://wg21.` `link/p3471r4`, 2025-02-14.

[P3499R1] Timur Doumler, Lisa Lippincott, and Joshua Berne. Exploring strict contract predicates.

`https://wg21.link/p3499r1`, 2025-02-09.

[P3500R1] Timur Doumler, Gašper Ažman, Joshua Berne, and Ryan McDougall. Are Contracts “safe”? `https://wg21.link/p3500r1`, 2025-02-09.

[P3541R1] Andrzej Krzemieński. Violation handlers vs noexcept. `https://wg21.link/p3541r1`, 2025-01-06.

[P3578R0] Ryan McDougall. What is Safety? `https://wg21.link/p3578r0`, 2024-12-12.

[P3589R2] Gabriel Dos Reis. C++ Profiles: The Framework. `https://wg21.link/p3589r2`, 2025- 05-19.

[P3596R2] Joshua Berne, Timur Doumler, Jens Maurer, and Shafik Yaghmour. Undefined Behavior and IFNDR Annexes. `https://wg21.link/p3596r2`, 2026-05-12.

[P3596R3] Joshua Berne, Timur Doumler, Jens Maurer, and Shafik Yaghmour. Undefined Behavior and IFNDR Annexes. `https://wg21.link/p3596r3`, 2026-06-11.

[P3627R0] Ulfar Erlingsson. Easy-to-adopt security profiles for preventing RCE (remote code execution) in existing C++ code. `https://wg21.link/p3627r0`, 2025-02-11.

[P3650R0] Bjarne Stroustrup. 21st century C++. `https://wg21.link/p3650r0`, 2025-03-06.

[P3656R1] Herb Sutter and Gašper Ažman. Initial draft proposal for core language UB white paper: Process and major work items. `https://wg21.link/p3656r1`, 2025-03-23.

[P3700R0] Peter Bindels. Making Safe C++ Happen. `https://wg21.link/p3700r0`, 2025-05-19.

[P3716R0] Peter Bindels. Subsetting. `https://wg21.link/p3716r0`, 2025-05-19.

[P3754R0] Timur Doumler and Joshua Berne. Slides for EWG presentation of P3100R2 Implicit Contract Assertions. `https://wg21.link/p3754r0`, 2025-06-20.

[P3984R0] Bjarne Stroustrup. A type-safety profile. `https://wg21.link/p3984r0`, 2026-02-22.

[P4277R0] Joshua Berne. Overview and Implementation Report for P3100. `http://www.open-std.` `org/jtc1/sc22/wg21/docs/papers/2026/p4277r0.pdf`, 2026-08-14.

[P4284R0] Joshua Berne. Addenda to the Undefined Behavior and IFNDR Annexes. `http:` `//www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4284r0.pdf`, 2026-08-14.

[P4298R0] Joshua Berne. Nonthrowing Evaluation Semantics. `http://www.open-std.org/jtc1/` `sc22/wg21/docs/papers/2026/p4298r0.pdf`, 2026-07-15.

[Sutter2024] Herb Sutter. C++ safety, in context. `https://herbsutter.com/2024/03/11/` `safety-in-context/`, 2024-03-11.

[Sutter2025] Herb Sutter. Crate-training Tiamat, un-calling Cthulhu: Taming the UB monsters in C++. `https://herbsutter.com/2025/03/30/` `crate-training-tiamat-un-calling-cthulhutaming-the-ub-monsters-in-c/`, 2025-03-30.
