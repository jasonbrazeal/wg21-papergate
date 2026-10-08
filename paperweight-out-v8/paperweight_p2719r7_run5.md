Verdict: Adequate (5/14)

The paper offers some useful context about existing techniques and prior discussions, but it does not build a sustained case that the proposed facility belongs in the C++ standard. The strongest material concerns alternatives and prior art, while the thinnest concerns the basic rationale for standardization, the affected audience, and evidence that the design works in practice.

- The paper’s discussion of prior art and alternatives is its most concrete support, including Apple’s published technique and earlier draft mechanisms.
- The claims about coordination problems and the limits of library-only solutions gesture at real concerns, but they are asserted rather than demonstrated with sufficient detail.
- The paper does not establish who is affected or why the standard is the necessary venue, leaving the core standardization need largely unargued.
- The implementation experience is only claimed, with no substantive evidence that the proposed approach has been tried and validated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 5 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.33   accumulate 5.67   max 7.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 1.00  insufficiency 0.50  implementation 0.33
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 4.00 / 4.50   (all 3 samples: 4.67)
headings: h2 9
on threshold: motivation, prior_art, coordination
splits: motivation[7] 2/1/2  prior_art[2] 1/0/1  prior_art[9] 1/0/0  implementation[7] 1/0/0
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 Design choices and notes                   2/1/2  -> 1.67
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In addition to providing valuable information to the allocator, this allows the creation of type-specific `operator new` and `operator delete` for types that cannot have intrusive class-scoped operators specified.
candidate 2 (found by 3 of 33 passes): In the current specification it is not possible for a user to specify a constexpr `operator new` or `operator delete`.
candidate 3 (found by 2 of 33 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators.
candidate 4 (found by 1 of 33 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators. Doing so today requires injecting operators into the relevant types, which often results in extensive use of macros.

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## prior_art - grade 1.50 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/0/1  -> 0.67
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   2/2/2  -> 2.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            1/0/0  -> 0.33
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Apple published [a blog post](https://security.apple.com/blog/towards-the-next-generation-of-xnu-memory-safety) explaining a technique used inside its kernel (XNU) to mitigate various exploits.
candidate 2 (found by 3 of 33 passes): In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism. Instead of using `std::type_identity<T>` as a tag, the compiler would search as per the following expression:
candidate 3 (found by 2 of 33 passes): C++ currently provides two ways of customizing the creation of objects in new expressions.
candidate 4 (found by 1 of 33 passes): The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”.

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
candidate 1 (found by 2 of 33 passes): For example, we’ve seen scenarios where multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time.
candidate 2 (found by 1 of 33 passes): multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)
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
candidate 1 (found by 2 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.
candidate 2 (found by 1 of 33 passes): they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.

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
