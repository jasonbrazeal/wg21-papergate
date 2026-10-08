Verdict: Strong (9/14)

The paper offers meaningful support for its standardization case in the areas of motivation, affected users, prior art, and implementation experience, but it leaves the core institutional questions essentially unaddressed. The thinnest parts are the arguments that this belongs in the standard rather than in a library, and that it can coordinate or interoperate with existing or future standardization work.

- The strongest support is the demonstrated real-world use and production shipping of the reference implementation and its GPU-specific variant.
- The paper also establishes clearly why the problem matters and who is affected, including performance evidence and expert assessment of coroutine-based async code.
- The case weakens considerably where it asserts, but does not establish, that the committee’s prior accommodation of GPU compute justifies standardizing this work.
- The most glaring omission is the absence of any established argument for why a library cannot suffice or how the proposal would coordinate with existing standards.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 5 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 8.50   max 9.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 119 of 126 section-criterion pairs unanimous (94%)
single-sample totals would have been: 9.00 / 8.50 / 8.00   (all 3 samples: 8.50)
headings: h2 17
on threshold: none
splits: motivation[6] 1/0/1  motivation[7] 2/1/2  motivation[10] 1/1/2  motivation[11] 1/0/1
        prior_art[17] 1/0/0  vehicle[9] 2/1/0  implementation[5] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 18 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. The Equivalents                           2/2/2  -> 2.00
  [6] 3. Why It Looks Like This                    1/0/1  -> 0.67
  [7] 4. How the Emphasis Changed                  2/1/2  -> 1.67
  [8] 5. The Sub-Language in Practice              1/1/1  -> 1.00
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                1/1/2  -> 1.33
  [11] 8. Suggested Straw Polls                     1/0/1  -> 0.67
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The trade-offs serve specific domains well. The question is whether other domains deserve the same freedom to choose the model that serves them.
candidate 2 (found by 3 of 54 passes): C++ developers who write asynchronous code will likely encounter it.
candidate 3 (found by 3 of 54 passes): Three of the four algorithms in the motivating example for `std::execution` are not part of C++26.
candidate 4 (found by 3 of 54 passes): The question is whether the committee should give asynchronous I/O the same domain-specific accommodation it gave heterogeneous compute.

## audience - grade 2.00 (fired in 2 of 18 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/0  -> 0.00
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  2/2/2  -> 2.00
  [8] 5. The Sub-Language in Practice              0/0/0  -> 0.00
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): Eric Niebler’s 2020 assessment, “90% of all async code in the future should be coroutines simply for maintainability,” captures the coroutine model’s strengths for I/O and general-purpose async programming.
candidate 2 (found by 3 of 54 passes): [HPC Wire](https://www.hpcwire.com/2022/12/05/new-c-sender-library-enables-portable-asynchrony/) reports performance “on par with the CUDA implementation”

## prior_art - grade 2.00 (fired in 9 of 18 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. The Equivalents                           2/2/2  -> 2.00
  [6] 3. Why It Looks Like This                    2/2/2  -> 2.00
  [7] 4. How the Emphasis Changed                  2/2/2  -> 2.00
  [8] 5. The Sub-Language in Practice              2/2/2  -> 2.00
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       1/0/0  -> 0.33
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): C++26 introduces a rich sub-language for asynchronous programming through `std::execution` ([P2300R10](https://wg21.link/p2300r10))[1].
candidate 2 (found by 3 of 54 passes): [P4007R0](https://wg21.link/p4007r0)[9] (“Senders and C++”) examines the coroutine integration; this paper focuses on what the Sub-Language is, where it came from, and what it looks like in practice.
candidate 3 (found by 3 of 54 passes): The P2300 authors built a framework grounded in four decades of programming language research.
candidate 4 (found by 3 of 54 passes): The `repeat_effect_until` algorithm is provided by the [stdexec](https://github.com/NVIDIA/stdexec)[23] reference implementation; it is not yet part of the C++26 working paper.

## vehicle - grade 0.50 (fired in 1 of 18 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/0  -> 0.00
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  0/0/0  -> 0.00
  [8] 5. The Sub-Language in Practice              0/0/0  -> 0.00
  [9] 6. What Complexity Buys                      2/1/0  -> 1.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 1 of 54 passes): The committee accommodated a domain that needed its own model. GPU compute got a complete, domain-specific implementation of `std::execution` with non-standard extensions, a specialized compiler, and reimplementations of every standard algorithm.
candidate 2 (found by 1 of 54 passes): The committee designed `std::execution` to accommodate domain-specific needs.

## coordination - grade 0.00 (fired in 0 of 18 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/0  -> 0.00
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  0/0/0  -> 0.00
  [8] 5. The Sub-Language in Practice              0/0/0  -> 0.00
  [9] 6. What Complexity Buys                      0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 18 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/0  -> 0.00
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  0/0/0  -> 0.00
  [8] 5. The Sub-Language in Practice              0/0/0  -> 0.00
  [9] 6. What Complexity Buys                      0/0/0  -> 0.00
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 6 of 18 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           2/1/2  -> 1.67
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  2/2/2  -> 2.00
  [8] 5. The Sub-Language in Practice              2/2/2  -> 2.00
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                2/2/2  -> 2.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       2/2/2  -> 2.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The reference implementation, [stdexec](https://github.com/NVIDIA/stdexec)[23], is maintained under NVIDIA’s GitHub organization.
candidate 2 (found by 3 of 54 passes): NVIDIA’s [nvexec](https://github.com/NVIDIA/stdexec/tree/main/include/nvexec)[41] demonstrates this accommodation in practice: a GPU-specific sender implementation that lives alongside [stdexec](https://github.com/NVIDIA/stdexec)[23] in the same repository but in a separate namespace.
candidate 3 (found by 3 of 54 passes): it is already [shipping in](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work/) [production](https://herbsutter.com/2025/04/23/living-in-the-future-using-c26-at-work/)[14] at NVIDIA and Citadel Securities.
candidate 4 (found by 3 of 54 passes): [nvexec](https://github.com/NVIDIA/stdexec/tree/main/include/nvexec). GPU-specific sender implementation in the stdexec repository.

-->
