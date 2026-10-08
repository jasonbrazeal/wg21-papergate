Verdict: Adequate (6/14)

The paper offers some useful grounding in existing practice and implementation work, but it leaves much of the case for standardization asserted rather than demonstrated. The thinnest support concerns the actual need for a standard library solution rather than a library-based one, and the paper does not establish who would be affected or why the current state is sufficiently problematic to warrant committee action.

- The strongest support is the implementation experience, since the author has produced a working version in the Beman Project.
- The paper also establishes prior art and alternatives by documenting the absence of searcher overloads in Boost.Ranges and range-v3, and by describing a less invasive possible change.
- The paper claims but does not establish why the inconsistency matters or who is affected beyond the author’s own implementation.
- The most glaring omission is the absence of any argument for why a library cannot adequately address the problem, leaving the case for standardization incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.67   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 1.17  audience 0.17  prior_art 2.00  vehicle 0.17  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 5.50 / 6.50   (all 3 samples: 6.17)
headings: h2 10
on threshold: implementation
splits: motivation[5] 2/1/1  audience[6] 0/0/1  prior_art[1] 1/0/0  vehicle[5] 0/0/1
        coordination[3] 2/1/1
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                1/1/1  -> 1.00
  [5] 4. Design                                    2/1/1  -> 1.33
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): It was originally introduced for more performant specialized searching.
candidate 2 (found by 3 of 33 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.
candidate 3 (found by 3 of 33 passes): There are several peculiarities in this API that make it unsuitable for the Ranges library, thus prompting this proposal to propose new `std::ranges` versions of the standard searchers

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/1  -> 0.33
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): The author implemented this proposal in [beman.range_searcher](https://github.com/bemanproject/range_searcher) as part of the Beman Project.

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/0/0  -> 0.33
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                2/2/2  -> 2.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    2/2/2  -> 2.00
  [6] 5. Implementation Experience                 1/1/1  -> 1.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): the `Searcher` overload is never included in either Boost.Ranges or range-v3, and as a result, the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.
candidate 2 (found by 3 of 33 passes): A possible less invasive change is to reuse the existing searchers, but only update `std::ranges::search` with the new overloads.
candidate 3 (found by 3 of 33 passes): The implementation basically copies libc++'s searcher implementation and modify them to accommodate the new API.
candidate 4 (found by 1 of 33 passes): This proposal introduces `std::ranges` versions of the `Searcher` overload of the `std::search` algorithm, which takes a searcher object instead of an iterator pair and (optionally) a predicate.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/1  -> 0.33
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): The author thinks that requiring the user to write `ranges::search(haystack, boyer_moore_searcher(needle.begin(), needle.end()))` is strictly worse than introducing Range-ified versions of the searchers.

## coordination - grade 0.67 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                2/1/1  -> 1.33
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.
candidate 2 (found by 1 of 33 passes): the `Searcher` overload is never included in either Boost.Ranges or range-v3, and as a result, the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 2/2/2  -> 2.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The author implemented this proposal in [beman.range_searcher](https://github.com/bemanproject/range_searcher) as part of the Beman Project.

-->
