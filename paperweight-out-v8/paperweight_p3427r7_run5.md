Verdict: Strong (8/14)

The paper offers solid grounding in production use and prior art, but its case for standardization is uneven: it demonstrates that object cohorts exist, perform well, and have shipped in Folly, yet it does not convincingly show why they belong in the standard rather than remaining a library facility. The thinnest areas are coordination with existing hazard pointer machinery and the absence of any interoperability discussion.

- The strongest support is implementation experience, with Folly’s `hazptr_obj_cohort` in heavy production use since 2018.
- The paper also establishes prior art and alternatives by contrasting object cohorts with the C++26 hazard pointer interface and global cleanup.
- The case for why a library will not do is only claimed, resting on performance drawbacks of global cleanup without showing that a non-standard library solution is insufficient.
- The most glaring omission is coordination and interoperability, where the paper offers nothing about how object cohorts would fit with the existing standard hazard pointer design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 8.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.50 / 7.50 / 8.00   (all 3 samples: 7.83)
headings: h2 11
on threshold: implementation
splits: audience[5] 1/1/0  audience[8] 0/1/1  prior_art[4] 1/1/0  prior_art[11] 1/0/0
        vehicle[5] 0/0/1  insufficiency[5] 1/0/0  insufficiency[7] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            2/2/2  -> 2.00
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 2/2/2  -> 2.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): The main advantage of the object cohort approach is its performance.
candidate 4 (found by 3 of 36 passes): Doing so avoids burdening the current thread with potentially performing amortized reclamation of tens of thousands of possibly unrelated retired objects, because calling `retire` may trigger amortized asynchronous reclamation.

## audience - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/0  -> 0.67
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/1/1  -> 0.67
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 2 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 3 (found by 2 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## prior_art - grade 2.00 (fired in 7 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 1/1/0  -> 0.67
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 1/0/0  -> 0.33
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): a concurrent hash map that uses hazard pointers is more generally usable if it allows arbitrary key and value types rather than only types without dependence on resources with independent lifetimes.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 3 of 36 passes): An alternative approach is the use of object cohorts, which are sets of protectable objects.
candidate 4 (found by 3 of 36 passes): The following table shows two code snippets one using the P2530R3 C++26 hazard pointer interface and one using object cohorts, respectively.

## vehicle - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/1  -> 0.33
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Therefore, we recommend object cohorts for standardization.
candidate 2 (found by 1 of 36 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 3 (found by 1 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

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

## insufficiency - grade 0.33 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/0/0  -> 0.33
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      1/0/0  -> 0.33
  [8] Object Cohorts                               0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): a concurrent hash map that uses hazard pointers is more generally usable if it allows arbitrary key and value types rather than only types without dependence on resources with independent lifetimes.
candidate 2 (found by 1 of 36 passes): The main drawback of the global cleanup approach is its high overhead that makes it impractical to use.

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
