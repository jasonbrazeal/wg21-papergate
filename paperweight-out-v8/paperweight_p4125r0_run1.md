Verdict: Adequate (5/14)

The paper offers some useful early evidence that coroutine-native I/O can work in a demanding production setting and that existing callback-based patterns do not map cleanly onto coroutines, but it leaves the core standardization rationale largely unaddressed. The thinnest areas are the absence of any argument for why this belongs in the standard rather than in a library, and the lack of detail about who would be affected or how the proposed facility would coordinate with existing I/O models.

- The strongest support is the concrete report of a derivatives exchange porting from Asio callbacks to a coroutine-native library, with engineers finding the coroutine structure simpler and more readable.
- The paper also establishes that recursive callback patterns such as retry loops and reconnection handlers do not translate directly to coroutines, and that the exception-vs-error-code boundary is a recurring design question.
- The implementation experience is only claimed, resting on a small number of interviews and two to three weeks of partial integration, which is too limited to establish broad practical viability.
- The most glaring omission is the complete lack of a case for why a library will not do, leaving the need for standardization itself unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.00   accumulate 5.83   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.83  insufficiency 0.00  implementation 1.00
sample agreement: 81 of 84 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 5.00 / 5.50   (all 3 samples: 5.33)
headings: h2 11
on threshold: prior_art
splits: coordination[5] 1/0/1  implementation[4] 0/1/1  implementation[5] 1/0/1
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
candidate 1 (found by 3 of 36 passes): The central research question is whether a coroutine-native I/O library can match or exceed Asio's performance in a mission-critical production system.
candidate 2 (found by 3 of 36 passes): Recursive callback patterns (retry loops, reconnection handlers) converted naturally to structured coroutine loops, which the engineers described as simpler and more readable than the callback originals.
candidate 3 (found by 3 of 36 passes): The exception-vs-error-code boundary is a recurring design question in C++ I/O libraries. This question is directly relevant to financial markets infrastructure, where exception-free code paths are a standard requirement.
candidate 4 (found by 2 of 36 passes): A derivatives exchange is porting from Asio callbacks to coroutine-native I/O. Early results: it works.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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

## prior_art - grade 1.50 (fired in 3 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                1/1/1  -> 1.00
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           2/2/2  -> 2.00
  [8] 5. Error Handling                            1/1/1  -> 1.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The Asio pattern uses recursive callbacks - a timer fires, executes a handler, and re-arms itself within the same handler. This pattern does not translate directly to coroutines.
candidate 2 (found by 2 of 36 passes): Capy is a C++ library providing async/coroutine building blocks and executor models. Corosio is a networking library built on Capy, providing async socket operations.
candidate 3 (found by 2 of 36 passes): The exception-vs-error-code boundary is a recurring design question in C++ I/O libraries.
candidate 4 (found by 1 of 36 passes): The integration involves a commercial derivatives exchange operator porting from Boost.Asio to a coroutine-native library developed by the C++ Alliance.

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

## coordination - grade 0.83 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                1/0/1  -> 0.67
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           0/0/0  -> 0.00
  [8] 5. Error Handling                            1/1/1  -> 1.00
  [9] 6. Early Assessment                          0/0/0  -> 0.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The exception-vs-error-code boundary is a recurring design question in C++ I/O libraries.
candidate 2 (found by 2 of 36 passes): The integration involves a commercial derivatives exchange operator porting from Boost.Asio to a coroutine-native library developed by the C++ Alliance.

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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

## implementation - grade 1.00  [binary: max] (fired in 5 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/1  -> 0.67
  [5] 2. Background                                1/0/1  -> 0.67
  [6] 3. Methodology                               0/0/0  -> 0.00
  [7] 4. Callback-to-Coroutine Migration           1/1/1  -> 1.00
  [8] 5. Error Handling                            0/0/0  -> 0.00
  [9] 6. Early Assessment                          1/1/1  -> 1.00
  [10] 7. Limitations of This Study                 0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The paper reports qualitative findings from three structured interviews with the engineering team.
candidate 2 (found by 3 of 36 passes): These assessments are based on two to three weeks of integration work covering a subset of the platform.
candidate 3 (found by 2 of 36 passes): Falco developed and maintains [Capy](https://github.com/cppalliance/capy)[1] and [Corosio](https://github.com/cppalliance/corosio)[2] and believes coroutine-native I/O is a practical foundation for networking in C++.
candidate 4 (found by 2 of 36 passes): The integration involves a commercial derivatives exchange operator porting from Boost.Asio to a coroutine-native library developed by the C++ Alliance.

-->
