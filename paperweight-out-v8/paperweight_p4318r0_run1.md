Verdict: Strong to Excellent (11/14)

The paper offers solid support for the existence of prior art, the inadequacy of a library-only solution, and the presence of implementation experience, but its case is thinnest where it needs to show who is concretely affected and how standardization would coordinate with existing vendor behavior. The strongest material is the evidence that the capability already exists as a non-portable, bounded opt-in, which paradoxically also undercuts the need for a portable standard guarantee.

- The paper clearly establishes that the proposed behavior already exists in libc++ and BDE as an opt-in, non-portable facility with documented adoption-period limits.
- It convincingly shows that a library cannot deliver the portable continuing-response guarantee the paper seeks, because the existing library mechanisms are explicitly bounded and non-portable.
- The weakest established area is coordination and interoperability, where the paper only gestures at libc++ documentation rather than showing how a standard guarantee would align with or improve on existing vendor hardening strategies.
- The most glaring omission is the affected constituency: the paper asserts a narrow set of codebases with unfixed latent undefined behavior but does not establish that this group is real, reachable, or sufficient to justify standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 11.33   accumulate 11.00   max 11.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 0.33  insufficiency 2.00  implementation 2.00
sample agreement: 111 of 133 section-criterion pairs unanimous (83%)
single-sample totals would have been: 11.00 / 11.50 / 10.00   (all 3 samples: 10.83)
headings: h2 18
on threshold: implementation
splits: motivation[8] 0/2/0  motivation[13] 2/0/0  motivation[14] 0/0/2  audience[5] 1/1/0
        audience[10] 1/0/0  audience[13] 1/0/0  prior_art[8] 2/2/0  prior_art[10] 2/0/0
        prior_art[11] 1/2/1  prior_art[13] 1/0/0  prior_art[17] 1/1/0  vehicle[9] 1/1/0
        vehicle[11] 2/0/2  vehicle[15] 1/0/0  coordination[10] 0/2/0  insufficiency[4] 1/0/0
        insufficiency[5] 1/2/2  insufficiency[16] 0/0/1  implementation[7] 0/0/1
        implementation[8] 0/1/0  implementation[14] 1/1/0  implementation[17] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 11 of 19 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/2/0  -> 0.67
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 2/2/2  -> 2.00
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 2/0/0  -> 0.67
  [14] 8. Possible Concerns                         0/0/2  -> 0.67
  [15] 9. Questions Worth Considering               2/2/2  -> 2.00
  [16] 10. Conclusion                               2/2/2  -> 2.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Both are opt-in, both are non-portable, and both are documented as bounded to an adoption period.
candidate 2 (found by 3 of 57 passes): The benefit stream decays. The beneficiaries ᵄ(ᵆ) are codebases in an active adoption window - on a toolchain that implements the feature, carrying latent core-language undefined behavior they have not yet fixed, and continuing past it while they fix it.
candidate 3 (found by 3 of 57 passes): The cost sits in three other places.
candidate 4 (found by 3 of 57 passes): Why does the continuing response need to be a portable standard guarantee rather than a vendor extension?

## audience - grade 0.50 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               1/1/0  -> 0.67
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 1/0/0  -> 0.33
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             0/0/0  -> 0.00
  [13] 7. Why the Usual Payoff From Standardizat... 1/0/0  -> 0.33
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 1 of 57 passes): Both are opt-in, both are non-portable, and both are documented as bounded to an adoption period.
candidate 3 (found by 1 of 57 passes): the constituency is narrow (codebases with unfixed latent core-language undefined behavior, on an implementing toolchain)

## prior_art - grade 2.00 (fired in 13 of 19 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 2/2/0  -> 1.33
  [9] 3. A Cost Model for a Language Feature       2/2/2  -> 2.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/0/0  -> 0.67
  [11] 5. A Transient Benefit Against a Perpetua... 1/2/1  -> 1.33
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 1/0/0  -> 0.33
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               2/2/2  -> 2.00
  [16] 10. Conclusion                               1/1/1  -> 1.00
  [17] 11. Disclosure                               1/1/0  -> 0.67
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): P3100R8 proposes to guard the runtime-checkable cases of core-language undefined behavior with implicit contract assertions
candidate 2 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 3 (found by 3 of 57 passes): Provenance: this is the language-feature form of the direction stated in P2000R5 [6] Section 5, "We change the language and standard library by gradually building on previous work or by providing a better alternative to an existing feature."
candidate 4 (found by 3 of 57 passes): libc++ states observe "should not be used outside of the adoption period" [9], and BDE frames review mode as "an interim step" [10].

## vehicle - grade 2.00 (fired in 10 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       1/1/0  -> 0.67
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 2/0/2  -> 1.33
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               1/0/0  -> 0.33
  [16] 10. Conclusion                               2/2/2  -> 2.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The priced object is the continuing response: log the violation through the handler, then proceed past it, for the class of checks whose continuation is undefined, offered as a portable guarantee that every conforming implementation must carry.
candidate 2 (found by 3 of 57 passes): What standardization would add on top of the vendor opt-in is portability: a guarantee that the continuing response behaves identically across GCC, Clang, and MSVC.
candidate 3 (found by 3 of 57 passes): The machinery the continuing response requires is machinery the implementers who ship hardening have stated they will not carry, and standardizing the portable guarantee obligates every implementation to carry it regardless.
candidate 4 (found by 3 of 57 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.

## coordination - grade 0.33 (fired in 1 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
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
  [12] 6. Where the Perpetual Cost Sits             0/0/0  -> 0.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): libc++'s hardening documentation describes its observe semantic in exactly these terms [9]:

## insufficiency - grade 2.00 (fired in 5 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/0/0  -> 0.33
  [5] In Plain Terms                               1/2/2  -> 1.67
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             0/0/0  -> 0.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/1  -> 0.33
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 57 passes): Both are opt-in, both are non-portable, and both are documented as bounded to an adoption period.
candidate 3 (found by 3 of 57 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.
candidate 4 (found by 1 of 57 passes): Standardizing the slice adds almost nothing over the vendor build option that already delivers the same behavior, so its marginal value is near zero

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               1/1/1  -> 1.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/1  -> 0.33
  [8] 2. The Priced Object Is One Slice, Not th... 0/1/0  -> 0.33
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             1/1/1  -> 1.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         1/1/0  -> 0.67
  [15] 9. Questions Worth Considering               1/1/1  -> 1.00
  [16] 10. Conclusion                               1/1/1  -> 1.00
  [17] 11. Disclosure                               0/1/1  -> 0.67
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 57 passes): libc++'s hardening documentation describes its observe semantic in exactly these terms [9]:
candidate 3 (found by 3 of 57 passes): The reference implementers decline this.
candidate 4 (found by 3 of 57 passes): libc++ [9] and Bloomberg's BDE [10] already ship it as an opt-in

-->
