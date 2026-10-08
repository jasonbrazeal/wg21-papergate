Verdict: Adequate to Strong (8/14)

The paper’s support for its own standardization is largely asserted rather than demonstrated: it repeatedly points to existing practice and jurisdictional constraints, but does not develop those points into a concrete case for why the standard must act. The only area with substantive backing is implementation experience, where the proposal provides a proof of concept and references to real library code.

- The strongest support is the implementation experience, with a compiler-tested proof of concept and a specific mp-units mechanism cited.
- The paper’s claims about prior art and alternatives are thin, since it names libraries but does not show how their workarounds fail or why standardization would improve them.
- The most glaring omission is the absence of a developed argument for why the standard is necessary, beyond the assertion that users cannot implement the bridge themselves.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.00   accumulate 7.67   max 12.67

## SUMMARY
grades: motivation 1.00  audience 0.67  prior_art 1.00  vehicle 1.33  coordination 1.00  insufficiency 0.67  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 8.50 / 7.00 / 7.50   (all 3 samples: 7.67)
headings: h2 5
on threshold: motivation, prior_art, vehicle, coordination
splits: audience[2] 2/1/1  vehicle[3] 1/0/1  insufficiency[2] 2/1/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Proposed Direction                         0/0/0  -> 0.00
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The existence of multiple widely-used libraries implementing exactly this machinery (see Existing Practice below) is evidence that there are real use-cases and that the status quo is encouraging unnecessary duplication.

## audience - grade 0.67 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/1  -> 1.33
  [3] 2 Proposed Direction                         0/0/0  -> 0.00
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Multiple independent, widely-used C++ libraries have been confronted with this problem and have each arrived at their own workaround.

## prior_art - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Proposed Direction                         0/0/0  -> 0.00
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): mp-units, Eigen, and Boost.Units have all independently converged on the same core mechanism: bring std::sqrt into scope and let ADL do the work.

## vehicle - grade 1.33 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Proposed Direction                         1/0/1  -> 0.67
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This proposal cannot be implemented by users and the bridge between the `std` namespace and user-defined namespace must therefore be built from within the Standard Library.
candidate 2 (found by 1 of 18 passes): The core problem outlined here is essentially jurisdictional: the naive solution of overloading the math functions in the `std` namespace is undefined behaviour and the alternative solutions are less satisfactory.
candidate 3 (found by 1 of 18 passes): This is not absolutely necessary to enable the extensibility of math functions, but offers several advantages:
candidate 4 (found by 1 of 18 passes): This also seems to follow recent precedents such as std::ranges::sort alongside std::sort.

## coordination - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Proposed Direction                         0/0/0  -> 0.00
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Multiple independent, widely-used C++ libraries have been confronted with this problem and have each arrived at their own workaround.

## insufficiency - grade 0.67 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/1  -> 1.33
  [3] 2 Proposed Direction                         0/0/0  -> 0.00
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): This proposal cannot be implemented by users and the bridge between the `std` namespace and user-defined namespace must therefore be built from within the Standard Library.
candidate 2 (found by 1 of 18 passes): The core problem outlined here is essentially jurisdictional: the naive solution of overloading the math functions in the `std` namespace is undefined behaviour and the alternative solutions are less satisfactory.

## implementation - grade 2.00  [binary: max] (fired in 2 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Proposed Direction                         2/2/2  -> 2.00
  [4] 3 Scope of This Proposal                     0/0/0  -> 0.00
  [5] 4 Suggested Polls                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): mp-units adds an explicit member function check. [[mp-units]](https://github.com/mpusz/mp-units/blob/b0e72810b983841b260d570b241c52586aa78999/src/core/include/mp-units/framework/representation_concepts.h#L227-L262)
candidate 2 (found by 2 of 18 passes): A proof of concept compiling under GCC, Clang, and MSVC is available at: [https://godbolt.org/z/cxYTozPrc](https://godbolt.org/z/cxYTozPrc) [[extmath-poc]](https://godbolt.org/z/cxYTozPrc)
candidate 3 (found by 1 of 18 passes): A proof of concept compiling under GCC, Clang, and MSVC is available at: [https://godbolt.org/z/cxYTozPrc](https://godbolt.org/z/cxYTozPrc)

-->
