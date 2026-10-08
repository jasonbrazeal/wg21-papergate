Verdict: Strong (8/14)

The paper offers solid evidence that object cohorts are a real, production-tested technique with meaningful performance advantages over the existing hazard pointer interface, but it does not adequately connect that usefulness to a need for ISO standardization rather than continued library use. The thinnest parts of the case concern who specifically is affected, why a library cannot suffice, and how the proposal would coordinate with the existing standard.

- The strongest support is the concrete, multi-year production use in Folly, which establishes both implementation experience and the practical importance of synchronous reclamation.
- The paper also clearly situates object cohorts against the already-standardized hazard pointer interface, showing what the new facility would add.
- The case weakens when it asserts general-purpose importance and performance benefits without identifying the affected user population or quantifying the claimed gains.
- The most glaring omission is the absence of any discussion of coordination and interoperability with the existing standard, leaving the standardization rationale incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.67   accumulate 8.00   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 79 of 84 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 8.50 / 7.50   (all 3 samples: 7.83)
headings: h2 11
on threshold: audience, implementation
splits: motivation[6] 1/2/2  audience[5] 0/1/0  audience[6] 2/2/1  audience[8] 0/1/0
        insufficiency[8] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            1/2/2  -> 1.67
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 2/2/2  -> 2.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.
candidate 4 (found by 3 of 36 passes): Doing so avoids burdening the current thread with potentially performing amortized reclamation of tens of thousands of possibly unrelated retired objects, because calling `retire` may trigger amortized asynchronous reclamation.

## audience - grade 1.00 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/1/0  -> 0.33
  [6] Implementation and Use Experience            2/2/1  -> 1.67
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/1/0  -> 0.33
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 3 (found by 1 of 36 passes): The main advantage of the object cohort approach is its performance.

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Hazard pointer interface from P2530R3 merged into the working draft (N5008):
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
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

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

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
  [8] Object Cohorts                               0/1/1  -> 0.67
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
