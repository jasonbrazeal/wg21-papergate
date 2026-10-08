Verdict: Weak to Adequate (4/14)

The paper offers only a narrow foundation for its standardization case: implementation experience is concrete, but the central rationale rests on an intuition about what would be surprising rather than a demonstrated need, and several essential justifications are simply absent. The thinnest areas are the failure to identify who is affected, why a library solution would not suffice, and how the feature coordinates with existing or adjacent standardization efforts.

- The strongest support is the established implementation experience, with GCC and Clang already providing `_BitInt` up to a documented maximum width.
- The paper’s motivation is asserted through the claim that it would be “very surprising” for `std::is_integral_v<_BitInt(N)>` to be false, but that surprise is not connected to concrete user or ecosystem impact.
- Prior art and alternatives are only gestured at, with C23’s `_BitInt` mentioned and a few possible scopes listed, but no substantive comparison or justification for the chosen scope.
- The most glaring omission is the absence of any established case for why the standard is needed or why a library cannot address the problem, leaving the proposal’s standardization rationale largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 4.67   accumulate 4.33   max 4.67

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 1.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.00 / 3.00 / 4.00   (all 3 samples: 3.67)
headings: h3 5   <- NOT h2, check the unit list
on threshold: implementation
splits: prior_art[3] 0/0/1  implementation[2] 2/1/2
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
  [3] P3666 Library decisions to be made           0/0/1  -> 0.33
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              1/1/1  -> 1.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 18 passes): library spec should prefer alias templates over keyword spelling
candidate 3 (found by 3 of 18 passes): mostly matches C2y taxonomy
candidate 4 (found by 1 of 18 passes): How much library support to provide? - Aggressively minimal: just the core feature - Minimal but useful: P3666R3 - More extensive: `<simd>`, `<atomic>`, etc.

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
  [2] Introduction                                 2/1/2  -> 1.67
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`

-->
