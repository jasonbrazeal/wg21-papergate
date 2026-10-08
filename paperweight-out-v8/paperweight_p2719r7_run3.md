Verdict: Adequate (5/14)

The paper offers a mixed case for its own standardization: it clearly motivates the problem and shows that existing mechanisms and prior design attempts leave a gap, but it does not establish why that gap must be filled by the standard rather than by a library, nor does it provide meaningful evidence of implementation experience or interoperability needs. The thinnest support is around the core standardization question itself, which is left entirely unaddressed.

- The strongest support is the explanation of why the feature matters, particularly the inability to provide type-specific allocation information or constexpr allocation operators under the current rules.
- The discussion of prior art and alternatives is also well established, showing both the limits of existing customization points and the evolution away from an earlier, simpler design.
- The paper claims but does not establish that a library solution is insufficient, relying on general statements about intrusive mechanisms without demonstrating that the proposed facility cannot be approximated outside the standard.
- The most glaring omission is the absence of any argument for why this belongs in the C++ standard at all, leaving the central justification for standardization unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 6 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.67   accumulate 6.00   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 1.00  insufficiency 0.50  implementation 0.33
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 6.50 / 5.00   (all 3 samples: 5.50)
headings: h2 9
on threshold: prior_art, coordination
splits: motivation[2] 2/1/2  audience[4] 0/1/0  prior_art[9] 1/0/0  implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/1/2  -> 1.67
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 Design choices and notes                   2/2/2  -> 2.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In addition to providing valuable information to the allocator, this allows the creation of type-specific `operator new` and `operator delete` for types that cannot have intrusive class-scoped operators specified.
candidate 2 (found by 3 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.
candidate 3 (found by 3 of 33 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators.
candidate 4 (found by 3 of 33 passes): In the current specification it is not possible for a user to specify a constexpr `operator new` or `operator delete`.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/1/0  -> 0.33
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
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   2/2/2  -> 2.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            1/0/0  -> 0.33
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): C++ currently provides two ways of customizing the creation of objects in new expressions.
candidate 2 (found by 3 of 33 passes): Apple published [a blog post](https://security.apple.com/blog/towards-the-next-generation-of-xnu-memory-safety) explaining a technique used inside its kernel (XNU) to mitigate various exploits.
candidate 3 (found by 2 of 33 passes): In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism.
candidate 4 (found by 1 of 33 passes): In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism. Instead of using `std::type_identity<T>` as a tag, the compiler would search as per the following expression:

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
candidate 1 (found by 2 of 33 passes): For example, we’ve seen scenarios where multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time
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
candidate 1 (found by 2 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.
candidate 2 (found by 1 of 33 passes): However, in addition to these intrusive mechanisms being cumbersome and error-prone, they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.

## implementation - grade 0.33  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/1/0  -> 0.33
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): During edge case testing we found that the non-universality of sized deallocation creates a hazard where a less constrained sized deallocation may be selected over a more constrained unsized deallocation function.

-->
