Verdict: Adequate to Strong (7/14)

The paper gives real support in a few areas—most clearly in showing that the problem matters, that existing alternatives are limited, and that the proposed facility has working implementation experience—but much of the standardization rationale is asserted rather than demonstrated. The thinnest support concerns why this belongs in the standard rather than remaining a library idiom, since the paper itself points to Mp11 as a mature existing solution without showing why standardizing a narrower type-list design is necessary.

- The strongest support is the demonstration of implementation experience, with a working repository and specific compiler version coverage.
- The paper also establishes that current concept-constraint approaches can be hard to understand and error-prone at scale, and that fold-expanded constraints are only a partial alternative.
- The most glaring omission is the lack of an established case for why a standard library facility is needed when the paper acknowledges Mp11 already makes the idiom possible.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 7.17   max 9.33

## SUMMARY
grades: motivation 1.67  audience 0.17  prior_art 1.50  vehicle 0.83  coordination 0.17  insufficiency 0.50  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.50 / 6.00   (all 3 samples: 6.83)
headings: h2 8
on threshold: motivation, prior_art, vehicle, implementation
splits: motivation[5] 1/2/1  audience[4] 0/1/0  vehicle[4] 2/2/1  coordination[4] 1/0/0
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
candidate 3 (found by 3 of 27 passes): However, this paper proposes type lists that are able to merge under a new type list, while cutting compile time checking for types mentioned more than once at definition and cutting the duplications out.

## audience - grade 0.17 (fired in 1 of 9 sections, strong in 0)
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

## prior_art - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    0/0/0  -> 0.00
  [5] Design decisions                             2/2/2  -> 2.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Concept constraints can be written by using the std::is_same_v tool, however the compile time logic is hard to understand, and at times, are error-prone at scale.
candidate 2 (found by 2 of 27 passes): This paper proposes type lists that are able to merge under a new type list, while cutting compile time checking for types mentioned more than once at definition and cutting the duplications out.
candidate 3 (found by 1 of 27 passes): As mentioned earlier, fold-expanded constraints are simple to write, they are very good for simple flat type lists, which I recommend in this case.

## vehicle - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Impact on standard                           0/0/0  -> 0.00
  [4] Prior art                                    2/2/1  -> 1.67
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
  [4] Prior art                                    1/0/0  -> 0.33
  [5] Design decisions                             0/0/0  -> 0.00
  [6] Proposed wording                             0/0/0  -> 0.00
  [7] Future directions                            0/0/0  -> 0.00
  [8] Acknowledgements                             0/0/0  -> 0.00
  [9] Appendix                                     0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This library does not address the problem of named, reusable, and mergeable type lists as a user-facing vocabulary for concept authoring.

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): This library does not address the problem of named, reusable, and mergeable type lists as a user-facing vocabulary for concept authoring.
candidate 2 (found by 1 of 27 passes): This proposal standardizes the idiom that Mp11 makes possible.

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
candidate 2 (found by 3 of 27 passes): Clang 15+, GCC 12+, MSVC 19.3+ [Github implementation repository](https://github.com/progress-3325/tagging/tree/main)

-->
