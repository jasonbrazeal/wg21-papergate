Verdict: Adequate to Strong (7/14)

The paper offers credible support for the usefulness of the feature and for the existence of a working implementation, but it leaves the standardization rationale thin in exactly the areas that matter most: why this belongs in the standard rather than in guidance or libraries, and how it fits with existing and future specifications.

- The strongest support is the concrete implementation experience, with a public branch and Compiler Explorer link demonstrating that the proposed syntax can be realized in a real compiler.
- The paper also establishes the motivating problem clearly, particularly the conflict between logically const lambdas and const-correct type-erased wrappers, and it shows awareness of existing workarounds and prior proposals.
- The case for why a library solution will not do is only asserted rather than demonstrated, since the paper does not show that the cited lifetime and readability concerns are inherent rather than manageable.
- The most glaring omission is the absence of any established argument for why the standard should change, including how the feature would interact with other language and library rules or with ongoing evolution of lambda capture semantics.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.33   accumulate 8.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 7.50 / 7.00   (all 3 samples: 7.00)
headings: h2 13
on threshold: implementation
splits: audience[6] 0/1/0  prior_art[4] 1/2/2  prior_art[8] 1/1/2  prior_art[9] 2/1/1
        prior_art[12] 2/1/2  insufficiency[5] 0/1/1  insufficiency[9] 1/0/0
        insufficiency[11] 1/0/1
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

## audience - grade 0.17 (fired in 1 of 14 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
  [6] Motivation                                   0/1/0  -> 0.33
  [7] Proposal                                     0/0/0  -> 0.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/0/0  -> 0.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): Type erased callables like `std::move_only_function` are the backbone of most asynchronous systems.

## prior_art - grade 1.83 (fired in 8 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   1/2/2  -> 1.67
  [5] Meta-Motivation                              1/1/1  -> 1.00
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     2/2/2  -> 2.00
  [8] Implementation                               1/1/2  -> 1.33
  [9] Feature 3: Const Capture by Reference        2/1/1  -> 1.33
  [10] Implementation                               1/1/1  -> 1.00
  [11] Feature 4: Const Default Capture             1/1/1  -> 1.00
  [12] Concerns                                     2/1/2  -> 1.67
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Following the direction set out in [P2095](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2095r0.html), using the example in [P0780](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p0780r2.html), we are able to move arguments from caller, to lambda, to callee
candidate 2 (found by 3 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.
candidate 3 (found by 3 of 42 passes): We could also invoke compiler magic using “as-if”
candidate 4 (found by 3 of 42 passes): Applying `std::cref` or `std::as_const` to each captured entity represents a chance to miss a variable and lose the protection of `const`.

## vehicle - grade 0.00 (fired in 0 of 14 sections, strong in 0)
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
  [5] Meta-Motivation                              0/1/1  -> 0.67
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     1/1/1  -> 1.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        1/0/0  -> 0.33
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             1/0/1  -> 0.67
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): The alternative is to simply leave otherwise const captures mutable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.
candidate 3 (found by 2 of 42 passes): Avoiding use of wrappers also makes lambda captures smaller and thus easier to read and reason about.
candidate 4 (found by 2 of 42 passes): Applying `std::cref` or `std::as_const` to each captured entity represents a chance to miss a variable and lose the protection of `const`.

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
