Verdict: Adequate (6/14)

The paper gives a partial account of why a type-list facility might be useful, but it leaves several central questions about standardization largely unaddressed. The strongest support is practical: the proposal points to a working implementation across major compilers and identifies a real ergonomic gap in writing large concept constraints. The thinnest support concerns the case for putting this in the standard rather than leaving it to existing libraries, since the paper does not establish who is affected, how the feature would coordinate with related facilities, or why a library solution is insufficient.

- The paper establishes implementation experience by citing a repository and confirming compatibility with GCC, Clang, and MSVC.
- The paper establishes the motivating problem by describing the difficulty of maintaining large `std::is_same_v`-based constraints and the absence of a standard tool for merging type lists.
- The paper claims but does not establish that standardization is warranted, since its comparison with Mp11 does not show why a mature library cannot serve the same need.
- The paper does not establish who is affected, leaving the audience and scale of the problem unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 5 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.00   accumulate 7.00   max 7.67

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.33  vehicle 0.50  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 6.50 / 6.50   (all 3 samples: 6.17)
headings: h2 8
on threshold: motivation, implementation
splits: motivation[5] 1/2/1  prior_art[4] 2/0/2  prior_art[5] 0/2/2  insufficiency[4] 2/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    2/2/2  -> 2.00
  [5] Design decisions                             1/2/1  -> 1.33
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Concept constraints can be written by using the std::is_same_v tool, however the compile time logic is hard to understand, and at times, are error-prone at scale.
candidate 2 (found by 3 of 27 passes): There isn’t a standard library tool that addresses this issue, the closest approximation is a fold-expanded constraint using any_of: template<typename T, typename… Args> concept any_of = (std::is_same_v<T, Args> || …);
candidate 3 (found by 2 of 27 passes): However, this paper proposes type lists that are able to merge under a new type list, while cutting compile time checking for types mentioned more than once at definition and cutting the duplications out.
candidate 4 (found by 1 of 27 passes): This paper proposes type lists meant for large scale concept constraints.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    2/0/2  -> 1.33
  [5] Design decisions                             0/2/2  -> 1.33
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Concept constraints can be written by using the std::is_same_v tool, however the compile time logic is hard to understand, and at times, are error-prone at scale.
candidate 2 (found by 2 of 27 passes): Mp11 operates on any variadic template, unlike this proposal which operates on its own type list, and is a mature and widely used library.
candidate 3 (found by 1 of 27 passes): This paper proposes a library approach of type lists, meaning that subsumption is not feasible.
candidate 4 (found by 1 of 27 passes): As mentioned earlier, fold-expanded constraints are simple to write, they are very good for simple flat type lists, which I recommend in this case.

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    1/1/1  -> 1.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This proposal standardizes the idiom that Mp11 makes possible.

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    0/0/0  -> 0.00
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): However, Mp11 is a general-purpose template meta programming toolkit, providing no concept integration, no requires-clause idiom and no method to merge designed for the type categorization use case.
candidate 2 (found by 1 of 27 passes): Mp11 operates on any variadic template, unlike this proposal which operates on its own type list, and is a mature and widely used library.

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
candidate 2 (found by 2 of 27 passes): [Github implementation repository](https://github.com/progress-3325/tagging/tree/main)
candidate 3 (found by 1 of 27 passes): Clang 15+, GCC 12+, MSVC 19.3+ [Github implementation repository](https://github.com/progress-3325/tagging/tree/main)

-->
