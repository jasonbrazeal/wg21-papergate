Verdict: Adequate (6/14)

The paper gives a clear account of the divergence between the specified partial-ordering rule and the behavior of major implementations, but it does not build a complete case for changing the standard. The strongest material concerns existing practice and the availability of a concrete alternative, while the thinnest concerns why standardization is necessary and why a non-standard solution would not suffice.

- The paper establishes that GCC, Clang, and MSVC all follow a different rule from the one currently specified, and it identifies a concrete alternative in reverting most of CWG 1395 while keeping one tie-breaker.
- The paper claims real-world impact through bug reports against EDG, but it does not substantiate who is affected or how widespread the problem is.
- The paper does not establish why the standard itself must change, as opposed to leaving the specification alone or addressing the issue through other means.
- The paper offers no argument for why a library-level or implementation-level accommodation could not handle the problem, and it does not demonstrate implementation experience with the proposed wording.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 7.00   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 10
on threshold: none
splits: prior_art[2] 1/1/0  prior_art[3] 1/1/2  implementation[6] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Examples                                     2/2/2  -> 2.00
  [5] Additional issues with the current wording   2/2/2  -> 2.00
  [6] Conclusion                                   1/1/1  -> 1.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).
candidate 2 (found by 3 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.
candidate 3 (found by 3 of 33 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 4 (found by 3 of 33 passes): Having a feature specified in a way almost no one implements is not really useful, particularly if there are additional issues with that specification that need to be fixed.

## audience - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Examples                                     0/0/0  -> 0.00
  [5] Additional issues with the current wording   0/0/0  -> 0.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Introduction                                 1/1/2  -> 1.33
  [4] Examples                                     2/2/2  -> 2.00
  [5] Additional issues with the current wording   2/2/2  -> 2.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     1/1/1  -> 1.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 2 (found by 3 of 33 passes): Another potential issue with the current wording was pointed out in CWG 3154 "Clarify partial ordering involving variadic templates"
candidate 3 (found by 3 of 33 passes): Revert the changes in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/8 from CWG 1395, only keeping the tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11.
candidate 4 (found by 2 of 33 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Examples                                     0/0/0  -> 0.00
  [5] Additional issues with the current wording   0/0/0  -> 0.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Examples                                     0/0/0  -> 0.00
  [5] Additional issues with the current wording   0/0/0  -> 0.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Examples                                     0/0/0  -> 0.00
  [5] Additional issues with the current wording   0/0/0  -> 0.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Examples                                     0/0/0  -> 0.00
  [5] Additional issues with the current wording   0/0/0  -> 0.00
  [6] Conclusion                                   0/1/1  -> 0.67
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.
candidate 2 (found by 2 of 33 passes): And as real-world code breaks with the rules as specified, I am not expecting other implementers to update their implementation any time soon.

-->
