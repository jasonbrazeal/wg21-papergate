Verdict: Adequate to Strong (7/14)

The paper offers a partial but uneven case for its own standardization, with its strongest material concentrated in motivation, prior art, and implementation experience. The thinnest areas are the absence of any identified affected audience and the lack of coordination or interoperability discussion, while the arguments about why the standard is the right venue and why a library solution is insufficient remain asserted rather than demonstrated.

- The paper clearly explains why the current behavior is surprising and why the change matters for usability.
- It grounds the discussion in the adopted P2781R5 design and points to existing implementations in both major standard libraries.
- It does not identify who is affected by the problem or what codebases would benefit from the change.
- It never establishes why the standard must act rather than leaving users to adopt a library type, nor how the change would coordinate with related standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.33   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 7.00 / 7.50   (all 3 samples: 7.17)
headings: h2 6
on threshold: vehicle, implementation
splits: motivation[5] 2/0/2  motivation[6] 2/1/1  prior_art[5] 0/0/2  insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Usage of constantwrapper                   2/2/2  -> 2.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  2/0/2  -> 1.33
  [6] 5 Proposal                                   2/1/1  -> 1.33
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We think that this change harms the usability of `std::constant_wrapper` for little benefit.
candidate 2 (found by 3 of 21 passes): It is fairly surprising that this doesn’t work.
candidate 3 (found by 3 of 21 passes): Now, it is true that string support in C++26 template arguments is still weak.
candidate 4 (found by 2 of 21 passes): We made `std::cw<"eve">` work, at the cost of making the whole type less convenient to use properly, to work around a language limitation.

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
candidate 2 (found by 2 of 21 passes): For example, [here](https://github.com/mattkretz/vir-reflect-light/blob/main/vir/fixed_string.h) those types are named `fixed_string` and `constexpr_string`.
candidate 3 (found by 1 of 21 passes): But such a thing actually gives meaningful string support, with some additional work:
candidate 4 (found by 1 of 21 passes): This would make `std::cw<"eve">` just work directly.

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
candidate 1 (found by 2 of 21 passes): Moreover, removing the string literal support from `std::constant_wrapper` doesn’t even prevent using it with strings in the present day.
candidate 2 (found by 1 of 21 passes): The lack of string support is temporary, and isn’t really solved by the workaround in `std::constant_wrapper` anyway, but the API of `std::constant_wrapper` is permanent.

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
  [5] 4 Future Language Evolution                  0/0/1  -> 0.33
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
