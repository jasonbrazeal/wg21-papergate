Verdict: Adequate to Strong (7/14)

The paper offers a reasonably concrete empirical basis for treating the current `#line` restrictions as out of step with practice, but it does not carry that evidence through to the standardization-specific questions that would justify changing the standard. The strongest material concerns prevalence and divergence from C, while the argument becomes much thinner when it turns to why the standard must act and what the coordinated outcome should be.

- The paper establishes that `#line 0` and similar values appear in real code across major implementations, so the affected population is not hypothetical.
- It also establishes that the standard’s current treatment conflicts with prior extension behavior and with C, giving the problem a clear standards context.
- The paper claims but does not establish that the change must be made in the C++ standard rather than through implementation documentation or other means.
- It offers no account of coordination with C or among implementations, and no explanation of why a library-level or non-normative solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.00/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.50   max 8.33

## SUMMARY
grades: motivation 1.50  audience 2.00  prior_art 1.83  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 6.00 / 7.50   (all 3 samples: 7.00)
headings: h2 10
on threshold: motivation
splits: prior_art[6] 2/1/2  vehicle[6] 2/0/2
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

## prior_art - grade 1.83 (fired in 2 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/1/2  -> 1.67
  [7] Solution                                     2/2/2  -> 2.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This diverges from C - where values outside of [1, 2147483647] are still UB.
candidate 2 (found by 2 of 33 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.
candidate 3 (found by 1 of 33 passes): In fact, testing Clang, EDG, GCC, and MSVC,

## vehicle - grade 0.67 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    2/0/2  -> 1.33
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] ■                                          0/0/0  -> 0.00
  [6] ? Line control [cpp.line]                    1/1/1  -> 1.00
  [7] Solution                                     0/0/0  -> 0.00
  [8] Wording approved by EWG                      0/0/0  -> 0.00
  [9] Alternate wording (not proposed)             0/0/0  -> 0.00
  [10] Acknowledgnments                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In fact, testing Clang, EDG, GCC, and MSVC,

-->
