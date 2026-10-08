Verdict: Adequate to Strong (8/14)

The paper offers a reasonably grounded case for why virtual functions need contract support and shows meaningful engagement with prior art, but it leans heavily on assertion rather than evidence for several key arguments. The strongest support concerns the problem space and the shortcomings of earlier designs, while the thinnest support appears in the areas of affected users, implementation experience, and why the feature belongs in the standard rather than in a library.

- The paper clearly establishes the expressive gap for virtual functions under the base contracts proposal and the practical risk that affected developers will simply avoid contract assertions.
- It credibly demonstrates awareness of prior approaches in Eiffel, D, Ada, and earlier C++ proposals, including specific failures in C++20 Contracts and GCC.
- The claims about who is affected rest on a single EWG poll without broader evidence of user demand or real-world code patterns.
- The most glaring omission is the lack of substantiated implementation experience, since the paper only asserts that a complete GCC implementation exists without describing its scope, maturity, or lessons learned.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 7 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 8.17   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.33  coordination 0.67  insufficiency 0.17  implementation 1.00
sample agreement: 41 of 49 section-criterion pairs unanimous (84%)
single-sample totals would have been: 7.00 / 8.00 / 8.50   (all 3 samples: 7.83)
headings: h2 5
on threshold: none
splits: audience[3] 2/1/1  prior_art[2] 0/2/2  prior_art[3] 0/2/0  vehicle[1] 0/1/1
        vehicle[4] 0/2/2  vehicle[5] 2/1/1  coordination[4] 0/2/2  insufficiency[5] 0/0/1
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
candidate 4 (found by 2 of 21 passes): Runtime polymorphism is a fundamental part of C++. Many libraries and APIs are designed around virtual functions, making it one of the core idioms of the language.

## audience - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   2/1/1  -> 1.33
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): EWG poll from St. Louis (June 2024): P3097R0 — Contracts for C++: Support for Virtual Functions, we would like to see this paper merged into P2900 and progress contracts with virtual function support. SF/F/N/A/SA 18/15/5/1/2

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/2/2  -> 1.33
  [3] 2 Overview                                   0/2/0  -> 0.67
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Eiffel and D implement widening of preconditions by OR-ing the precondition assertions of the final overrider with those of all overridden functions, which removes the caller-facing precondition check.
candidate 2 (found by 3 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns
candidate 3 (found by 3 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 4 (found by 2 of 21 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.

## vehicle - grade 1.33 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/2/2  -> 1.33
  [5] 3 Design goals and principles  (part 2 of 2) 2/1/1  -> 1.33
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 2 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 3 (found by 1 of 21 passes): By contrast, C++ is a multi-paradigm language. Unlike Eiffel, C++ must accommodate adding assertions to existing code organised across independently developed components, and cannot reject *correct* code simply because it does not fit a particular programming paradigm.
candidate 4 (found by 1 of 21 passes): Extending the C++ facility to virtual functions requires understanding the kinds of correctness expectations that commonly apply to such functions, and ensuring that the proposed extension can express those expectations effectively.

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
candidate 1 (found by 1 of 21 passes): A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 2 (found by 1 of 21 passes): Inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/1  -> 0.33
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns

## implementation - grade 1.00  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             1/1/1  -> 1.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): a complete implementation of that wording available in GCC.

-->
