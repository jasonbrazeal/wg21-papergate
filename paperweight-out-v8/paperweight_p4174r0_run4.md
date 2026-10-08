Verdict: Adequate (6/14)

The paper offers some concrete support for standardization, chiefly through a working implementation and a clear statement of the problem it addresses, but much of the surrounding case is asserted rather than demonstrated. The thinnest support concerns why this belongs in the standard rather than remaining a library facility, and how it would coordinate with existing practice.

- The paper establishes that the problem is real and that a working implementation exists across major compilers.
- It claims relevance and prior art by referencing Mp11, but does not develop the comparison enough to show what standardization would add.
- It asserts that a library alone will not do, yet the reasoning is not established beyond stating that existing libraries do not provide this exact vocabulary.
- The most glaring omission is the lack of an established case for why the standard is the right venue, since the paper itself frames the proposal as standardizing an idiom already made possible by a mature library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 7 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 6.33   accumulate 6.33   max 8.33

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 0.50  vehicle 0.67  coordination 0.17  insufficiency 0.83  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 6.50 / 6.00 / 5.00   (all 3 samples: 5.83)
headings: h2 8
on threshold: motivation, insufficiency, implementation
splits: audience[4] 0/1/0  prior_art[2] 1/1/0  prior_art[7] 1/0/0  vehicle[4] 2/1/1
        coordination[4] 0/1/0  insufficiency[4] 2/1/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    2/2/2  -> 2.00
  [5] Design decisions                             1/1/1  -> 1.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Concept constraints can be written by using the std::is_same_v tool, however the compile time logic is hard to understand, and at times, are error-prone at scale.
candidate 2 (found by 3 of 27 passes): There isn’t a standard library tool that addresses this issue, the closest approximation is a fold-expanded constraint using any_of: template<typename T, typename… Args> concept any_of = (std::is_same_v<T, Args> || …);
candidate 3 (found by 3 of 27 passes): However, this paper proposes type lists that are able to merge under a new type list, while cutting compile time checking for types mentioned more than once at definition and cutting the duplications out.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    0/1/0  -> 0.33
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Mp11 operates on any variadic template, unlike this proposal which operates on its own type list, and is a mature and widely used library.

## prior_art - grade 0.50 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            1/0/0  -> 0.33
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This paper explores the possibility of adding a library addition to <type_traits> to assist the programmer when writing concept constraints.
candidate 2 (found by 1 of 27 passes): An issue that modern concept constraints have is that, despite how simple it is once you implement fold expressions, they have no deduplication logic, concepts aren’t first-class types, and errors will dump every type.
candidate 3 (found by 1 of 27 passes): This paper leaves place for a potential compiler implementation of type lists that could track the ancestry of type lists for subsumption, additionally, it could implement compiler native lookup which could potentially result in a time complexity of O(1).

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    2/1/1  -> 1.33
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This proposal standardizes the idiom that Mp11 makes possible.

## coordination - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    0/1/0  -> 0.33
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This proposal standardizes the idiom that Mp11 makes possible.

## insufficiency - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    2/1/2  -> 1.67
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Mp11 operates on any variadic template, unlike this proposal which operates on its own type list, and is a mature and widely used library.
candidate 2 (found by 1 of 27 passes): This library does not address the problem of named, reusable, and mergeable type lists as a user-facing vocabulary for concept authoring.

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           1/1/1  -> 1.00
  [4] Prior art                                    0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     2/2/2  -> 2.00
candidate 1 (found by 3 of 27 passes): This library works today using GCC, Clang, or MSVC.
candidate 2 (found by 2 of 27 passes): Clang 15+, GCC 12+, MSVC 19.3+ [Github implementation repository](https://github.com/progress-3325/tagging/tree/main)
candidate 3 (found by 1 of 27 passes): [Github implementation repository](https://github.com/progress-3325/tagging/tree/main)

-->
