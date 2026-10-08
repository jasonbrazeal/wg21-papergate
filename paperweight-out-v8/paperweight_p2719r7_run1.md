Verdict: Adequate (5/14)

The paper offers a solid conceptual motivation for why type-aware allocation customization would be useful, but it falls short of demonstrating that this particular mechanism is ready for standardization. The strongest material concerns the problem space and the design alternatives, while the case for standardization itself is largely asserted rather than shown.

- The paper clearly establishes why the feature matters, especially the inability to write constexpr allocation functions and the lack of type information available to class-scoped operators.
- The discussion of prior art and alternatives is substantive, including the Apple XNU technique and a rejected simpler design, which helps frame the proposal’s design choices.
- The paper claims but does not establish that real-world codebases suffer from global `operator new` replacement conflicts, and it offers no concrete implementation experience beyond a single edge-case observation.
- The paper does not establish why this cannot be done as a library or why standardization is necessary, leaving the central justification for a language change unproven.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 6 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 4.67   accumulate 6.00   max 7.67

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 1.00  insufficiency 0.50  implementation 0.33
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.00 / 5.00 / 4.50   (all 3 samples: 5.00)
headings: h2 9
on threshold: motivation, prior_art, coordination
splits: motivation[4] 0/2/0  audience[4] 1/0/0  prior_art[6] 0/0/1  implementation[7] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/2/0  -> 0.67
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 Design choices and notes                   2/2/2  -> 2.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In addition to providing valuable information to the allocator, this allows the creation of type-specific `operator new` and `operator delete` for types that cannot have intrusive class-scoped operators specified.
candidate 2 (found by 3 of 33 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators.
candidate 3 (found by 3 of 33 passes): In the current specification it is not possible for a user to specify a constexpr `operator new` or `operator delete`.
candidate 4 (found by 1 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/0/0  -> 0.33
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism

## prior_art - grade 1.50 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/1  -> 0.33
  [7] 6 Design choices and notes                   2/2/2  -> 2.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): C++ currently provides two ways of customizing the creation of objects in new expressions.
candidate 2 (found by 3 of 33 passes): Apple published [a blog post](https://security.apple.com/blog/towards-the-next-generation-of-xnu-memory-safety) explaining a technique used inside its kernel (XNU) to mitigate various exploits.
candidate 3 (found by 2 of 33 passes): In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism. Instead of using `std::type_identity<T>` as a tag, the compiler would search as per the following expression:
candidate 4 (found by 1 of 33 passes): This is analogous to the current behavior where we require specific concrete types in the parameter list even in dependent contexts.

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): we’ve seen scenarios where multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time
candidate 2 (found by 1 of 33 passes): multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.
candidate 2 (found by 1 of 33 passes): However, in addition to these intrusive mechanisms being cumbersome and error-prone, they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.
candidate 3 (found by 1 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.

## implementation - grade 0.33  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   1/0/0  -> 0.33
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): During edge case testing we found that the non-universality of sized deallocation creates a hazard where a less constrained sized deallocation may be selected over a more constrained unsized deallocation function.

-->
