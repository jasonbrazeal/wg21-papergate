Verdict: Adequate to Strong (8/14)

The paper offers solid support in the areas that matter most for framing the problem: it explains why virtual functions are currently a gap in C++ contracts, surveys prior art and alternatives credibly, and argues why a language-level solution fits C++ better than a library or a more restrictive model. The support becomes much thinner when the paper turns to the practical case for standardization, particularly around who is concretely affected, how the feature would interoperate across component boundaries, and what implementation experience actually demonstrates.

- The strongest support is the established case for why virtual function contract support matters and why existing language-level alternatives are insufficient for C++.
- The paper also credibly establishes that prior designs and other languages do not adequately address the usage patterns the proposal targets.
- A notable weakness is that the affected-user evidence rests on a single EWG poll and a general claim about C++’s scale, without concrete user or codebase data.
- The most glaring omission is implementation experience: the paper claims a complete GCC implementation but does not establish what that implementation validates about the design’s feasibility or correctness.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 7 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.00   accumulate 8.50   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.50  coordination 1.00  insufficiency 0.50  implementation 0.33
sample agreement: 40 of 49 section-criterion pairs unanimous (82%)
single-sample totals would have been: 6.50 / 9.50 / 8.50   (all 3 samples: 8.17)
headings: h2 5
on threshold: vehicle
splits: motivation[3] 1/2/1  audience[3] 1/2/1  audience[4] 0/0/1  vehicle[5] 1/0/1
        coordination[4] 0/2/2  coordination[6] 0/2/0  insufficiency[5] 1/1/0
        insufficiency[6] 0/1/0  implementation[2] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/2  -> 2.00
  [3] 2 Overview                                   1/2/1  -> 1.33
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 2 (found by 3 of 21 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 3 (found by 3 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 4 (found by 3 of 21 passes): With the base proposal, if an overriding function wishes to have the same sequence of precondition and postcondition assertions as the overridden function, and have that sequence evaluated even when called directly, it needs to repeat the sequence.

## audience - grade 0.83 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   1/2/1  -> 1.33
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/1  -> 0.33
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): EWG poll from St. Louis (June 2024): P3097R0 — Contracts for C++: Support for Virtual Functions, we would like to see this paper merged into P2900 and progress contracts with virtual function support. SF/F/N/A/SA 18/15/5/1/2
candidate 2 (found by 1 of 21 passes): C++ is a mature and widely used language with billions of lines of existing code deployed across many diverse domains

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/2  -> 2.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.
candidate 2 (found by 3 of 21 passes): Eiffel and D implement widening of preconditions by OR-ing the precondition assertions of the final overrider with those of all overridden functions, which removes the caller-facing precondition check.
candidate 3 (found by 3 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns
candidate 4 (found by 3 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.

## vehicle - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 1/0/1  -> 0.67
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 2 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 3 (found by 1 of 21 passes): Extending the C++ facility to virtual functions requires understanding the kinds of correctness expectations that commonly apply to such functions, and ensuring that the proposed extension can express those expectations effectively.
candidate 4 (found by 1 of 21 passes): By contrast, C++ is a multi-paradigm language. Unlike Eiffel, C++ must accommodate adding assertions to existing code organised across independently developed components, and cannot reject correct code simply because it does not fit a particular programming paradigm.

## coordination - grade 1.00 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/2/2  -> 1.33
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/2/0  -> 0.67
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 2 (found by 1 of 21 passes): As an example, consider `QIODevice`, the base interface class of all I/O devices in the Qt framework.

## insufficiency - grade 0.50 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 1/1/0  -> 0.67
  [6] 5 Possible extensions                        0/1/0  -> 0.33
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): By contrast, designs based on "widen preconditions, narrow postconditions" — as in Eiffel, D, and Ada — cannot represent such cases correctly.
candidate 2 (found by 1 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns, even though they are both correct and common in real-world C++ systems
candidate 3 (found by 1 of 21 passes): However, this approach requires refactoring the base class function definition, which may not always be possible or practical.

## implementation - grade 0.33  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/1  -> 0.33
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): a complete implementation of that wording available in GCC.

-->
