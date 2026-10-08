Verdict: Strong (8/14)

The paper offers solid evidence that the current `#line` restrictions conflict with real-world practice and that implementations have already converged on accepting values the standard does not permit. Its support is thinnest, however, on the institutional questions: why this needs to be fixed in the C++ standard itself, how it coordinates with C, and why the problem cannot be addressed outside the standard.

- The strongest support is the implementation experience, with concrete testing across Clang, EDG, GCC, and MSVC plus evidence of thousands of existing `#line 0` uses.
- The paper also establishes why the issue matters by showing that prior standardization accidentally removed a de facto extension point and forced implementations to warn on accepted practice.
- The prior art and alternatives section is reasonably grounded, citing P2843R3 and the divergence from C as context for the proposed change.
- The most glaring omission is the absence of any case for why the standard is the right venue, including coordination with C or an explanation of why a library or implementation-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 4 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.00   accumulate 8.00   max 8.00

## SUMMARY
grades: motivation 1.50  audience 2.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 7.50 / 7.50   (all 3 samples: 7.50)
headings: h2 9
on threshold: motivation, implementation
splits: audience[2] 0/1/0  implementation[6] 0/0/1
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

## audience - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
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
candidate 3 (found by 1 of 30 passes): The restrictions on `#line` do not match existing practices.

## prior_art - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [6] Solution                                     2/2/2  -> 2.00
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [P2843R3](https://wg21.link/P2843R3) [1] made the following change.
candidate 2 (found by 3 of 30 passes): This diverges from C - where values outside of [1, 2147483647] are still UB.
candidate 3 (found by 2 of 30 passes): Yet, only EDG diagnoses the first directives, and all implementations accept the second. So the standard is overly restrictive.
candidate 4 (found by 1 of 30 passes): So the UB that existed in the standard was used as an extension point by implementations, extension point that we accidentally took away, forcing implementations to emit a warning.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] ■                                          0/0/0  -> 0.00
  [5] ? Line control [cpp.line]                    2/2/2  -> 2.00
  [6] Solution                                     0/0/1  -> 0.33
  [7] Proposed wording                             0/0/0  -> 0.00
  [8] Alternative wording, not favored             0/0/0  -> 0.00
  [9] Acknowledgnments                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In fact, testing Clang, EDG, GCC, and MSVC,
candidate 2 (found by 1 of 30 passes): For example, I’ve found a few thousands [instances of](https://github.com/search?q=%2F%5C%23line+0%2F+%28language%3AC+OR+language%3AC%2B%2B%29&type=code) `#line` `0`.

-->
