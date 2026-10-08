Verdict: Adequate (4/14)

The paper offers only a thin, largely asserted case for standardization: it gestures at useful applications and existing practice, but does not develop the argument that this belongs in the standard rather than in a library or portable abstraction. The support is thinnest where the proposal needs to justify standardization itself, coordinate with existing facilities, or show why implementation outside the standard is insufficient.

- The strongest support is the claim of existing use in `simdjson` and the mention of widespread hardware support across major architectures.
- The paper asserts relevance to CRC, AES-GCM, parsing, and bit manipulation, but does not establish who is affected or why that matters for standardization.
- The paper does not establish prior art and alternatives beyond naming conventions and a table whose significance is not explained.
- The most glaring omission is the absence of any case for why the standard, rather than a library, is the right home for this facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.67   accumulate 4.67   max 3.67

## SUMMARY
grades: motivation 1.00  audience 0.67  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.50 / 4.00 / 3.50   (all 3 samples: 3.67)
headings: h3 5   <- NOT h2, check the unit list
on threshold: none
splits: audience[2] 1/1/0  audience[3] 0/1/1  prior_art[6] 1/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): useful for CRC, AES-GCM, parsing, bit manipulation, …
candidate 2 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

## audience - grade 0.67 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/0  -> 0.67
  [3] Motivating example                           0/1/1  -> 0.67
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): useful for CRC, AES-GCM, parsing, bit manipulation, …
candidate 2 (found by 2 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

## prior_art - grade 1.00 (fired in 5 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             1/1/1  -> 1.00
  [5] Proposed design                              1/1/1  -> 1.00
  [6] Implementation and wording                   1/1/0  -> 0.67
candidate 1 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.
candidate 2 (found by 3 of 18 passes): `clmul` names used because it is most common (Intel, LLVM, RV64, etc.)
candidate 3 (found by 2 of 18 passes): Marked rows are integrated in this proposal.
candidate 4 (found by 1 of 18 passes): widespread hardware support (x86_64, ARM, RISC-V)

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

-->
