Verdict: Adequate to Strong (7/14)

The paper offers solid evidence that its topic sits at a real and current intersection of C++ async models, with credible implementation and production use behind the underlying machinery. The support is thinnest, however, on the questions that matter most for a standardization proposal: why this belongs in the standard, how it would coordinate with existing facilities, and why a library cannot suffice.

- The strongest support is the implementation experience, anchored by stdexec’s longevity and reported production use at Citadel Securities.
- The paper also establishes why the problem matters by showing a genuine tension between C++20 coroutines and C++26 senders, including allocator and security concerns.
- The most glaring omission is the absence of any established case for why the standard is the right venue rather than a library solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 24. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 6.00   accumulate 7.50   max 8.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.50 / 7.50 / 7.50   (all 3 samples: 7.17)
headings: h2 14
on threshold: audience, prior_art
splits: motivation[6] 1/1/0  motivation[7] 0/1/1  motivation[11] 0/0/2  motivation[12] 2/1/2
        motivation[13] 0/1/0  prior_art[5] 1/0/1  prior_art[10] 0/0/2  prior_art[12] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 15 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 1/1/0  -> 0.67
  [7] 3. What std::execution Does Well             0/1/1  -> 0.67
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        2/2/2  -> 2.00
  [10] 6. Structural Observations                   2/2/2  -> 2.00
  [11] 7. Established Practice                      0/0/2  -> 0.67
  [12] 8. Ecosystem Adoption                        2/1/2  -> 1.67
  [13] 9. Open Question                             0/1/0  -> 0.33
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The question is whether the C++26 model subsumes the C++20 model, or whether they serve different domains.
candidate 2 (found by 3 of 45 passes): The reference implementation has 1,300 stars. The I/O ecosystem built on it has 21.
candidate 3 (found by 2 of 45 passes): Having iterative code that is actually recursive is a potential security vulnerability.
candidate 4 (found by 2 of 45 passes): Senders get the allocator they do not need. Coroutines need the frame allocator they do not get.

## audience - grade 1.50 (fired in 2 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 1/1/1  -> 1.00
  [7] 3. What std::execution Does Well             0/0/0  -> 0.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/0  -> 0.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        2/2/2  -> 2.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): "I think that 90% of all async code in the future should be coroutines simply for maintainability."
candidate 2 (found by 3 of 45 passes): The reference implementation has 1,300 stars. The I/O ecosystem built on it has 21.

## prior_art - grade 1.67 (fired in 6 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                1/0/1  -> 0.67
  [6] 2. Two Standard Async Models                 2/2/2  -> 2.00
  [7] 3. What std::execution Does Well             1/1/1  -> 1.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/2  -> 0.67
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        2/2/0  -> 1.33
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): C++20 standardized coroutines. C++26 adds `std::execution`. Both are asynchronous models.
candidate 2 (found by 3 of 45 passes): [stdexec](https://github.com/NVIDIA/stdexec) [48] - the reference implementation - was built at NVIDIA.
candidate 3 (found by 2 of 45 passes): Coroutine-native I/O and `std::execution` are complementary.
candidate 4 (found by 2 of 45 passes): The framework's architect placed 90% of async code in the coroutine column.

## vehicle - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 0/0/0  -> 0.00
  [7] 3. What std::execution Does Well             0/0/0  -> 0.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/0  -> 0.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        0/0/0  -> 0.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 0/0/0  -> 0.00
  [7] 3. What std::execution Does Well             0/0/0  -> 0.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/0  -> 0.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        0/0/0  -> 0.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 0/0/0  -> 0.00
  [7] 3. What std::execution Does Well             0/0/0  -> 0.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/0  -> 0.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        0/0/0  -> 0.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 15 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 0/0/0  -> 0.00
  [7] 3. What std::execution Does Well             2/2/2  -> 2.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/0  -> 0.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        2/2/2  -> 2.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): [stdexec](https://github.com/NVIDIA/stdexec) [48] has existed as a reference implementation throughout.
candidate 2 (found by 1 of 45 passes): Herb Sutter [reported](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [47] that Citadel Securities uses `std::execution` in production
candidate 3 (found by 1 of 45 passes): Herb Sutter [reported](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [47] that Citadel Securities uses `std::execution` in production: *"We already use C++26's* `std::execution` *in* *production for an entire asset class, and as the foundation of our new messaging infrastructure."*
candidate 4 (found by 1 of 45 passes): [stdexec](https://github.com/NVIDIA/stdexec) [48] - the reference implementation - was built at NVIDIA.

-->
