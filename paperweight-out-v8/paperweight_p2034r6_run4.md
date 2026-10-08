Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of why const captures matter and how the feature could be implemented, but it leaves several parts of the standardization case underdeveloped, particularly around the affected audience and how the feature would fit with existing language and library machinery. The strongest material concerns motivation and implementation experience, while the weakest concerns the necessity of a core-language change and coordination with the broader ecosystem.

- The paper establishes a concrete motivation by showing that const-correct library components such as `move_only_function` cannot work with logically const lambdas under current rules.
- It also offers credible implementation experience, including a GCC implementation with regression tests and a public Compiler Explorer link.
- The discussion of prior art and alternatives is supported by references to `std::cref`, `std::as_const`, and the related P2034R5 work.
- The most glaring omission is any real account of who is affected or how widely the problem arises in practice.
- The case for why a library solution will not do is asserted mainly through repetition of the motivation, without a separate demonstration that the language change is required.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.67   accumulate 7.67   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 93 of 98 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.50 / 7.50   (all 3 samples: 7.33)
headings: h2 13
on threshold: implementation
splits: motivation[6] 2/2/1  prior_art[9] 2/1/2  prior_art[10] 1/0/0  vehicle[9] 0/1/1
        insufficiency[11] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   2/2/2  -> 2.00
  [5] Meta-Motivation                              1/1/1  -> 1.00
  [6] Motivation                                   2/2/1  -> 1.67
  [7] Proposal                                     2/2/2  -> 2.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        1/1/1  -> 1.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             2/2/2  -> 2.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): Applying `const` with more purpose and simpler syntax would improve the safety and security of such code
candidate 3 (found by 3 of 42 passes): Lambdas in such cases require work-arounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating intermediary types.
candidate 4 (found by 3 of 42 passes): There is no way to express the intent of const capture for capture defaults.

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
  [9] Feature 3: Const Capture by Reference        2/1/2  -> 1.67
  [10] Implementation                               1/0/0  -> 0.33
  [11] Feature 4: Const Default Capture             1/1/1  -> 1.00
  [12] Concerns                                     2/2/2  -> 2.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.
candidate 2 (found by 3 of 42 passes): It is the default-capture analogue of “Const Capture on Mutable Call Operator”.
candidate 3 (found by 3 of 42 passes): Ville Voutilainen implemented the proposal along with the extensions proposed in P2034R5 in GCC with regression tests, and gave the following report.
candidate 4 (found by 2 of 42 passes): [P0288](https://wg21.link/P0288) (`move_only_function`) was approved by LEWG, and a central improvement is that it respects the const modifier on function types (ie. `move_only_function<void(int) const>`).

## vehicle - grade 0.33 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/1/1  -> 0.67
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.

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

## insufficiency - grade 1.00 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     1/1/1  -> 1.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/0/0  -> 0.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             1/1/0  -> 0.67
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): The alternative is to simply leave otherwise const captures mutable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.
candidate 3 (found by 2 of 42 passes): Applying `std::cref` or `std::as_const` to each captured entity represents a chance to miss a variable and lose the protection of `const`.

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
