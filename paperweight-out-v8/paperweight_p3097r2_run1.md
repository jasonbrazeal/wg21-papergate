Verdict: Strong (8/14)

The paper makes a credible start by establishing why virtual function contract assertions matter and by situating its design against prior art, but it leaves much of the practical case for standardization asserted rather than demonstrated. The thinnest support concerns evidence of real-world need, implementability, and why existing library or language mechanisms cannot suffice.

- The strongest support is the clear explanation of the expressiveness gap for virtual functions and the risk that developers will avoid contract assertions altogether without this feature.
- The discussion of prior proposals and other languages is substantive and shows awareness of where earlier designs failed.
- The paper claims but does not establish who is concretely affected, relying on a single poll rather than user or codebase evidence.
- The most glaring omission is the lack of demonstrated implementation experience or interoperability evidence beyond an asserted GCC implementation, leaving the standardization need largely unproven in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 7 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 9.00   accumulate 8.00   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.17  coordination 0.67  insufficiency 0.33  implementation 1.33
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.50 / 7.50 / 9.00   (all 3 samples: 8.00)
headings: h2 5
on threshold: none
splits: vehicle[5] 1/1/2  coordination[4] 0/2/2  insufficiency[4] 0/2/0  implementation[2] 2/0/2
        implementation[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/2  -> 2.00
  [3] 2 Overview                                   1/1/1  -> 1.00
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 2 (found by 3 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 3 (found by 3 of 21 passes): With the base proposal, if an overriding function wishes to have the same sequence of precondition and postcondition assertions as the overridden function, and have that sequence evaluated even when called directly, it needs to repeat the sequence.
candidate 4 (found by 2 of 21 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found

## audience - grade 0.50 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   1/1/1  -> 1.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): EWG poll from St. Louis (June 2024): P3097R0 — Contracts for C++: Support for Virtual Functions, we would like to see this paper merged into P2900 and progress contracts with virtual function support. SF/F/N/A/SA 18/15/5/1/2

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/2  -> 2.00
  [3] 2 Overview                                   2/2/2  -> 2.00
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.
candidate 2 (found by 3 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 3 (found by 2 of 21 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions. It also deliberately diverges from Eiffel and D, where satisfying the preconditions of any overridden function is sufficient to call a virtual function.
candidate 4 (found by 2 of 21 passes): We are aware of three languages that provide built-in precondition and postcondition assertions fully integrated with runtime polymorphism: Eiffel, D, and Ada.

## vehicle - grade 1.17 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 1/1/2  -> 1.33
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 2 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 3 (found by 1 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns, even though they are both correct and common in real-world C++ systems.

## coordination - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/2/2  -> 1.33
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): A base class may be defined in a library header and derived from another component, or independently in multiple components.

## insufficiency - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/2/0  -> 0.67
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): In a language where precondition assertions are OR-ed with those of overridden functions, these assertions could not be made to work.

## implementation - grade 1.33  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/0/2  -> 1.33
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/1  -> 0.33
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): a complete implementation of that wording available in GCC.
candidate 2 (found by 1 of 21 passes): with wording rebased on the current C++26 working draft [[N5014](https://wg21.link/n5014)] and a complete implementation of that wording available in GCC.
candidate 3 (found by 1 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.

-->
