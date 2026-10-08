Verdict: Strong (8/14)

The paper offers meaningful support in a few areas, particularly by pointing to years of production use in Folly and by contrasting its approach with the existing C++26 hazard pointer interface. However, the case for standardization remains thin where it matters most: it does not explain why this needs to be in the standard rather than remaining a library facility, nor does it address how the proposed feature would coordinate or interoperate with the existing standard hazard pointer machinery.

- The strongest support is the implementation experience, with object cohorts in heavy production use in Folly since 2018.
- The paper also establishes prior art and alternatives by comparing its approach to the P2530R3 C++26 hazard pointer interface.
- The argument for why the standard should adopt this is asserted rather than developed, resting mainly on a recommendation and a general claim about usability.
- The most glaring omission is the absence of any discussion of coordination and interoperability with existing standard facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 8.00   accumulate 8.00   max 8.00

## SUMMARY
grades: motivation 1.83  audience 1.00  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 78 of 84 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 8.00 / 7.50   (all 3 samples: 7.50)
headings: h2 11
on threshold: implementation
splits: motivation[5] 2/1/2  motivation[10] 1/2/2  audience[7] 1/1/0  prior_art[3] 1/0/1
        prior_art[4] 0/0/1  vehicle[4] 0/1/0
## END SUMMARY

## motivation - grade 1.83 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            2/1/2  -> 1.67
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                1/1/1  -> 1.00
  [10] Separating Cohort Object Retirement from ... 1/2/2  -> 1.67
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): As a result, hazard pointer users must guarantee separately that the deleters of such objects do not depends on resources that may become subsequently unavailable.
candidate 4 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## audience - grade 1.00 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/1/0  -> 0.67
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 1 of 36 passes): The main advantage of the object cohort approach is its performance.
candidate 4 (found by 1 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 1/0/1  -> 0.67
  [4] Motivation                                   0/0/1  -> 0.33
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                2/2/2  -> 2.00
  [10] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 3 of 36 passes): The P2530R3 C++26 hazard pointer interface supports only asynchronous reclamation which does not guarantee the timing of the reclamation of protectable objects that are no longer protected.
candidate 3 (found by 3 of 36 passes): The main advantage of the object cohort approach is its performance.
candidate 4 (found by 3 of 36 passes): The following table shows two code snippets one using the P2530R3 C++26 hazard pointer interface and one using object cohorts, respectively.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Therefore, we recommend object cohorts for standardization.
candidate 2 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.

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

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
