Verdict: Adequate (5/14)

The paper gives a clear account of the existing divergence between the standard’s wording and mainstream implementation practice, and it grounds its motivation in a specific defect report and observed compiler behavior. The support is thinnest around the standardization-specific justifications: the paper does not explain why a standard change is the necessary remedy, nor does it address coordination, interoperability, or why a library-level solution would be inadequate.

- The strongest support is the established description of prior art, including CWG 1395, the proposed reversion, and the observed behavior of GCC, Clang, and MSVC.
- The paper also establishes why the issue matters by showing that the current specification is implemented almost nowhere and produces results users do not expect.
- Implementation experience is only claimed, since the paper cites EDG bug reports and real-world breakage without providing concrete examples or evidence of that experience.
- The most glaring omission is the absence of any case for why the standard itself must change, leaving the core standardization rationale unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 5.33   max 5.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 5.50 / 5.00   (all 3 samples: 5.33)
headings: h2 11
on threshold: none
splits: motivation[2] 0/1/1  motivation[7] 2/1/1  audience[4] 1/1/0  implementation[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Additional issues with the current wording   2/2/2  -> 2.00
  [7] Conclusion                                   2/1/1  -> 1.33
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.
candidate 2 (found by 3 of 36 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 3 (found by 3 of 36 passes): Having a feature specified in a way almost no one implements is not really useful, particularly if there are additional issues with that specification that need to be fixed.
candidate 4 (found by 2 of 36 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).

## audience - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/0  -> 0.67
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Additional issues with the current wording   2/2/2  -> 2.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     1/1/1  -> 1.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): [CWG 1395](https://cplusplus.github.io/CWG/issues/1395.html) "Partial ordering of variadic templates reconsidered" was raised to address the ambiguity for a trailing function parameter pack
candidate 2 (found by 3 of 36 passes): Revert the changes in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/8 from CWG 1395, only keeping the tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11.
candidate 3 (found by 2 of 36 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 4 (found by 2 of 36 passes): Another potential issue with the current wording was pointed out in CWG 3154 "Clarify partial ordering involving variadic templates"

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

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
