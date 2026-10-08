Verdict: Adequate (4/14)

The paper’s support for its own standardization is uneven: it can point to real implementation experience, but most of the argument rests on assertions about C23 alignment and programmer expectations rather than demonstrated need, affected users, or why standardization is the right vehicle. The thinnest areas are the absence of any discussion of who is affected, how the feature would coordinate with existing C++ library specifications, and why a library-level solution would not suffice.

- The strongest support is implementation experience, with GCC and Clang already providing `_BitInt` up to very large widths.
- The paper asserts, but does not establish, that it would be surprising for `std::is_integral_v<_BitInt(N)>` to be false, which is its main argument for why the feature matters.
- The paper gestures at C23 prior art and a range of possible library-support levels, but does not establish that those alternatives were seriously evaluated or why the proposed scope is the right one.
- The most glaring omission is the complete lack of discussion of who is affected or how the proposal would coordinate with existing C++ library facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 4 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 5.00   accumulate 4.83   max 5.00

## SUMMARY
grades: motivation 0.67  audience 0.00  prior_art 1.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 4.00 / 4.00 / 4.50   (all 3 samples: 4.17)
headings: h3 5   <- NOT h2, check the unit list
on threshold: implementation
splits: motivation[2] 0/0/1  prior_art[3] 0/1/1  prior_art[5] 1/1/0
## END SUMMARY

## motivation - grade 0.67 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/1  -> 0.33
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): *very surprising* if `std::is_integral_v<_BitInt(N)>` was `false`
candidate 2 (found by 1 of 18 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)

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

## prior_art - grade 1.00 (fired in 4 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666 Library decisions to be made           0/1/1  -> 0.67
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              1/1/0  -> 0.67
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

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`

-->
