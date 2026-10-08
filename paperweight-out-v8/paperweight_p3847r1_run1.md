Verdict: Adequate to Strong (6/14)

The paper offers solid support on implementation practice and the existence of a concrete defect, but its broader case rests on assertions that are not backed up with evidence, particularly around who is affected and why standardization is the right remedy. The thinnest part is the absence of any discussion of non-standard solutions, which leaves a gap in the argument for why a library approach cannot address the problem.

- The strongest support comes from the reported implementation experience, which indicates that major implementations already follow the proposed ordering and that the paper targets a real defect in the standard’s wording.
- The discussion of prior art and alternatives is also well grounded, since it identifies a plausible analogy and explains why that analogy does not hold.
- The claim that the implementation freedom provides no useful benefits is asserted rather than demonstrated, weakening the argument that standardization is necessary.
- Most glaringly, the paper does not establish why a library will not do, leaving unaddressed a core question about whether the change belongs in the standard at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 5.67   accumulate 6.17   max 8.67

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.50  vehicle 0.17  coordination 0.33  insufficiency 0.00  implementation 1.67
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 6.00 / 5.00 / 7.50   (all 3 samples: 6.17)
headings: h2 4
on threshold: motivation, audience, prior_art, implementation
splits: vehicle[3] 0/0/1  coordination[3] 0/0/2  implementation[3] 2/1/2
        implementation[4] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     1/1/1  -> 1.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): However, it does mean that code like the following is unsafe:
candidate 2 (found by 2 of 15 passes): Specify, as a defect report, that all explicit captures are declared in the order in which they appear, as is existing practice.
candidate 3 (found by 1 of 15 passes): Also repair the defect that [expr.prim.lambda.capture]/15 does not describe initialization for reference *init-capture*s at all if, per /12, there are no members for them.

## audience - grade 1.00 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): tests indicate that all major implementations define members for all non-reference explicit captures (*simple-capture*s and *init-capture*s) in order and then for all implicit captures in order of first capturing appearance.

## prior_art - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     1/1/1  -> 1.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There is precedent in the out-of-order evaluation of *mem-initializer*s, but (aside from those already being a known usability problem) the analogy fails because there is no canonical list of the members elsewhere whose order must be controlling.
candidate 2 (found by 3 of 15 passes): Specify, as a defect report, that all explicit captures are declared in the order in which they appear, as is existing practice.

## vehicle - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/0/1  -> 0.33
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): This implementation freedom does not seem to provide useful benefits.

## coordination - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/0/2  -> 0.67
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): Moreover, the Itanium ABI [intends](https://github.com/itanium-cxx-abi/cxx-abi/issues/141) to specify this order for the layout of closure types.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/0/0  -> 0.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.67  [binary: max] (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/1/2  -> 1.67
  [4] Proposal                                     1/1/0  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): tests indicate that all major implementations define members for all non-reference explicit captures (*simple-capture*s and *init-capture*s) in order and then for all implicit captures in order of first capturing appearance.
candidate 2 (found by 2 of 15 passes): as is existing practice

-->
