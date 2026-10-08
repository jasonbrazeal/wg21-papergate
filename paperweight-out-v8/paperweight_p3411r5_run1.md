Verdict: Strong (9/14)

The paper offers a reasonably grounded case in the areas of motivation, affected users, prior art, and implementation experience, but it leaves the central question of why this belongs in the standard, rather than a library, essentially unargued. The thinnest support is around the need for standardization itself and how the facility would coordinate with existing or future standard components.

- The strongest support comes from the demonstrated implementation experience, including range-v3, a proof-of-concept implementation, and constexpr-capable reference implementations.
- The paper also establishes the practical motivation clearly, particularly the compilation-time costs of template-heavy range APIs and the common use of `any_view` at API boundaries.
- Prior art and alternatives are adequately covered through discussion of `std::span`, range-v3, and the naming divergence from `category`.
- The most glaring omission is the absence of any established argument for why a library solution would be insufficient, leaving the standardization rationale largely asserted rather than shown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 8.67   accumulate 9.00   max 10.67

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 0.33  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 9.00 / 9.00 / 9.00   (all 3 samples: 9.00)
headings: h2 10
on threshold: audience, coordination
splits: motivation[3] 1/0/0  motivation[5] 1/0/1  audience[9] 1/2/1  prior_art[8] 0/2/2
        vehicle[4] 1/0/1  implementation[11] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/0/0  -> 0.33
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 1/0/1  -> 0.67
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 1/1/1  -> 1.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 2 (found by 3 of 33 passes): Due to the lack of type erasure utilities, typically the API takes a `vector`, even though the implementation only needs to iterate once over the elements.
candidate 3 (found by 2 of 33 passes): In Wrocław meeting, one important point was made: The majority of the use case of `any_view` is to use it as a function parameter in the API boundary.
candidate 4 (found by 1 of 33 passes): This paper proposes a new type-erased view: `std::ranges::any_view`.

## audience - grade 1.67 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  1/2/1  -> 1.33
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The following benchmarks were compiled with clang 20 with libc++, with -O3, run on APPLE M4 MAX CPU with 16 cores.
candidate 2 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 2/2/2  -> 2.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                0/2/2  -> 1.33
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `std::span<T>` is another type-erasure utility recently added to the standard; and is closely related to ranges in fact, by allowing type-erased *reference* of any underlying *contiguous* range of objects.
candidate 2 (found by 3 of 33 passes): This is inspired by Barry’s [blog post](https://brevzin.github.io/c++/2019/12/02/named-arguments/).
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.
candidate 4 (found by 2 of 33 passes): `range-v3` uses the name `category` for the category enumeration type. However, the authors believe that the name `std::ranges::category` is too general and it should be reserved for more general purpose utility in ranges library.

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
  [11] 10 References                                0/0/2  -> 0.67
candidate 1 (found by 3 of 33 passes): An implementation of this approach would look like this: [link](https://godbolt.org/z/qdnoE7Mb9)
candidate 2 (found by 3 of 33 passes): Both of our two reference implementations have proper `constexpr` support.
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.
candidate 4 (found by 1 of 33 passes): [ours] Hui Xie, S. Levent Yilmaz, and Dionne Louis. A proof-of-concept implementation of any_view. https://github.com/huixie90/cpp_papers/tree/main/impl/any_view

-->
