Verdict: Strong (8/14)

The paper offers meaningful support for the relevance and real-world use of the async model it discusses, but it does not make the case that standardization of the proposed facility is necessary or that existing standard mechanisms are insufficient. The strongest material concerns ecosystem adoption and production experience, while the argument thins out almost entirely when it comes to why the standard should act, how the proposal would coordinate with related facilities, and why a library solution cannot suffice.

- The paper clearly establishes that the facility has substantial implementation experience, including production use at Citadel Securities and a long-lived reference implementation.
- It also establishes who is affected and why the problem matters, pointing to broad expected use of coroutine-based async code and concrete ecosystem adoption.
- The paper does not establish why standardization is needed, leaving the central justification for a standards-track proposal essentially unaddressed.
- It likewise offers no established case for coordination with existing standards or for why a library implementation would not be adequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 23. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.00   accumulate 8.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 99 of 105 section-criterion pairs unanimous (94%)
single-sample totals would have been: 8.00 / 7.50 / 8.00   (all 3 samples: 7.67)
headings: h2 14
on threshold: audience
splits: motivation[7] 1/2/1  motivation[13] 0/1/1  audience[6] 2/1/1  audience[7] 0/0/2
        prior_art[3] 0/1/1  prior_art[12] 2/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 15 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 1/1/1  -> 1.00
  [7] 3. What std::execution Does Well             1/2/1  -> 1.33
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        2/2/2  -> 2.00
  [10] 6. Structural Observations                   2/2/2  -> 2.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        2/2/2  -> 2.00
  [13] 9. Open Question                             0/1/1  -> 0.67
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The question is whether the C++26 model subsumes the C++20 model, or whether they serve different domains.
candidate 2 (found by 3 of 45 passes): Both are standard facilities. Both are async models. The question is the relationship between them.
candidate 3 (found by 3 of 45 passes): "Having iterative code that is actually recursive is a potential security vulnerability."
candidate 4 (found by 3 of 45 passes): The reference implementation has 1,300 stars. The I/O ecosystem built on it has 21.

## audience - grade 1.67 (fired in 3 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                0/0/0  -> 0.00
  [6] 2. Two Standard Async Models                 2/1/1  -> 1.33
  [7] 3. What std::execution Does Well             0/0/2  -> 0.67
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   0/0/0  -> 0.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        2/2/2  -> 2.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The reference implementation has 1,300 stars. The I/O ecosystem built on it has 21.
candidate 2 (found by 1 of 45 passes): "I think that 90% of all async code in the future should be coroutines simply for maintainability."
candidate 3 (found by 1 of 45 passes): Eric Niebler wrote in ["Structured Concurrency"](https://ericniebler.com/2020/11/08/structured-concurrency/) [45] (2020): *"I think that 90% of all async code in the future should be coroutines simply for maintainability."*
candidate 4 (found by 1 of 45 passes): *"I think that 90% of all async code in the future should be coroutines simply for maintainability."*

## prior_art - grade 2.00 (fired in 6 of 15 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/1/1  -> 0.67
  [4] Revision History                             0/0/0  -> 0.00
  [5] 1. Disclosure                                1/1/1  -> 1.00
  [6] 2. Two Standard Async Models                 2/2/2  -> 2.00
  [7] 3. What std::execution Does Well             1/1/1  -> 1.00
  [8] 4. The Post-Adoption Record                  0/0/0  -> 0.00
  [9] 5. Published Findings                        0/0/0  -> 0.00
  [10] 6. Structural Observations                   2/2/2  -> 2.00
  [11] 7. Established Practice                      0/0/0  -> 0.00
  [12] 8. Ecosystem Adoption                        2/0/1  -> 1.00
  [13] 9. Open Question                             0/0/0  -> 0.00
  [14] Acknowledgments                              0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The framework's architect placed 90% of async code in the coroutine column.
candidate 2 (found by 3 of 45 passes): [stdexec](https://github.com/NVIDIA/stdexec) [48] - the reference implementation - was built at NVIDIA.
candidate 3 (found by 3 of 45 passes): Both [P2300R10](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2300r10.html) [7] bridges - `sender-awaitable` and `connect-awaitable` - use `void await_suspend`.
candidate 4 (found by 2 of 45 passes): C++20 standardized coroutines. C++26 adds `std::execution`. Both are asynchronous models.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 15 sections, strong in 2)
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
candidate 1 (found by 3 of 45 passes): Herb Sutter [reported](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work) [47] that Citadel Securities uses `std::execution` in production: *"We already use C++26's* `std::execution` *in* *production for an entire asset class, and as the foundation of our new messaging infrastructure."*
candidate 2 (found by 3 of 45 passes): [stdexec](https://github.com/NVIDIA/stdexec) [48] has existed as a reference implementation throughout.

-->
