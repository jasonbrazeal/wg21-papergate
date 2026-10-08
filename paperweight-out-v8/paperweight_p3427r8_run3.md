Verdict: Strong (8/14)

The paper offers meaningful support in a few areas, particularly through its production use in Folly and its contrast with the asynchronous C++26 hazard pointer interface, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns coordination and interoperability, where the paper provides no evidence at all, and the arguments for why the standard—rather than a library—should contain this facility remain more asserted than shown.

- The strongest support comes from implementation experience, with object cohorts in heavy production use in Folly since 2018.
- The paper also establishes why the problem matters by showing that the C++26 hazard pointer interface supports only asynchronous reclamation and does not guarantee reclamation timing.
- Prior art and alternatives are established through the Folly reference and the comparison with the impractical global cleanup approach.
- The most glaring omission is coordination and interoperability, where the paper offers no evidence about how the proposed facility would interact with existing or future standard library components.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.67   accumulate 8.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.50  vehicle 1.00  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.00 / 7.50 / 7.50   (all 3 samples: 7.67)
headings: h2 10
on threshold: prior_art, implementation
splits: motivation[6] 2/1/1  audience[5] 1/0/0  insufficiency[7] 1/1/0  insufficiency[9] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            2/1/1  -> 1.33
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                2/2/2  -> 2.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 33 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 3 (found by 2 of 33 passes): The P2530R3 C++26 hazard pointer interface supports only asynchronous reclamation which does not guarantee the timing of the reclamation of protectable objects that are no longer protected.
candidate 4 (found by 2 of 33 passes): In the code snippet on the left side, the removed object is retired by submitting the retirement code to a dedicated thread pool (details not shown) to be executed asynchronously.

## audience - grade 0.67 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/0/0  -> 0.33
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 1 of 33 passes): For example, a concurrent hash map that uses hazard pointers is more generally usable if it allows arbitrary key and value types rather than only types without dependence on resources with independent lifetimes.

## prior_art - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            1/1/1  -> 1.00
  [7] Synchronous Reclamation                      2/2/2  -> 2.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                1/1/1  -> 1.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.
candidate 2 (found by 3 of 33 passes): The main drawback of the global cleanup approach is its high overhead that makes it impractical to use.
candidate 3 (found by 3 of 33 passes): The following table shows two code snippets one using the C++26 hazard pointer interface and one using object cohorts, respectively.

## vehicle - grade 1.00 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      1/1/1  -> 1.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes supporting object cohorts due to the importance of synchronous reclamation for general purpose usability.
candidate 2 (found by 3 of 33 passes): Therefore, we recommend object cohorts for standardization.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            0/0/0  -> 0.00
  [7] Synchronous Reclamation                      1/1/0  -> 0.67
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/1  -> 0.33
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The main drawback of the global cleanup approach is its high overhead that makes it impractical to use.
candidate 2 (found by 1 of 33 passes): In order for an object to be included in synchronous reclamation in association with a cohort, the object must be retired to the cohort.

## implementation - grade 2.00  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History 2                                    0/0/0  -> 0.00
  [3] History                                      0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Implementation and Use Experience            2/2/2  -> 2.00
  [7] Synchronous Reclamation                      0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
  [9] Usage Example                                0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Object cohorts have been part of the Folly open-source library (under the name `hazptr_obj_cohort`) and in heavy use in production since 2018.

-->
