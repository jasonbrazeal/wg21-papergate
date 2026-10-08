Verdict: Adequate (5/14)

The paper offers a solid opening case for why typed allocation and deallocation would be useful, but it does not carry that case through the areas that would justify standardization. The strongest material concerns the problem and the available design space, while the thinnest support appears where the paper needs to show that this belongs in the standard, that it can be implemented, and that existing practice or library solutions are insufficient.

- The paper clearly establishes that type-specific allocation functions would provide flexibility that current class-scoped and global operators cannot.
- It also establishes that the proposed direction has been considered against existing customization mechanisms and an earlier design.
- The paper claims but does not establish that the problem affects real codebases or that multiple libraries replacing global `operator new` creates the described ODR hazards.
- The most glaring omission is the absence of any established implementation experience or demonstration that the feature cannot be achieved through a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 5 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.33   accumulate 5.33   max 6.67

## SUMMARY
grades: motivation 1.67  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.67  insufficiency 0.50  implementation 0.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.00 / 5.50 / 4.50   (all 3 samples: 4.50)
headings: h2 9
on threshold: motivation, prior_art
splits: motivation[2] 2/1/1  motivation[4] 2/2/0  audience[4] 0/1/0  coordination[4] 0/2/2
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/1/1  -> 1.33
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/0  -> 1.33
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 Design choices and notes                   2/2/2  -> 2.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In addition to providing valuable information to the allocator, this allows the creation of type-specific `operator new` and `operator delete` for types that cannot have intrusive class-scoped operators specified.
candidate 2 (found by 3 of 33 passes): In the current specification it is not possible for a user to specify a constexpr `operator new` or `operator delete`.
candidate 3 (found by 2 of 33 passes): Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.
candidate 4 (found by 2 of 33 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators.

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
candidate 1 (found by 1 of 33 passes): Beyond these issues, a common problem in we see in the wild is codebases overriding the global (and untyped) `operator new` via the usual link-time mechanism and running into problems

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
  [9] 8 Proposed wording  (part 1 of 2)            1/1/1  -> 1.00
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

## coordination - grade 0.67 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/2/2  -> 1.33
  [5] 4 Current behavior recap                     0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Design choices and notes                   0/0/0  -> 0.00
  [8] 7 Overview of the wording                    0/0/0  -> 0.00
  [9] 8 Proposed wording  (part 1 of 2)            0/0/0  -> 0.00
  [10] 8 Proposed wording  (part 2 of 2)            0/0/0  -> 0.00
  [11] 9 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): multiple libraries attempt to replace the global `operator new` and end up with a complex ODR violation bug that depends on how the dynamic linker resolved weak definitions at load time

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
candidate 1 (found by 3 of 33 passes): However, even when defining `T::operator new` in-class, the only information available to the implementation is the type declaring the operator, not the type being allocated.

## implementation - grade 0.00  [binary: max] (fired in 0 of 11 sections, strong in 0)
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

-->
