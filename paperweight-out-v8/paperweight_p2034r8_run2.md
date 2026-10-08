Verdict: Strong (8/14)

The paper offers solid support in a few important areas, particularly in showing that the feature has real motivation, prior standardization interest, and a working implementation. The case is much thinner, however, when it comes to demonstrating who is affected, why the standard is the right venue, and why a library solution cannot suffice.

- The strongest support comes from the implementation experience, where a proof-of-concept compiler change was completed quickly and is publicly available for testing.
- The paper also establishes meaningful prior art and alternatives, including EWG’s expressed interest and the precedent of P3963 for ordinary captures.
- The motivation is well grounded in the incompatibility between const-correct callable libraries and logically const lambdas, with concrete standard types cited.
- The most glaring omission is the absence of any established evidence about who is affected, leaving the scale and practical urgency of the problem unquantified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.67   accumulate 8.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 1.00  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.50 / 8.00 / 8.50   (all 3 samples: 8.33)
headings: h2 12
on threshold: vehicle
splits: motivation[7] 2/2/1  motivation[9] 1/2/2  prior_art[5] 1/2/2  prior_art[7] 0/0/2
        coordination[4] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 2/2/2  -> 2.00
  [5] 2 Initial Motivation: Const-correctness      2/2/2  -> 2.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 1/1/1  -> 1.00
  [7] 4 Design                                     2/2/1  -> 1.67
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 1/2/2  -> 1.67
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Taken together, this means the above standard types, and *any* other const-correct callable library, *cannot* work with logically const lambdas in the current form.
candidate 2 (found by 3 of 39 passes): Lambdas in such cases require workarounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating types.
candidate 3 (found by 3 of 39 passes): There seems to be a commonly shared feeling that there is a simpler language hiding in C++, and that the lambda syntax should be orthogonal to all the other ways of declaring callable types, not a microcosm unto itself.
candidate 4 (found by 3 of 39 passes): Capturing by `const` reference is nonetheless useful – read-only access to an object too large to copy – but today it takes `std::cref` or `std::as_const`, neither as concise nor as discoverable as `const&`.

## audience - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 0/0/0  -> 0.00
  [5] 2 Initial Motivation: Const-correctness      0/0/0  -> 0.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 0/0/0  -> 0.00
  [7] 4 Design                                     0/0/0  -> 0.00
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 0/0/0  -> 0.00
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 2/2/2  -> 2.00
  [5] 2 Initial Motivation: Const-correctness      1/2/2  -> 1.67
  [6] 3 Subsequent Motivation: Symmetry and Sim... 1/1/1  -> 1.00
  [7] 4 Design                                     0/0/2  -> 0.67
  [8] 5 Concerns                                   2/2/2  -> 2.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 2/2/2  -> 2.00
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): EWG has expressed interest in symmetry and simplicity for its own sake, and asked the authors to investigate the design space.
candidate 2 (found by 3 of 39 passes): P3963 (approved by EWG) restores it for ordinary captures; a const capture then correctly opts back out – exactly as a `const` member of a hand-written callable would.
candidate 3 (found by 2 of 39 passes): `std::move_only_function` (P0288, C++23), and since then `std::copyable_function` (P2548) and `std::function_ref` (P0792) in C++26, improved on `std::function` by respecting the `const` qualifier on their call signature.
candidate 4 (found by 2 of 39 passes): The alternative is to simply leave otherwise const captures modifiable, or to use `std::cref`.

## vehicle - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 0/0/0  -> 0.00
  [5] 2 Initial Motivation: Const-correctness      0/0/0  -> 0.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 0/0/0  -> 0.00
  [7] 4 Design                                     0/0/0  -> 0.00
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 2/2/2  -> 2.00
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): The standard specifies the closure as a class.
candidate 2 (found by 1 of 39 passes): We are not proposing a new model of lambdas; we are completing one the language has converged on since C++11 – letting the programmer spell the `const` and `mutable` members the desugared function object could always have held.

## coordination - grade 0.33 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 1/0/1  -> 0.67
  [5] 2 Initial Motivation: Const-correctness      0/0/0  -> 0.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 0/0/0  -> 0.00
  [7] 4 Design                                     0/0/0  -> 0.00
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 0/0/0  -> 0.00
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Taken together, this means the above standard types, and *any* other const-correct callable library, *cannot* work with logically const lambdas in the current form.

## insufficiency - grade 1.00 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 1/1/1  -> 1.00
  [5] 2 Initial Motivation: Const-correctness      1/1/1  -> 1.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 0/0/0  -> 0.00
  [7] 4 Design                                     0/0/0  -> 0.00
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 0/0/0  -> 0.00
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Taken together, this means the above standard types, and *any* other const-correct callable library, *cannot* work with logically const lambdas in the current form.
candidate 2 (found by 3 of 39 passes): The alternative is to simply leave otherwise const captures modifiable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 0/0/0  -> 0.00
  [5] 2 Initial Motivation: Const-correctness      0/0/0  -> 0.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 0/0/0  -> 0.00
  [7] 4 Design                                     2/2/2  -> 2.00
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 2/2/2  -> 2.00
  [10] 7 Wording Design                             0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Thanks                                       0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The implementation is available on [GitHub](https://github.com/villevoutilainen/gcc/tree/lambda-p2034) and can be tried on [Compiler Explorer](https://godbolt.org/z/9fcoYeMMf).
candidate 2 (found by 3 of 39 passes): GCC: Ville Voutilainen’s proof-of-concept for this proposal was “adjusting the types of the capture members … and the storage-class-specifier for mutable” – “a single afternoon” ([branch](https://github.com/villevoutilainen/gcc/tree/lambda-p2034))

-->
