Verdict: Excellent (12/14)

The paper’s support for its own standardization is uneven: it is strongest when arguing that the behavior already exists as vendor opt-ins and that portability is the only real addition, but it never convincingly shows who would be harmed by relying on those existing options or that the shipped implementations constitute experience with the exact portable guarantee being proposed.

- The paper firmly establishes that libc++ and Bloomberg’s BDE already provide the continuing response as a non-portable opt-in, so the marginal value of a standard guarantee is essentially portability alone.
- It also establishes that a library solution is already in use and that the reference implementers have no plans to generate exception-handling code around contract predicates.
- The thinnest support is in implementation experience, where the paper points to existing vendor options but does not establish that anyone has experience with the standardized, portable version of the guarantee it asks for.
- The most glaring omission is the affected audience: the paper claims teams would gain almost nothing from portability, but it never establishes who those teams are or why their existing build-option workflow is sufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 11.00   accumulate 12.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 1.67  insufficiency 2.00  implementation 1.33
sample agreement: 85 of 98 section-criterion pairs unanimous (87%)
single-sample totals would have been: 12.50 / 13.00 / 12.00   (all 3 samples: 11.50)
headings: h2 13
on threshold: coordination
splits: audience[4] 0/1/1  audience[5] 0/1/0  audience[11] 1/0/0  prior_art[4] 0/2/0
        prior_art[12] 0/1/1  vehicle[7] 0/1/1  coordination[4] 1/0/1  coordination[5] 2/2/0
        insufficiency[11] 1/2/2  implementation[5] 1/2/1  implementation[7] 0/0/1
        implementation[10] 2/0/2  implementation[12] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 2/2/2  -> 2.00
  [9] 3. A Cost Model for a Language Feature       2/2/2  -> 2.00
  [10] retirement date ᵄ, paying only �         2/2/2  -> 2.00
  [11] 10. Conclusion                               2/2/2  -> 2.00
  [12] 11. Disclosure                               0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): A team can already continue past a detected violation today, without the standard requiring it.
candidate 2 (found by 3 of 42 passes): Among the semantics that machinery carries is observe: on a detected violation the handler is called, and if it returns, execution continues past the violation.
candidate 3 (found by 3 of 42 passes): The continuing response already ships as a vendor opt-in.
candidate 4 (found by 2 of 42 passes): Standardizing the slice adds almost nothing over the build options libc++ and Bloomberg's BDE already ship, which deliver the same behavior, so its marginal value is near zero

## audience - grade 0.50 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/1/1  -> 0.67
  [5] In Plain Terms                               0/1/0  -> 0.33
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] retirement date ᵄ, paying only �         0/0/0  -> 0.00
  [11] 10. Conclusion                               1/0/0  -> 0.33
  [12] 11. Disclosure                               0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): the build options libc++ and Bloomberg's BDE already ship, which deliver the same behavior
candidate 2 (found by 1 of 42 passes): Standardizing the slice adds almost nothing over the build options libc++ and Bloomberg's BDE already ship, which deliver the same behavior, so its marginal value is near zero
candidate 3 (found by 1 of 42 passes): The first argument is that vendors already ship this.
candidate 4 (found by 1 of 42 passes): The continuing response for the class whose continuation is into undefined state, offered as a portable guarantee, is a different object, and priced on its own it does not earn standardization.

## prior_art - grade 2.00 (fired in 7 of 14 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/2/0  -> 0.67
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 2/2/2  -> 2.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] retirement date ᵄ, paying only �         2/2/2  -> 2.00
  [11] 10. Conclusion                               2/2/2  -> 2.00
  [12] 11. Disclosure                               0/1/1  -> 0.67
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 42 passes): P3100R8 makes observe available for implicit assertions on core-language operations.
candidate 3 (found by 3 of 42 passes): standardizing the guarantee adds almost nothing over the build options libc++ and Bloomberg's BDE already ship, so its marginal value is near zero
candidate 4 (found by 2 of 42 passes): P2000R5 [6], the Direction Group's direction paper, states the change strategy that the model turns into its benefit term.

## vehicle - grade 2.00 (fired in 6 of 14 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/1/1  -> 0.67
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       2/2/2  -> 2.00
  [10] retirement date ᵄ, paying only �         2/2/2  -> 2.00
  [11] 10. Conclusion                               2/2/2  -> 2.00
  [12] 11. Disclosure                               0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): What standardization would add on top of the vendor opt-in is portability: a guarantee that the continuing response behaves identically across GCC, Clang, and MSVC.
candidate 2 (found by 3 of 42 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.
candidate 3 (found by 2 of 42 passes): standardizing the slice adds almost nothing over the build options libc++ and Bloomberg's BDE already ship, which deliver the same behavior, so its marginal value is near zero
candidate 4 (found by 2 of 42 passes): Standardizing the response would add one thing on top: portability across vendors. A team turns this on per codebase, through a build setting it already controls, on a compiler it has already chosen. Cross-vendor portability buys that team almost nothing.

## coordination - grade 1.67 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/0/1  -> 0.67
  [5] In Plain Terms                               2/2/0  -> 1.33
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] retirement date ᵄ, paying only �         2/2/2  -> 2.00
  [11] 10. Conclusion                               0/0/0  -> 0.00
  [12] 11. Disclosure                               0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Standardizing the slice adds almost nothing over the build options libc++ and Bloomberg's BDE already ship, which deliver the same behavior, so its marginal value is near zero
candidate 2 (found by 2 of 42 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 3 (found by 1 of 42 passes): libc++ [9] and Bloomberg's BDE [10] already ship it as an opt-in, and both document it as bounded to an adoption period.
candidate 4 (found by 1 of 42 passes): The reference implementers state they will not generate exception-handling code around contract predicates (P3191R0 [8]).

## insufficiency - grade 2.00 (fired in 4 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] retirement date ᵄ, paying only �         2/2/2  -> 2.00
  [11] 10. Conclusion                               1/2/2  -> 1.67
  [12] 11. Disclosure                               0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 42 passes): libc++ [9] and Bloomberg's BDE [10] already ship it as an opt-in, and both document it as bounded to an adoption period.
candidate 3 (found by 2 of 42 passes): the marginal-value test then ends the analysis, because no other term can rescue it.
candidate 4 (found by 2 of 42 passes): standardizing the guarantee adds almost nothing over the build options libc++ and Bloomberg's BDE already ship, so its marginal value is near zero

## implementation - grade 1.33  [binary: max] (fired in 6 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] In Plain Terms                               1/2/1  -> 1.33
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/1  -> 0.33
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] retirement date ᵄ, paying only �         2/0/2  -> 1.33
  [11] 10. Conclusion                               1/1/1  -> 1.00
  [12] 11. Disclosure                               1/0/1  -> 0.67
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): the build options libc++ and Bloomberg's BDE already ship, which deliver the same behavior
candidate 2 (found by 3 of 42 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 3 (found by 3 of 42 passes): The continuing response for the class whose continuation is into undefined state, offered as a portable guarantee, is a different object, and priced on its own it does not earn standardization.
candidate 4 (found by 2 of 42 passes): libc++ [9] and Bloomberg's BDE [10] already ship it as an opt-in, and both document it as bounded to an adoption period.

-->
