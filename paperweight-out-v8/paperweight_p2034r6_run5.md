Verdict: Strong (8/14)

The paper offers a reasonably grounded case for the problem it addresses and for the feasibility of the proposed direction, but its argument for why this belongs in the standard—rather than in libraries or existing workarounds—is largely asserted rather than demonstrated. The thinnest support concerns the affected audience and the concrete interoperability consequences, which are mentioned but not substantiated.

- The strongest support is the implementation experience, with a working compiler branch and online testing available.
- The paper also clearly establishes why the issue matters for const-correct code and identifies relevant prior art and alternatives.
- The weakest part is the absence of any established description of who is affected by the problem.
- The claims about why a library solution will not do and why standardization is necessary are asserted through examples, but the paper does not establish them as broadly applicable or unavoidable.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 8.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.17  insufficiency 1.17  implementation 2.00
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.00 / 8.00 / 7.50   (all 3 samples: 7.83)
headings: h2 13
on threshold: implementation
splits: motivation[6] 1/2/2  motivation[11] 2/1/2  prior_art[9] 1/1/2  prior_art[10] 1/1/0
        coordination[4] 0/1/0  insufficiency[5] 0/1/0  insufficiency[7] 2/1/1
        insufficiency[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   2/2/2  -> 2.00
  [5] Meta-Motivation                              1/1/1  -> 1.00
  [6] Motivation                                   1/2/2  -> 1.67
  [7] Proposal                                     2/2/2  -> 2.00
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        1/1/1  -> 1.00
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             2/1/2  -> 1.67
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): Applying `const` with more purpose and simpler syntax would improve the safety and security of such code
candidate 3 (found by 3 of 42 passes): Lambdas in such cases require work-arounds, such as abandoning logical const correctness, abandoning ownership, or introducing intermediary {non-}const-propagating intermediary types.
candidate 4 (found by 3 of 42 passes): In addition to const-correctness, these features improve the consistency and symmetry – which the authors believe is a justification in its own right.

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

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 3)
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
  [9] Feature 3: Const Capture by Reference        1/1/2  -> 1.33
  [10] Implementation                               1/1/0  -> 0.67
  [11] Feature 4: Const Default Capture             1/1/1  -> 1.00
  [12] Concerns                                     2/2/2  -> 2.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P0288](https://wg21.link/P0288) (`move_only_function`) was approved by LEWG, and a central improvement is that it respects the const modifier on function types (ie. `move_only_function<void(int) const>`).
candidate 2 (found by 3 of 42 passes): Applying `const` with more purpose and simpler syntax would improve the safety and security of such code – especially for programmers that have learned about the `const` declarations, but are not yet comfortable with `const`-{non-} propagating wrappers.
candidate 3 (found by 3 of 42 passes): Following the direction set out in [P2095](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2095r0.html), using the example in [P0780](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p0780r2.html), we are able to move arguments from caller, to lambda, to callee
candidate 4 (found by 3 of 42 passes): A `const` member would make the lambda closure assignment operators deleted, but lambda closures with captures [already delete the copy assignment operator](https://eel.is/c++draft/expr#prim.lambda.closure-15).

## vehicle - grade 0.50 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Meta-Motivation                              0/0/0  -> 0.00
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

## coordination - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   0/1/0  -> 0.33
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

## insufficiency - grade 1.17 (fired in 4 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Polls                                        0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] Meta-Motivation                              0/1/0  -> 0.33
  [6] Motivation                                   0/0/0  -> 0.00
  [7] Proposal                                     2/1/1  -> 1.33
  [8] Implementation                               0/0/0  -> 0.00
  [9] Feature 3: Const Capture by Reference        0/1/0  -> 0.33
  [10] Implementation                               0/0/0  -> 0.00
  [11] Feature 4: Const Default Capture             0/0/0  -> 0.00
  [12] Concerns                                     0/0/0  -> 0.00
  [13] Thanks                                       0/0/0  -> 0.00
  [14] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This means `move_only_function`, and *any* other const-correct library, *cannot* work with logically const lambdas.
candidate 2 (found by 3 of 42 passes): The alternative is to simply leave otherwise const captures mutable, or to use `std::cref`. The former is less safe, and the latter may be undesirable because the lambda does not own the object referred to, which may create lifetime issues.
candidate 3 (found by 1 of 42 passes): Avoiding use of wrappers also makes lambda captures smaller and thus easier to read and reason about.
candidate 4 (found by 1 of 42 passes): The same effect can be achieved using `std::cref` and `std::as_const` – but this syntax is intuitive, concise and improves symmetry of this proposal.

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
