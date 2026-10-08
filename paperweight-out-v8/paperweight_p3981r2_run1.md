Verdict: Adequate to Strong (6/14)

The paper offers real support for the value of `optional<T&>` as a return type and shows awareness of prior art, but it does not make a complete case for standardization because several essential points are asserted rather than demonstrated. The thinnest areas are the absence of any identified audience, the lack of implementation experience within the standard library context, and the failure to show why a library solution would be insufficient.

- The strongest support is the paper’s explanation of why the change matters, including concrete benefits and broad existing experience with optional references outside C++.
- The paper also credibly engages with prior art and alternatives, such as `T*` returns, `inplace_vector`, Rust’s APIs, and the related hardening proposal.
- The case for why this belongs in the standard, rather than in a library, rests on the bare claim that there are no benefits to returning `T*`, without establishing that a non-standard library type could not serve the same purpose.
- The most glaring omission is that the paper never identifies who is affected by the current return types or who would benefit from the proposed change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 7.00   accumulate 6.50   max 8.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.17  coordination 0.50  insufficiency 0.17  implementation 0.67
sample agreement: 49 of 56 section-criterion pairs unanimous (88%)
single-sample totals would have been: 6.00 / 5.50 / 7.50   (all 3 samples: 6.33)
headings: h2 7
on threshold: vehicle
splits: motivation[6] 1/2/2  prior_art[3] 2/0/0  prior_art[4] 2/0/2  vehicle[6] 0/0/1
        coordination[4] 1/0/2  insufficiency[4] 0/1/0  implementation[6] 1/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           1/2/2  -> 1.67
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

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/0/0  -> 0.67
  [4] 3 T makes for a poor optional<T&>            2/0/2  -> 1.33
  [5] 4 Iterator or Subrange?                      2/2/2  -> 2.00
  [6] 5 Why not do this?                           2/2/2  -> 2.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.
candidate 2 (found by 2 of 24 passes): A previous revision of this paper made the argument that `v.try_append_range(r)` should return a `subrange` instead of an `iterator` (as pointed out by PL-006). But we’ve decided it is best to remove the function entirely for now
candidate 3 (found by 2 of 24 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 4 (found by 1 of 24 passes): We are aware that [[P3739R4] (Standard Library Hardening - using std::optional)](https://wg21.link/p3739r4) exists, but we feel that this is an important change to make, and that paper’s motivation is weak

## vehicle - grade 1.17 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/1  -> 0.33
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): There are simply no benefits to returning `T*`.
candidate 2 (found by 1 of 24 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

## coordination - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 T makes for a poor optional<T&>            1/0/2  -> 1.00
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
  [4] 3 T makes for a poor optional<T&>            0/1/0  -> 0.33
  [5] 4 Iterator or Subrange?                      0/0/0  -> 0.00
  [6] 5 Why not do this?                           0/0/0  -> 0.00
  [7] 6 Proposal                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): There are simply no benefits to returning `T*`.

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
