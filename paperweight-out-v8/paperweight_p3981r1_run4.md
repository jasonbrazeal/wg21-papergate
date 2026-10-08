Verdict: Adequate (7/14)

The paper gives a reasonably clear account of why optional references would be useful in the algorithms it targets, and it situates that argument against existing practice in Rust and prior C++ discussions. The support is much thinner, however, when it comes to showing that this needs to be done in the standard library itself, that the affected audience and interoperability costs are understood, or that the approach has meaningful implementation experience behind it.

- The strongest part of the paper is its motivation, with concrete examples of return types where `optional<T&>` would be a better fit than the current alternatives.
- The paper also does a fair job of acknowledging prior art, including Rust’s use of optional references and earlier C++ discussions about pointers as poor substitutes.
- The case for standardization itself is mostly asserted rather than demonstrated, since the paper claims there are “simply no benefits” to the status quo without fully developing that argument.
- Most notably, the paper does not establish who is affected by the change, leaving the practical scope and impact of the proposal unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.00   accumulate 6.50   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.17  implementation 1.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 6.50 / 6.00   (all 3 samples: 6.50)
headings: h2 7
on threshold: vehicle
splits: coordination[4] 1/1/0  insufficiency[4] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.
candidate 2 (found by 2 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three
candidate 3 (found by 2 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.
candidate 4 (found by 1 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three and `ranges::borrowed_subrange_t<R>` for the fourth.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      1/1/1  -> 1.00
  [6] 5 Why not do this?                           2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): A previous revision of this paper made the argument that `v.try_append_range(r)` should return a `subrange` instead of an `iterator` (as pointed out by PL-006).
candidate 2 (found by 3 of 24 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 3 (found by 2 of 24 passes): Barry wrote a whole blog post several years about about how [`T*` makes for a poor `optional<T&>`](https://brevzin.github.io/c++/2021/12/13/optional-ref-ptr/) responding to this claim.
candidate 4 (found by 1 of 24 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

## vehicle - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): There are simply no benefits to returning `T*`.
candidate 2 (found by 1 of 24 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.

## coordination - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            1/1/0  -> 0.67
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            1/0/0  -> 0.33
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): There are simply no benefits to returning `T*`.

## implementation - grade 1.00  [binary: max] (fired in 1 of 8 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           1/1/1  -> 1.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
