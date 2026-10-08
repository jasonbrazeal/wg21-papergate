Verdict: Adequate (6/14)

The paper offers some support for changing these return types, chiefly by arguing that optional references are a better fit and by pointing to existing practice outside C++. Its case is much thinner on the practical questions that usually matter for standardization: who is actually affected, how the change coordinates with existing library and language features, and whether there is implementation experience with the specific design.

- The strongest support is the argument that optional references would be a better return type, with several benefits enumerated and an explicit acknowledgment that the current situation is inconvenient.
- The paper also establishes some prior art by citing PL-006, Rust’s liberal use of optional references, and a related proposal arguing against the change.
- The most glaring omission is the absence of any established account of who is affected by the current return types or who would benefit from the proposed change.
- The paper also leaves coordination and interoperability unestablished, and its claims about why a library solution will not do and about implementation experience are asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 5 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.00   accumulate 6.17   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.00  coordination 0.00  insufficiency 0.67  implementation 1.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.50 / 5.50 / 6.50   (all 3 samples: 6.17)
headings: h2 6
on threshold: prior_art, vehicle
splits: insufficiency[3] 2/0/2
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
candidate 3 (found by 3 of 21 passes): This is inconvenient, as pointed out by PL-006.
candidate 4 (found by 2 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

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

## prior_art - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      1/1/1  -> 1.00
  [5] 4 Why not do this?                           2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This is inconvenient, as pointed out by PL-006.
candidate 2 (found by 2 of 21 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 3 (found by 1 of 21 passes): [[P3830R0] (NB-Commenting is Not a Vehicle for Redesigning inplace_vector)] argues that we simply should not make this change, mostly on the basis that it is new.

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
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

## insufficiency - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            2/0/2  -> 1.33
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): There are some operations that `T*` and `optional<T&>` share in the middle, those have the same semantics and meaning either way.

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
