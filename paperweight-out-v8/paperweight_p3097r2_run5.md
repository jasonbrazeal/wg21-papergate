Verdict: Strong (8/14)

The paper offers solid support for its standardization case in the areas that matter most: it clearly motivates the need for virtual function contract support, demonstrates meaningful prior art and alternatives, and backs its design with implementation experience in GCC. The support is thinnest where the paper relies on assertions rather than evidence, particularly in establishing who is affected, why the standard is the right venue, and why a library solution cannot suffice.

- The strongest support comes from the paper’s implementation experience, with a complete GCC implementation of the proposed wording available.
- The paper also clearly establishes why the feature matters, especially the current inability to use `pre` and `post` on virtual functions and the risk of non-adoption in affected domains.
- Prior art and alternatives are well covered, including specific shortcomings in earlier C++ proposals and comparisons with Eiffel, D, and Ada.
- The most glaring omission is the lack of established evidence for why a library will not do, leaving that central standardization argument largely asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 7 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.67   accumulate 8.50   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.33  coordination 0.33  insufficiency 0.17  implementation 1.67
sample agreement: 41 of 49 section-criterion pairs unanimous (84%)
single-sample totals would have been: 8.00 / 8.50 / 8.50   (all 3 samples: 8.17)
headings: h2 5
on threshold: vehicle, implementation
splits: audience[3] 1/1/2  prior_art[2] 2/0/2  prior_art[3] 0/0/2  vehicle[4] 2/0/0
        vehicle[5] 1/2/2  coordination[4] 0/0/2  insufficiency[5] 0/1/0  implementation[2] 2/2/1
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
candidate 1 (found by 3 of 21 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 2 (found by 3 of 21 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 3 (found by 3 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 4 (found by 3 of 21 passes): With the base proposal, if an overriding function wishes to have the same sequence of precondition and postcondition assertions as the overridden function, and have that sequence evaluated even when called directly, it needs to repeat the sequence.

## audience - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   1/1/2  -> 1.33
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): EWG poll from St. Louis (June 2024): P3097R0 — Contracts for C++: Support for Virtual Functions, we would like to see this paper merged into P2900 and progress contracts with virtual function support. SF/F/N/A/SA 18/15/5/1/2

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/0/2  -> 1.33
  [3] 2 Overview                                   0/0/2  -> 0.67
  [4] 3 Design goals and principles  (part 1 of 2) 2/2/2  -> 2.00
  [5] 3 Design goals and principles  (part 2 of 2) 2/2/2  -> 2.00
  [6] 5 Possible extensions                        2/2/2  -> 2.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns
candidate 2 (found by 3 of 21 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 3 (found by 2 of 21 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.
candidate 4 (found by 2 of 21 passes): Eiffel and D implement widening of preconditions by OR-ing the precondition assertions of the final overrider with those of all overridden functions, which removes the caller-facing precondition check.

## vehicle - grade 1.33 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 2/0/0  -> 0.67
  [5] 3 Design goals and principles  (part 2 of 2) 1/2/2  -> 1.67
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 1 of 21 passes): Any new C++ feature should be informed by prior art. We are aware of three languages that provide built-in precondition and postcondition assertions fully integrated with runtime polymorphism: Eiffel, D, and Ada.
candidate 3 (found by 1 of 21 passes): If C++ contract assertions fail to support them, developers in these domains are unlikely to refactor their code to follow the canonical object-oriented paradigm that requires unconditional substitutability — instead, they will simply not adopt contract assertions.
candidate 4 (found by 1 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns

## coordination - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/2  -> 0.67
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/1/0  -> 0.33
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): By contrast, designs that treat substitutability as a static property — as in Eiffel, D, Ada, and most earlier C++ proposals — cannot accommodate such usage patterns, even though they are both correct and common in real-world C++ systems

## implementation - grade 1.67  [binary: max] (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             2/2/1  -> 1.67
  [3] 2 Overview                                   0/0/0  -> 0.00
  [4] 3 Design goals and principles  (part 1 of 2) 0/0/0  -> 0.00
  [5] 3 Design goals and principles  (part 2 of 2) 0/0/0  -> 0.00
  [6] 5 Possible extensions                        0/0/0  -> 0.00
  [7] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): a complete implementation of that wording available in GCC.
candidate 2 (found by 1 of 21 passes): with wording rebased on the current C++26 working draft [[N5014](https://wg21.link/n5014)] and a complete implementation of that wording available in GCC.

-->
