Verdict: Strong to Excellent (12/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates real implementation experience, identifies affected users, and shows credible prior art and alternatives. The support is thinnest where the paper needs to explain why this belongs in the standard rather than in a library, and why the standard itself—rather than one async path among several—must adopt this approach.

- The strongest support comes from concrete implementation experience, with two libraries delivering the proposed abstractions on C++20 today and multiple Boost projects already building on them.
- The paper also clearly establishes who is affected, citing production use of Asio, institutional evaluation in trading infrastructure, and active adoption by Boost.HTTP, Boost.MySQL, and Boost.Redis.
- The most glaring omission is the failure to establish why a library will not do, since the paper asserts that external libraries can implement portable I/O in terms of these abstractions but does not show why standardization is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.67/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.67 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.67   corroborated 11.00   accumulate 12.83   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 1.17  coordination 2.00  insufficiency 0.83  implementation 2.00
sample agreement: 116 of 133 section-criterion pairs unanimous (87%)
single-sample totals would have been: 11.00 / 11.50 / 12.50   (all 3 samples: 11.67)
headings: h2 17 + bold numbered 1
on threshold: audience, implementation
splits: motivation[5] 1/2/1  motivation[6] 2/1/1  motivation[13] 2/2/0  motivation[16] 0/1/1
        audience[7] 1/1/2  prior_art[8] 2/1/2  prior_art[9] 0/1/0  prior_art[14] 2/2/1
        prior_art[17] 0/0/1  vehicle[6] 1/1/2  vehicle[8] 1/1/0  vehicle[12] 1/0/0
        coordination[8] 1/0/1  insufficiency[11] 0/1/1  implementation[4] 0/1/1
        implementation[6] 0/1/0  implementation[7] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              1/2/1  -> 1.33
  [6] 3. What We Found                             2/1/1  -> 1.33
  [7] 4. Design Criteria                           1/1/1  -> 1.00
  [8] 5. Asio Continuity                           2/2/2  -> 2.00
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          2/2/2  -> 2.00
  [13] 9. std::execution                            2/2/0  -> 1.33
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/1/1  -> 0.67
  [17] 13. std::io                                  1/1/1  -> 1.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The five properties converge on problems that are specific to C++:
candidate 2 (found by 3 of 57 passes): Today, every C++ project that does I/O invents its own buffer types.
candidate 3 (found by 3 of 57 passes): We built this. It works. We are reporting what we found.
candidate 4 (found by 2 of 57 passes): C++ coroutines have five language mechanisms that combine into the ideal substrate for coroutine-native I/O.

## audience - grade 1.67 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              2/2/2  -> 2.00
  [6] 3. What We Found                             0/0/0  -> 0.00
  [7] 4. Design Criteria                           1/1/2  -> 1.33
  [8] 5. Asio Continuity                           1/1/1  -> 1.00
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                0/0/0  -> 0.00
  [12] 8. The Paper Series                          0/0/0  -> 0.00
  [13] 9. std::execution                            0/0/0  -> 0.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two libraries - Capy and Corosio - use those mechanisms directly to deliver type-erased streams, separate compilation, and ABI stability on C++20 today.
candidate 2 (found by 3 of 57 passes): Asio has been used in production worldwide for over twenty years.
candidate 3 (found by 2 of 57 passes): A production trading infrastructure company is evaluating Corosio for high-performance networking.
candidate 4 (found by 2 of 57 passes): Boost.Http, Boost.MySQL, and Boost.Redis are building on these abstractions today.

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. The Evidence                              1/1/1  -> 1.00
  [6] 3. What We Found                             2/2/2  -> 2.00
  [7] 4. Design Criteria                           2/2/2  -> 2.00
  [8] 5. Asio Continuity                           2/1/2  -> 1.67
  [9] 6. The Three-Layer Architecture              0/1/0  -> 0.33
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          0/0/0  -> 0.00
  [13] 9. std::execution                            0/0/0  -> 0.00
  [14] 10. Limitations                              2/2/1  -> 1.67
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             1/1/1  -> 1.00
  [17] 13. std::io                                  0/0/1  -> 0.33
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two libraries - Capy and Corosio - use those mechanisms directly to deliver type-erased streams, separate compilation, and ABI stability on C++20 today.
candidate 2 (found by 3 of 57 passes): Coroutine-native I/O and `std::execution` are complementary. Each serves the domain where its design choices pay off.
candidate 3 (found by 3 of 57 passes): [P4125R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4125r0.pdf) [1] documents qualitative findings from a derivatives exchange porting from Asio callbacks to coroutine-native I/O.
candidate 4 (found by 3 of 57 passes): Asio got many things right. We built on its stream model, its buffer sequences, its executor architecture.

## vehicle - grade 1.17 (fired in 6 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              0/0/0  -> 0.00
  [6] 3. What We Found                             1/1/2  -> 1.33
  [7] 4. Design Criteria                           1/1/1  -> 1.00
  [8] 5. Asio Continuity                           1/1/0  -> 0.67
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          1/0/0  -> 0.33
  [13] 9. std::execution                            1/1/1  -> 1.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The series proposes the abstractions that HTTP and WebSocket libraries are built from - not the HTTP or WebSocket libraries themselves.
candidate 2 (found by 3 of 57 passes): Stage One alone delivers the vocabulary for the entire async I/O ecosystem.
candidate 3 (found by 3 of 57 passes): If the committee relies exclusively on one async path for networking and that path encounters delays, the networking timeline slips again.
candidate 4 (found by 2 of 57 passes): The five properties converge on problems that are specific to C++:

## coordination - grade 2.00 (fired in 6 of 19 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              2/2/2  -> 2.00
  [6] 3. What We Found                             0/0/0  -> 0.00
  [7] 4. Design Criteria                           2/2/2  -> 2.00
  [8] 5. Asio Continuity                           1/0/1  -> 0.67
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          2/2/2  -> 2.00
  [13] 9. std::execution                            0/0/0  -> 0.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two libraries - Capy and Corosio - use those mechanisms directly to deliver type-erased streams, separate compilation, and ABI stability on C++20 today.
candidate 2 (found by 3 of 57 passes): The ABI stability of Stage One provides the boundary. `any_stream` is the contract.
candidate 3 (found by 3 of 57 passes): Today, every C++ project that does I/O invents its own buffer types. Standard buffer concepts create shared vocabulary: a database driver that accepts `MutableBufferSequence` works with any I/O stack that speaks the same concepts.
candidate 4 (found by 2 of 57 passes): These libraries are maintained by other Boost authors: Boost.MySQL v2 planned on Capy/Corosio; Boost.Redis experimental port completed; Boost.Postgres building on Corosio from day one.

## insufficiency - grade 0.83 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              0/0/0  -> 0.00
  [6] 3. What We Found                             0/0/0  -> 0.00
  [7] 4. Design Criteria                           0/0/0  -> 0.00
  [8] 5. Asio Continuity                           0/0/0  -> 0.00
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                0/1/1  -> 0.67
  [12] 8. The Paper Series                          0/0/0  -> 0.00
  [13] 9. std::execution                            1/1/1  -> 1.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): A sender layer between the coroutine and the platform loses them.
candidate 2 (found by 1 of 57 passes): Pure C++20. No platform code. These abstractions enable sans-I/O protocols in the ecosystem: HTTP, WebSocket, TLS wrappers.
candidate 3 (found by 1 of 57 passes): External libraries implement portable, platform-specific I/O in terms of `std::io`.

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/1/1  -> 0.67
  [5] 2. The Evidence                              2/2/2  -> 2.00
  [6] 3. What We Found                             0/1/0  -> 0.33
  [7] 4. Design Criteria                           1/2/1  -> 1.33
  [8] 5. Asio Continuity                           1/1/1  -> 1.00
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               1/1/1  -> 1.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          0/0/0  -> 0.00
  [13] 9. std::execution                            0/0/0  -> 0.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  1/1/1  -> 1.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two libraries - Capy and Corosio - use those mechanisms directly to deliver type-erased streams, separate compilation, and ABI stability on C++20 today.
candidate 2 (found by 3 of 57 passes): The benchmark suite is published at [redis-cli-comp](https://github.com/mzimbres/redis-cli-comp) [2]; further profiling and characterisation are planned.
candidate 3 (found by 3 of 57 passes): Three independent Boost library adopters (MySQL, Redis, Postgres). One institutional evaluation in production trading infrastructure ([P4125R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4125r0.pdf) [1]).
candidate 4 (found by 3 of 57 passes): Asio has been used in production worldwide for over twenty years.

-->
