Verdict: Weak to Adequate (3/14)

The paper offers only a thin evidentiary basis for standardization, resting mostly on assertions about surprise and brief references to existing practice rather than on demonstrated need, affected users, or coordination requirements. The thinnest support is in the areas that would justify committee action: who is affected, why a library cannot suffice, and how the feature interoperates with the rest of the standard.

- The strongest support is the mention that GCC and Clang already implement the feature, though even that is only claimed and not developed into evidence of experience or demand.
- The paper gestures at prior art by citing C23’s `_BitInt` and a preference for alias templates, but it does not establish how those alternatives were evaluated or why they are insufficient.
- The argument for why the standard should act leans entirely on the intuition that it would be surprising for `std::is_integral_v<_BitInt(N)>` to be false, without showing who would encounter that surprise or what breaks as a result.
- The most glaring omission is any account of affected users, coordination with other library components, or why a library-only solution would not meet the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 4.33   accumulate 4.33   max 4.33

## SUMMARY
grades: motivation 0.50  audience 0.00  prior_art 1.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 4.00 / 2.00 / 4.00   (all 3 samples: 3.33)
headings: h3 5   <- NOT h2, check the unit list
on threshold: none
splits: implementation[2] 2/0/2
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
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666 Library decisions to be made           1/1/1  -> 1.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              1/1/1  -> 1.00
  [6] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 18 passes): library spec should prefer alias templates over keyword spelling
candidate 3 (found by 3 of 18 passes): mostly matches C2y taxonomy
candidate 4 (found by 2 of 18 passes): How much library support to provide? - Aggressively minimal: just the core feature - Minimal but useful: P3666R3 - More extensive: `<simd>`, `<atomic>`, etc.

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

## implementation - grade 1.33  [binary: max] (fired in 1 of 6 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/0/2  -> 1.33
  [3] P3666 Library decisions to be made           0/0/0  -> 0.00
  [4] Anecdote: std::cmpless                       0/0/0  -> 0.00
  [5] Alias templates                              0/0/0  -> 0.00
  [6] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`

-->
