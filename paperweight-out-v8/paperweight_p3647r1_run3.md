Verdict: Weak to Adequate (4/14)

The paper gestures toward real use cases and existing hardware practice, but it does not develop those gestures into a case for standardization. The support is thinnest where the proposal needs to explain why the standard, rather than a library or existing intrinsic, is the right home for the facility.

- The strongest support is the mention of simdjson as a concrete user of the technique, though even that is only asserted rather than demonstrated.
- The paper claims broad hardware support and common naming, but it does not show how those facts bear on the need for a C++ standard facility.
- The paper does not establish why a library cannot provide what is proposed, nor what coordination or interoperability concerns standardization would address.
- The most glaring omission is the absence of any argument for why the C++ standard itself should adopt the facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.67   accumulate 4.50   max 4.00

## SUMMARY
grades: motivation 1.17  audience 0.33  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.00 / 4.00 / 3.50   (all 3 samples: 3.50)
headings: h3 5   <- NOT h2, check the unit list
on threshold: none
splits: motivation[3] 1/2/1  audience[3] 0/1/1
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivating example                           1/2/1  -> 1.33
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): useful for CRC, AES-GCM, parsing, bit manipulation, …
candidate 2 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

## audience - grade 0.33 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivating example                           0/1/1  -> 0.67
  [4] Hardware support                             0/0/0  -> 0.00
  [5] Proposed design                              0/0/0  -> 0.00
  [6] Implementation and wording                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.

## prior_art - grade 1.00 (fired in 5 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivating example                           1/1/1  -> 1.00
  [4] Hardware support                             1/1/1  -> 1.00
  [5] Proposed design                              1/1/1  -> 1.00
  [6] Implementation and wording                   1/1/1  -> 1.00
candidate 1 (found by 3 of 18 passes): widespread hardware support (x86_64, ARM, RISC-V)
candidate 2 (found by 3 of 18 passes): This technique is used to accelerate string parsing in `simdjson`.
candidate 3 (found by 3 of 18 passes): Marked rows are integrated in this proposal.
candidate 4 (found by 3 of 18 passes): `clmul` names used because it is most common (Intel, LLVM, RV64, etc.)

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
