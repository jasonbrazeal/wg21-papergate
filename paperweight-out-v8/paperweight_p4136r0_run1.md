Verdict: Adequate to Strong (7/14)

The paper gives a reasonably concrete account of the problem and the affected code, but it leaves several parts of the standardization argument underdeveloped, particularly around interoperability and why a library solution cannot address the need.

- The strongest support is the evidence that `#line 0` appears in thousands of real-world uses across major implementations, showing both prevalence and practical impact.
- The discussion of prior art usefully identifies how a previous change narrowed previously tolerated behavior and created implementation divergence.
- The claim that the standard must act because implementations were forced into warnings is asserted rather than demonstrated as a standardization requirement.
- The paper does not address coordination with C or interoperability concerns, and it offers no explanation of why a library-based approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.67   max 8.00

## SUMMARY
grades: motivation 1.50  audience 2.00  prior_art 1.83  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.00 / 7.50   (all 3 samples: 7.00)
headings: h2 9
on threshold: motivation
splits: prior_art[5] 2/1/2  vehicle[5] 0/2/0  implementation[5] 2/0/2  implementation[6] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [6] Solution                                     1/1/1  -> 1.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The restrictions on `#line` do not match existing practices.
candidate 2 (found by 3 of 30 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.
candidate 3 (found by 3 of 30 passes): Given that all implementations use different strategies to represent source locations, which have a significant impact on compiler performance, we cannot reasonably mandate widening the requirements.

## audience - grade 2.00 (fired in 2 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [6] Solution                                     2/2/2  -> 2.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In fact, testing Clang, EDG, GCC, and MSVC,
candidate 2 (found by 3 of 30 passes): I’ve found a few thousands [instances of](https://github.com/search?q=%2F%5C%23line+0%2F+%28language%3AC+OR+language%3AC%2B%2B%29&type=code) `#line` `0`.

## prior_art - grade 1.83 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    2/1/2  -> 1.67
  [6] Solution                                     2/2/2  -> 2.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [P2843R3](https://wg21.link/P2843R3) [1] made the following change.
candidate 2 (found by 3 of 30 passes): This diverges from C - where values outside of [1, 2147483647] are still UB.
candidate 3 (found by 2 of 30 passes): Yet, only EDG diagnoses the first directives, and all implementations accept the second.
candidate 4 (found by 1 of 30 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.

## vehicle - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    0/2/0  -> 0.67
  [6] Solution                                     0/0/0  -> 0.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    0/0/0  -> 0.00
  [6] Solution                                     0/0/0  -> 0.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    0/0/0  -> 0.00
  [6] Solution                                     0/0/0  -> 0.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    2/0/2  -> 1.33
  [6] Solution                                     0/1/0  -> 0.33
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): In fact, testing Clang, EDG, GCC, and MSVC,
candidate 2 (found by 1 of 30 passes): For example, I’ve found a few thousands [instances of](https://github.com/search?q=%2F%5C%23line+0%2F+%28language%3AC+OR+language%3AC%2B%2B%29&type=code) `#line` `0`.

-->
