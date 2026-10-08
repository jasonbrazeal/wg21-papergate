Verdict: Adequate to Strong (6/14)

The paper gives a reasonably clear account of why bitmask boilerplate is a recurring problem and points to concrete prior work, but it leaves several parts of the standardization case largely asserted rather than demonstrated. The thinnest support concerns the need for a standard facility specifically, as opposed to a library solution, and there is no discussion of coordination or interoperability.

- The strongest support is the identification of existing bitmask conventions in the standard and prior designs that the proposal explicitly builds upon.
- The paper establishes that the problem matters by citing widespread boilerplate and the loss of scoped-enum benefits when workarounds are used.
- The claim that many standalone solutions exist is not backed by examples or evidence, weakening the argument that standardization is necessary.
- The most glaring omission is the absence of any case for why a library cannot adequately provide the proposed behavior.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.67   accumulate 6.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 0.67
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 5.50 / 5.00   (all 3 samples: 6.00)
headings: h2 6
on threshold: audience
splits: motivation[2] 1/1/0  audience[3] 2/2/1  implementation[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   1/1/0  -> 0.67
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          2/2/2  -> 2.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): A repeated boilerplate code for bitmask behavior can be found with quite high frequency in the wild
candidate 2 (found by 3 of 21 passes): Reverting to using C-style enums means losing the benefits of scoped constants and the type safety provided by C++ `enum class`.
candidate 3 (found by 1 of 21 passes): We propose enabling bitmask operators for enum classes that have a `std::bitmask_type` annotation, to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).
candidate 4 (found by 1 of 21 passes): to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).

## audience - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                2/2/1  -> 1.67
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): For example, in LLVM project, the same boilerplate code is repeated multiple times.
candidate 2 (found by 1 of 21 passes): A repeated boilerplate code for bitmask behavior can be found with quite high frequency in the wild

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   1/1/1  -> 1.00
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          2/2/2  -> 2.00
  [5] 4 Design                                     1/1/1  -> 1.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We propose enabling bitmask operators for enum classes that have a `std::bitmask_type` annotation, to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).
candidate 2 (found by 3 of 21 passes): A bitmask solution was proposed by Anthony Williams in 2015: [Using Enum Classes as Bitfields](https://www.justsoftwaresolutions.co.uk/cplusplus/using-enum-classes-as-bitfields.html).
candidate 3 (found by 3 of 21 passes): While std::bitset supports bitwise operations, it is limited in other respects.
candidate 4 (found by 2 of 21 passes): The design builds upon the solution proposed by Andreas Fertig [C++20 Concepts applied - Safe bitmasks using scoped enums](https://andreasfertig.com/blog/2024/01/cpp20-concepts-applied/) which in itself is an extension to [Using Enum Classes as Bitfields](https://www.justsoftwaresolutions.co.uk/cplusplus/using-enum-classes-as-bitfields.html) initially devised by Anthony Williams

## vehicle - grade 0.50 (fired in 1 of 7 sections, strong in 0)
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

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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

## implementation - grade 0.67  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                0/0/0  -> 0.00
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   2/0/0  -> 0.67
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): On godbolt Clang reflection [https://godbolt.org/z/zebW6hGYY](https://godbolt.org/z/zebW6hGYY)

-->
