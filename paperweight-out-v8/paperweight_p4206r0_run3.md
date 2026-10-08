Verdict: Adequate to Strong (8/14)

The paper offers a mixed case for its own standardization, with its strongest grounding in prior art and implementation experience, but it leaves several core justifications more asserted than demonstrated. The thinnest areas are the absence of any coordination or interoperability discussion and the underdeveloped arguments for why the standard must act rather than users relying on library-level solutions.

- The paper clearly establishes that the change has real usability costs and that the earlier design, as well as current implementations, provides concrete prior art and implementation experience.
- The claim that a typical use of constant wrapping would be affected is plausible but not backed by concrete examples or user reports.
- The argument that removing string literal support does not prevent string use, and that users can supply their own wrapper types, is asserted without enough detail to show why standardization is necessary.
- The paper provides no discussion of coordination with existing or proposed string facilities or interoperability concerns, leaving a significant gap in the standardization case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 8.00   accumulate 7.50   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.00 / 7.00 / 7.50   (all 3 samples: 7.50)
headings: h2 6
on threshold: vehicle, implementation
splits: motivation[2] 2/1/1  motivation[6] 1/1/2  audience[3] 1/0/1  insufficiency[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/1/1  -> 1.33
  [3] 2 Usage of constantwrapper                   2/2/2  -> 2.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  2/2/2  -> 2.00
  [6] 5 Proposal                                   1/1/2  -> 1.33
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We think that this change harms the usability of `std::constant_wrapper` for little benefit.
candidate 2 (found by 3 of 21 passes): It is fairly surprising that this doesn’t work.
candidate 3 (found by 3 of 21 passes): Now, it is true that string support in C++26 template arguments is still weak.
candidate 4 (found by 2 of 21 passes): We made `std::cw<"eve">` work, at the cost of making the whole type less convenient to use properly, to work around a language limitation.

## audience - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   1/0/1  -> 0.67
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): A fairly typical use of constant wrapping would be:

## prior_art - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   1/1/1  -> 1.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In [[P2781R5]](https://wg21.link/p2781r5) of the paper, the shape changed significantly in order to support strings, and was eventually adopted in this form:
candidate 2 (found by 3 of 21 passes): For example, [here](https://github.com/mattkretz/vir-reflect-light/blob/main/vir/fixed_string.h) those types are named `fixed_string` and `constexpr_string`.
candidate 3 (found by 2 of 21 passes): Both libstdc++ and libc++ have already implemented the `std::constant_wrapper` design that we shipped in C++26, and will ship a release with that utility.
candidate 4 (found by 1 of 21 passes): As a DR against C++26: Revert the `std::constant_wrapper` and `std::cw` design to the R4 shape

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

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  1/0/0  -> 0.33
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): With a suitable `strlit<N>`/`fixed_string<N>` type (or a dynamically typed solution using `std::define_static_string`), users can add a `cstr<"alice">` or `cw_str<"bob">` or however they want to spell it, and get all the functionality with minor cost.

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
