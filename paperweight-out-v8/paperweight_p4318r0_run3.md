Verdict: Strong to Excellent (11/14)

The paper offers solid support for its claims about existing implementation experience and the availability of non-standard alternatives, but its case for who is affected and how the proposal would coordinate with other efforts is thin, resting more on assertion than demonstration. The strongest material concerns why the standard is not needed, since the paper argues the portable guarantee adds little over vendor opt-ins that already exist.

- The paper most convincingly establishes that the capability already exists as a vendor build option and a library facility, so the marginal value of standardization is near zero.
- It also clearly shows that a library or vendor extension can serve the recurring need without requiring a portable standard guarantee.
- The weakest part is the claim about who is affected, which cites the reference implementers’ decline but does not establish the broader population or its actual dependence on the feature.
- The most glaring omission is the lack of established coordination with related standardization efforts, since the paper notes the reference implementers decline but does not show how the proposal would interoperate with their stated requirements.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 10.33   accumulate 11.33   max 11.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 0.67  insufficiency 1.67  implementation 2.00
sample agreement: 111 of 133 section-criterion pairs unanimous (83%)
single-sample totals would have been: 10.50 / 13.00 / 10.00   (all 3 samples: 10.83)
headings: h2 18
on threshold: insufficiency, implementation
splits: motivation[8] 1/2/2  motivation[9] 0/0/1  motivation[10] 2/0/2  motivation[13] 2/2/0
        motivation[15] 1/1/2  audience[5] 0/1/1  audience[10] 0/1/0  audience[12] 1/0/0
        prior_art[4] 2/2/1  prior_art[9] 0/2/2  prior_art[10] 2/0/0  vehicle[8] 2/0/2
        vehicle[11] 2/1/2  vehicle[15] 0/0/2  coordination[10] 0/2/0  coordination[12] 0/2/0
        insufficiency[5] 2/2/0  insufficiency[14] 2/2/0  insufficiency[16] 0/1/1
        implementation[12] 1/0/2  implementation[15] 1/1/0  implementation[17] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 1/2/2  -> 1.67
  [9] 3. A Cost Model for a Language Feature       0/0/1  -> 0.33
  [10] 4. The Marginal Value Over a Vendor Optio... 2/0/2  -> 1.33
  [11] 5. A Transient Benefit Against a Perpetua... 2/2/2  -> 2.00
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 2/2/0  -> 1.33
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               1/1/2  -> 1.33
  [16] 10. Conclusion                               2/2/2  -> 2.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Standardizing the slice adds almost nothing over the vendor build option that already delivers the same behavior, so its marginal value is near zero.
candidate 2 (found by 3 of 57 passes): A team turns on continuation while it works through the latent violations in a codebase it is bringing under checking.
candidate 3 (found by 3 of 57 passes): Among the semantics that machinery carries is observe: on a detected violation the handler is called, and if it returns, execution continues past the violation.
candidate 4 (found by 3 of 57 passes): A cost model returns a wrong answer when it is pointed at the wrong object, so this section fixes the object before Section 3 supplies the model.

## audience - grade 0.50 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               0/1/1  -> 0.67
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 0/1/0  -> 0.33
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             1/0/0  -> 0.33
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 1 of 57 passes): libc++'s hardening documentation describes its observe semantic in exactly these terms [9]:
candidate 3 (found by 1 of 57 passes): The reference implementers decline this.

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/1  -> 1.67
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 2/2/2  -> 2.00
  [9] 3. A Cost Model for a Language Feature       0/2/2  -> 1.33
  [10] 4. The Marginal Value Over a Vendor Optio... 2/0/0  -> 0.67
  [11] 5. A Transient Benefit Against a Perpetua... 1/1/1  -> 1.00
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               2/2/2  -> 2.00
  [16] 10. Conclusion                               1/1/1  -> 1.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): P3100R8 proposes to guard the runtime-checkable cases of core-language undefined behavior with implicit contract assertions: checks the compiler inserts and evaluates under the C++26 Contracts semantics.
candidate 2 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 3 (found by 3 of 57 passes): P3100R8 [2] extends that machinery from assertions the programmer writes to assertions the language inserts at each runtime-checkable case of core-language undefined behavior.
candidate 4 (found by 3 of 57 passes): P3100R8 makes observe available for implicit assertions on core-language operations.

## vehicle - grade 2.00 (fired in 10 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              1/1/1  -> 1.00
  [8] 2. The Priced Object Is One Slice, Not th... 2/0/2  -> 1.33
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 2/1/2  -> 1.67
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               0/0/2  -> 0.67
  [16] 10. Conclusion                               2/2/2  -> 2.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): A vendor extension already carries the capability for the teams and the time that need it, and the vendor can retire it when the need passes.
candidate 2 (found by 3 of 57 passes): What standardization would add on top of the vendor opt-in is portability: a guarantee that the continuing response behaves identically across GCC, Clang, and MSVC.
candidate 3 (found by 3 of 57 passes): standardizing the portable guarantee obligates every implementation to carry it regardless.
candidate 4 (found by 3 of 57 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.

## coordination - grade 0.67 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               0/0/0  -> 0.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 0/2/0  -> 0.67
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             0/2/0  -> 0.67
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): Bloomberg's BDE library ships the same capability as a separate facility, bsls_review, whose own documentation frames review mode as "an interim step towards lowering the assertion level threshold for an existing application" [10].
candidate 2 (found by 1 of 57 passes): The reference implementers decline this. P3191R0 [8], from the libc++ team, sets the production requirement that a contract violation "should generate no code at all beyond the equivalent of a branch and a `__builtin_trap()`,"

## insufficiency - grade 1.67 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               2/2/0  -> 1.33
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             0/0/0  -> 0.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         2/2/0  -> 1.33
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/1/1  -> 0.67
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Both are opt-in, both are non-portable, and both are documented as bounded to an adoption period.
candidate 2 (found by 2 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 3 (found by 2 of 57 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.
candidate 4 (found by 1 of 57 passes): standardizing the guarantee adds almost nothing over the vendor build option that already ships, so its marginal value is near zero

## implementation - grade 2.00  [binary: max] (fired in 8 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               1/1/1  -> 1.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              1/1/1  -> 1.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             1/0/2  -> 1.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         1/1/1  -> 1.00
  [15] 9. Questions Worth Considering               1/1/0  -> 0.67
  [16] 10. Conclusion                               1/1/1  -> 1.00
  [17] 11. Disclosure                               1/0/0  -> 0.33
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 57 passes): No compiler yet implements implicit contract assertions, so the comparison reasons from deployed analogues rather than from a conforming implementation.
candidate 3 (found by 3 of 57 passes): libc++'s hardening documentation describes its observe semantic in exactly these terms [9]:
candidate 4 (found by 3 of 57 passes): The continuing response for the class whose continuation is into undefined state, offered as a portable guarantee, is a different object, and priced on its own it does not earn standardization.

-->
