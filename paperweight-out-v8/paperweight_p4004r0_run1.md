Verdict: Adequate (6/14)

The paper gives a clear account of the technical problem and the divergence between the standard’s current direction and widespread implementation practice, but it leaves several parts of the standardization case largely asserted rather than demonstrated. The strongest support is for why the issue matters and what alternatives exist, while the thinnest areas concern the need for a standard change as such, why a library solution cannot suffice, and concrete implementation experience.

- The paper establishes why the issue matters by showing that the CWG 1395 resolution conflicts with the behavior of GCC, Clang, and MSVC and leaves real cases ambiguous.
- The paper establishes prior art and alternatives by identifying the relevant core issues and explaining both the pre-CWG 1395 behavior and a possible partial revert.
- The paper only claims, without substantiating detail, that users are affected and that implementation experience exists, relying on a general reference to bug reports against EDG.
- The paper does not establish why a standard change is needed or why a library solution would not do, leaving the standardization rationale incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 7.00   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 10
on threshold: none
splits: motivation[6] 1/2/1  prior_art[2] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Examples                                     2/2/2  -> 2.00
  [5] Additional issues with the current wording   2/2/2  -> 2.00
  [6] Conclusion                                   1/2/1  -> 1.33
  [7] Option 1                                     0/0/0  -> 0.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).
candidate 2 (found by 3 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.
candidate 3 (found by 3 of 33 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 4 (found by 3 of 33 passes): The tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11 doesn’t actually cover these cases, making the latter two function calls in the example ambiguous.

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

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Examples                                     2/2/2  -> 2.00
  [5] Additional issues with the current wording   2/2/2  -> 2.00
  [6] Conclusion                                   0/0/0  -> 0.00
  [7] Option 1                                     1/1/1  -> 1.00
  [8] Option 2                                     0/0/0  -> 0.00
  [9] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Another potential issue with the current wording was pointed out in CWG 3154 "Clarify partial ordering involving variadic templates"
candidate 2 (found by 3 of 33 passes): Revert the changes in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/8 from CWG 1395, only keeping the tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11.
candidate 3 (found by 2 of 33 passes): 10 years later only EDG implements that approach and gets bugs reports for real-world code where users expect a different partial ordering result.
candidate 4 (found by 2 of 33 passes): Prior to CWG 1395, trying to deduce a non-pack from an argument pack always failed, resulting in #1 to not be at least as specialized as #2 (and ultimately making #2 more specialized).

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
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

-->
