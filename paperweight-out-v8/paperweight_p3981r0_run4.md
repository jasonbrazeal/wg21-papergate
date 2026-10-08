Verdict: Adequate (7/14)

The paper offers some grounding for its motivation and points to relevant prior art, but it leaves several essential parts of the standardization case largely undeveloped, especially around who is affected, how the change would interoperate with existing code, and whether a library solution is truly insufficient. The strongest material concerns why the proposed return types would be preferable and the existence of analogous practice elsewhere, while the thinnest support appears in the areas of affected users, standardization necessity, and implementation experience.

- The paper establishes that the proposed return types would offer meaningful benefits and that optional references are a familiar concept outside the standard library.
- It also establishes relevant prior art by contrasting the proposed API with iterator-returning algorithms and citing Rust’s liberal use of optional references.
- The paper claims but does not establish that there are no benefits to returning `T*`, leaving the core argument for standardization under-supported.
- It does not establish who is affected, how the change coordinates with existing standard library or user code, or why a library-level solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 6.83   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.83  implementation 1.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.83)
headings: h2 6
on threshold: vehicle, insufficiency
splits: insufficiency[3] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [4] 3 Iterator or Subrange?                      2/2/2  -> 2.00
  [5] 4 Why not do this?                           1/1/1  -> 1.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three and `ranges::borrowed_subrange_t<R>` for the fourth.
candidate 2 (found by 3 of 21 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.
candidate 3 (found by 3 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.
candidate 4 (found by 2 of 21 passes): This is inconvenient, as pointed out by PL-006.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      2/2/2  -> 2.00
  [5] 4 Why not do this?                           2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This API is quite unlike a few algorithms which return an iterator, like `std::find`, where the iterator itself is specifically desired.
candidate 2 (found by 3 of 21 passes): The Rust standard library returns optional references from many APIs quite liberally.

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): There are simply no benefits to returning `T*`.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            2/1/2  -> 1.67
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): There are some operations that `T*` and `optional<T&>` share in the middle, those have the same semantics and meaning either way.
candidate 2 (found by 1 of 21 passes): There are simply no benefits to returning `T*`.

## implementation - grade 1.00  [binary: max] (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           1/1/1  -> 1.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
