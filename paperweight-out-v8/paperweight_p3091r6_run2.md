Verdict: Adequate (7/14)

The paper gives a reasonably clear account of the problem and shows that the proposed `lookup` functions have been implemented and tested, but it leaves the core standardization argument largely unstated. The thinnest support concerns why this belongs in the standard library rather than in a library, and how it would fit with existing or forthcoming facilities.

- The strongest support is the concrete implementation with tests and usage examples, which demonstrates that the design is workable in practice.
- The paper also establishes the motivation well by contrasting the desired expression with the clumsier `find`-based code users must currently write.
- Prior art is adequately identified through Python’s `get` and Meta’s Folly library, though the paper does not fully develop how those inform the proposed design.
- The most glaring omission is the absence of any argument for why the standard is the right place for this functionality, or how it coordinates with related proposals and existing library conventions.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.00   max 7.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 10
on threshold: audience, implementation
splits: motivation[7] 1/0/0  audience[2] 1/0/0  audience[8] 1/2/2  prior_art[7] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Feature                           1/1/1  -> 1.00
  [6] 5 Before and After Comparisons               1/1/1  -> 1.00
  [7] 6 Alternatives Considered                    1/0/0  -> 0.33
  [8] 7 Implementation Experience                  0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): These limitations often force the user to resort to the `find` member function, which returns an iterator that points to a `pair` and typically leads to more complex code having at least one `if` statement and/or duplicate lookup operations.
candidate 2 (found by 3 of 33 passes): Unfortunately, the index operator in the C++ associative containers has a number of shortcomings compared to many other languages.
candidate 3 (found by 3 of 33 passes): What’s desired is a simple expression that, given a key, returns the mapped value if the key exists in a specific map and a user-supplied *alternative value* if the key does not exist.
candidate 4 (found by 3 of 33 passes): The following table shows how operations are simplified using the proposed new member functions.

## audience - grade 1.00 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/0/0  -> 0.33
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Feature                           0/0/0  -> 0.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  1/2/2  -> 1.67
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.
candidate 2 (found by 1 of 33 passes): These limitations often force the user to resort to the `find` member function, which returns an iterator that points to a `pair` and typically leads to more complex code having at least one `if` statement and/or duplicate lookup operations.
candidate 3 (found by 1 of 33 passes): Some of the functionality can be found in Meta’s [Folly] library.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Feature                           2/2/2  -> 2.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    2/2/0  -> 1.33
  [8] 7 Implementation Experience                  1/1/1  -> 1.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In this paper, I propose `lookup` member functions for `std::map` , `std::unordered_map` , and `std::flat_map` similar to the `get` member in Python dictionaries.
candidate 2 (found by 3 of 33 passes): Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.
candidate 3 (found by 2 of 33 passes): Taking inspiration from other languages, especially Python, this paper proposes the addition (in C++29) of a `lookup` member function
candidate 4 (found by 2 of 33 passes): Although such an extension would be useful, it can also be provided through a non-member function that is expected to be in the next revision of [[P1255]] by Steve Downey.

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Feature                           0/0/0  -> 0.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Feature                           0/0/0  -> 0.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Feature                           0/0/0  -> 0.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Feature                           0/0/0  -> 0.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): An implementation, with tests and usage examples, can be found at [https://github.com/phalpern/WG21-halpern/tree/main/P3091-map_lookup/code](https://github.com/phalpern/WG21-halpern/tree/main/P3091-map_lookup/code).

-->
