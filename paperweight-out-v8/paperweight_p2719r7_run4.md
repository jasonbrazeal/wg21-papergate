Verdict: Adequate (5/14)

The paper offers a mixed case for its own standardization, with its strongest support concentrated in explaining why the problem matters and in surveying existing mechanisms and alternatives. The argument becomes noticeably thinner when it moves from motivation to evidence: claims about real-world impact, implementation experience, interoperability hazards, and the necessity of a language change are asserted rather than demonstrated.

- The paper clearly establishes that current language mechanisms do not allow type-specific allocation customization for third-party or open sets of types, and that constexpr allocation functions are currently impossible.
- The discussion of existing customization points and the Apple XNU technique provides a credible account of prior art and the design space.
- The paper claims widespread real-world problems from global `operator new` replacement and ODR violations, but does not substantiate how common or severe these are.
- The most glaring omission is the absence of any established implementation experience or evidence that a library-level solution cannot address the problem, leaving the case for standardization itself largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 6 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.67   accumulate 5.50   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 1.50  vehicle 0.00  coordination 0.33  insufficiency 0.50  implementation 0.33
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 4.50 / 6.50 / 4.00   (all 3 samples: 5.00)
headings: h2 9
on threshold: prior_art
splits: motivation[2] 1/2/2  audience[4] 1/1/0  prior_art[9] 1/1/0  coordination[4] 0/2/0
        implementation[3] 0/1/0  implementation[4] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/2/2  -> 1.67
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
candidate 2 (found by 3 of 33 passes): This results in developers various creative (often macro-based) mechanisms to define these allocation functions manually, or circumventing the language-provided allocation mechanisms entirely in order to track the allocated types.
candidate 3 (found by 3 of 33 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators.
candidate 4 (found by 3 of 33 passes): In the current specification it is not possible for a user to specify a constexpr `operator new` or `operator delete`.

## audience - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/0  -> 0.67
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism
candidate 2 (found by 1 of 33 passes): Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism and running into problems

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
  [9] 8 Proposed wording  (part 1 of 2)            1/1/0  -> 0.67
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): C++ currently provides two ways of customizing the creation of objects in new expressions.
candidate 2 (found by 3 of 33 passes): Apple published [a blog post](https://security.apple.com/blog/towards-the-next-generation-of-xnu-memory-safety) explaining a technique used inside its kernel (XNU) to mitigate various exploits.
candidate 3 (found by 3 of 33 passes): In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism. Instead of using `std::type_identity<T>` as a tag, the compiler would search as per the following expression:
candidate 4 (found by 1 of 33 passes): [ Drafting note: The new wording for the return type of allocation and deallocation operators should resolve CWG1676 “`auto` return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “`auto` return type for `main`”. ]

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

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/2/0  -> 0.67
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time

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
candidate 1 (found by 1 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.
candidate 2 (found by 1 of 33 passes): they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.
candidate 3 (found by 1 of 33 passes): However, in addition to these intrusive mechanisms being cumbersome and error-prone, they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.

## implementation - grade 0.33  [binary: max] (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/1/0  -> 0.33
  [4] 3 Motivation                                 0/1/0  -> 0.33
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Simplified the lookup mechanism by removing the need to perform ADL (based on implementation experience)
candidate 2 (found by 1 of 33 passes): A few years ago, Apple published [a blog post](https://security.apple.com/blog/towards-the-next-generation-of-xnu-memory-safety) explaining a technique used inside its kernel (XNU) to mitigate various exploits.

-->
