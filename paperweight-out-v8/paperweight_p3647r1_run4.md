Verdict: Adequate (4/14)

The paper offers only a thin, largely asserted case for standardization: it gestures at useful applications and existing hardware support, but does not develop the argument that this belongs in the standard rather than in a library or compiler intrinsic. The strongest material is a single external reference to `simdjson`, while the core questions about why the standard should act, how implementations would coordinate, and what standardization would add are left unaddressed.

- The paper’s most concrete support is the mention that `simdjson` uses this technique to accelerate string parsing, which at least suggests real-world use.
- The claim of widespread hardware support across x86_64, ARM, and RISC-V is asserted but not substantiated with evidence or references.
- The paper does not establish why a library or existing intrinsic cannot already provide what is proposed.
- The most glaring omission is the absence of any argument for why the C++ standard itself should adopt the facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 4.00   accumulate 4.67   max 4.33

## SUMMARY
grades: motivation 1.17  audience 0.50  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 3.50 / 3.50 / 4.00   (all 3 samples: 3.67)
headings: h3 5   <- NOT h2, check the unit list
on threshold: none
splits: motivation[3] 1/1/2  prior_art[4] 1/0/1  prior_art[6] 1/1/0  implementation[6] 1/0/0
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivating example                           1/1/2  -> 1.33
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): useful for CRC, AES-GCM, parsing, bit manipulation, …
candidate 2 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

## audience - grade 0.50 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

## prior_art - grade 1.00 (fired in 5 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             1/0/1  -> 0.67
  [5] Proposed design                              1/1/1  -> 1.00
  [6] Implementation and wording                   1/1/0  -> 0.67
candidate 1 (found by 3 of 18 passes): widespread hardware support (x86_64, ARM, RISC-V)
candidate 2 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.
candidate 3 (found by 3 of 18 passes): `clmul` names used because it is most common (Intel, LLVM, RV64, etc.)
candidate 4 (found by 2 of 18 passes): Marked rows are integrated in this proposal.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           0/0/0  -> 0.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           0/0/0  -> 0.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           0/0/0  -> 0.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   1/0/0  -> 0.33
candidate 1 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.
candidate 2 (found by 1 of 18 passes): naive fallback implementation is trivial

-->
