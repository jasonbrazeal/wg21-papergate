Verdict: Strong to Excellent (11/14)

The paper offers a reasonably grounded case for the existence of a transitional, opt-in observe semantic and for the fact that library-level or vendor-level mechanisms already deliver it, but it is much thinner when it comes to showing who would actually be served by making that behavior a portable standard guarantee. The strongest material concerns prior art and the limits of a library-only approach; the weakest concerns the affected population and the interoperability consequences of imposing the guarantee on all conforming implementations.

- The paper’s clearest support comes from established prior art and implementation experience, showing that libc++ and BDE already provide the observe semantic as a bounded, non-portable option.
- It also establishes why a library will not do, since the existing library and vendor mechanisms are explicitly opt-in and documented as transitional rather than portable.
- The case for why the standard should act is thinner, because the paper itself concedes that the recurring need is served equally by the non-portable vendor opt-in and that standardization adds almost nothing over it.
- The most glaring omission is the affected population: the paper claims vendors already ship this and that codebases in an adoption window would benefit, but it does not establish who those beneficiaries are or why they require a portable rather than vendor-specific guarantee.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 11.33   accumulate 11.33   max 11.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 2.00  coordination 0.67  insufficiency 2.00  implementation 2.00
sample agreement: 117 of 133 section-criterion pairs unanimous (88%)
single-sample totals would have been: 11.00 / 11.50 / 11.00   (all 3 samples: 11.17)
headings: h2 18
on threshold: implementation
splits: motivation[14] 0/2/0  motivation[15] 1/2/1  audience[5] 0/1/0  audience[12] 2/0/0
        prior_art[10] 2/2/0  prior_art[17] 1/0/0  vehicle[8] 0/0/1  vehicle[11] 1/0/0
        vehicle[13] 0/2/0  vehicle[15] 2/0/0  coordination[5] 0/0/1  coordination[8] 0/1/1
        coordination[10] 0/1/1  implementation[7] 1/0/1  implementation[12] 0/1/1
        implementation[17] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 8)  (SHARED PASSAGE)
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
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 2/2/2  -> 2.00
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         0/2/0  -> 0.67
  [15] 9. Questions Worth Considering               1/2/1  -> 1.33
  [16] 10. Conclusion                               2/2/2  -> 2.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Among the semantics that machinery carries is observe: on a detected violation the handler is called, and if it returns, execution continues past the violation.
candidate 2 (found by 3 of 57 passes): The object this paper prices is the decision to standardize that continuing response as a portable guarantee: a semantic every conforming implementation must provide, so that a program written against it behaves the same across vendors.
candidate 3 (found by 3 of 57 passes): Both are opt-in, both are non-portable, and both are documented as bounded to an adoption period.
candidate 4 (found by 3 of 57 passes): The benefit stream decays. The beneficiaries ᵄ(ᵆ) are codebases in an active adoption window - on a toolchain that implements the feature, carrying latent core-language undefined behavior they have not yet fixed, and continuing past it while they fix it.

## audience - grade 0.50 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               0/1/0  -> 0.33
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 0/0/0  -> 0.00
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             2/0/0  -> 0.67
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The first argument is that vendors already ship this.
candidate 2 (found by 1 of 57 passes): P3191R0 [8], from the libc++ team, sets the production requirement that a contract violation "should generate no code at all beyond the equivalent of a branch and a `__builtin_trap()`,"

## prior_art - grade 2.00 (fired in 12 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     1/1/1  -> 1.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              2/2/2  -> 2.00
  [8] 2. The Priced Object Is One Slice, Not th... 2/2/2  -> 2.00
  [9] 3. A Cost Model for a Language Feature       2/2/2  -> 2.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/0  -> 1.33
  [11] 5. A Transient Benefit Against a Perpetua... 1/1/1  -> 1.00
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               2/2/2  -> 2.00
  [16] 10. Conclusion                               1/1/1  -> 1.00
  [17] 11. Disclosure                               1/0/0  -> 0.33
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): P3100R8 proposes to guard the runtime-checkable cases of core-language undefined behavior with implicit contract assertions
candidate 2 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 3 (found by 3 of 57 passes): P3100R8 makes observe available for implicit assertions on core-language operations.
candidate 4 (found by 3 of 57 passes): Provenance: this is the language-feature form of the direction stated in P2000R5 [6] Section 5, "We change the language and standard library by gradually building on previous work or by providing a better alternative to an existing feature."

## vehicle - grade 2.00 (fired in 10 of 19 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     2/2/2  -> 2.00
  [5] In Plain Terms                               2/2/2  -> 2.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/1  -> 0.33
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 1/0/0  -> 0.33
  [12] 6. Where the Perpetual Cost Sits             2/2/2  -> 2.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/2/0  -> 0.67
  [14] 8. Possible Concerns                         2/2/2  -> 2.00
  [15] 9. Questions Worth Considering               2/0/0  -> 0.67
  [16] 10. Conclusion                               2/2/2  -> 2.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): What standardization would add on top of the vendor opt-in is portability: a guarantee that the continuing response behaves identically across GCC, Clang, and MSVC.
candidate 2 (found by 3 of 57 passes): The machinery the continuing response requires is machinery the implementers who ship hardening have stated they will not carry, and standardizing the portable guarantee obligates every implementation to carry it regardless.
candidate 3 (found by 3 of 57 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.
candidate 4 (found by 2 of 57 passes): Standardizing the slice adds almost nothing over the vendor build option that already delivers the same behavior, so its marginal value is near zero

## coordination - grade 0.67 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               0/0/1  -> 0.33
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              0/0/0  -> 0.00
  [8] 2. The Priced Object Is One Slice, Not th... 0/1/1  -> 0.67
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 0/1/1  -> 0.67
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             0/0/0  -> 0.00
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         0/0/0  -> 0.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The object this paper prices is the decision to standardize that continuing response as a portable guarantee: a semantic every conforming implementation must provide, so that a program written against it behaves the same across vendors.
candidate 2 (found by 2 of 57 passes): What standardization would add on top of the vendor opt-in is portability: a guarantee that the continuing response behaves identically across GCC, Clang, and MSVC.
candidate 3 (found by 1 of 57 passes): A portable guarantee means every conforming compiler must provide it, and a program can rely on it behaving the same on GCC, Clang, and MSVC.

## insufficiency - grade 2.00 (fired in 3 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               2/2/2  -> 2.00
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
  [16] 10. Conclusion                               0/0/0  -> 0.00
  [17] 11. Disclosure                               0/0/0  -> 0.00
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 57 passes): Both are opt-in, both are non-portable, and both are documented as bounded to an adoption period.
candidate 3 (found by 3 of 57 passes): The recurring need is served equally by the non-portable vendor opt-in of Section 4, which is what libc++ and BDE ship for exactly this purpose [9] [10], so it does not require the portable standard guarantee.

## implementation - grade 2.00  [binary: max] (fired in 7 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Acknowledgments                              0/0/0  -> 0.00
  [3] References                                   0/0/0  -> 0.00
  [4] Abstract                                     0/0/0  -> 0.00
  [5] In Plain Terms                               1/1/1  -> 1.00
  [6] Revision History                             0/0/0  -> 0.00
  [7] 1. Introduction                              1/0/1  -> 0.67
  [8] 2. The Priced Object Is One Slice, Not th... 0/0/0  -> 0.00
  [9] 3. A Cost Model for a Language Feature       0/0/0  -> 0.00
  [10] 4. The Marginal Value Over a Vendor Optio... 2/2/2  -> 2.00
  [11] 5. A Transient Benefit Against a Perpetua... 0/0/0  -> 0.00
  [12] 6. Where the Perpetual Cost Sits             0/1/1  -> 0.67
  [13] 7. Why the Usual Payoff From Standardizat... 0/0/0  -> 0.00
  [14] 8. Possible Concerns                         1/1/1  -> 1.00
  [15] 9. Questions Worth Considering               0/0/0  -> 0.00
  [16] 10. Conclusion                               1/1/1  -> 1.00
  [17] 11. Disclosure                               0/0/1  -> 0.33
  [18] Acknowledgments                              0/0/0  -> 0.00
  [19] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): libc++ provides the observe semantic as a build option. Bloomberg's BDE ships the same capability as bsls_review.
candidate 2 (found by 3 of 57 passes): libc++'s hardening documentation describes its observe semantic in exactly these terms [9]:
candidate 3 (found by 3 of 57 passes): A transitional capability ships today as a vendor opt-in, and its users' own documentation bounds it to a rollout period.
candidate 4 (found by 2 of 57 passes): No compiler yet implements implicit contract assertions, so the comparison reasons from deployed analogues rather than from a conforming implementation.

-->
