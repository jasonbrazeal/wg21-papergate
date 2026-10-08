Verdict: Adequate (6/14)

The paper gives a clear account of the divergence between the CWG 1395 resolution and mainstream implementation practice, and it identifies a concrete alternative in reverting most of that change. Its support is thinnest where it needs to show that this is a problem only the standard can solve, rather than a matter of implementation convergence or non-normative guidance.

- The strongest support is the documented mismatch between the specified behavior and what GCC, Clang, and MSVC actually do, backed by a specific issue and a proposed wording direction.
- The paper also establishes prior art by citing the relevant CWG issues and naming the alternative of retaining only the tie-breaker from the earlier resolution.
- The case for who is affected rests on a single claim about EDG bug reports, without evidence of the volume or nature of the real-world code involved.
- The most glaring omission is the absence of any argument for why the standard must change, as opposed to accepting existing practice or issuing implementation guidance.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 5 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 6.67   accumulate 5.83   max 6.67

## SUMMARY
grades: motivation 1.83  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 1.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 6.00 / 6.00   (all 3 samples: 5.67)
headings: h2 10
on threshold: none
splits: motivation[4] 2/2/1  motivation[5] 1/2/2  prior_art[2] 1/1/0  prior_art[8] 0/1/1
        coordination[3] 0/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Examples                                     2/2/1  -> 1.67
  [5] Additional issues with the current wording   1/2/2  -> 1.67
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

## prior_art - grade 2.00 (fired in 6 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Examples                                     2/2/2  -> 2.00
  [5] Additional issues with the current wording   2/2/2  -> 2.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     1/1/1  -> 1.00
  [8] Option 2                                     0/1/1  -> 0.67
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): [CWG 1395](https://cplusplus.github.io/CWG/issues/1395.html) "Partial ordering of variadic templates reconsidered" was raised to address the ambiguity for a trailing function parameter pack
candidate 2 (found by 3 of 33 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 3 (found by 3 of 33 passes): Another potential issue with the current wording was pointed out in CWG 3154 "Clarify partial ordering involving variadic templates"
candidate 4 (found by 3 of 33 passes): Revert the changes in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/8 from CWG 1395, only keeping the tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11.

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

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Introduction                                 0/1/1  -> 0.67
  [4] Examples                                     0/0/0  -> 0.00
  [5] Additional issues with the current wording   0/0/0  -> 0.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.

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
  [6] Conclusion                                   1/1/1  -> 1.00
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.
candidate 2 (found by 3 of 33 passes): And as real-world code breaks with the rules as specified, I am not expecting other implementers to update their implementation any time soon.

-->
