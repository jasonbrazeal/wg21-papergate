Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its own standardization, particularly in showing that the problem is real, that the proposed mechanism follows an established language precedent, and that a nonstandard implementation already exists. The thinnest part of the case is the claim about who is affected: the paper asserts a broad community need and points to ongoing work, but does not itself establish the scale or representativeness of that need beyond repeated references to the same examples.

- The strongest support is the implementation experience, since the paper grounds its design in Clang’s existing `nonblocking` and `nonallocating` effects and their observed behavior.
- The argument for why the standard must act is also well supported, because the paper shows that attributes cannot carry the needed guarantee and that `noexcept` provides a workable in-type precedent.
- The most glaring omission is the lack of established evidence about who is affected, since the paper repeatedly asserts the real-time audio community’s reliance and the libc++ annotation effort without demonstrating their scope or confirming the reported behavior independently.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 10.00   accumulate 11.33   max 12.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 1.50  implementation 2.00
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 11.50 / 11.00 / 11.00   (all 3 samples: 11.17)
headings: h2 12
on threshold: vehicle, coordination, insufficiency, implementation
splits: motivation[3] 1/0/1  audience[10] 0/0/1  prior_art[10] 0/2/0  prior_art[11] 1/0/0
        prior_art[14] 2/0/0  vehicle[3] 1/0/0  coordination[7] 2/1/2  coordination[10] 2/2/0
        implementation[9] 0/2/0
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
candidate 1 (found by 3 of 42 passes): The real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 3 (found by 2 of 42 passes): C++ today carries exactly **one** aspect of a function’s dynamic behaviour in its type: `noexcept` — the guarantee not to throw.

## audience - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
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
  [10] 4. Why a type specifier and not an attrib... 0/0/1  -> 0.33
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 1 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 1 of 42 passes): This is not hypothetical: the January 2026 libc++ effort to annotate the standard library for `[[nonblocking]]` reports exactly this behaviour

## prior_art - grade 2.00 (fired in 6 of 14 sections, strong in 3)  (SHARED PASSAGE)
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
  [10] 4. Why a type specifier and not an attrib... 0/2/0  -> 0.67
  [11] 4. Why a type specifier and not an attrib... 1/0/0  -> 0.33
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               2/0/0  -> 0.67
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` ) and the established treatment of `noexcept` as part of the type (since C++17).
candidate 2 (found by 3 of 42 passes): P3271 deliberately keeps the property **out of** the individual function’s type to allow backwards-compatible contractualization of existing code — the opposite tradeoff from this paper, which binds the effect to the function type for a published, definition-site, everywhere-visible guarantee.
candidate 3 (found by 2 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it.
candidate 4 (found by 1 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it. The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

## vehicle - grade 1.50 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
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
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 2 (found by 2 of 42 passes): `noexcept` proves that C++ can carry such an effect cleanly in the type system: it is declarable, checkable, part of type identity, sound across indirect calls, and equipped with well-defined conversion rules.
candidate 3 (found by 1 of 42 passes): This paper generalizes that principle into a small, closed, orthogonal family of effects that are declared as part of the function type, checked by the compiler, propagated through the call graph, and discharged at region boundaries.
candidate 4 (found by 1 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it.

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
  [10] 4. Why a type specifier and not an attrib... 2/2/0  -> 1.33
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 1 of 42 passes): Clang’s implementation treats `nonblocking` as the stronger constraint: a function declared `[[clang::nonblocking(true)]]` together with `[[clang::nonallocating(false)]]` is rejected, because on mainstream hosted platforms the global allocator may take locks, so “does not block” subsumes “does not allocate”.
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
candidate 1 (found by 3 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 2 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 3 (found by 1 of 42 passes): Clang’s `[[clang::nonblocking]]` is a nonstandard *type* attribute — the exception that proves the rule; tellingly, even it has no effect on name mangling.

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
  [9] 3. Prior art                                 0/2/0  -> 0.67
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` )
candidate 2 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 3 (found by 3 of 42 passes): Clang’s implementation treats `nonblocking` as the stronger constraint: a function declared `[[clang::nonblocking(true)]]` together with `[[clang::nonallocating(false)]]` is rejected
candidate 4 (found by 1 of 42 passes): Clang applies these to **function types** and treats them as conceptually a superset of `noexcept` ; the override-conflict and call-graph-propagation behaviour described below already exists there.

-->
