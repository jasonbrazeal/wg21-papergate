Verdict: Strong (8/14)

The paper offers a solid foundation for its motivation and shows that the proposed syntax has a working implementation, but it leaves several parts of the standardization case largely unargued. The thinnest areas are the absence of any identified user population and the lack of discussion about how the feature would fit into the broader standard or interoperate with existing rules.

- The paper clearly establishes why the problem matters by connecting it to `move_only_function` and the broader difficulty of writing const-correct lambdas.
- It provides credible prior art and alternatives, including the approved direction of P0288 and the existing deleted assignment behavior for capture-bearing closures.
- The availability of a compiler implementation on GitHub and Compiler Explorer gives the proposal concrete implementation experience.
- The most glaring omission is that the paper never establishes who is affected by the problem, leaving the scale and urgency of the need unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.00   accumulate 8.50   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 93 of 98 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.50 / 8.00 / 7.50   (all 3 samples: 7.67)
headings: h2 13
on threshold: implementation
splits: motivation[9] 1/1/2  prior_art[10] 0/1/1  vehicle[5] 0/1/0  insufficiency[6] 0/1/0
        insufficiency[11] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   2/2/2  -> 2.00
  [5] Meta-Motivation                              1/1/1  -> 1.00
  [6] Motivation                                   2/2/2  -> 2.00
  [7] Proposal                                     2/2/2  -> 2.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        1/1/2  -> 1.33
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             2/2/2  -> 2.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): Applying `const` with more purpose and simpler syntax would improve the safety and security of such code
candidate 3 (found by 3 of 42 passes): Lambdas in such cases require work-arounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating intermediary types.
candidate 4 (found by 3 of 42 passes): The alternative is to simply leave otherwise const captures mutable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.

## audience - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/0/0  -> 0.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   2/2/2  -> 2.00
  [5] Meta-Motivation                              1/1/1  -> 1.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     2/2/2  -> 2.00
  [8] Implementation                               1/1/1  -> 1.00
  [9] Feature 3: Const Capture by Reference        2/2/2  -> 2.00
  [10] Implementation                               0/1/1  -> 0.67
  [11] Feature 4: Const Default Capture             1/1/1  -> 1.00
  [12] Concerns                                     2/2/2  -> 2.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P0288](https://wg21.link/P0288) (`move_only_function`) was approved by LEWG, and a central improvement is that it respects the const modifier on function types
candidate 2 (found by 3 of 42 passes): A `const` member would make the lambda closure assignment operators deleted, but lambda closures with captures [already delete the copy assignment operator](https://eel.is/c++draft/expr#prim.lambda.closure-15).
candidate 3 (found by 3 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.
candidate 4 (found by 3 of 42 passes): It is the default-capture analogue of “Const Capture on Mutable Call Operator”.

## vehicle - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/1/0  -> 0.33
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        1/1/1  -> 1.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.
candidate 2 (found by 1 of 42 passes): Applying `const` with more purpose and simpler syntax would improve the safety and security of such code

## coordination - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/0/0  -> 0.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 5 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/1/0  -> 0.33
  [7] Proposal                                     1/1/1  -> 1.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        1/1/1  -> 1.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/1/0  -> 0.33
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): The alternative is to simply leave otherwise const captures mutable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.
candidate 3 (found by 3 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.
candidate 4 (found by 1 of 42 passes): Lambdas in such cases require work-arounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating intermediary types.

## implementation - grade 2.00  [binary: max] (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/0/0  -> 0.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     2/2/2  -> 2.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The implementation is available on [GitHub](https://github.com/villevoutilainen/gcc/tree/lambda-p2034) and can be tested on [Compiler Explorer](https://godbolt.org/z/9fcoYeMMf).

-->
