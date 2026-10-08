Verdict: Adequate to Strong (8/14)

The paper gives a workable but uneven account of why object cohorts should be standardized, with the strongest evidence coming from production use and implementation experience, while the case for coordination, interoperability, and why a library-only solution is insufficient remains largely unpersuasive.

- The clearest support is the documented use of object cohorts in Folly under the name `hazptr_obj_cohort` in heavy production since 2018, which grounds the proposal in real implementation experience.
- The paper also establishes prior art and alternatives by comparing the proposed cohort interface with the existing C++26 hazard pointer interface and showing how a free function enables the cohort equivalent.
- The thinnest part of the case is the absence of any discussion of coordination and interoperability with other standardization efforts or existing library facilities.
- The claim that a library will not do is asserted mainly through a single sentence about efficiency, without enough explanation of what specifically prevents a non-standard library implementation from providing the same guarantees.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.67   accumulate 8.17   max 8.67

## SUMMARY
grades: motivation 1.83  audience 0.83  prior_art 2.00  vehicle 0.83  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 8.50 / 8.50   (all 3 samples: 7.83)
headings: h2 11
on threshold: implementation
splits: motivation[5] 1/2/2  motivation[9] 1/2/2  motivation[10] 1/2/2  audience[4] 0/1/0
        audience[10] 1/0/1  vehicle[4] 0/1/1  insufficiency[7] 0/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Implementation and Use Experience            1/2/2  -> 1.67
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                1/2/2  -> 1.67
  [10] Separating Cohort Object Retirement from ... 1/2/2  -> 1.67
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): Doing so avoids burdening the current thread with potentially performing amortized reclamation of tens of thousands of possibly unrelated retired objects, because calling `retire` may trigger amortized asynchronous reclamation.
candidate 4 (found by 3 of 36 passes): However, it is often desirable to invoke asynchronous reclamation asynchronously in order to avoid burdening the thread retiring the object (typically a worker thread) with reclaiming a large number (e.g., tens of thousands) of (possibly unrelated) retired objects.

## audience - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 1/0/1  -> 0.67
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 2 of 36 passes): If a cohort is long-lived, large numbers (e.g., billions) of objects may be retired to it.
candidate 3 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.

## prior_art - grade 2.00 (fired in 5 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            1/1/1  -> 1.00
  [6] Synchronous Reclamation                      2/2/2  -> 2.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                2/2/2  -> 2.00
  [10] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 3 of 36 passes): An alternative approach is the use of object cohorts, which are sets of protectable objects.
candidate 3 (found by 3 of 36 passes): The following table shows two code snippets one using the P2530R3 C++26 hazard pointer interface and one using object cohorts, respectively.
candidate 4 (found by 3 of 36 passes): Therefore a free function hazard_pointer_try_reclamation() is added, so that users can write the cohort equivalent to the above non-cohort code snippet as follows:

## vehicle - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/1/1  -> 0.67
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [11] History                                      0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Therefore, we recommend object cohorts for standardization.
candidate 2 (found by 2 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.

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

## insufficiency - grade 0.33 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Implementation and Use Experience            0/0/0  -> 0.00
  [6] Synchronous Reclamation                      0/0/0  -> 0.00
  [7] Object Cohorts                               0/1/1  -> 0.67
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
