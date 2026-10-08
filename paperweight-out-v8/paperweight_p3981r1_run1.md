Verdict: Adequate (5/14)

The paper makes a clear case that the proposed return types would be preferable for the algorithms it discusses, but it does not adequately establish the broader need for standardization. The strongest support is concentrated in the motivation for changing these specific return types, while the thinnest areas are interoperability, implementability outside the standard library, and evidence that the change belongs in the standard rather than in user code.

- The paper convincingly argues that `optional<T&>` and `borrowed_subrange_t<R>` are better return types for the algorithms under discussion.
- The paper gestures at prior art and implementation experience, but does not substantiate these with enough detail to count as established support.
- The paper asserts there are no benefits to returning `T*`, but does not establish why this requires a standard library change.
- The paper offers no discussion of coordination with other proposals or of why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 5 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 4.33   accumulate 5.50   max 6.67

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.33  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 50 of 56 section-criterion pairs unanimous (89%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 4.67)
headings: h2 7
on threshold: motivation, prior_art
splits: motivation[6] 1/0/0  audience[6] 1/0/0  prior_art[3] 2/0/0  prior_art[4] 0/2/0
        prior_art[5] 0/0/2  vehicle[4] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           1/0/0  -> 0.33
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.
candidate 2 (found by 1 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three
candidate 3 (found by 1 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms
candidate 4 (found by 1 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three and `ranges::borrowed_subrange_t<R>` for the fourth.

## audience - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           1/0/0  -> 0.33
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The Rust standard library returns optional references from many APIs quite liberally.

## prior_art - grade 1.33 (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/0/0  -> 0.67
  [4] 3 T makes for a poor optional<T&>            0/2/0  -> 0.67
  [5] 4 Iterator or Subrange?                      0/0/2  -> 0.67
  [6] 5 Why not do this?                           2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): We are aware that [[P3739R4] (Standard Library Hardening - using std::optional)](https://wg21.link/p3739r4) exists, but we feel that this is an important change to make, and that paper’s motivation is weak
candidate 2 (found by 1 of 24 passes): Barry wrote a whole blog post several years about about how [`T*` makes for a poor `optional<T&>`](https://brevzin.github.io/c++/2021/12/13/optional-ref-ptr/) responding to this claim.
candidate 3 (found by 1 of 24 passes): A previous revision of this paper made the argument that `v.try_append_range(r)` should return a `subrange` instead of an `iterator` (as pointed out by PL-006).
candidate 4 (found by 1 of 24 passes): The paper additionally points out several issues with `std::optional&lt;T&>` specifically, which are:

## vehicle - grade 0.67 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/2/2  -> 1.33
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): There are simply no benefits to returning `T*`.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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
candidate 1 (found by 3 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
