Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case, particularly by grounding the proposal in existing practice and the precedent of `noexcept`. Its thinnest area is the claim about who is affected: the real-time audio community is invoked repeatedly, but the paper does not establish that community’s scale, requirements, or inability to continue with the existing Clang attributes.

- The strongest support is the implementation experience, since the paper points to a working Clang model that has been relied upon for years and already enforces the relevant constraints.
- The argument that a library or attribute cannot express the guarantee is well supported by the distinction between attributes and type-carried behavioral properties.
- The most glaring omission is the lack of evidence about who is affected beyond a repeated assertion that the real-time audio community needs this, without demonstrating the breadth or depth of that need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 10.00   accumulate 11.50   max 12.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 1.50  implementation 2.00
sample agreement: 88 of 98 section-criterion pairs unanimous (90%)
single-sample totals would have been: 11.50 / 10.00 / 11.50   (all 3 samples: 11.00)
headings: h2 12
on threshold: vehicle, coordination, insufficiency, implementation
splits: motivation[3] 1/1/0  motivation[9] 0/1/1  prior_art[3] 1/2/2  prior_art[10] 2/2/0
        prior_art[13] 1/0/1  prior_art[14] 2/0/0  vehicle[3] 1/1/0  vehicle[9] 1/1/0
        coordination[7] 2/1/2  coordination[10] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/0  -> 0.67
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                2/2/2  -> 2.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/1/1  -> 0.67
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 2 (found by 2 of 42 passes): C++ today carries exactly **one** aspect of a function’s dynamic behaviour in its type: `noexcept` — the guarantee not to throw.
candidate 3 (found by 2 of 42 passes): Demonstrates the value of categorical behavioural guarantees in certification.
candidate 4 (found by 1 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

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
candidate 1 (found by 3 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/2/2  -> 1.67
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                2/2/2  -> 2.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 2/2/2  -> 2.00
  [10] 4. Why a type specifier and not an attrib... 2/2/0  -> 1.33
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    1/0/1  -> 0.67
  [14] 13. References                               2/0/0  -> 0.67
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` ) and the established treatment of `noexcept` as part of the type (since C++17).
candidate 2 (found by 3 of 42 passes): P3271 deliberately keeps the property **out of** the individual function’s type to allow backwards-compatible contractualization of existing code — the opposite tradeoff from this paper, which binds the effect to the function type for a published, definition-site, everywhere-visible guarantee.
candidate 3 (found by 2 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it. The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 4 (found by 2 of 42 passes): P3271 prioritizes backward compatibility (property on the pointer); this paper prioritizes a published, definition-site, everywherevisible guarantee of the function itself (property on the function type, like `noexcept`).

## vehicle - grade 1.50 (fired in 4 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/0  -> 0.67
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/1  -> 1.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 1/1/0  -> 0.67
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): `noexcept` proves that C++ can carry such an effect cleanly in the type system: it is declarable, checkable, part of type identity, sound across indirect calls, and equipped with well-defined conversion rules.
candidate 2 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 3 (found by 2 of 42 passes): The proposal is **entirely static and** decidable, and therefore standardizable independently of any research-grade, quantitative resource-bound extensions.
candidate 4 (found by 2 of 42 passes): An implementation existence proof for precisely this paper.

## coordination - grade 1.50 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                2/1/2  -> 1.67
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 2/0/2  -> 1.33
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 2 of 42 passes): the linker may select, for a given call, a variant of the function in which the check does not occur — for instance when the call is not inlined and a client-emitted, ignore-compiled version is chosen.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
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
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` )
candidate 2 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 3 of 42 passes): Clang’s implementation treats `nonblocking` as the stronger constraint: a function declared `[[clang::nonblocking(true)]]` together with `[[clang::nonallocating(false)]]` is rejected

-->
