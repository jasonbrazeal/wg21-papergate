Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most: it explains why the feature belongs in the standard rather than in attributes or libraries, it grounds the design in existing practice and prior art, and it demonstrates real implementation experience. The support is thinnest where the paper relies on the same sentence about the real-time audio community to carry several distinct burdens, leaving the affected-user case and the insufficiency of library solutions more asserted than shown.

- The strongest support is the concrete implementation experience with Clang’s `nonblocking` and `nonallocating` attributes, including how their interaction is already checked.
- The paper also clearly establishes why the standard is the right venue, since attributes cannot carry the guarantee across type-based interfaces and the check is static and decidable.
- The case for prior art and alternatives is well made through the explicit contrast with `noexcept` and with P3271’s opposite tradeoff.
- The most glaring omission is that the claim about who is affected rests on a single repeated sentence, without evidence of the breadth or depth of that community’s reliance.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.67   accumulate 10.83   max 11.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.67  coordination 1.83  insufficiency 0.67  implementation 2.00
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 10.50 / 12.00 / 9.50   (all 3 samples: 10.67)
headings: h2 12
on threshold: vehicle
splits: motivation[3] 0/1/1  prior_art[9] 2/2/0  vehicle[3] 0/0/1  vehicle[7] 1/2/1
        coordination[7] 2/2/1  insufficiency[7] 1/1/0  insufficiency[10] 0/2/0
        implementation[7] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/1/1  -> 0.67
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
candidate 3 (found by 1 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 4 (found by 1 of 42 passes): Today this guarantee is documented informally or forbidden wholesale by coding standards, rather than carried as a checked promise to callers.

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

## prior_art - grade 2.00 (fired in 4 of 14 sections, strong in 3)
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
  [9] 3. Prior art                                 2/2/0  -> 1.33
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): It follows a model already implemented in Clang ( `[[clang::nonblocking]]` / `[[clang::nonallocating]]` ) and the established treatment of `noexcept` as part of the type (since C++17).
candidate 2 (found by 3 of 42 passes): This paper takes `noexcept` as a blueprint and generalizes it.
candidate 3 (found by 2 of 42 passes): P3271 deliberately keeps the property **out of** the individual function’s type to allow backwards-compatible contractualization of existing code — the opposite tradeoff from this paper, which binds the effect to the function type for a published, definition-site, everywhere-visible guarantee.
candidate 4 (found by 2 of 42 passes): P3271 prioritizes backward compatibility (property on the pointer); this paper prioritizes a published, definition-site, everywherevisible guarantee of the function itself (property on the function type, like `noexcept`).

## vehicle - grade 1.67 (fired in 3 of 14 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/1  -> 0.33
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/2/1  -> 1.33
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): An attribute carries two properties in C++ that disqualify it from expressing an effect guarantee.
candidate 2 (found by 1 of 42 passes): The proposal is **entirely static and** decidable, and therefore standardizable independently of any research-grade, quantitative resource-bound extensions.
candidate 3 (found by 1 of 42 passes): The practical need is real and already implemented: the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 4 (found by 1 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.

## coordination - grade 1.83 (fired in 2 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
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
  [10] 4. Why a type specifier and not an attrib... 2/2/2  -> 2.00
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 2 of 42 passes): The pointer `p` has type `void(*)(Event&)` . The attribute, not being part of type identity, has **vanished** at the conversion to a pointer.
candidate 3 (found by 1 of 42 passes): A property that is not part of type identity cannot be carried reliably across separate compilation: it does not survive the type-based interface (function pointer, vtable slot, template argument).

## insufficiency - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/1/0  -> 0.67
  [8] 2. The idea in one sentence                  0/0/0  -> 0.00
  [9] 3. Prior art                                 0/0/0  -> 0.00
  [10] 4. Why a type specifier and not an attrib... 0/2/0  -> 0.67
  [11] 4. Why a type specifier and not an attrib... 0/0/0  -> 0.00
  [12] 11. Open questions                           0/0/0  -> 0.00
  [13] 12. Recommended next step                    0/0/0  -> 0.00
  [14] 13. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): the real-time audio community has for years relied on Clang’s `nonblocking` / `nonallocating` effects to check exactly these guarantees at callback boundaries.
candidate 2 (found by 1 of 42 passes): Clang’s `[[clang::nonblocking]]` is a nonstandard *type* attribute — the exception that proves the rule; tellingly, even it has no effect on name mangling.

## implementation - grade 2.00  [binary: max] (fired in 3 of 14 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] noexcept for C++                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] 1. Motivation                                0/0/0  -> 0.00
  [5] 13. References                               0/0/0  -> 0.00
  [6] Revision history                             0/0/0  -> 0.00
  [7] 1. Motivation                                1/2/2  -> 1.67
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
