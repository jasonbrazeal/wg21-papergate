Verdict: Strong (8/14)

The paper offers solid evidence that object cohorts are a real, production-tested technique with a meaningful performance motivation, but it does not adequately connect that evidence to the case for ISO C++ standardization. The strongest support concerns implementation experience and the existence of prior art, while the thinnest parts are the arguments for why this belongs in the standard, why a library cannot suffice, and how the feature would coordinate with existing hazard pointer facilities.

- The paper clearly establishes implementation experience through Folly’s `hazptr_obj_cohort`, in production use since 2018.
- The paper establishes prior art and alternatives by showing concrete code comparisons and explaining how object cohorts differ from existing `retire`-based reclamation.
- The paper only claims, without establishing, why standardization is needed rather than continued use as a library facility.
- The paper does not establish coordination and interoperability with the existing C++26 hazard pointer interface beyond a general statement about synchronous reclamation’s importance.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 9.00   accumulate 7.83   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.50  coordination 0.17  insufficiency 0.33  implementation 2.00
sample agreement: 76 of 84 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.50 / 8.50 / 7.50   (all 3 samples: 7.67)
headings: h2 11
on threshold: implementation
splits: motivation[6] 2/1/2  motivation[11] 1/1/2  audience[5] 0/1/0  audience[8] 0/0/1
        prior_art[4] 1/1/0  prior_art[5] 1/1/0  coordination[5] 0/1/0  insufficiency[8] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            2/1/2  -> 1.67
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 1/1/2  -> 1.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.
candidate 4 (found by 3 of 36 passes): Doing so avoids burdening the current thread with potentially performing amortized reclamation of tens of thousands of possibly unrelated retired objects, because calling `retire` may trigger amortized asynchronous reclamation.

## audience - grade 0.67 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/1/0  -> 0.33
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/0/1  -> 0.33
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 3 (found by 1 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 1/1/0  -> 0.67
  [5] Motivation                                   1/1/0  -> 0.67
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 3 of 36 passes): An alternative approach is the use of object cohorts, which are sets of protectable objects.
candidate 3 (found by 3 of 36 passes): The following table shows two code snippets one using the P2530R3 C++26 hazard pointer interface and one using object cohorts, respectively.
candidate 4 (found by 3 of 36 passes): In contrast, the retirement of non-cohort objects (using `retire`) by convention may implicitly invoke asynchronous reclamation.

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Therefore, we recommend object cohorts for standardization.

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/1/0  -> 0.33
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.

## insufficiency - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               1/1/0  -> 0.67
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## implementation - grade 2.00  [binary: max] (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            2/2/2  -> 2.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.

-->
