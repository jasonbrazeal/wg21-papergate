Verdict: Strong (8/14)

The paper offers solid grounding for the value of object cohorts in production and for the inadequacy of global cleanup as a general-purpose alternative, but its case for standardization rests largely on assertion rather than demonstrated need. The thinnest support appears where the paper must connect that production experience to a problem only the standard can solve, and where it must show how the proposed facility would fit with existing or expected practice.

- The strongest support is the established implementation experience, with object cohorts in heavy production use in Folly since 2018.
- The paper also establishes why the feature matters by showing that synchronous reclamation is important for general-purpose usability and that global cleanup is often impractical.
- The paper establishes prior art and alternatives by contrasting object cohorts with the P2530R3 interface and explaining the convention around non-cohort retirement.
- The most glaring omission is the absence of an established argument for why a library cannot provide this capability, since the paper leans on an existing library implementation without showing what standardization would add.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 7 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 9.33   accumulate 8.17   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 0.17  insufficiency 0.50  implementation 2.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 8.00 / 8.50 / 8.00   (all 3 samples: 8.17)
headings: h2 11
on threshold: implementation
splits: prior_art[4] 1/0/0  coordination[8] 0/1/0
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
candidate 3 (found by 3 of 36 passes): As a result, hazard pointer users must guarantee separately that the deleters of such objects do not depends on resources that may become subsequently unavailable.
candidate 4 (found by 2 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

## audience - grade 1.00 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): For example, a concurrent hash map that uses hazard pointers is more generally usable if it allows arbitrary key and value types rather than only types without dependence on resources with independent lifetimes.
candidate 2 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Object Cohorts                               1/1/1  -> 1.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                2/2/2  -> 2.00
  [11] Separating Cohort Object Retirement from ... 1/1/1  -> 1.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 3 of 36 passes): The main drawback of the global cleanup approach is its high overhead that makes it impractical to use.
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

## coordination - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Object Cohorts                               0/1/0  -> 0.33
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Usage Example                                0/0/0  -> 0.00
  [11] Separating Cohort Object Retirement from ... 0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): Object cohorts support synchronous reclamation by guaranteeing that all the deleters of the object cohort members are completed before the completion of the cohorts destructor.

## insufficiency - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 36 passes): While its guarantees are weaker and less flexible than global cleanup, its efficiency enables users to use it in performance sensitive cases where the cost of global cleanup may be impractical.

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
