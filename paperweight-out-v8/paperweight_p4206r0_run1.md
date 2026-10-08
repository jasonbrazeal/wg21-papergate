Verdict: Adequate (7/14)

The paper offers a narrow but genuine basis for its standardization case, centered on implementation experience and the existence of prior designs, but it leaves several essential questions about affected users, interoperability, and why a library solution is insufficient largely unaddressed. The strongest support is practical and historical, while the thinnest areas are the absence of any demonstrated audience or coordination story.

- The paper establishes that the relevant design has already been implemented in both major standard libraries and in external code, which grounds the discussion in real experience.
- It also establishes that the current shape came from prior standardization work and that alternatives have been considered in earlier proposals.
- The paper claims but does not establish that the standard is the right venue, relying on an observation about string support rather than a full argument.
- It offers no established account of who is affected, how the change coordinates with existing practice, or why a library cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 6
on threshold: vehicle, implementation
splits: motivation[5] 0/1/2  prior_art[5] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Usage of constantwrapper                   2/2/2  -> 2.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  0/1/2  -> 1.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We think that this change harms the usability of `std::constant_wrapper` for little benefit.
candidate 2 (found by 3 of 21 passes): It is fairly surprising that this doesn’t work.
candidate 3 (found by 3 of 21 passes): Now, it is true that string support in C++26 template arguments is still weak.
candidate 4 (found by 3 of 21 passes): That would be pretty surprising also, so instead we specify it this way:

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  0/0/2  -> 0.67
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In [[P2781R5]](https://wg21.link/p2781r5) of the paper, the shape changed significantly in order to support strings, and was eventually adopted in this form:
candidate 2 (found by 3 of 21 passes): For example, [here](https://github.com/mattkretz/vir-reflect-light/blob/main/vir/fixed_string.h) those types are named `fixed_string` and `constexpr_string`.
candidate 3 (found by 3 of 21 passes): Both libstdc++ and libc++ have already implemented the `std::constant_wrapper` design that we shipped in C++26, and will ship a release with that utility.
candidate 4 (found by 1 of 21 passes): [[P0424R2] (String literals as non-type template parameters)](https://wg21.link/p0424r2) proposed making string literals work as constant template arguments by way of implicitly transforming them into static storage duration arrays.

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Moreover, removing the string literal support from `std::constant_wrapper` doesn’t even prevent using it with strings in the present day.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): For example, [here](https://github.com/mattkretz/vir-reflect-light/blob/main/vir/fixed_string.h) those types are named `fixed_string` and `constexpr_string`.
candidate 2 (found by 3 of 21 passes): Both libstdc++ and libc++ have already implemented the `std::constant_wrapper` design that we shipped in C++26, and will ship a release with that utility.

-->
