Verdict: Strong (8/14)

The paper offers meaningful support in a few areas, particularly in showing existing implementation experience and identifying why type erasure matters, but it leaves several core parts of its standardization case asserted rather than demonstrated. The thinnest support concerns the need for standardization itself and the claim that a library solution would be insufficient.

- The strongest support is the implementation experience, with working examples and prior art in range-v3 credited as established.
- The motivation for type-erased views is clearly established, especially the compilation-time and API-boundary concerns.
- The paper only claims, without fully establishing, who is affected and why this belongs in the standard rather than in a library.
- The most glaring omission is the absence of any established argument for why a library implementation will not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.33   accumulate 8.33   max 10.33

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 0.17  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.00 / 9.00 / 8.00   (all 3 samples: 8.33)
headings: h2 10
on threshold: audience, coordination
splits: motivation[3] 1/0/0  motivation[7] 0/0/1  audience[9] 0/1/0  vehicle[4] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/0/0  -> 0.33
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/1  -> 0.33
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In large applications, such liberal use of `std::ranges` can lead to increased header dependencies and often a significant compilation time penalty.
candidate 2 (found by 3 of 33 passes): Due to the lack of type erasure utilities, typically the API takes a `vector`, even though the implementation only needs to iterate once over the elements.
candidate 3 (found by 1 of 33 passes): This paper proposes a new type-erased view: `std::ranges::any_view`.
candidate 4 (found by 1 of 33 passes): In Wrocław meeting, one important point was made: The majority of the use case of `any_view` is to use it as a function parameter in the API boundary.

## audience - grade 1.17 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  0/1/0  -> 0.33
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The following benchmarks were compiled with clang 20 with libc++, with -O3, run on APPLE M4 MAX CPU with 16 cores.
candidate 2 (found by 1 of 33 passes): In Hagenberg, SG9 recommended to make it move-only by default with the votes: | SF | F | N | A | SA | | 4 | 5 | 1 | 0 | 1 |
candidate 3 (found by 1 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Design Space and Prior Art                 2/2/2  -> 2.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 2/2/2  -> 2.00
  [8] 7 Other Design Considerations                2/2/2  -> 2.00
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `std::span<T>` is another type-erasure utility recently added to the standard; and is closely related to ranges in fact, by allowing type-erased *reference* of any underlying *contiguous* range of objects.
candidate 2 (found by 3 of 33 passes): This is inspired by Barry’s [blog post](https://brevzin.github.io/c++/2019/12/02/named-arguments/).
candidate 3 (found by 3 of 33 passes): `range-v3` uses the name `category` for the category enumeration type. However, the authors believe that the name `std::ranges::category` is too general and it should be reserved for more general purpose utility in ranges library.
candidate 4 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Motivation                                 0/1/0  -> 0.33
  [5] 4 Design Space and Prior Art                 0/0/0  -> 0.00
  [6] 5 Proposed Design                            0/0/0  -> 0.00
  [7] 6 Alternative Design for Template Parameters 0/0/0  -> 0.00
  [8] 7 Other Design Considerations                0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): In this paper, we propose to extend the standard library with `std::ranges::any_view`, which provides a convenient and generalized type-erasure facility to hold any object of any type that satisfies the `ranges::view` concept itself.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 3)  (SHARED PASSAGE)
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
  [11] 10 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): An implementation of this approach would look like this: [link](https://godbolt.org/z/qdnoE7Mb9)
candidate 2 (found by 3 of 33 passes): There was a bug report on the beman project implementation which is based on the R5 wording.
candidate 3 (found by 3 of 33 passes): `any_view` has been implemented in [[range-v3]](https://github.com/ericniebler/range-v3), with equivalent semantics as proposed here.

-->
