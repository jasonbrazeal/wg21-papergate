Verdict: Adequate (4/14)

The paper offers a solid foundation for the feature’s motivation and design space, but it leaves several essential parts of the standardization case unaddressed. The strongest support is concentrated in the explanation of why the feature matters and the discussion of prior art, while the arguments for standard-library impact, the need for a standard rather than a library solution, coordination, and implementation experience are largely absent.

- The paper clearly establishes that postcondition captures enable common postconditions that C++26 cannot express, such as `push_back` incrementing a container’s size.
- It also grounds the design in prior art and alternatives, including a reasoned rejection of a closure-based syntax and explicit choices about capture initialization and restrictions.
- The claim that such postconditions are relatively common in libraries, including the standard library, is asserted but not backed up with concrete evidence.
- The most glaring omission is the absence of any established case for why this needs to be in the standard, why a library cannot provide it, or how it coordinates with existing and forthcoming contract facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 3 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.67   accumulate 4.33   max 4.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 4.00 / 4.50 / 4.50   (all 3 samples: 4.33)
headings: h2 8
on threshold: none
splits: motivation[7] 1/1/0  audience[3] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   2/2/2  -> 2.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  2/2/2  -> 2.00
  [7] 4 Discussion  (part 2 of 2)                  1/1/0  -> 0.67
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Postcondition captures allow the user to assert common postconditions inexpressible in C++26, e.g., that `push_back` increments the size of the container by one.
candidate 2 (found by 3 of 30 passes): The ability to write init-captures on postcondition assertions is the "must-have" minimal feature to provide the functionality missing in C++26.
candidate 3 (found by 2 of 30 passes): Such postconditions are inexpressible in C++26. Further, C++26 places restrictions on using non-reference parameters in postcondition assertions.
candidate 4 (found by 2 of 30 passes): postconditions that refer to the state of the program at the time the function was called — such as the postcondition of `push_back` that the size of the container is incremented by one — can be expressed as follows:

## audience - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/1/1  -> 0.67
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Yet, such postconditions are relatively common in C++ libraries including the C++ standard library

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   1/1/1  -> 1.00
  [5] 3 History and context                        2/2/2  -> 2.00
  [6] 4 Discussion  (part 1 of 2)                  2/2/2  -> 2.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): for examples, see [[P2900R14](https://wg21.link/p2900r14)] Section 3.4.4, and [[P3484R2](https://wg21.link/p3484r2)] Section 1
candidate 2 (found by 3 of 30 passes): The closure-based syntax proposal had a design issue: it placed the contract predicate inside braces `{...}`, even though C++ usually surrounds expressions with parentheses `(...)` and statements with braces `{...}`, and the predicate is an expression.
candidate 3 (found by 3 of 30 passes): The initialisation of a postcondition-assertion capture happens as part of evaluating the precondition assertions of the function, in the same lexical ordering that the postcondition assertion is in relation to the precondition assertions of that function.
candidate 4 (found by 2 of 30 passes): We also do not allow default captures (see Section 4.3.3), or capturing `this` or `*this` (see Section 4.3.5), as these are less useful on postcondition assertions than they are on lambdas.

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

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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
