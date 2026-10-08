Verdict: Strong (8/14)

The paper offers solid grounding in implementation experience and a clear rationale for why type-erased views matter, but its case thins considerably when it comes to showing that this belongs in the standard rather than a library. The strongest support is practical and concrete, while the weakest areas are almost entirely asserted rather than demonstrated.

- The paper convincingly establishes that `any_view` addresses a real problem and that working implementations already exist, including prior art in range-v3.
- It shows familiarity with existing type-erasure facilities and alternative designs, giving the proposal a reasonable foundation in prior practice.
- The argument for why this must be standardized, rather than shipped as a library, is left essentially unstated.
- The paper does not establish who is actually affected, why standardization is necessary, or how the proposed facility would coordinate with existing ABI and interoperability concerns.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.67   accumulate 8.50   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.33  coordination 1.17  insufficiency 0.00  implementation 2.00
sample agreement: 70 of 77 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.00 / 7.50 / 8.50   (all 3 samples: 8.33)
headings: h2 10
on threshold: coordination
splits: motivation[7] 0/1/1  audience[4] 1/0/0  audience[8] 2/0/0  prior_art[4] 2/2/1
        vehicle[4] 1/0/1  coordination[4] 0/0/1  implementation[11] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/1/1  -> 0.67
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 2 (found by 2 of 33 passes): The majority of the use case of `any_view` is to use it as a function parameter in the API boundary.
candidate 3 (found by 2 of 33 passes): Due to the lack of type erasure utilities, typically the API takes a `vector`, even though the implementation only needs to iterate once over the elements.
candidate 4 (found by 1 of 33 passes): While such use of ranges is exceedingly convenient, it has the drawback of leaking implementation details into the interface.

## audience - grade 0.83 (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/0/0  -> 0.33
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                2/0/0  -> 0.67
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.
candidate 2 (found by 1 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 3 (found by 1 of 33 passes): The following benchmarks were compiled with clang 20 with libc++, with -O3, run on APPLE M4 MAX CPU with 16 cores.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/1  -> 1.67
  [5] 4 Design Space and Prior Art                 2/2/2  -> 2.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `std::string_view` `std::function` and `std::function_ref`, and `std::any` are the type-erased facilities for the examples above.
candidate 2 (found by 3 of 33 passes): Boost.Range ranges are `copyable`, `borrowed_range` and `common_range`. `sized_range` and `range_rvalue_reference_t` are not considered in the design.
candidate 3 (found by 3 of 33 passes): This is inspired by Barry’s [blog post](https://brevzin.github.io/c++/2019/12/02/named-arguments/).
candidate 4 (found by 3 of 33 passes): `range-v3` uses the name `category` for the category enumeration type. However, the authors believe that the name `std::ranges::category` is too general and it should be reserved for more general purpose utility in ranges library.

## vehicle - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 1/0/1  -> 0.67
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): In this paper, we propose to extend the standard library with `std::ranges::any_view`, which provides a convenient and generalized type-erasure facility to hold any object of any type that satisfies the `ranges::view` concept itself.

## coordination - grade 1.17 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/1  -> 0.33
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): As a type intended to exist at ABI boundaries, ensuring the ABI stability of `any_view` is extremely important.
candidate 2 (found by 1 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
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
  [11] 10 References                                0/2/0  -> 0.67
candidate 1 (found by 3 of 33 passes): An implementation of this approach would look like this: [link](https://godbolt.org/z/qdnoE7Mb9)
candidate 2 (found by 3 of 33 passes): Both of our two reference implementations have proper `constexpr` support.
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.
candidate 4 (found by 1 of 33 passes): [ours] Hui Xie, S. Levent Yilmaz, and Dionne Louis. A proof-of-concept implementation of any_view. https://github.com/huixie90/cpp_papers/tree/main/impl/any_view

-->
