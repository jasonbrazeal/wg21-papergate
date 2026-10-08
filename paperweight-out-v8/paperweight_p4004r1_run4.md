Verdict: Adequate (6/14)

The paper gives a partial account of why the current wording causes divergence, but it leaves several core justifications for standardization largely unstated. The strongest material concerns existing implementation behavior and the desire to align the standard with that practice, while the thinnest areas are the absence of a direct case for why this belongs in the standard and why a library-level solution would not suffice.

- The paper clearly establishes that GCC, Clang, and MSVC already choose the non-variadic template, creating a body of existing practice worth standardizing.
- It also establishes that reverting most of CWG 1395 is the intended direction, with only the tie-breaker retained.
- The claim that real-world users are affected rests on a single mention of EDG bug reports and is not developed into a concrete demonstration of who is impacted or how widely.
- The paper does not establish why the standard is the necessary venue for this change or why a library-based approach could not address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 5 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 6.33   accumulate 5.67   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 5.50 / 6.00   (all 3 samples: 5.67)
headings: h2 11
on threshold: none
splits: prior_art[4] 1/2/2  prior_art[9] 1/1/0  coordination[4] 0/0/1  implementation[7] 1/0/0
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
candidate 4 (found by 3 of 36 passes): The tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11 doesn’t actually cover these cases, making the latter two function calls in the example ambiguous.

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

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/2/2  -> 1.67
  [5] Examples                                     2/2/2  -> 2.00
  [6] Additional issues with the current wording   2/2/2  -> 2.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     1/1/1  -> 1.00
  [9] Option 2                                     1/1/0  -> 0.67
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes to reconsider the resolution of CWG 1395 by reverting most of it, standardizing existing practice (or something close to existing practice).
candidate 2 (found by 3 of 36 passes): GCC, Clang, and MSVC all pick #2 (preferring the non-variadic template), but with the resolution of CWG 1395, #1 should be chosen.
candidate 3 (found by 3 of 36 passes): Revert the changes in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/8 from CWG 1395, only keeping the tie-breaker in [[temp.deduct.partial]](https://eel.is/c++draft/temp.deduct.partial)/11.
candidate 4 (found by 2 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.

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
  [4] Introduction                                 0/0/1  -> 0.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Additional issues with the current wording   0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.

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
  [7] Conclusion                                   1/0/0  -> 0.33
  [8] Option 1                                     0/0/0  -> 0.00
  [9] Option 2                                     0/0/0  -> 0.00
  [10] Wording for Option 1 (relative to N5032)     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): 10 years later only EDG implements that approach and gets bug reports for real-world code where users expect a different partial ordering result.
candidate 2 (found by 1 of 36 passes): It therefore seems reasonable to specify existing practice (or something close to existing practice).

-->
