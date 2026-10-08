Verdict: Adequate to Strong (7/14)

The paper gives a reasonably concrete account of the problem and of implementation behavior, but it leaves several parts of the standardization case essentially unargued, particularly around why the standard is the right venue and how the change fits with C or other specifications.

- The strongest support is the direct evidence that `#line 0` appears widely in real code and is accepted across Clang, EDG, GCC, and MSVC.
- The paper also establishes that the current wording is more restrictive than existing practice and that P2843R3 accidentally narrowed an extension point.
- The most glaring omission is the absence of any discussion of why standardization is needed here, as opposed to leaving the behavior as an accepted extension or documenting it elsewhere.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 6.00   accumulate 8.00   max 8.00

## SUMMARY
grades: motivation 1.67  audience 2.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 7.50 / 7.00   (all 3 samples: 7.33)
headings: h2 10
on threshold: motivation, prior_art, implementation
splits: motivation[7] 1/2/1  prior_art[6] 2/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [7] Solution                                     1/2/1  -> 1.33
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The restrictions on `#line` do not match existing practices.
candidate 2 (found by 3 of 33 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.
candidate 3 (found by 3 of 33 passes): Given that all implementations use different strategies to represent source locations, which have a significant impact on compiler performance, we cannot reasonably mandate widening the requirements.

## audience - grade 2.00 (fired in 2 of 11 sections, strong in 2)  (SHARED PASSAGE)
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
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In fact, testing Clang, EDG, GCC, and MSVC,
candidate 2 (found by 3 of 33 passes): I’ve found a few thousands [instances of](https://github.com/search?q=%2F%5C%23line+0%2F+%28language%3AC+OR+language%3AC%2B%2B%29&type=code) `#line` `0`.

## prior_art - grade 1.67 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/1/1  -> 1.33
  [7] Solution                                     2/2/2  -> 2.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): [P2843R3](https://wg21.link/P2843R3) [1] made the following change.
candidate 2 (found by 3 of 33 passes): This diverges from C - where values outside of [1, 2147483647] are still UB.
candidate 3 (found by 1 of 33 passes): Yet, only EDG diagnoses the first directives, and all implementations accept the second. So the standard is overly restrictive.
candidate 4 (found by 1 of 33 passes): testing Clang, EDG, GCC, and MSVC,

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In fact, testing Clang, EDG, GCC, and MSVC,

-->
