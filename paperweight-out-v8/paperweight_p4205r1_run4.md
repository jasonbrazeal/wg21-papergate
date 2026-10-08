Verdict: Adequate (6/14)

The paper offers some concrete grounding in implementation experience and prior art, but its central rationale for standardization rests largely on assertions about API inconsistency and user inconvenience rather than demonstrated need. The thinnest parts of the case are the absence of any identified affected users and the lack of an argument for why a library solution would be insufficient.

- The strongest support comes from the author’s implementation in the Beman Project and the investigation showing existing searchers can plausibly be made `constexpr`-compatible.
- The paper establishes that neither Boost.Ranges nor range-v3 included a `Searcher` overload, and it documents a considered alternative of reusing existing searchers with updated overloads.
- The claim that users are forced out of the Ranges world is repeated but never tied to concrete users, use cases, or reported experience.
- The paper does not address why a library cannot provide the proposed functionality, leaving the standardization need asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 5 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.67   max 6.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 6.50 / 6.00   (all 3 samples: 6.17)
headings: h2 10
on threshold: implementation
splits: motivation[4] 2/1/1  motivation[5] 1/2/1  prior_art[7] 1/0/0  vehicle[4] 0/0/1
        coordination[5] 0/1/0  implementation[5] 0/2/0
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                2/1/1  -> 1.33
  [5] 4. Design                                    1/2/1  -> 1.33
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

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                2/2/2  -> 2.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    2/2/2  -> 2.00
  [6] 5. Implementation Experience                 1/1/1  -> 1.00
  [7] 6. Questions To Resolve                      1/0/0  -> 0.33
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): the `Searcher` overload is never included in either Boost.Ranges or range-v3, and as a result, the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.
candidate 2 (found by 3 of 33 passes): A possible less invasive change is to reuse the existing searchers, but only update `std::ranges::search` with the new overloads.
candidate 3 (found by 3 of 33 passes): The implementation basically copies libc++'s searcher implementation and modify them to accommodate the new API.
candidate 4 (found by 1 of 33 passes): Should the searchers be templated on range types or iterator/sentinel types? - Resolved ✅ as the proposal switched to use `views::all` to solve lifetime issues.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/1  -> 0.33
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.

## coordination - grade 0.67 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                1/1/1  -> 1.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    0/1/0  -> 0.33
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.
candidate 2 (found by 1 of 33 passes): the `Searcher` overload is never included in either Boost.Ranges or range-v3, and as a result, the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.
candidate 3 (found by 1 of 33 passes): During SG9 review in Brno (2026-06), the author is asked to investigate whether the new range-based searchers can be used with the existing `std::search` algorithm, and whether the existing searchers can be used with `std::ranges::search`.

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
  [5] 4. Design                                    0/2/0  -> 0.67
  [6] 5. Implementation Experience                 2/2/2  -> 2.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Wording for Optional Additional Changes   0/0/0  -> 0.00
  [10] 9. Poll Results                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The author implemented this proposal in [beman.range_searcher](https://github.com/bemanproject/range_searcher) as part of the Beman Project.
candidate 2 (found by 1 of 33 passes): After investigating the current implementation of searchers among [libstdc++](https://github.com/gcc-mirror/gcc/blob/17f084306c68c437b1350682bcde6075ae749f15/libstdc%2B%2B-v3/include/std/functional#L1299), [libc++](https://github.com/llvm/llvm-project/blob/2a00d50e6012e1ee31904d394c088be907b6aa8b/libcxx/include/__functional/boyer_moore_searcher.h#L36) and [MSVC STL](https://github.com/microsoft/STL/blob/020513e211529e7be30cb3e0ca310869701286da/stl/inc/functional#L2881), it seems that there is no inherent difficulty in making standard non-trivial searchers (`boyer_moore_[horspool_]searcher`) `constexpr`-compatible

-->
