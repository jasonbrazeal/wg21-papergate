Verdict: Strong (10/14)

The paper offers solid grounding for its central technical claim—that the feature follows an existing, deployed implementation—but its broader case for standardization rests on a narrow evidentiary base. The strongest material concerns implementation experience and the inadequacy of attributes, while the thinnest concerns who is actually affected and how the work would coordinate with the wider ecosystem.

- The paper’s strongest support is its implementation experience, since the Clang model it generalizes already exists and has been used in real code.
- The case that a library solution cannot express these guarantees is also well established through the limitations of attributes and the precedent of `noexcept`.
- The paper claims but does not establish who is affected, relying on a single reference to the real-time audio community without broader evidence of adoption or demand.
- The most glaring omission is coordination and interoperability, where the paper gestures at libc++ annotation work but does not establish how the proposal would fit with existing practice or other standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 15. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 10.00   accumulate 9.83   max 11.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.67  coordination 1.17  insufficiency 1.50  implementation 2.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 10.00 / 9.50 / 10.00   (all 3 samples: 9.83)
headings: h2 12
on threshold: coordination, insufficiency
splits: motivation[3] 1/0/1  prior_art[11] 1/0/0  prior_art[14] 2/0/2  vehicle[3] 1/0/0
        coordination[7] 2/2/1  coordination[10] 0/0/2  implementation[7] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/0/1  -> 0.67
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                2/2/2  -> 2.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 2 (found by 2 of 42 passes): C++ today carries exactly **one** aspect of a function’s dynamic behaviour in its type: `noexcept` — the guarantee not to throw.
candidate 3 (found by 2 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 4 (found by 1 of 42 passes): For hard real-time paths, latency-critical middleware, and freestanding code, the decisive interface question is not “what does this function compute?” but “which dynamic effects does it exclude?” — allocation, blocking, recursion, throwing exceptions.

## audience - grade 0.50 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/1  -> 1.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                2/2/2  -> 2.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 2/2/2  -> 2.00
  [10] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [11] 4. Why a type specifier and not an attrib... 1/0/0  -> 0.33
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    1/1/1  -> 1.00
  [14] 13. References                               2/0/2  -> 1.33
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` ) and the established treatment of `noexcept` as part of the type (since C++17).
candidate 2 (found by 3 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it. The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 3 of 42 passes): P3271 deliberately keeps the property **out of** the individual function’s type to allow backwards-compatible contractualization of existing code — the opposite tradeoff from this paper, which binds the effect to the function type for a published, definition-site, everywhere-visible guarantee.
candidate 4 (found by 3 of 42 passes): Effect polymorphism (§5.8), the effect-parameterized `std::function` , and the library-annotation programme follow in a later revision.

## vehicle - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/0/0  -> 0.33
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/1  -> 1.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 1 of 42 passes): The proposal is **entirely static and** decidable, and therefore standardizable independently of any research-grade, quantitative resource-bound extensions.

## coordination - grade 1.17 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                2/2/1  -> 1.67
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 0/0/2  -> 0.67
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 1 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 1 of 42 passes): the January 2026 libc++ effort to annotate the standard library for `[[nonblocking]]` reports exactly this behaviour — when the compiler cannot see a function’s body ... it must treat the function as potentially blocking.

## insufficiency - grade 1.50 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/1  -> 1.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 2 (found by 2 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 1 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/2  -> 1.33
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 2/2/2  -> 2.00
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` )
candidate 2 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 3 of 42 passes): Clang applies these to **function types** and treats them as conceptually a superset of `noexcept` ; the override-conflict and call-graph-propagation behaviour described below already exists there.
candidate 4 (found by 2 of 42 passes): Clang’s implementation treats `nonblocking` as the stronger constraint: a function declared `[[clang::nonblocking(true)]]` together with `[[clang::nonallocating(false)]]` is rejected

-->
