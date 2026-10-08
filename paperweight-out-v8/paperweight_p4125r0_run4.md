Verdict: Adequate (5/14)

The paper offers some grounding for why coroutine-native I/O deserves attention, but it falls well short of showing that this particular work belongs in the C++ standard. The strongest material concerns motivation and the contrast with existing Asio-style patterns, while the case for standardization itself, coordination with the ecosystem, and the limits of a library solution are essentially asserted rather than argued.

- The paper establishes that the exception-versus-error-code boundary and the translation of recursive callback patterns into coroutine loops are real, recurring concerns in production I/O design.
- The prior-art discussion credibly positions Corosio and Capy against Asio and explains why the callback pattern does not map directly onto coroutines.
- The claims about who is affected and about implementation experience rest on a short, partial integration and a small number of interviews, so the breadth of the problem is not yet demonstrated.
- The paper does not establish why this needs standardization rather than remaining a library, nor how it would coordinate with existing networking and execution proposals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 6 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 5.83   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.50  insufficiency 0.17  implementation 1.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.00 / 6.00 / 5.00   (all 3 samples: 5.33)
headings: h2 11
on threshold: prior_art
splits: audience[5] 0/1/0  prior_art[4] 1/0/0  insufficiency[8] 0/1/0  implementation[2] 0/1/1
        implementation[4] 0/1/1  implementation[5] 0/0/1  implementation[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                1/1/1  -> 1.00
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           2/2/2  -> 2.00
  [8] 5. Error Handling                            2/2/2  -> 2.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): A derivatives exchange is porting from Asio callbacks to coroutine-native I/O.
candidate 2 (found by 3 of 36 passes): The central research question is whether a coroutine-native I/O library can match or exceed Asio's performance in a mission-critical production system.
candidate 3 (found by 3 of 36 passes): Recursive callback patterns (retry loops, reconnection handlers) converted naturally to structured coroutine loops, which the engineers described as simpler and more readable than the callback originals.
candidate 4 (found by 3 of 36 passes): The exception-vs-error-code boundary is a recurring design question in C++ I/O libraries. This question is directly relevant to financial markets infrastructure, where exception-free code paths are a standard requirement.

## audience - grade 0.17 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/1/0  -> 0.33
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           0/0/0  -> 0.00
  [8] 5. Error Handling                            0/0/0  -> 0.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The integration partner has developed one of the world's highest performance derivatives exchange platforms.

## prior_art - grade 1.50 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/0  -> 0.33
  [5] 2. Background                                1/1/1  -> 1.00
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           2/2/2  -> 2.00
  [8] 5. Error Handling                            1/1/1  -> 1.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Corosio throws exceptions where Asio provides `error_code` overloads.
candidate 2 (found by 2 of 36 passes): Capy is a C++ library providing async/coroutine building blocks and executor models. Corosio is a networking library built on Capy, providing async socket operations.
candidate 3 (found by 2 of 36 passes): The Asio pattern uses recursive callbacks - a timer fires, executes a handler, and re-arms itself within the same handler. This pattern does not translate directly to coroutines.
candidate 4 (found by 1 of 36 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy)[1] and [Corosio](https://github.com/cppalliance/corosio)[2] and believes coroutine-native I/O is a practical foundation for networking in C++.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/0/0  -> 0.00
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           0/0/0  -> 0.00
  [8] 5. Error Handling                            0/0/0  -> 0.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/0/0  -> 0.00
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           0/0/0  -> 0.00
  [8] 5. Error Handling                            1/1/1  -> 1.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The exception-vs-error-code boundary is a recurring design question in C++ I/O libraries.

## insufficiency - grade 0.17 (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/0/0  -> 0.00
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           0/0/0  -> 0.00
  [8] 5. Error Handling                            0/1/0  -> 0.33
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 36 passes): The exception-vs-error-code boundary is a recurring design question in C++ I/O libraries.

## implementation - grade 1.00  [binary: max] (fired in 6 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/1  -> 0.67
  [5] 2. Background                                0/0/1  -> 0.33
  [6] 3. Methodology                               0/1/0  -> 0.33
  [7] 4. Callback-to-Coroutine Migration           1/1/1  -> 1.00
  [8] 5. Error Handling                            0/0/0  -> 0.00
  [9] 6. Early Assessment                          1/1/1  -> 1.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): These assessments are based on two to three weeks of integration work covering a subset of the platform.
candidate 2 (found by 2 of 36 passes): The paper reports qualitative findings from three structured interviews with the engineering team.
candidate 3 (found by 2 of 36 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy)[1] and [Corosio](https://github.com/cppalliance/corosio)[2] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 4 (found by 2 of 36 passes): The CMake snippet in the repository README compiled cleanly on the first attempt, and the dependency relationship between Capy and Corosio was handled automatically.

-->
