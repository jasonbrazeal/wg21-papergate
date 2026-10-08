Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it demonstrates real-world use, identifies affected communities, and shows credible prior art and interoperability with existing libraries. The support is thinnest where the paper needs to justify why this belongs in the standard rather than remaining a library, and where it needs to show that the specific abstractions proposed have been implemented and validated broadly enough to warrant standardization.

- The strongest support comes from concrete production and institutional use, including Asio’s two-decade history and independent Boost libraries building on these abstractions today.
- The paper also establishes meaningful prior art and coordination, showing that Capy and Corosio already deliver the promised properties on C++20 and that adjacent Boost projects are adopting the approach.
- The case for why the standard is the right home is asserted rather than demonstrated, with claims about vocabulary and ecosystem convergence not backed by evidence that a library cannot serve the same role.
- The most glaring omission is implementation experience for the specific proposal: two of the papers in the series are not yet implemented, and the broader claim of backing implementation experience is not substantiated beyond the existence of related libraries.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.50/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.50 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.50   corroborated 11.00   accumulate 11.83   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 1.00  coordination 2.00  insufficiency 0.50  implementation 1.33
sample agreement: 116 of 133 section-criterion pairs unanimous (87%)
single-sample totals would have been: 11.50 / 11.50 / 10.00   (all 3 samples: 10.50)
headings: h2 17 + bold numbered 1
on threshold: none
splits: motivation[7] 2/1/2  motivation[14] 0/1/0  motivation[17] 0/1/1  audience[5] 1/2/2
        audience[7] 2/2/1  prior_art[6] 1/2/1  prior_art[9] 0/0/1  prior_art[12] 0/0/2
        prior_art[14] 2/1/1  vehicle[7] 2/1/0  vehicle[8] 0/1/0  vehicle[11] 0/1/1
        coordination[8] 1/2/1  implementation[7] 1/2/1  implementation[8] 2/1/1
        implementation[11] 1/0/1  implementation[12] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 10 of 19 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              0/0/0  -> 0.00
  [6] 3. What We Found                             1/1/1  -> 1.00
  [7] 4. Design Criteria                           2/1/2  -> 1.67
  [8] 5. Asio Continuity                           2/2/2  -> 2.00
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          2/2/2  -> 2.00
  [13] 9. std::execution                            2/2/2  -> 2.00
  [14] 10. Limitations                              0/1/0  -> 0.33
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             1/1/1  -> 1.00
  [17] 13. std::io                                  0/1/1  -> 0.67
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): C++ coroutines have five language mechanisms that combine into the ideal substrate for coroutine-native I/O.
candidate 2 (found by 3 of 57 passes): The series proposes the abstractions that HTTP and WebSocket libraries are built from - not the HTTP or WebSocket libraries themselves.
candidate 3 (found by 3 of 57 passes): Today, every C++ project that does I/O invents its own buffer types.
candidate 4 (found by 3 of 57 passes): Production C++ lags the standard by three to seven years.

## audience - grade 1.67 (fired in 4 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              1/2/2  -> 1.67
  [6] 3. What We Found                             0/0/0  -> 0.00
  [7] 4. Design Criteria                           2/2/1  -> 1.67
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
candidate 2 (found by 3 of 57 passes): A production trading infrastructure company is evaluating Corosio for high-performance networking.
candidate 3 (found by 3 of 57 passes): Asio has been used in production worldwide for over twenty years.
candidate 4 (found by 2 of 57 passes): Three independent Boost library adopters (MySQL, Redis, Postgres). One institutional evaluation in production trading infrastructure ([P4125R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4125r0.pdf)[1]).

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. The Evidence                              1/1/1  -> 1.00
  [6] 3. What We Found                             1/2/1  -> 1.33
  [7] 4. Design Criteria                           2/2/2  -> 2.00
  [8] 5. Asio Continuity                           2/2/2  -> 2.00
  [9] 6. The Three-Layer Architecture              0/0/1  -> 0.33
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                1/1/1  -> 1.00
  [12] 8. The Paper Series                          0/0/2  -> 0.67
  [13] 9. std::execution                            0/0/0  -> 0.00
  [14] 10. Limitations                              2/1/1  -> 1.33
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             1/1/1  -> 1.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two libraries - Capy and Corosio - use those mechanisms directly to deliver type-erased streams, separate compilation, and ABI stability on C++20 today.
candidate 2 (found by 3 of 57 passes): Coroutine-native I/O and `std::execution` are complementary.
candidate 3 (found by 3 of 57 passes): [P4125R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4125r0.pdf)[1] documents qualitative findings from a derivatives exchange porting from Asio callbacks to coroutine-native I/O.
candidate 4 (found by 3 of 57 passes): Asio got many things right. We built on its stream model, its buffer sequences, its executor architecture.

## vehicle - grade 1.00 (fired in 6 of 19 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              0/0/0  -> 0.00
  [6] 3. What We Found                             1/1/1  -> 1.00
  [7] 4. Design Criteria                           2/1/0  -> 1.00
  [8] 5. Asio Continuity                           0/1/0  -> 0.33
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               0/0/0  -> 0.00
  [11] 1 IoAwaitable                                0/1/1  -> 0.67
  [12] 8. The Paper Series                          1/1/1  -> 1.00
  [13] 9. std::execution                            1/1/1  -> 1.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The five properties converge on problems that are specific to C++:
candidate 2 (found by 3 of 57 passes): The standard provides the vocabulary; adapters bridge to the I/O backend.
candidate 3 (found by 2 of 57 passes): Stage One alone delivers the vocabulary for the entire async I/O ecosystem.
candidate 4 (found by 2 of 57 passes): The committee invested years in this work. It delivers real value for compile-time work graphs and heterogeneous dispatch.

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
  [8] 5. Asio Continuity                           1/2/1  -> 1.33
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
candidate 2 (found by 3 of 57 passes): These libraries are maintained by other Boost authors: Boost.MySQL ... Migrating to Corosio; Boost.Redis ... Experimental port completed; Boost.Postgres ... Building on Corosio from day one.
candidate 3 (found by 3 of 57 passes): Boost.Http, Boost.MySQL, and Boost.Redis are building on these abstractions today.
candidate 4 (found by 2 of 57 passes): Asio has been used in production worldwide for over twenty years. It is the foundation of the Networking TS. Boost.Beast, Boost.MySQL, Boost.Redis, and hundreds of proprietary codebases depend on it.

## insufficiency - grade 0.50 (fired in 1 of 19 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
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
  [11] 1 IoAwaitable                                0/0/0  -> 0.00
  [12] 8. The Paper Series                          0/0/0  -> 0.00
  [13] 9. std::execution                            1/1/1  -> 1.00
  [14] 10. Limitations                              0/0/0  -> 0.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  0/0/0  -> 0.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): A sender layer between the coroutine and the platform loses them.

## implementation - grade 1.33  [binary: max] (fired in 8 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Evidence                              0/0/0  -> 0.00
  [6] 3. What We Found                             0/0/0  -> 0.00
  [7] 4. Design Criteria                           1/2/1  -> 1.33
  [8] 5. Asio Continuity                           2/1/1  -> 1.33
  [9] 6. The Three-Layer Architecture              0/0/0  -> 0.00
  [10] 7. Approach to Standardization               1/1/1  -> 1.00
  [11] 1 IoAwaitable                                1/0/1  -> 0.67
  [12] 8. The Paper Series                          0/1/0  -> 0.33
  [13] 9. std::execution                            0/0/0  -> 0.00
  [14] 10. Limitations                              1/1/1  -> 1.00
  [15] 11. Timeline                                 0/0/0  -> 0.00
  [16] 12. What We Continue to Maintain             0/0/0  -> 0.00
  [17] 13. std::io                                  1/1/1  -> 1.00
  [18] References                                   0/0/0  -> 0.00
  [19] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Two libraries - Capy and Corosio - use those mechanisms directly to deliver type-erased streams, separate compilation, and ABI stability on C++20 today.
candidate 2 (found by 3 of 57 passes): Asio has been used in production worldwide for over twenty years.
candidate 3 (found by 3 of 57 passes): each is backed by implementation experience
candidate 4 (found by 3 of 57 passes): Papers 9 (Files) and 12 (UDP) are not yet implemented in Corosio.

-->
