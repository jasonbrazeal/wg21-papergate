Verdict: Adequate (7/14)

The paper makes a persuasive start by explaining why virtual functions need contract support and by showing that prior language designs and earlier C++ proposals have not handled assertion inheritance correctly. However, much of the remaining case is asserted rather than demonstrated, particularly around the breadth of affected users, the need for standardization rather than a library solution, and practical implementation experience.

- The strongest support is the established argument that virtual functions are a core C++ idiom and that current contract assertions cannot express preconditions and postconditions for them, which would discourage adoption in important domains.
- The paper also credibly establishes that prior art in Eiffel, D, Ada, and earlier C++ proposals fails to support the needed usage patterns or does so incorrectly.
- The case for who is affected rests mainly on a single EWG poll, without evidence of how widespread the need is among developers or codebases.
- The most glaring omission is the lack of established implementation experience or a demonstrated path from the proposed design to a working implementation, leaving the feasibility claims largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 8.00   accumulate 6.83   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.33  implementation 0.67
sample agreement: 43 of 49 section-criterion pairs unanimous (88%)
single-sample totals would have been: 6.50 / 7.00 / 7.00   (all 3 samples: 6.83)
headings: h2 5
on threshold: none
splits: motivation[3] 2/1/1  prior_art[2] 2/2/0  prior_art[3] 0/2/0  coordination[4] 1/1/0
        insufficiency[5] 1/0/1  implementation[6] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/2  -> 2.00
  [3] 2 Overview                                   2/1/1  -> 1.33
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 2 (found by 3 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 3 (found by 3 of 21 passes): With the base proposal, if an overriding function wishes to have the same sequence of precondition and postcondition assertions as the overridden function, and have that sequence evaluated even when called directly, it needs to repeat the sequence.
candidate 4 (found by 2 of 21 passes): Runtime polymorphism is a fundamental part of C++. Many libraries and APIs are designed around virtual functions, making it one of the core idioms of the language.

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

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/0  -> 1.33
  [3] 2 Overview                                   0/2/0  -> 0.67
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns
candidate 2 (found by 3 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 3 (found by 2 of 21 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.
candidate 4 (found by 2 of 21 passes): Eiffel and D implement widening of preconditions by OR-ing the precondition assertions of the final overrider with those of all overridden functions, which removes the caller-facing precondition check.

## vehicle - grade 1.00 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 1/1/1  -> 1.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 3 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.

## coordination - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 1/1/0  -> 0.67
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Dependencies are often provided as headers and precompiled binaries.
candidate 2 (found by 1 of 21 passes): inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.

## insufficiency - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 1/0/1  -> 0.67
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): By contrast, designs based on "widen preconditions, narrow postconditions" — as in Eiffel, D, and Ada — cannot represent such cases correctly.

## implementation - grade 0.67  [binary: max] (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/1/1  -> 0.67
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.

-->
