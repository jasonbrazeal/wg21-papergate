Verdict: Adequate (5/14)

The paper offers solid support for the core motivation and for having considered prior art and alternatives, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas are the absence of a direct case for why this belongs in the standard, how it coordinates with existing or in-flight features, and whether any implementation experience exists.

- The strongest support is the clear demonstration that postcondition captures enable common and otherwise inexpressible assertions, such as `push_back` incrementing a container’s size.
- The paper also credibly establishes prior art and design alternatives, including references to related proposals and an explanation of why certain capture forms were excluded.
- The claim that such postconditions are relatively common in libraries, including the standard library, is asserted but not backed up with concrete examples or evidence.
- The most glaring omission is the lack of any established case for why this requires standardization or how it interoperates with the broader contracts feature set.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.67   accumulate 4.83   max 5.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.33  implementation 0.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 4.50 / 4.50   (all 3 samples: 4.83)
headings: h2 8
on threshold: none
splits: motivation[7] 0/1/1  prior_art[4] 1/1/2  insufficiency[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   2/2/2  -> 2.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  2/2/2  -> 2.00
  [7] 4 Discussion  (part 2 of 2)                  0/1/1  -> 0.67
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Postcondition captures allow the user to assert common postconditions inexpressible in C++26, e.g., that `push_back` increments the size of the container by one.
candidate 2 (found by 3 of 30 passes): The ability to write init-captures on postcondition assertions is the "must-have" minimal feature to provide the functionality missing in C++26.
candidate 3 (found by 2 of 30 passes): postconditions that refer to the state of the program at the time the function was called — such as the postcondition of `push_back` that the size of the container is incremented by one — can be expressed as follows
candidate 4 (found by 2 of 30 passes): Such behaviour subverts the intent of postcondition captures, but we cannot really do anything about it as the regularity of a type is not a compile-time-checkable property.

## audience - grade 0.50 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): such postconditions are relatively common in C++ libraries including the C++ standard library
candidate 2 (found by 1 of 30 passes): Yet, such postconditions are relatively common in C++ libraries including the C++ standard library

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   1/1/2  -> 1.33
  [5] 3 History and context                        2/2/2  -> 2.00
  [6] 4 Discussion  (part 1 of 2)                  2/2/2  -> 2.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): for examples, see [[P2900R14](https://wg21.link/p2900r14)] Section 3.4.4, and [[P3484R2](https://wg21.link/p3484r2)] Section 1
candidate 2 (found by 3 of 30 passes): We also do not allow default captures (see Section 4.3.3), or capturing `this` or `*this` (see Section 4.3.5), as these are less useful on postcondition assertions than they are on lambdas.
candidate 3 (found by 3 of 30 passes): The closure-based syntax proposal had a design issue: it placed the contract predicate inside braces `{...}`, even though C++ usually surrounds expressions with parentheses `(...)` and statements with braces `{...}`, and the predicate is an expression.
candidate 4 (found by 2 of 30 passes): The initialisation of a postcondition-assertion capture happens as part of evaluating the precondition assertions of the function, in the same lexical ordering that the postcondition assertion is in relation to the precondition assertions of that function.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  2/0/0  -> 0.67
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): However, for `pre` and `contract_assert`, the predicates of these contract assertions are checked immediately after such a capture is constructed; there is no temporal separation between the two as there is for `post`.

## implementation - grade 0.00  [binary: max] (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

-->
