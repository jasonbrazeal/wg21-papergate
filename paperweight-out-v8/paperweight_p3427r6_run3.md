Verdict: Strong (8/14)

The paper offers solid grounding for its core motivation and for the existence of a production-tested implementation, but it leaves several parts of the standardization case more asserted than demonstrated. The thinnest support concerns how the proposed facility would fit with existing standard library reclamation mechanisms and why the same functionality could not be delivered adequately by a library outside the standard.

- The strongest support is the documented production use of object cohorts in Folly since 2018, which directly backs both the practical need and the implementation experience.
- The paper also clearly establishes the performance motivation by contrasting object cohorts with the impractical overhead of global cleanup.
- The case for standardization itself rests mainly on a recommendation and a rejection of the alternative, without showing what the standard specifically enables that a library cannot.
- The most glaring omission is any discussion of coordination or interoperability with existing or proposed standard reclamation facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 6 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 9.00   accumulate 8.17   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 75 of 84 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.50 / 7.50 / 8.00   (all 3 samples: 8.00)
headings: h2 11
on threshold: implementation
splits: motivation[5] 1/2/2  motivation[9] 1/2/1  audience[4] 1/0/1  audience[7] 1/0/0
        prior_art[4] 1/0/0  vehicle[6] 1/0/0  implementation[2] 0/1/0  implementation[6] 1/1/0
        implementation[7] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            1/2/2  -> 1.67
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                1/2/1  -> 1.33
  [10] Separating Cohort Object Retirement from ... 2/2/2  -> 2.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.
candidate 4 (found by 3 of 36 passes): If a cohort is long-lived, large numbers (e.g., billions) of objects may be retired to it. If such objects are not included in asynchronous reclamation, they would remain not reclaimed.

## audience - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/0/1  -> 0.67
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/0/0  -> 0.33
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 3 (found by 1 of 36 passes): For example, a concurrent hash map that uses hazard pointers is more generally usable if it allows arbitrary key and value types rather than only types without dependence on resources with independent lifetimes.
candidate 4 (found by 1 of 36 passes): The main advantage of the object cohort approach is its performance.

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/0/0  -> 0.33
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                2/2/2  -> 2.00
  [10] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 3 of 36 passes): The main drawback of the global cleanup approach is its high overhead that makes it impractical to use.
candidate 3 (found by 3 of 36 passes): The following table shows two code snippets one using the P2530R3 C++26 hazard pointer interface and one using object cohorts, respectively.
candidate 4 (found by 2 of 36 passes): The main advantage of the object cohort approach is its performance.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      1/0/0  -> 0.33
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Therefore, we recommend object cohorts for standardization.
candidate 2 (found by 1 of 36 passes): We do not recommend the standardization of the global cleanup approach due to these drawbacks and the lack of production experience of the necessity of such approach in contrast to the more efficient approach discussed in the following section.

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

## insufficiency - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## implementation - grade 2.00  [binary: max] (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/1/0  -> 0.33
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            2/2/2  -> 2.00
  [6] Synchronous Reclamation                      1/1/0  -> 0.67
  [7] Object Cohorts                               1/1/0  -> 0.67
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 2 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.
candidate 3 (found by 1 of 36 passes): Implementation and Use Experience 3 **Synchronous Reclamation** **3** Global Cleanup 3 **Object Cohorts** **4**
candidate 4 (found by 1 of 36 passes): We do not recommend the standardization of the global cleanup approach due to these drawbacks and the lack of production experience of the necessity of such approach in contrast to the more efficient approach discussed in the following section.

-->
