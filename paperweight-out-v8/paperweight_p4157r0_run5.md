Verdict: Adequate (4/14)

The paper offers only a thin case for standardization: it gestures at the surprise of `_BitInt` not being an integral type and at the burden of special-casing it, but does not develop those points into evidence about affected users, alternatives, or why standardization is the right remedy. The strongest concrete support is the existence of GCC and Clang implementations, while the weakest areas are the complete absence of any discussion of coordination, interoperability, or why a library solution would not suffice.

- The paper’s implementation experience is its most solid grounding, since both GCC and Clang already provide `_BitInt` with a documented maximum width.
- The motivation rests mainly on an appeal to surprise and teaching burden, but the paper does not show who is concretely affected or how widespread that burden is.
- The discussion of prior art and alternatives is asserted rather than examined, leaving the choice among minimal, useful, and extensive library support unexplored.
- The paper offers no account of coordination with C or other standards, and no argument for why the necessary behavior could not be provided by a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 5 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 5.00   accumulate 4.67   max 5.00

## SUMMARY
grades: motivation 0.83  audience 0.17  prior_art 1.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.50 / 4.50 / 4.50   (all 3 samples: 4.17)
headings: h3 5   <- NOT h2, check the unit list
on threshold: implementation
splits: motivation[2] 0/1/1  audience[6] 1/0/0  implementation[2] 1/2/2
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/1/1  -> 0.67
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): *very surprising* if `std::is_integral_v<_BitInt(N)>` was `false`
candidate 2 (found by 2 of 18 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)

## audience - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  1/0/0  -> 0.33
candidate 1 (found by 1 of 18 passes): huge wording/teaching effort to treat `_BitInt(N)` specially

## prior_art - grade 1.00 (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666 Library decisions to be made           1/1/1  -> 1.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 18 passes): mostly matches C2y taxonomy
candidate 3 (found by 2 of 18 passes): How much library support to provide? - Aggressively minimal: just the core feature - Minimal but useful: P3666R3 - More extensive: `<simd>`, `<atomic>`, etc.
candidate 4 (found by 1 of 18 passes): More extensive: `<simd>`, `<atomic>`, etc.

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

## implementation - grade 1.67  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/2/2  -> 1.67
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`

-->
