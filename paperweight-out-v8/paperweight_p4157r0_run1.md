Verdict: Weak (3/14)

The paper offers only a thin evidentiary basis for standardization, resting almost entirely on assertions about surprise and brief references to existing implementations and C23. The support is thinnest where the proposal should be most concrete: it does not identify who is affected, explain why a library cannot address the need, or discuss coordination and interoperability.

- The strongest support is the mention that GCC and Clang already implement `_BitInt`, though the paper only claims this without demonstrating how that experience informs the proposed design.
- The paper gestures at prior art in C23 and sketches possible levels of library support, but it does not establish that any of those alternatives were evaluated or why the chosen approach is preferable.
- The most glaring omission is the absence of any discussion of who is affected or why the standard is the right venue, leaving the motivating need almost entirely unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 4.00   accumulate 3.67   max 4.00

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 1.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h3 5   <- NOT h2, check the unit list
on threshold: none
splits: prior_art[3] 0/1/1  prior_art[5] 1/0/1
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): *very surprising* if `std::is_integral_v<_BitInt(N)>` was `false`

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 4 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666 Library decisions to be made           0/1/1  -> 0.67
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              1/0/1  -> 0.67
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 18 passes): mostly matches C2y taxonomy
candidate 3 (found by 2 of 18 passes): How much library support to provide? - Aggressively minimal: just the core feature - Minimal but useful: P3666R3 - More extensive: `<simd>`, `<atomic>`, etc.
candidate 4 (found by 2 of 18 passes): library spec should prefer alias templates over keyword spelling

## vehicle - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): *very surprising* if `std::is_integral_v<_BitInt(N)>` was `false`

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 6 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`

-->
