Verdict: Adequate to Strong (8/14)

The paper gives a reasonably grounded account of why object cohorts are useful and that they have real production history, but it does not carry that evidence through to the parts of the standardization argument that depend on it most. The strongest material concerns motivation and implementation experience, while the case for why this belongs in the standard rather than remaining a library facility is asserted rather than developed.

- The paper’s strongest support is its concrete, dated production use in Folly, which directly backs both the importance of the problem and the existence of implementation experience.
- The discussion of prior art and alternatives is adequately established, particularly through the reference to SG1 feedback and the contrast with global cleanup.
- The weakest part of the argument is the absence of any treatment of coordination and interoperability with other standardization efforts or existing facilities.
- The paper also leaves the central standardization question thin, since it recommends standardization and implies a library would be insufficient without actually making that case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.67   accumulate 7.67   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.00 / 8.00 / 7.00   (all 3 samples: 7.67)
headings: h2 11
on threshold: implementation
splits: motivation[5] 1/1/2  motivation[10] 2/1/2  audience[7] 1/1/0  insufficiency[7] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            1/1/2  -> 1.33
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                2/2/2  -> 2.00
  [10] Separating Cohort Object Retirement from ... 2/1/2  -> 1.67
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.
candidate 4 (found by 3 of 36 passes): Doing so avoids burdening the current thread with potentially performing amortized reclamation of tens of thousands of possibly unrelated retired objects, because calling `retire` may trigger amortized asynchronous reclamation.

## audience - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/1/0  -> 0.67
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 1 of 36 passes): It strikes a better balance between practicality and performance.
candidate 3 (found by 1 of 36 passes): The main advantage of the object cohort approach is its performance.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                2/2/2  -> 2.00
  [10] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This revision, P3427R2, revises R1 by following SG1 feedback.
candidate 2 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 3 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 4 (found by 3 of 36 passes): An alternative approach is the use of object cohorts, which are sets of protectable objects.

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Therefore, we recommend object cohorts for standardization.

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/1/0  -> 0.67
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## implementation - grade 2.00  [binary: max] (fired in 1 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            2/2/2  -> 2.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.

-->
