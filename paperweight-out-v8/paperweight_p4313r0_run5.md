Verdict: Strong (8/14)

The paper offers some useful grounding for its proposal, particularly in identifying prior art, acknowledging existing workarounds, and providing a concrete implementation experiment. However, much of the case for standardization rests on general assertions about frequency and demand rather than demonstrated evidence, leaving the argument thin in several important areas.

- The strongest support comes from the implementation experience, where a working example on Godbolt demonstrates the technical approach in practice.
- The discussion of prior art and alternatives is also well established, showing awareness of earlier designs and how this proposal builds on them.
- The weakest support is in showing why a library solution would not suffice, since the paper only asserts that many standalone solutions exist without explaining why they are inadequate.
- The paper also does not establish who is actually affected, relying on a vague claim about high frequency in the wild and a single unquantified mention of the LLVM project.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 7 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 9.00   accumulate 7.83   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 0.17  insufficiency 0.33  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 8.50 / 7.50 / 7.50   (all 3 samples: 7.83)
headings: h2 6
on threshold: audience, implementation
splits: motivation[2] 0/1/0  audience[3] 2/1/2  coordination[3] 1/0/0  insufficiency[3] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/1/0  -> 0.33
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          2/2/2  -> 2.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): A repeated boilerplate code for bitmask behavior can be found with quite high frequency in the wild
candidate 2 (found by 3 of 21 passes): Reverting to using C-style enums means losing the benefits of scoped constants and the type safety provided by C++ `enum class`.
candidate 3 (found by 1 of 21 passes): We propose enabling bitmask operators for enum classes that have a `std::bitmask_type` annotation, to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).

## audience - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                2/1/2  -> 1.67
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): For example, in LLVM project, the same boilerplate code is repeated multiple times.
candidate 2 (found by 1 of 21 passes): A repeated boilerplate code for bitmask behavior can be found with quite high frequency in the wild

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   1/1/1  -> 1.00
  [3] 2 Motivations                                2/2/2  -> 2.00
  [4] 3 Considered alternatives solutions          2/2/2  -> 2.00
  [5] 4 Design                                     2/2/2  -> 2.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): A bitmask solution was proposed by Anthony Williams in 2015: [Using Enum Classes as Bitfields](https://www.justsoftwaresolutions.co.uk/cplusplus/using-enum-classes-as-bitfields.html).
candidate 2 (found by 3 of 21 passes): While std::bitset supports bitwise operations, it is limited in other respects.
candidate 3 (found by 3 of 21 passes): The design builds upon the solution proposed by Andreas Fertig [C++20 Concepts applied - Safe bitmasks using scoped enums] which in itself is an extension to [Using Enum Classes as Bitfields] initially devised by Anthony Williams
candidate 4 (found by 2 of 21 passes): to provide similar behavior to 16.3.3.3.3 [[bitmask.types]](https://wg21.link/bitmask.types).

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

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                1/0/0  -> 0.33
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): A repeated boilerplate code for bitmask behavior can be found with quite high frequency in the wild

## insufficiency - grade 0.33 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Proposal                                   0/0/0  -> 0.00
  [3] 2 Motivations                                1/1/0  -> 0.67
  [4] 3 Considered alternatives solutions          0/0/0  -> 0.00
  [5] 4 Design                                     0/0/0  -> 0.00
  [6] 5 Reference Implementation                   0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): This type of use case is a sought-after feature and has led to the development of many standalone solutions.

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
