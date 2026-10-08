Verdict: Weak to Adequate (4/14)

The paper offers a narrow but genuine foundation for its motivation, centered on real undefined behavior in x87 `long double` padding and a concrete divergence in MSVC’s handling of it. Beyond that, however, the case for standardization is largely asserted rather than demonstrated: the affected audience, prior art, implementation experience, and the need for a standard rather than a library solution are all thin or absent.

- The strongest support is the established motivation, which identifies a specific UB pitfall and shows how the proposed functions could avoid special cases tied to padding bits.
- The paper claims implementation experience through MSVC’s accidental behavior, but it does not establish that this amounts to meaningful, portable implementation practice.
- The most glaring omission is the absence of any argument for why the standard, rather than a library, is the right vehicle for the proposed functionality.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.67   accumulate 4.00   max 4.67

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 0.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.00 / 4.50 / 3.00   (all 3 samples: 3.50)
headings: h3 5   <- NOT h2, check the unit list
on threshold: motivation
splits: motivation[4] 1/0/0  audience[2] 0/1/0  implementation[3] 1/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  2/2/2  -> 2.00
  [3] The problem, cont.                           1/1/1  -> 1.00
  [4] Possible solutions                           1/0/0  -> 0.33
  [5] Gotcha: clearing padding in unions           1/1/1  -> 1.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): UB due to padding bits in 80-bit x87 `long double`
candidate 2 (found by 3 of 18 passes): MSVC treats padding in the original as zero
candidate 3 (found by 3 of 18 passes): cannot clear padding without knowing active alternative
candidate 4 (found by 1 of 18 passes): "Mathematically correct" functions eliminate special cases and UB pitfalls:

## audience - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  0/1/0  -> 0.33
  [3] The problem, cont.                           0/0/0  -> 0.00
  [4] Possible solutions                           0/0/0  -> 0.00
  [5] Gotcha: clearing padding in unions           0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): it would be useful if it worked (for math function implementations)

## prior_art - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  0/0/0  -> 0.00
  [3] The problem, cont.                           1/1/1  -> 1.00
  [4] Possible solutions                           0/0/0  -> 0.00
  [5] Gotcha: clearing padding in unions           0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): MSVC treats padding in the original as zero

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  0/0/0  -> 0.00
  [3] The problem, cont.                           0/0/0  -> 0.00
  [4] Possible solutions                           0/0/0  -> 0.00
  [5] Gotcha: clearing padding in unions           0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  0/0/0  -> 0.00
  [3] The problem, cont.                           0/0/0  -> 0.00
  [4] Possible solutions                           0/0/0  -> 0.00
  [5] Gotcha: clearing padding in unions           0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  0/0/0  -> 0.00
  [3] The problem, cont.                           0/0/0  -> 0.00
  [4] Possible solutions                           0/0/0  -> 0.00
  [5] Gotcha: clearing padding in unions           0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] The problem                                  0/0/0  -> 0.00
  [3] The problem, cont.                           1/2/1  -> 1.33
  [4] Possible solutions                           1/1/1  -> 1.00
  [5] Gotcha: clearing padding in unions           0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): ✔️ already implemented (accidentally)
candidate 2 (found by 2 of 18 passes): MSVC treats padding in the original as zero
candidate 3 (found by 1 of 18 passes): MSVC treats padding in the original as zero - see https://developercommunity.visualstudio.com/t/11027496

-->
