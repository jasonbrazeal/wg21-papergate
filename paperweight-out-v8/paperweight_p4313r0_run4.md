Verdict: Strong (8/14)

The paper offers a reasonable foundation for the problem and the design space, but it does not yet make a complete case for standardization. The strongest material concerns the existence of repeated boilerplate, the limitations of alternatives, and a concrete implementation, while the thinnest parts are the lack of evidence about affected users and the absence of any discussion of coordination or interoperability.

- The paper clearly establishes that bitmask boilerplate is common and that C-style enums and `std::bitset` are unsatisfactory alternatives.
- It credits prior work and provides a working implementation, which gives the proposal some practical grounding.
- The claim that many standalone solutions show a need for standardization is asserted but not backed by examples or evidence.
- The paper does not address coordination with existing or forthcoming features, leaving a significant gap in the standardization case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.33   accumulate 7.67   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.50 / 8.00 / 7.50   (all 3 samples: 7.67)
headings: h2 6
on threshold: audience, implementation
splits: motivation[2] 0/1/1  prior_art[5] 2/2/1  prior_art[6] 0/0/1  insufficiency[3] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/1/1  -> 0.67
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          2/2/2  -> 2.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): A repeated boilerplate code for bitmask behavior can be found with quite high frequency in the wild
candidate 2 (found by 3 of 21 passes): Reverting to using C-style enums means losing the benefits of scoped constants and the type safety provided by C++ `enum class`.
candidate 3 (found by 2 of 21 passes): We propose enabling bitmask operators for enum classes that have a `std::bitmask_type` annotation, to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).

## audience - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): For example, in LLVM project, the same boilerplate code is repeated multiple times.

## prior_art - grade 2.00 (fired in 5 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   1/1/1  -> 1.00
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          2/2/2  -> 2.00
  [5] 4 Design                                     2/2/1  -> 1.67
  [6] 5 Reference Implementation                   0/0/1  -> 0.33
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): While std::bitset supports bitwise operations, it is limited in other respects.
candidate 2 (found by 3 of 21 passes): The design builds upon the solution proposed by Andreas Fertig [C++20 Concepts applied - Safe bitmasks using scoped enums](https://andreasfertig.com/blog/2024/01/cpp20-concepts-applied/) which in itself is an extension to [Using Enum Classes as Bitfields](https://www.justsoftwaresolutions.co.uk/cplusplus/using-enum-classes-as-bitfields.html) initially devised by Anthony Williams
candidate 3 (found by 2 of 21 passes): to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).
candidate 4 (found by 2 of 21 passes): A bitmask solution was proposed by Anthony Williams in 2015: [Using Enum Classes as Bitfields](https://www.justsoftwaresolutions.co.uk/cplusplus/using-enum-classes-as-bitfields.html).

## vehicle - grade 0.50 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                1/1/1  -> 1.00
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This type of use case is a sought-after feature and has led to the development of many standalone solutions.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                0/0/0  -> 0.00
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                0/1/0  -> 0.33
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): This type of use case is a sought-after feature and has led to the development of many standalone solutions.

## implementation - grade 2.00  [binary: max] (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                0/0/0  -> 0.00
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   2/2/2  -> 2.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): On godbolt Clang reflection [https://godbolt.org/z/zebW6hGYY](https://godbolt.org/z/zebW6hGYY)

-->
