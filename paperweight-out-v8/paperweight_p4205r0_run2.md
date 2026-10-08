Verdict: Adequate (6/14)

The paper gives a partial account of why range-based searchers would be useful, with concrete implementation experience and some discussion of alternatives, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who is actually affected and why the existing library facilities cannot adequately address the problem.

- The strongest support is the existence of a working implementation in the Beman Project, which shows the proposed API is at least implementable.
- The paper also identifies a real inconsistency in the current `std::ranges::search` interface and points to the existing `std::ranges::less` precedent as a model.
- The discussion of prior art and alternatives is grounded in libc++’s searcher implementation and considers a less invasive overload-based approach.
- The most glaring omission is any identification of the user population affected by the current API, leaving the practical demand for the change unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.00   accumulate 7.00   max 8.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.67  coordination 0.50  insufficiency 0.17  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 6.00 / 6.00   (all 3 samples: 6.33)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: prior_art[1] 0/0/1  vehicle[5] 2/1/1  coordination[3] 0/0/1  coordination[4] 1/1/0
        insufficiency[4] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                1/1/1  -> 1.00
  [5] 4. Design                                    2/2/2  -> 2.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It was originally introduced for more performant specialized searching.
candidate 2 (found by 3 of 27 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.
candidate 3 (found by 3 of 27 passes): There are several peculiarities in this API that make it unsuitable for the Ranges library, thus prompting this proposal to propose new `std::ranges` versions of the standard searchers

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    2/2/2  -> 2.00
  [6] 5. Implementation Experience                 1/1/1  -> 1.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The implementation basically copies libc++'s searcher implementation and modify them to accommodate the new API.
candidate 2 (found by 2 of 27 passes): A possible less invasive change is to reuse the existing searchers, but only update `std::ranges::search` with the new overloads.
candidate 3 (found by 1 of 27 passes): This proposal introduces `std::ranges` versions of the `Searcher` overload of the `std::search` algorithm, which takes a searcher object instead of an iterator pair and (optionally) a predicate.
candidate 4 (found by 1 of 27 passes): There are several peculiarities in this API that make it unsuitable for the Ranges library, thus prompting this proposal to propose new `std::ranges` versions of the standard searchers, similarly to the relation between `std::ranges::less` and `std::less<T>`.

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Design                                    2/1/1  -> 1.33
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The author thinks that requiring the user to write `ranges::search(haystack, boyer_moore_searcher(needle.begin(), needle.end()))` is strictly worse than introducing Range-ified versions of the searchers.
candidate 2 (found by 1 of 27 passes): There are several peculiarities in this API that make it unsuitable for the Ranges library, thus prompting this proposal to propose new `std::ranges` versions of the standard searchers, similarly to the relation between `std::ranges::less` and `std::less<T>`.

## coordination - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/1  -> 0.33
  [4] 3. Motivation                                1/1/0  -> 0.67
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.
candidate 2 (found by 1 of 27 passes): the current Ranges library never included a `std::ranges::search` overload with `Searcher` arguments.

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Revision History                          0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                1/0/0  -> 0.33
  [5] 4. Design                                    0/0/0  -> 0.00
  [6] 5. Implementation Experience                 0/0/0  -> 0.00
  [7] 6. Questions To Resolve                      0/0/0  -> 0.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Current inconsistency in the `std::ranges::search` API forces users to exit the Ranges world to use searchers and resort to using traditional STL algorithms instead, which is undesirable.

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
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
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The author implemented this proposal in [beman.range_searcher](https://github.com/bemanproject/range_searcher) as part of the Beman Project.

-->
