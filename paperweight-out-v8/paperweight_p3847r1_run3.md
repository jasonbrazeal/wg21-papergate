Verdict: Adequate (6/14)

The paper offers a narrow but real basis for its standardization request, chiefly by showing that the proposed ordering matches existing implementation behavior and has a plausible precedent in the standard’s treatment of related constructs. The support is thinnest around the actual need for normative action: the paper does not identify who is concretely affected, and its claims about implementation freedom, ABI coordination, and the inadequacy of library workarounds are asserted rather than demonstrated.

- The strongest support is the reported implementation experience that all major implementations already define explicit captures in order, which gives the proposal a practical foundation.
- The paper also establishes prior art by pointing to the analogous out-of-order evaluation of mem-initializers and by explaining why that analogy is imperfect.
- The case for why the standard must act is weaker, resting mainly on the unsupported assertion that the current implementation freedom provides no useful benefits.
- The most glaring omission is the absence of any identified user population or concrete harm, leaving unclear who would be helped by standardizing this behavior.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 6 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.33   accumulate 5.83   max 8.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.17  coordination 1.00  insufficiency 0.33  implementation 1.33
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 5.50 / 5.50 / 6.50   (all 3 samples: 5.83)
headings: h2 4
on threshold: motivation, prior_art, coordination
splits: vehicle[3] 0/1/0  insufficiency[3] 1/0/1  implementation[3] 1/1/2
        implementation[4] 0/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     1/1/1  -> 1.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): However, it does mean that code like the following is unsafe:
candidate 2 (found by 3 of 15 passes): It would then be safe to allow *init-capture*s to refer to previous captures (in `[v, size0 = v.size()]`, the captured `v` would have been initialized), but that is not proposed for obvious compatibility reasons.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/0/0  -> 0.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     1/1/1  -> 1.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There is precedent in the out-of-order evaluation of *mem-initializer*s, but (aside from those already being a known usability problem) the analogy fails because there is no canonical list of the members elsewhere whose order must be controlling.
candidate 2 (found by 3 of 15 passes): For simplicity, extend this to reference *simple-capture*s, which can be observed only via implementation-defined reflection extensions ([meta.reflection.member.queries]/2).

## vehicle - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/1/0  -> 0.33
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): This implementation freedom does not seem to provide useful benefits.

## coordination - grade 1.00 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Moreover, the Itanium ABI [intends](https://github.com/itanium-cxx-abi/cxx-abi/issues/141) to specify this order for the layout of closure types.

## insufficiency - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      1/0/1  -> 0.67
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): It is possible but unergonomic to force the ordering:

## implementation - grade 1.33  [binary: max] (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      1/1/2  -> 1.33
  [4] Proposal                                     0/1/1  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): tests indicate that all major implementations define members for all non-reference explicit captures (*simple-capture*s and *init-capture*s) in order and then for all implicit captures in order of first capturing appearance.
candidate 2 (found by 2 of 15 passes): Specify, as a defect report, that all explicit captures are declared in the order in which they appear, as is existing practice.

-->
