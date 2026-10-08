Verdict: Adequate (6/14)

The paper offers a clear account of the problem and the existing implementation divergence, but it does not build a complete case for why the standard should be changed now. The strongest material concerns the mismatch between the CWG 1395 resolution and widespread compiler behavior, while the thinnest parts are the absence of any direct argument for standardization itself and the reliance on a single sentence to carry several distinct burdens.

- The paper establishes that the current specification is out of step with GCC, Clang, and MSVC, and that this divergence has persisted for a decade.
- The paper establishes that reverting most of CWG 1395 would align the standard with existing practice or something close to it.
- The paper only claims, without supporting detail, that real-world users are affected and that other implementers are unlikely to change.
- The paper does not establish why this needs a standard change rather than remaining a known divergence, nor why a library solution or non-normative guidance would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 6 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 6.67   accumulate 5.83   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.17  implementation 1.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 5.50 / 5.50   (all 3 samples: 5.83)
headings: h2 11
on threshold: none
splits: prior_art[6] 2/1/2  coordination[4] 1/0/0  insufficiency[4] 1/0/0
        implementation[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Additional issues with the current wording   2/2/2  -> 2.00
  [7] Conclusion                                   1/1/1  -> 1.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).
candidate 2 (found by 3 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.
candidate 3 (found by 3 of 36 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 4 (found by 3 of 36 passes): Having a feature specified in a way almost no one implements is not really useful, particularly if there are additional issues with that specification that need to be fixed.

## audience - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Additional issues with the current wording   2/1/2  -> 1.67
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     2/2/2  -> 2.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).
candidate 2 (found by 3 of 36 passes): [CWG 1395](https://cplusplus.github.io/CWG/issues/1395.html) "Partial ordering of variadic templates reconsidered" was raised to address the ambiguity for a trailing function parameter pack
candidate 3 (found by 3 of 36 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 4 (found by 3 of 36 passes): Revert the changes in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/8 from CWG 1395, only keeping the tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.

## implementation - grade 1.00  [binary: max] (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/1  -> 0.33
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.
candidate 2 (found by 1 of 36 passes): And as real-world code breaks with the rules as specified, I am not expecting other implementers to update their implementation any time soon.

-->
