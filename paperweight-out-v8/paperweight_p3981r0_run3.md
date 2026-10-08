Verdict: Adequate (6/14)

The paper offers some grounding for its motivation and shows awareness of existing practice, but it leaves much of the standardization case asserted rather than demonstrated. The thinnest areas are the absence of any identified affected users and the lack of concrete implementation experience or interoperability reasoning tied to the proposed design.

- The strongest support is the paper’s explanation of why the current return types are inconvenient and its appeal to established practice with optional references outside C++.
- The paper also credibly engages with prior art, including a specific critique of `T*` as a poor substitute for `optional<T&>` and the general principle that ranges are more convenient than iterator pairs.
- The case for why this belongs in the standard is only asserted, resting on the claim that there are no benefits to returning `T*` without showing that the alternative requires standardization.
- The most glaring omission is any account of who is affected by the current design, leaving the practical urgency and scope of the problem unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 7.00   accumulate 6.50   max 8.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.17  implementation 1.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.50 / 6.50 / 6.00   (all 3 samples: 6.33)
headings: h2 6
on threshold: vehicle
splits: motivation[5] 2/2/1  prior_art[4] 1/1/2  coordination[3] 1/1/0  insufficiency[3] 0/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      2/2/2  -> 2.00
  [5] 4 Why not do this?                           2/2/1  -> 1.67
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three and `ranges::borrowed_subrange_t<R>` for the fourth.
candidate 2 (found by 3 of 21 passes): This is inconvenient, as pointed out by PL-006.
candidate 3 (found by 3 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

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

## prior_art - grade 2.00 (fired in 3 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [4] 3 Iterator or Subrange?                      1/1/2  -> 1.33
  [5] 4 Why not do this?                           2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Barry wrote a whole blog post several years about about how [`T*` makes for a poor `optional<T&>`](https://brevzin.github.io/c++/2021/12/13/optional-ref-ptr/) responding to this claim.
candidate 2 (found by 3 of 21 passes): This follows the general principle that ranges are simply more convenient for users than iterators, because you only need the one object rather than two.
candidate 3 (found by 3 of 21 passes): The Rust standard library returns optional references from many APIs quite liberally.

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

## coordination - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            1/1/0  -> 0.67
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/1  -> 0.33
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): There are simply no benefits to returning `T*`.

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
