Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of the problem it wants to solve and shows that a working implementation exists, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who is actually affected by the problem and whether the proposed syntax is necessary given the acknowledged library workarounds.

- The strongest support is the concrete demonstration that the feature has been implemented and can be tested in a compiler.
- The paper also establishes why the issue matters for const-correct libraries such as `move_only_function`, where logically const lambdas currently fail to work as expected.
- Prior art and alternatives are adequately grounded in earlier proposals and existing standard components, though the paper itself concedes that `std::cref` and `std::as_const` can achieve the same effect.
- The most glaring omission is any real account of who is affected, leaving the audience and the scale of the need unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.67   accumulate 8.00   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.17  insufficiency 0.83  implementation 2.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 7.00 / 7.50   (all 3 samples: 7.17)
headings: h2 13
on threshold: implementation
splits: prior_art[9] 1/2/2  vehicle[9] 0/0/1  coordination[4] 1/0/0  insufficiency[5] 1/0/1
        insufficiency[7] 1/0/1  insufficiency[9] 0/1/1  insufficiency[11] 1/0/0
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
  [9] Feature 3: Const Capture by Reference        1/1/1  -> 1.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             2/2/2  -> 2.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): Applying `const` with more purpose and simpler syntax would improve the safety and security of such code
candidate 3 (found by 3 of 42 passes): Lambdas in such cases require work-arounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating intermediary types.
candidate 4 (found by 3 of 42 passes): However there are situations where it would be useful to capture by `const` reference, such as when a read-only object is too large to copy.

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

## prior_art - grade 2.00 (fired in 9 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   2/2/2  -> 2.00
  [5] Meta-Motivation                              1/1/1  -> 1.00
  [6] Motivation                                   1/1/1  -> 1.00
  [7] Proposal                                     2/2/2  -> 2.00
  [8] Implementation                               1/1/1  -> 1.00
  [9] Feature 3: Const Capture by Reference        1/2/2  -> 1.67
  [10] Implementation                               1/1/1  -> 1.00
  [11] Feature 4: Const Default Capture             1/1/1  -> 1.00
  [12] Concerns                                     2/2/2  -> 2.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P0288](https://wg21.link/P0288) (`move_only_function`) was approved by LEWG, and a central improvement is that it respects the const modifier on function types (ie. `move_only_function<void(int) const>`).
candidate 2 (found by 3 of 42 passes): Type erased callables like `std::move_only_function` are the backbone of most asynchronous systems.
candidate 3 (found by 3 of 42 passes): Following the direction set out in [P2095](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2095r0.html), using the example in [P0780](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p0780r2.html), we are able to move arguments from caller, to lambda, to callee
candidate 4 (found by 3 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.

## vehicle - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/0/1  -> 0.33
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.

## coordination - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   1/0/0  -> 0.33
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
candidate 1 (found by 1 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.

## insufficiency - grade 0.83 (fired in 5 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] Meta-Motivation                              1/0/1  -> 0.67
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     1/0/1  -> 0.67
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/1/1  -> 0.67
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             1/0/0  -> 0.33
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 2 of 42 passes): Avoiding use of wrappers also makes lambda captures smaller and thus easier to read and reason about.
candidate 3 (found by 2 of 42 passes): The alternative is to simply leave otherwise const captures mutable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.
candidate 4 (found by 2 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.

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
