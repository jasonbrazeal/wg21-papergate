Verdict: Adequate to Strong (7/14)

The paper gives a partial account of why the change is worth considering, with its strongest material concentrated in the motivation and the existence of prior and current implementations. The case becomes much thinner when it turns to who is actually affected, why the standard is the right venue, and how the change would fit with existing practice.

- The paper clearly establishes that the current behavior is surprising and that the proposed shape has implementation experience in major standard libraries.
- It also establishes relevant prior art by pointing to the adopted form in P2781R5 and to similar external fixed-string types.
- The claim that Boost.Mp11 users are affected is asserted through a single implementation detail rather than demonstrated as a practical or widespread problem.
- The paper does not establish why a library solution would be insufficient or how the proposal would coordinate with existing specifications and implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.00/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.67   accumulate 7.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 7.00 / 6.00   (all 3 samples: 7.00)
headings: h2 6
on threshold: implementation
splits: motivation[2] 1/1/2  motivation[5] 2/2/0  motivation[6] 1/0/1  audience[3] 2/0/0
        vehicle[5] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/2  -> 1.33
  [3] 2 Usage of constantwrapper                   2/2/2  -> 2.00
  [4] 3 String Support                             2/2/2  -> 2.00
  [5] 4 Future Language Evolution                  2/2/0  -> 1.33
  [6] 5 Proposal                                   1/0/1  -> 0.67
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We think that this change harms the usability of `std::constant_wrapper` for little benefit.
candidate 2 (found by 3 of 21 passes): It is fairly surprising that this doesn’t work.
candidate 3 (found by 3 of 21 passes): Now, it is true that string support in C++26 template arguments is still weak.
candidate 4 (found by 2 of 21 passes): That would be pretty surprising also, so instead we specify it this way:

## audience - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   2/0/0  -> 0.67
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Boost.Mp11’s [mp_value](https://github.com/boostorg/mp11/blob/48019a04608c09f09f5baf4b63133f8c54df3758/include/boost/mp11/detail/mp_value.hpp#L18) is implemented like this.

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
candidate 3 (found by 3 of 21 passes): Both libstdc++ and libc++ have already implemented the `std::constant_wrapper` design that we shipped in C++26, and will ship a release with that utility.

## vehicle - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Usage of constantwrapper                   0/0/0  -> 0.00
  [4] 3 String Support                             0/0/0  -> 0.00
  [5] 4 Future Language Evolution                  2/2/0  -> 1.33
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Moreover, removing the string literal support from `std::constant_wrapper` doesn’t even prevent using it with strings in the present day.

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
