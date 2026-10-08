Verdict: Weak (3/14)

The paper offers only partial support for its own standardization, with the strongest grounding in its relationship to existing proposals and standards, but it leaves several essential parts of the case largely unargued. The thinnest areas are the absence of any account of who is affected, how the feature would interoperate with existing practice, why a library solution is insufficient, and whether anyone has actually implemented the idea.

- The paper does establish that the proposal builds on prior work and aligns with existing specifications for square root behavior.
- The paper claims but does not establish why the ergonomic problem matters or why standardization is the right remedy.
- The paper does not establish who is affected by the problem or what implementation experience exists.
- The paper does not address coordination and interoperability or why a library would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.67   accumulate 3.33   max 4.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.50  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 3.00 / 2.50   (all 3 samples: 2.83)
headings: h2 5
on threshold: motivation, prior_art
splits: vehicle[3] 1/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Changing rounding modes, for example for calculations that require correct rounding in a set of optimized expression evaluations, is unergonomic.

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

## vehicle - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/0  -> 0.67
  [4] 2. Design considerations                     0/0/0  -> 0.00
  [5] 3. Wording                                   0/0/0  -> 0.00
  [6] 4. References and bibliography               0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This solves problem 1 directly by providing a more ergonomic way of expressing intention: the client can explicitly state that they require correctly rounded calculation without having to ensure that the floating-point state is set appropriately.

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
