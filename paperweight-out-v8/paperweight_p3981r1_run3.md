Verdict: Adequate (6/14)

The paper gives a reasonably clear motivation for preferring `optional<T&>` over raw pointers in these return types, and it situates that preference within existing practice and prior discussion. The support is much thinner, however, when it comes to showing that this change belongs in the standard, that it coordinates cleanly with already-adopted APIs, or that a library solution would be insufficient.

- The strongest part of the paper is its explanation of why the return type choice matters and its grounding in prior art, including Rust practice and earlier C++ discussions.
- The paper also establishes that alternatives have been considered, particularly the earlier `subrange` suggestion and the use of `T*` in `inplace_vector`.
- The most glaring omission is any real account of who is affected by the proposed change or what concrete interoperability problems it would create or solve.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.67   accumulate 6.17   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 0.17  insufficiency 0.17  implementation 1.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.00 / 5.50 / 7.00   (all 3 samples: 6.17)
headings: h2 7
on threshold: vehicle
splits: prior_art[5] 1/1/2  vehicle[4] 2/1/2  coordination[4] 0/0/1  insufficiency[4] 0/0/1
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
candidate 1 (found by 3 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms
candidate 2 (found by 3 of 24 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.
candidate 3 (found by 3 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

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
  [5] 4 Iterator or Subrange?                      1/1/2  -> 1.33
  [6] 5 Why not do this?                           2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): A previous revision of this paper made the argument that `v.try_append_range(r)` should return a `subrange` instead of an `iterator` (as pointed out by PL-006).
candidate 2 (found by 3 of 24 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 3 (found by 2 of 24 passes): Barry wrote a whole blog post several years about about how [`T*` makes for a poor `optional<T&>`](https://brevzin.github.io/c++/2021/12/13/optional-ref-ptr/) responding to this claim.
candidate 4 (found by 1 of 24 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

## vehicle - grade 0.83 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            2/1/2  -> 1.67
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): There are simply no benefits to returning `T*`.
candidate 2 (found by 1 of 24 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/1  -> 0.33
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/1  -> 0.33
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): There are simply no benefits to returning `T*`.

## implementation - grade 1.00  [binary: max] (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 24 passes): we have a lot of experience with it outside of the standard library — and even outside of C++.
candidate 2 (found by 1 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
