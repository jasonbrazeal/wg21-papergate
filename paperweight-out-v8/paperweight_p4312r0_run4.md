Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing its proposed effect guarantees, particularly through its grounding in existing Clang implementation experience and the clear precedent of `noexcept` as a type-level behavioral contract. The case is thinnest where it needs to demonstrate who specifically is affected and why the standard—rather than continued compiler-specific extension—is the necessary venue, since those points are asserted more than evidenced.

- The strongest support comes from implementation experience, with Clang’s `nonblocking` and `nonallocating` attributes already deployed and relied upon by the real-time audio community for years.
- The paper clearly establishes why a library or attribute cannot express the guarantee, since attributes lack type-level enforcement and the existing Clang attribute tellingly does not even affect name mangling.
- Prior art and alternatives are well covered, including the explicit contrast with P3271’s decision to keep the property out of the function type.
- The most glaring omission is the failure to establish who is affected beyond repeated references to the real-time audio community, leaving the breadth and urgency of the need under-supported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 10.00   accumulate 11.67   max 12.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.17  coordination 1.67  insufficiency 1.50  implementation 2.00
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 11.00 / 10.50 / 11.50   (all 3 samples: 10.83)
headings: h2 12
on threshold: coordination, insufficiency, implementation
splits: motivation[3] 1/1/0  prior_art[7] 1/2/2  prior_art[10] 0/2/0  prior_art[11] 1/0/1
        vehicle[9] 1/1/0  vehicle[10] 2/0/2  coordination[7] 1/1/2  implementation[9] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 14 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 3 (found by 2 of 42 passes): C++ today carries exactly **one** aspect of a function’s dynamic behaviour in its type: `noexcept` — the guarantee not to throw.

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
candidate 1 (found by 2 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 1 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     2/2/2  -> 2.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/2/2  -> 1.67
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 2/2/2  -> 2.00
  [10] 4. Why a type specifier and not an attrib... 0/2/0  -> 0.67
  [11] 4. Why a type specifier and not an attrib... 1/0/1  -> 0.67
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               2/2/2  -> 2.00
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` ) and the established treatment of `noexcept` as part of the type (since C++17).
candidate 2 (found by 3 of 42 passes): P3271 deliberately keeps the property **out of** the individual function’s type to allow backwards-compatible contractualization of existing code — the opposite tradeoff from this paper, which binds the effect to the function type for a published, definition-site, everywhere-visible guarantee.
candidate 3 (found by 3 of 42 passes): Discussed as the third design option in §3–§4.
candidate 4 (found by 2 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it.

## vehicle - grade 1.17 (fired in 4 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/1  -> 1.00
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 1/1/0  -> 0.67
  [10] 4. Why a type specifier and not an attrib... 2/0/2  -> 1.33
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it.
candidate 2 (found by 2 of 42 passes): The proposal is **entirely static and** decidable, and therefore standardizable independently of any research-grade, quantitative resource-bound extensions.
candidate 3 (found by 2 of 42 passes): An implementation existence proof for precisely this paper.
candidate 4 (found by 2 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.

## coordination - grade 1.67 (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/2  -> 1.33
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 2 of 42 passes): the January 2026 libc++ effort to annotate the standard library for `[[nonblocking]]` reports exactly this behaviour — when the compiler cannot see a function’s body ... it must treat the function as potentially blocking.
candidate 3 (found by 1 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 4 (found by 1 of 42 passes): The January 2026 libc++ effort to annotate the standard library for `[[nonblocking]]` reports exactly this behaviour — when the compiler cannot see a function’s body... it must treat the function as potentially blocking.

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
candidate 1 (found by 2 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 2 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 3 (found by 1 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 4 (found by 1 of 42 passes): Clang’s `[[clang::nonblocking]]` is a nonstandard *type* attribute — the exception that proves the rule; tellingly, even it has no effect on name mangling.

## implementation - grade 2.00  [binary: max] (fired in 4 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [9] 3. Prior art                                 2/0/2  -> 1.33
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` )
candidate 2 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 3 of 42 passes): Clang’s implementation treats `nonblocking` as the stronger constraint: a function declared `[[clang::nonblocking(true)]]` together with `[[clang::nonallocating(false)]]` is rejected
candidate 4 (found by 2 of 42 passes): Clang applies these to **function types** and treats them as conceptually a superset of `noexcept` ; the override-conflict and call-graph-propagation behaviour described below already exists there.

-->
