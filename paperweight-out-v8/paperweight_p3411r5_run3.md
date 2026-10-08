Verdict: Adequate to Strong (8/14)

The paper offers a mixed case for standardization, with its strongest material concentrated in implementation experience, prior art, and a clear statement of the compilation-time and API-design problem it addresses. The support becomes much thinner when the paper turns to the questions most specific to standardization: why this belongs in the standard, why a library cannot suffice, and who exactly is affected.

- The paper most convincingly establishes implementation experience through reference implementations, a proof-of-concept link, and the existing range-v3 implementation with equivalent semantics.
- It also establishes meaningful prior art and alternatives by situating `any_view` alongside existing type-erasure facilities and Barry Revzin’s related design discussion.
- The paper claims but does not establish who is affected, since the benchmark description and range-v3 reference do not by themselves demonstrate the breadth or severity of the problem for the C++ community.
- The most glaring omission is the absence of any established argument for why the standard is the right venue or why a library solution would not be adequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.00/14)

Provisionally addressed: 5 of 7. Provisional points: 8.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.00   corroborated 8.00   accumulate 8.00   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 70 of 77 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.00 / 8.50 / 8.50   (all 3 samples: 8.00)
headings: h2 10
on threshold: coordination
splits: motivation[3] 1/0/0  motivation[5] 0/1/0  motivation[7] 1/0/0  audience[8] 0/2/2
        audience[9] 0/1/1  prior_art[4] 2/2/1  prior_art[5] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/0/0  -> 0.33
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 0/1/0  -> 0.33
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 1/0/0  -> 0.33
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 2 (found by 3 of 33 passes): Due to the lack of type erasure utilities, typically the API takes a `vector`, even though the implementation only needs to iterate once over the elements.
candidate 3 (found by 1 of 33 passes): This paper proposes a new type-erased view: `std::ranges::any_view`.
candidate 4 (found by 1 of 33 passes): Designing a type like `any_view` raises a lot of questions.

## audience - grade 1.00 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/2/2  -> 1.33
  [9] 8 Implementation Experience                  0/1/1  -> 0.67
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The following benchmarks were compiled with clang 20 with libc++, with -O3, run on APPLE M4 MAX CPU with 16 cores.
candidate 2 (found by 2 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/1  -> 1.67
  [5] 4 Design Space and Prior Art                 0/2/2  -> 1.33
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This is inspired by Barry’s [blog post](https://brevzin.github.io/c++/2019/12/02/named-arguments/).
candidate 2 (found by 3 of 33 passes): `range-v3` uses the name `category` for the category enumeration type. However, the authors believe that the name `std::ranges::category` is too general and it should be reserved for more general purpose utility in ranges library.
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.
candidate 4 (found by 2 of 33 passes): `std::string_view` `std::function` and `std::function_ref`, and `std::any` are the type-erased facilities for the examples above.

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): As a type intended to exist at ABI boundaries, ensuring the ABI stability of `any_view` is extremely important.

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 4 of 11 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  2/2/2  -> 2.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                2/2/2  -> 2.00
candidate 1 (found by 3 of 33 passes): An implementation of this approach would look like this: [link](https://godbolt.org/z/qdnoE7Mb9)
candidate 2 (found by 3 of 33 passes): Both of our two reference implementations have proper `constexpr` support.
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.
candidate 4 (found by 3 of 33 passes): [ours] Hui Xie, S. Levent Yilmaz, and Dionne Louis. A proof-of-concept implementation of any_view. https://github.com/huixie90/cpp_papers/tree/main/impl/any_view

-->
