Verdict: Adequate (5/14)

The paper offers solid support for the core motivation and for having considered alternatives, but it leaves several essential parts of the standardization case largely asserted rather than demonstrated. The thinnest areas are the absence of any implementation experience and the failure to show why the standard, rather than a library facility, is the necessary vehicle.

- The paper clearly establishes why postcondition captures matter and that existing C++26 facilities cannot express common postconditions such as `push_back` incrementing size.
- The discussion of prior art and alternatives is well grounded, including references to earlier proposals and a reasoned rejection of closure-based syntax and capture-by-reference.
- The claims about how frequently such postconditions arise and how many library authors are affected are repeated but not substantiated with concrete evidence.
- The paper provides no implementation experience and does not establish why this capability cannot be delivered through a library or why standardization is required.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 5 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 6.00   accumulate 5.33   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.33  implementation 0.00
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 5.50 / 5.00 / 5.50   (all 3 samples: 5.33)
headings: h2 8
on threshold: none
splits: audience[5] 0/1/1  prior_art[3] 2/2/1  prior_art[4] 2/2/1  coordination[3] 0/0/1
        insufficiency[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/2/2  -> 2.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   2/2/2  -> 2.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  2/2/2  -> 2.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Postcondition captures allow the user to assert common postconditions inexpressible in C++26, e.g., that `push_back` increments the size of the container by one.
candidate 2 (found by 3 of 30 passes): The ability to write init-captures on postcondition assertions is the "must-have" minimal feature to provide the functionality missing in C++26.
candidate 3 (found by 2 of 30 passes): postconditions that refer to the state of the program at the time the function was called — such as the postcondition of `push_back` that the size of the container is incremented by one — can be expressed as follows:
candidate 4 (found by 1 of 30 passes): postconditions that refer to the state of the program at the time the function was called — such as the postcondition of `push_back` that the size of the container is incremented by one — can be expressed as follows

## audience - grade 0.83 (fired in 2 of 10 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/1/1  -> 0.67
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Yet, such postconditions are relatively common in C++ libraries including the C++ standard library
candidate 2 (found by 2 of 30 passes): The need to refer to the state of the program at the time the function was called when checking the postcondition of that function arises frequently.
candidate 3 (found by 1 of 30 passes): Such postconditions are relatively common in C++ libraries including the C++ standard library

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/1  -> 1.67
  [4] 2 Overview                                   2/2/1  -> 1.67
  [5] 3 History and context                        2/2/2  -> 2.00
  [6] 4 Discussion  (part 1 of 2)                  2/2/2  -> 2.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): for examples, see [[P2900R14](https://wg21.link/p2900r14)] Section 3.4.4, and [[P3484R2](https://wg21.link/p3484r2)] Section 1
candidate 2 (found by 3 of 30 passes): The closure-based syntax proposal had a design issue: it placed the contract predicate inside braces `{...}`, even though C++ usually surrounds expressions with parentheses `(...)` and statements with braces `{...}`, and the predicate is an expression.
candidate 3 (found by 2 of 30 passes): We also do not allow default captures (see Section 4.3.3), or capturing `this` or `*this` (see Section 4.3.5), as these are less useful on postcondition assertions than they are on lambdas.
candidate 4 (found by 1 of 30 passes): However, we do not allow capture-by-reference. This would introduce several specification and implementation challenges (see Section 4.3.4) while not being all that useful in practice:

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

## coordination - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/1  -> 0.33
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 History and context                        0/0/0  -> 0.00
  [6] 4 Discussion  (part 1 of 2)                  0/0/0  -> 0.00
  [7] 4 Discussion  (part 2 of 2)                  0/0/0  -> 0.00
  [8] 5 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Such postconditions are relatively common in C++ libraries including the C++ standard library — for example, the postcondition of `push_back` that, if the function returns normally, the size of the container is incremented by one.

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
