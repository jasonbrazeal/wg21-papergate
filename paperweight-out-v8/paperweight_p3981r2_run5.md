Verdict: Adequate (6/14)

The paper’s strongest support is concentrated in its motivation: it clearly explains why optional references would be a better return type for the algorithms under discussion. Beyond that, the case for standardization is largely asserted rather than demonstrated, with several key requirements left unaddressed or only gestured at. The thinnest areas are the absence of any discussion of who is affected and the lack of a case for why a library solution would not suffice.

- The paper establishes why the change matters by enumerating concrete benefits of `optional<T&>` for the relevant return types.
- It gestures at prior art and implementation experience through references to Rust and general use of optional references, but does not develop these into a substantive argument.
- It claims there are no benefits to returning `T*` and that standardization is necessary, but offers little supporting reasoning for either point.
- It does not identify who is affected by the change or explain why a library implementation would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 5 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 4.67   accumulate 6.00   max 8.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.67
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 4.50 / 6.00   (all 3 samples: 5.50)
headings: h2 7
on threshold: motivation, prior_art, vehicle, coordination
splits: prior_art[5] 1/0/1  implementation[6] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           1/1/1  -> 1.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.
candidate 2 (found by 3 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.
candidate 3 (found by 2 of 24 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms
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

## prior_art - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [5] 4 Iterator or Subrange?                      1/0/1  -> 0.67
  [6] 5 Why not do this?                           2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 2 (found by 2 of 24 passes): A previous revision of this paper made the argument that `v.try_append_range(r)` should return a `subrange` instead of an `iterator` (as pointed out by PL-006).

## vehicle - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 24 passes): There are simply no benefits to returning `T*`.

## coordination - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 24 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

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

## implementation - grade 0.67  [binary: max] (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           1/0/1  -> 0.67
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
