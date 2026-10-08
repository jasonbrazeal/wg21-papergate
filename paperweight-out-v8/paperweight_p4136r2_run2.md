Verdict: Adequate to Strong (7/14)

The paper gives a reasonably concrete account of the practical problem and of existing implementation behavior, but it leaves the standardization rationale largely implicit. The strongest material concerns real-world usage and compiler divergence, while the case for why a standard change—rather than continued implementation discretion or another mechanism—is needed remains undeveloped.

- The paper establishes that `#line 0` appears widely in real code across major implementations, showing that the affected practice is not hypothetical.
- It also establishes that implementations have treated the former undefined behavior as an extension point and that a prior change inadvertently narrowed that space.
- The discussion of alternatives is thin, resting mainly on the divergence from C and the cited prior change rather than evaluating other ways to address the problem.
- The paper does not establish why standardization is necessary at all, nor does it address coordination with C or explain why a library-level or non-standard solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.00/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 6.67   accumulate 7.67   max 7.67

## SUMMARY
grades: motivation 1.50  audience 2.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 6.50 / 7.50   (all 3 samples: 7.00)
headings: h2 9
on threshold: motivation, implementation
splits: prior_art[4] 0/1/0  prior_art[6] 1/2/2  implementation[6] 2/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [7] Solution                                     1/1/1  -> 1.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The restrictions on `#line` do not match existing practices.
candidate 2 (found by 3 of 30 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.
candidate 3 (found by 3 of 30 passes): Given that all implementations use different strategies to represent source locations, which have a significant impact on compiler performance, we cannot reasonably mandate widening the requirements.

## audience - grade 2.00 (fired in 2 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [7] Solution                                     2/2/2  -> 2.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In fact, testing Clang, EDG, GCC, and MSVC,
candidate 2 (found by 3 of 30 passes): I’ve found a few thousands [instances of](https://github.com/search?q=%2F%5C%23line+0%2F+%28language%3AC+OR+language%3AC%2B%2B%29&type=code) `#line` `0`.

## prior_art - grade 1.83 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    1/2/2  -> 1.67
  [7] Solution                                     2/2/2  -> 2.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.
candidate 2 (found by 3 of 30 passes): This diverges from C - where values outside of [1, 2147483647] are still UB.
candidate 3 (found by 1 of 30 passes): [P2843R3](https://wg21.link/P2843R3) [1] made the following change.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    0/0/0  -> 0.00
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    0/0/0  -> 0.00
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    0/0/0  -> 0.00
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.67  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/1/2  -> 1.67
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Acknowledgments                              0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In fact, testing Clang, EDG, GCC, and MSVC,

-->
