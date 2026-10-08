Verdict: Adequate (7/14)

The paper offers a reasonably clear motivation for the proposed `lookup` member functions and points to concrete prior art and an implementation, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest support concerns why this belongs in the standard library rather than remaining a library facility, and how it would coordinate with existing or planned container APIs.

- The strongest support is the explanation of the practical shortcomings of `operator[]` and the simplification the proposed functions would provide.
- The paper also establishes relevant prior art in other languages and in Folly, and provides an implementation with tests and examples.
- The most glaring omission is the absence of any argument for why a library solution would not suffice, leaving the need for standardization itself unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 6.50 / 7.00 / 6.50   (all 3 samples: 6.67)
headings: h2 10
on threshold: implementation
splits: audience[8] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Feature                           1/1/1  -> 1.00
  [6] 5 Before and After Comparisons               1/1/1  -> 1.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This operator cannot be used, however, when 1) the container is `const` , 2) the mapped type is not default constructible, 3) the default-constructed value is inappropriate for the context, or 4) the container should not be modified.
candidate 2 (found by 3 of 33 passes): Unfortunately, the index operator in the C++ associative containers has a number of shortcomings compared to many other languages.
candidate 3 (found by 3 of 33 passes): The following table shows how operations are simplified using the proposed new member functions.
candidate 4 (found by 2 of 33 passes): What’s desired is a simple expression that, given a key, returns the mapped value if the key exists in a specific map and a user-supplied *alternative value* if the key does not exist.

## audience - grade 0.67 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Feature                           0/0/0  -> 0.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    0/0/0  -> 0.00
  [8] 7 Implementation Experience                  1/2/1  -> 1.33
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Feature                           2/2/2  -> 2.00
  [6] 5 Before and After Comparisons               0/0/0  -> 0.00
  [7] 6 Alternatives Considered                    2/2/2  -> 2.00
  [8] 7 Implementation Experience                  1/1/1  -> 1.00
  [9] 8 Wording                                    0/0/0  -> 0.00
  [10] 9 Acknowledgments                            0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Taking inspiration from other languages, especially Python, this paper proposes the addition (in C++29) of a `lookup` member function
candidate 2 (found by 3 of 33 passes): In this paper, I propose `lookup` member functions for `std::map` , `std::unordered_map` , and `std::flat_map` similar to the `get` member in Python dictionaries.
candidate 3 (found by 3 of 33 passes): Since that change does not directly relate to the subject of this proposal, there is no reason to combine it with this paper.
candidate 4 (found by 3 of 33 passes): Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.

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
