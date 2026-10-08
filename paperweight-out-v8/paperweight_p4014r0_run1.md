Verdict: Strong (8/14)

The paper offers solid grounding in real-world use, prior art, and implementation experience, but it leaves the standardization-specific case largely unargued. The thinnest parts are exactly where a proposal must connect an existing practice to the need for a standard: coordination, interoperability, and why a library cannot suffice.

- The strongest support is the demonstrated implementation experience, with maintained reference code and domain-specific deployments that show the model works in practice.
- The paper also establishes who is affected and why the problem matters, pointing to real users and performance-sensitive domains that have already opted in.
- The most glaring omission is the absence of any established case for coordination and interoperability with the existing standard or other components.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 5 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.00   accumulate 8.33   max 9.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 114 of 126 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 8.50 / 8.00   (all 3 samples: 8.17)
headings: h2 17
on threshold: audience
splits: motivation[6] 0/0/1  motivation[7] 1/2/1  motivation[11] 1/0/0  audience[7] 2/1/2
        audience[9] 1/2/1  audience[10] 1/0/0  prior_art[7] 0/0/2  prior_art[8] 1/2/1
        vehicle[9] 1/2/1  implementation[5] 0/0/2  implementation[10] 2/2/0
        implementation[14] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 18 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. The Equivalents                           2/2/2  -> 2.00
  [6] 3. Why It Looks Like This                    0/0/1  -> 0.33
  [7] 4. How the Emphasis Changed                  1/2/1  -> 1.33
  [8] 5. The Sub-Language in Practice              1/1/1  -> 1.00
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Polls                     1/0/0  -> 0.33
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

## audience - grade 1.50 (fired in 3 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/0  -> 0.00
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  2/1/2  -> 1.67
  [8] 5. The Sub-Language in Practice              0/0/0  -> 0.00
  [9] 6. What Complexity Buys                      1/2/1  -> 1.33
  [10] 7. Conclusion                                1/0/0  -> 0.33
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): Eric Niebler’s 2020 assessment, “90% of all async code in the future should be coroutines simply for maintainability,” captures the coroutine model’s strengths for I/O and general-purpose async programming.
candidate 2 (found by 2 of 54 passes): For GPU dispatch, high-frequency trading, embedded systems, and scientific computing, every party involved has opted in.
candidate 3 (found by 1 of 54 passes): [HPC Wire](https://www.hpcwire.com/2022/12/05/new-c-sender-library-enables-portable-asynchrony/) reports performance “on par with the CUDA implementation”
candidate 4 (found by 1 of 54 passes): Real users depend on it.

## prior_art - grade 2.00 (fired in 9 of 18 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. The Equivalents                           2/2/2  -> 2.00
  [6] 3. Why It Looks Like This                    2/2/2  -> 2.00
  [7] 4. How the Emphasis Changed                  0/0/2  -> 0.67
  [8] 5. The Sub-Language in Practice              1/2/1  -> 1.33
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                1/1/1  -> 1.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       1/1/1  -> 1.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): C++26 introduces a rich sub-language for asynchronous programming through `std::execution` ([P2300R10](https://wg21.link/p2300r10))[1].
candidate 2 (found by 3 of 54 passes): [P4007R0](https://wg21.link/p4007r0)[9] (“Senders and C++”) examines the coroutine integration; this paper focuses on what the Sub-Language is, where it came from, and what it looks like in practice.
candidate 3 (found by 3 of 54 passes): The P2300 authors built a framework grounded in four decades of programming language research.
candidate 4 (found by 3 of 54 passes): The `repeat_effect_until` algorithm is provided by the [stdexec](https://github.com/NVIDIA/stdexec)[23] reference implementation; it is not yet part of the C++26 working paper.

## vehicle - grade 0.67 (fired in 1 of 18 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/0  -> 0.00
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  0/0/0  -> 0.00
  [8] 5. The Sub-Language in Practice              0/0/0  -> 0.00
  [9] 6. What Complexity Buys                      1/2/1  -> 1.33
  [10] 7. Conclusion                                0/0/0  -> 0.00
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       0/0/0  -> 0.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 2 of 54 passes): The committee accommodated a domain that needed its own model.
candidate 2 (found by 1 of 54 passes): The committee accommodated a domain that needed its own model. GPU compute got a complete, domain-specific implementation of `std::execution` with non-standard extensions, a specialized compiler, and reimplementations of every standard algorithm.

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

## implementation - grade 2.00  [binary: max] (fired in 7 of 18 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. The Equivalents                           0/0/2  -> 0.67
  [6] 3. Why It Looks Like This                    0/0/0  -> 0.00
  [7] 4. How the Emphasis Changed                  2/2/2  -> 2.00
  [8] 5. The Sub-Language in Practice              2/2/2  -> 2.00
  [9] 6. What Complexity Buys                      2/2/2  -> 2.00
  [10] 7. Conclusion                                2/2/0  -> 1.33
  [11] 8. Suggested Straw Polls                     0/0/0  -> 0.00
  [12] Further Reading                              0/0/0  -> 0.00
  [13] Acknowledgements                             0/0/0  -> 0.00
  [14] References                                   2/0/2  -> 1.33
  [15] examples                                     0/0/0  -> 0.00
  [16] Background                                   0/0/0  -> 0.00
  [17] NVIDIA CUDA and nvexec                       2/2/2  -> 2.00
  [18] Concurrent Selection Gap                     0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The reference implementation, [stdexec](https://github.com/NVIDIA/stdexec)[23], is maintained under NVIDIA’s GitHub organization.
candidate 2 (found by 3 of 54 passes): The following examples are drawn from the official [stdexec](https://github.com/NVIDIA/stdexec)[23] repository and the [sender-examples](https://github.com/steve-downey/sender-examples)[28] collection.
candidate 3 (found by 3 of 54 passes): NVIDIA’s [nvexec](https://github.com/NVIDIA/stdexec/tree/main/include/nvexec)[41] demonstrates this accommodation in practice: a GPU-specific sender implementation that lives alongside [stdexec](https://github.com/NVIDIA/stdexec)[23] in the same repository but in a separate namespace.
candidate 4 (found by 3 of 54 passes): [nvexec](https://github.com/NVIDIA/stdexec/tree/main/include/nvexec). GPU-specific sender implementation in the stdexec repository.

-->
