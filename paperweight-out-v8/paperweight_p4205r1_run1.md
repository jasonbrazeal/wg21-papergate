Verdict: Adequate (7/14)

The paper offers solid grounding in implementation experience and a clear account of the problem and available alternatives, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who is actually affected, why a library solution would be insufficient, and how the proposed facility would coordinate with existing practice.

- The strongest support is the existence of a working implementation in the Beman Project, along with evidence that making the searchers constexpr-compatible is feasible across major standard libraries.
- The paper clearly explains the motivating inconsistency in the Ranges API and identifies the less invasive alternative of only adding new `std::ranges::search` overloads.
- The case for standardization itself rests mainly on the author’s preference for Range-ified searchers, without showing that the current escape hatch is broadly burdensome.
- The paper does not establish who is affected by the current API gap or why a library-level solution would not address the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 5.67   accumulate 7.33   max 8.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.67  vehicle 1.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 77 section-criterion pairs unanimous (88%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.67)
headings: h2 10
on threshold: motivation, prior_art, implementation
splits: motivation[4] 2/1/1  prior_art[1] 0/1/0  prior_art[3] 2/2/0  prior_art[4] 0/1/0
        prior_art[8] 1/0/0  vehicle[4] 0/1/1  vehicle[5] 1/1/2  coordination[3] 1/0/1
        implementation[5] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                2/1/1  -> 1.33
  [5] 4. Design                                    2/2/2  -> 2.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): It was originally introduced for more performant specialized searching.
candidate 2 (found by 3 of 33 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.
candidate 3 (found by 3 of 33 passes): There are several peculiarities in this API that make it unsuitable for the Ranges library, thus prompting this proposal to propose new `std::ranges` versions of the standard searchers

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## prior_art - grade 1.67 (fired in 6 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/0  -> 0.33
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                2/2/0  -> 1.33
  [4] 3. Motivation                                0/1/0  -> 0.33
  [5] 4. Design                                    2/2/2  -> 2.00
  [6] 5. Implementation Experience                 1/1/1  -> 1.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   1/0/0  -> 0.33
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The implementation basically copies libc++'s searcher implementation and modify them to accommodate the new API.
candidate 2 (found by 2 of 33 passes): A possible less invasive change is to reuse the existing searchers, but only update `std::ranges::search` with the new overloads.
candidate 3 (found by 1 of 33 passes): This proposal introduces `std::ranges` versions of the `Searcher` overload of the `std::search` algorithm, which takes a searcher object instead of an iterator pair and (optionally) a predicate.
candidate 4 (found by 1 of 33 passes): the standard `boyer_moore_searcher` implements the [Boyer-Moore String Search Algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm), which can achieve a worst-case running time of `O(N + S)` instead

## vehicle - grade 1.00 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/1/1  -> 0.67
  [5] 4. Design                                    1/1/2  -> 1.33
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.
candidate 2 (found by 2 of 33 passes): The author thinks that requiring the user to write `ranges::search(haystack, boyer_moore_searcher(needle.begin(), needle.end()))` is strictly worse than introducing Range-ified versions of the searchers.
candidate 3 (found by 1 of 33 passes): There are several peculiarities in this API that make it unsuitable for the Ranges library, thus prompting this proposal to propose new `std::ranges` versions of the standard searchers, similarly to the relation between `std::ranges::less` and `std::less<T>`.

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                1/0/1  -> 0.67
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Unfortunately, perhaps due to its late entrance to the standard, the `Searcher` overload is never included in either Boost.Ranges or range-v3, and as a result, the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/0/1  -> 0.33
  [6] 5. Implementation Experience                 2/2/2  -> 2.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The author implemented this proposal in [beman.range_searcher](https://github.com/bemanproject/range_searcher) as part of the Beman Project.
candidate 2 (found by 1 of 33 passes): After investigating the current implementation of searchers among libstdc++, libc++ and MSVC STL, it seems that there is no inherent difficulty in making standard non-trivial searchers constexpr-compatible.

-->
