Verdict: Adequate to Strong (8/14)

The paper offers a solid conceptual foundation for why frame-visible coroutines would address a real structural limitation in C++’s async models, and it points to relevant prior art and existing workarounds. However, the case for standardization remains thin where it matters most: the paper does not establish who is concretely affected, nor does it demonstrate implementation experience, interoperability, or why a library solution cannot suffice.

- The strongest support is the clear articulation of the structural constraint and the concrete example of a socket read producing both a byte count and an error condition that cannot round-trip through a single disposition.
- The paper also credibly grounds its motivation in prior art, citing P2300R10’s workarounds, the `io_result` example, and P3552R3’s heap-allocation rationale.
- The most glaring omission is the absence of any established audience or affected-user analysis, leaving the proposal without a demonstrated constituency.
- The claims about eliminating heap allocation and improving optimizer visibility are repeated as benefits but are not backed by implementation experience or evidence that a library approach cannot achieve the same ends.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.00   accumulate 8.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.67  insufficiency 1.00  implementation 1.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.00 / 8.50 / 8.00   (all 3 samples: 7.67)
headings: h2 13
on threshold: none
splits: motivation[12] 1/1/2  vehicle[11] 1/0/0  vehicle[12] 0/0/1  coordination[2] 0/1/0
        insufficiency[2] 1/0/1  insufficiency[6] 0/1/0  insufficiency[9] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 14 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/1/1  -> 1.00
  [5] 2. The Three-Channel Achievement             1/1/1  -> 1.00
  [6] 3. Compound Results in the Three-Channel ... 2/2/2  -> 2.00
  [7] 4. The Forward Mapping                       0/0/0  -> 0.00
  [8] 5. The Reverse Mapping                       2/2/2  -> 2.00
  [9] 6. The Frame Opacity Cost                    2/2/2  -> 2.00
  [10] 7. Frame-Visible Coroutines                  2/2/2  -> 2.00
  [11] 8. What Each Model Gains                     2/2/2  -> 2.00
  [12] 9. Conclusion                                1/1/2  -> 1.33
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): A structural constraint exists - compound I/O results cannot round-trip through three mutually exclusive channels - and two of the three properties that senders currently provide beyond the coroutine model trace to one language choice: the coroutine frame is opaque.
candidate 2 (found by 3 of 42 passes): The author believes that C++ would benefit from having all three coroutine models in the language simultaneously
candidate 3 (found by 3 of 42 passes): A socket read that transfers 500 bytes and then encounters `ECONNRESET` has both an error condition and a byte count. Both are produced. Both are meaningful. One disposition does not describe the completion.
candidate 4 (found by 3 of 42 passes): An I/O read that transfers 500 bytes and then encounters a connection reset produces both an `error_code` and a byte count.

## audience - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Three-Channel Achievement             0/0/0  -> 0.00
  [6] 3. Compound Results in the Three-Channel ... 0/0/0  -> 0.00
  [7] 4. The Forward Mapping                       0/0/0  -> 0.00
  [8] 5. The Reverse Mapping                       0/0/0  -> 0.00
  [9] 6. The Frame Opacity Cost                    0/0/0  -> 0.00
  [10] 7. Frame-Visible Coroutines                  0/0/0  -> 0.00
  [11] 8. What Each Model Gains                     0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 7 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                2/2/2  -> 2.00
  [5] 2. The Three-Channel Achievement             1/1/1  -> 1.00
  [6] 3. Compound Results in the Three-Channel ... 2/2/2  -> 2.00
  [7] 4. The Forward Mapping                       1/1/1  -> 1.00
  [8] 5. The Reverse Mapping                       0/0/0  -> 0.00
  [9] 6. The Frame Opacity Cost                    2/2/2  -> 2.00
  [10] 7. Frame-Visible Coroutines                  0/0/0  -> 0.00
  [11] 8. What Each Model Gains                     1/1/1  -> 1.00
  [12] 9. Conclusion                                1/1/1  -> 1.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [P2300R10](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p2300r10.html) [6] Section 5.1
candidate 2 (found by 3 of 42 passes): P2300R10 also proposes a third workaround - returning a range of senders
candidate 3 (found by 3 of 42 passes): [io_result](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/io_result.hpp) [4] is an example:
candidate 4 (found by 3 of 42 passes): [P3552R3](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3552r3.html) [7] `std::execution::task` heap-allocates for this reason - the sender operation state cannot embed a coroutine frame whose size is unknown at compile time.

## vehicle - grade 1.00 (fired in 4 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Three-Channel Achievement             0/0/0  -> 0.00
  [6] 3. Compound Results in the Three-Channel ... 0/0/0  -> 0.00
  [7] 4. The Forward Mapping                       0/0/0  -> 0.00
  [8] 5. The Reverse Mapping                       0/0/0  -> 0.00
  [9] 6. The Frame Opacity Cost                    0/0/0  -> 0.00
  [10] 7. Frame-Visible Coroutines                  1/1/1  -> 1.00
  [11] 8. What Each Model Gains                     1/0/0  -> 0.33
  [12] 9. Conclusion                                0/0/1  -> 0.33
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): If C++ added frame-visible coroutines alongside the existing opaque-frame model, `std::execution::task` eliminates its heap allocation, coroutine-based sender algorithms gain full optimizer visibility, and both async models that C++26 ships improve.
candidate 2 (found by 3 of 42 passes): If C++ added a frame-visible coroutine type alongside the existing opaque-frame coroutines, `std::execution::task` would no longer need to heap-allocate.
candidate 3 (found by 1 of 42 passes): Frame-visible coroutines remove that choice.
candidate 4 (found by 1 of 42 passes): Frame-visible coroutines would eliminate `std::execution::task`'s heap allocation and give both async models optimizer visibility.

## coordination - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Three-Channel Achievement             0/0/0  -> 0.00
  [6] 3. Compound Results in the Three-Channel ... 0/0/0  -> 0.00
  [7] 4. The Forward Mapping                       0/0/0  -> 0.00
  [8] 5. The Reverse Mapping                       0/0/0  -> 0.00
  [9] 6. The Frame Opacity Cost                    0/0/0  -> 0.00
  [10] 7. Frame-Visible Coroutines                  1/1/1  -> 1.00
  [11] 8. What Each Model Gains                     0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): If C++ added a frame-visible coroutine type alongside the existing opaque-frame coroutines, `std::execution::task` would no longer need to heap-allocate.
candidate 2 (found by 1 of 42 passes): If C++ added frame-visible coroutines alongside the existing opaque-frame model, `std::execution::task` eliminates its heap allocation, coroutine-based sender algorithms gain full optimizer visibility, and both async models that C++26 ships improve.

## insufficiency - grade 1.00 (fired in 3 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Three-Channel Achievement             0/0/0  -> 0.00
  [6] 3. Compound Results in the Three-Channel ... 0/1/0  -> 0.33
  [7] 4. The Forward Mapping                       0/0/0  -> 0.00
  [8] 5. The Reverse Mapping                       0/0/0  -> 0.00
  [9] 6. The Frame Opacity Cost                    0/2/2  -> 1.33
  [10] 7. Frame-Visible Coroutines                  0/0/0  -> 0.00
  [11] 8. What Each Model Gains                     0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): If C++ added frame-visible coroutines alongside the existing opaque-frame model, `std::execution::task` eliminates its heap allocation, coroutine-based sender algorithms gain full optimizer visibility
candidate 2 (found by 2 of 42 passes): The coroutine frame must be heap-allocated because its size is determined after inlining and optimization passes. No compiler guarantees HALO.
candidate 3 (found by 1 of 42 passes): The standard provides a mechanism to reduce three channels to two.

## implementation - grade 1.00  [binary: max] (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. The Three-Channel Achievement             0/0/0  -> 0.00
  [6] 3. Compound Results in the Three-Channel ... 0/0/0  -> 0.00
  [7] 4. The Forward Mapping                       1/1/1  -> 1.00
  [8] 5. The Reverse Mapping                       0/0/0  -> 0.00
  [9] 6. The Frame Opacity Cost                    0/0/0  -> 0.00
  [10] 7. Frame-Visible Coroutines                  0/0/0  -> 0.00
  [11] 8. What Each Model Gains                     0/0/0  -> 0.00
  [12] 9. Conclusion                                0/0/0  -> 0.00
  [13] Acknowledgments                              0/0/0  -> 0.00
  [14] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): [io_result](https://github.com/cppalliance/capy/blob/p4088r0/include/boost/capy/io_result.hpp) [4] is an example:

-->
