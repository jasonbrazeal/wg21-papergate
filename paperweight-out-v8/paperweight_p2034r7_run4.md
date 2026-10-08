Verdict: Strong (9/14)

The paper offers solid support for the core motivation and for the feasibility of the change, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who is actually affected and why the work cannot be done outside the standard.

- The strongest support is the concrete implementation experience, including a working compiler branch and a publicly testable proof-of-concept.
- The paper also establishes the motivating problem clearly, especially the incompatibility between logically const lambdas and const-correct callable libraries.
- Prior art and alternatives are well covered, with explicit references to related standard types and recent EWG direction.
- The most glaring omission is any real account of who is affected, leaving the practical reach and urgency of the problem largely unquantified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.50  insufficiency 1.00  implementation 2.00
sample agreement: 83 of 84 section-criterion pairs unanimous (99%)
single-sample totals would have been: 8.50 / 8.50 / 8.50   (all 3 samples: 8.50)
headings: h2 11
on threshold: vehicle
splits: motivation[7] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 2/2/2  -> 2.00
  [5] 2 Initial Motivation: Const-correctness      2/2/2  -> 2.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 1/1/1  -> 1.00
  [7] 4 Design                                     2/1/2  -> 1.67
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 2/2/2  -> 2.00
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Taken together, this means the above standard types, and *any* other const-correct callable library, *cannot* work with logically const lambdas in the current form.
candidate 2 (found by 3 of 36 passes): Lambdas in such cases require workarounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating types.
candidate 3 (found by 3 of 36 passes): There seems to be a commonly shared feeling that there is a simpler language hiding in C++, and that the lambda syntax should be orthogonal to all the other ways of declaring callable types, not a microcosm unto itself.
candidate 4 (found by 3 of 36 passes): Capturing by `const` reference is nonetheless useful – for read-only access to an object too large to copy – and today requires `std::cref` or `std::as_const`, which is not as concise, intuitive, or discoverable as `const&`.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 2/2/2  -> 2.00
  [5] 2 Initial Motivation: Const-correctness      2/2/2  -> 2.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 1/1/1  -> 1.00
  [7] 4 Design                                     0/0/0  -> 0.00
  [8] 5 Concerns                                   2/2/2  -> 2.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 2/2/2  -> 2.00
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): `std::move_only_function` (P0288, C++23), and since then `std::copyable_function` (P2548) and `std::function_ref` (P0792) in C++26, improved on `std::function` by respecting the `const` qualifier on their call signature.
candidate 2 (found by 3 of 36 passes): The alternative is to simply leave otherwise const captures modifiable, or to use `std::cref`.
candidate 3 (found by 3 of 36 passes): P3963 (approved by EWG) restores it for ordinary captures; a const capture then correctly opts back out – exactly as a `const` member of a hand-written callable would.
candidate 4 (found by 2 of 36 passes): EWG has expressed interest in symmetry and simplicity for its own sake, and asked the authors to investigate the design space.

## vehicle - grade 1.00 (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)
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
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): We are not proposing a new model of lambdas; we are completing one the language has converged on since C++11 – letting the programmer spell the `const` and `mutable` members the desugared function object could always have held.

## coordination - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] 1 Background                                 1/1/1  -> 1.00
  [5] 2 Initial Motivation: Const-correctness      0/0/0  -> 0.00
  [6] 3 Subsequent Motivation: Symmetry and Sim... 0/0/0  -> 0.00
  [7] 4 Design                                     0/0/0  -> 0.00
  [8] 5 Concerns                                   0/0/0  -> 0.00
  [9] 6 Lambdas Are Syntactic Sugar for Functio... 0/0/0  -> 0.00
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Taken together, this means the above standard types, and *any* other const-correct callable library, *cannot* work with logically const lambdas in the current form.

## insufficiency - grade 1.00 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Taken together, this means the above standard types, and *any* other const-correct callable library, *cannot* work with logically const lambdas in the current form.
candidate 2 (found by 2 of 36 passes): The alternative is to simply leave otherwise const captures modifiable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.
candidate 3 (found by 1 of 36 passes): Avoiding use of wrappers also makes lambda captures smaller and thus easier to read and reason about.

## implementation - grade 2.00  [binary: max] (fired in 2 of 12 sections, strong in 2)
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
  [10] Thanks                                       0/0/0  -> 0.00
  [11] Proposed Wording                             0/0/0  -> 0.00
  [12] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The implementation is available on [GitHub](https://github.com/villevoutilainen/gcc/tree/lambda-p2034) and can be tried on [Compiler Explorer](https://godbolt.org/z/9fcoYeMMf).
candidate 2 (found by 3 of 36 passes): GCC: Ville Voutilainen’s proof-of-concept for this proposal was “adjusting the types of the capture members … and the storage-class-specifier for mutable” – “a single afternoon” ([branch](https://github.com/villevoutilainen/gcc/tree/lambda-p2034))

-->
