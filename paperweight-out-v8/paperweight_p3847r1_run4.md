Verdict: Adequate (6/14)

The paper gives a reasonably concrete account of existing implementation behavior and some relevant precedent, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why a standard change is necessary at all and why the issue cannot be handled outside the standard.

- The strongest support is the implementation-experience evidence that major implementations already define closure members in a consistent order.
- The paper also establishes relevant prior art and an alternative path through a defect report.
- It claims, but does not establish, who is affected or how coordination with the Itanium ABI would work.
- The most glaring omission is the absence of any established reason the standard itself must change, as opposed to relying on existing practice or other mechanisms.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 5.67   accumulate 6.33   max 8.67

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.50  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 6.00 / 6.00   (all 3 samples: 6.33)
headings: h2 4
on threshold: motivation, audience, prior_art, implementation
splits: coordination[3] 2/0/0  implementation[4] 1/0/1
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

## audience - grade 1.00 (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): tests indicate that all major implementations define members for all non-reference explicit captures (*simple-capture*s and *init-capture*s) in order and then for all implicit captures in order of first capturing appearance.

## prior_art - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     1/1/1  -> 1.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): There is precedent in the out-of-order evaluation of *mem-initializer*s, but (aside from those already being a known usability problem) the analogy fails because there is no canonical list of the members elsewhere whose order must be controlling.
candidate 2 (found by 3 of 15 passes): Specify, as a defect report, that all explicit captures are declared in the order in which they appear, as is existing practice.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/0/0  -> 0.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/0/0  -> 0.67
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): the Itanium ABI [intends](https://github.com/itanium-cxx-abi/cxx-abi/issues/141) to specify this order for the layout of closure types.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      0/0/0  -> 0.00
  [4] Proposal                                     0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Problem                                      2/2/2  -> 2.00
  [4] Proposal                                     1/0/1  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): tests indicate that all major implementations define members for all non-reference explicit captures (*simple-capture*s and *init-capture*s) in order and then for all implicit captures in order of first capturing appearance.
candidate 2 (found by 2 of 15 passes): as is existing practice

-->
