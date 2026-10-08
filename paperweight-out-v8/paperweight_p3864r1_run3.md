Verdict: Weak (2/14)

The paper offers some useful grounding in prior work, but it does not yet make a persuasive case that this facility belongs in the C++ standard. The strongest support is the clear lineage from P3375R3, N5014, and ISO/IEC 60559:2020, while the thinnest areas are the absence of any identified affected users, implementation experience, or argument for why a library solution would be insufficient.

- The proposal’s prior-art discussion is its most solid element, showing how the design follows existing specifications and reproducibility efforts.
- The rationale for why this matters and why it belongs in the standard is asserted mainly through a brief ergonomics claim, without demonstrating the practical burden or demand.
- The paper does not identify who would be affected by the change, leaving the audience and impact unclear.
- The most glaring omission is the lack of any implementation experience or evidence that a non-standard library cannot already meet the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 2.33   accumulate 3.00   max 3.67

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 1.50  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 2.50 / 3.00 / 2.00   (all 3 samples: 2.50)
headings: h2 5
on threshold: prior_art
splits: motivation[2] 0/1/0  motivation[3] 2/2/0  vehicle[3] 0/0/1
## END SUMMARY

## motivation - grade 0.83 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1. Introduction                              2/2/0  -> 1.33
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): Changing rounding modes, for example for calculations that require correct rounding in a set of optimized expression evaluations, is unergonomic.
candidate 2 (found by 1 of 18 passes): This paper proposes adding five overload sets to the standard library for addition, subtraction, multiplication, division, and square root calculation, correctly rounded as specified in ISO/IEC 60559:2020.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design considerations                     1/1/1  -> 1.00
  [5] 3. Wording                                   1/1/1  -> 1.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Proposal [[P3375R3]](https://wg21%2elink/p3375r3) seeks to introduce reliable reproducibility to floating-point operations regardless of platform. This proposal partially addresses this problem by reducing the places where implementations can diverge.
candidate 2 (found by 3 of 18 passes): The proposed changes are based on [[N5014]](https://wg21%2elink/n5014).
candidate 3 (found by 2 of 18 passes): This matches the behavior of `sqrt` in typical implementations (although this behavior is not mandated by the C standard), and it matches the behavior specified for **squareRoot**(-0) in [[60559:2020]](https://www%2eiso%2eorg/standard/80985%2ehtml).
candidate 4 (found by 1 of 18 passes): it matches the behavior specified for **squareRoot**(-0) in [[60559:2020]](https://www%2eiso%2eorg/standard/80985%2ehtml).

## vehicle - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/1  -> 0.33
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): This solves problem 1 directly by providing a more ergonomic way of expressing intention: the client can explicitly state that they require correctly rounded calculation without having to ensure that the floating-point state is set appropriately.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidates: (none validated)

-->
