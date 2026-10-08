Verdict: Adequate to Strong (8/14)

The paper offers a reasonably solid empirical and historical basis for treating the `#line` restriction as a real problem, but its argument for why this needs a standard change rather than some other remedy is largely asserted rather than demonstrated. The strongest material concerns observed implementation behavior and existing code, while the thinnest concerns coordination with C, interoperability, and the impossibility of a library solution.

- The paper establishes that the current restriction conflicts with widespread existing practice, with concrete evidence of thousands of `#line 0` uses across major implementations.
- It also establishes that implementations have already diverged in how they handle the affected directives, supporting the claim that the standard’s previous UB served as a de facto extension point.
- The paper does not establish coordination or interoperability considerations, leaving unexamined how the proposed change would interact with C or with other tooling.
- The claim that a library solution cannot address the problem is repeated but not substantiated, and the case for standardization itself rests on the same unsupported assertion.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.67   accumulate 8.17   max 8.67

## SUMMARY
grades: motivation 1.50  audience 2.00  prior_art 1.83  vehicle 0.33  coordination 0.00  insufficiency 0.17  implementation 1.67
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 8.50 / 8.00   (all 3 samples: 7.50)
headings: h2 10
on threshold: motivation, implementation
splits: prior_art[4] 1/0/1  prior_art[6] 1/2/2  vehicle[6] 0/2/0  insufficiency[6] 0/0/1
        implementation[6] 1/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## prior_art - grade 1.83 (fired in 3 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   1/0/1  -> 0.67
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    1/2/2  -> 1.67
  [7] Solution                                     2/2/2  -> 2.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This diverges from C - where values outside of [1, 2147483647] are still UB.
candidate 2 (found by 2 of 33 passes): [P2843R3](https://wg21.link/P2843R3) [1] made the following change.
candidate 3 (found by 2 of 33 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.
candidate 4 (found by 1 of 33 passes): Yet, only EDG diagnoses the first directives, and all implementations accept the second.

## vehicle - grade 0.33 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    0/2/0  -> 0.67
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.

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

## insufficiency - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    0/0/1  -> 0.33
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.

## implementation - grade 1.67  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    1/2/2  -> 1.67
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In fact, testing Clang, EDG, GCC, and MSVC,

-->
