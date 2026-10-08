Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why optional references would be useful and what existing practice informs the design, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns the affected audience and the argument that this cannot be done adequately as a library feature.

- The strongest support is the discussion of prior art and alternatives, including Rust’s use of optional references and the limitations of `T*` as a substitute.
- The motivation for the feature is also established through concrete examples of inconvenient return types and the benefits of `optional<T&>`.
- The paper claims but does not establish that standardization is necessary, since the enumerated benefits are not tied clearly to a need for a standard library type.
- The most glaring omission is any identification of who is affected, leaving the scope and demand for the proposal unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.67   accumulate 6.17   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.17  insufficiency 0.33  implementation 0.67
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.50 / 5.50 / 6.50   (all 3 samples: 6.17)
headings: h2 6
on threshold: vehicle
splits: prior_art[4] 1/2/1  coordination[3] 0/0/1  insufficiency[3] 1/1/0
        implementation[5] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [4] 3 Iterator or Subrange?                      2/2/2  -> 2.00
  [5] 4 Why not do this?                           2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.
candidate 2 (found by 3 of 21 passes): This is inconvenient, as pointed out by PL-006.
candidate 3 (found by 3 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.
candidate 4 (found by 2 of 21 passes): We argue in this paper that there is a better choice for the return type for each of these algorithms: `optional<reference>` for the first three and `ranges::borrowed_subrange_t<R>` for the fourth.

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

## prior_art - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [4] 3 Iterator or Subrange?                      1/2/1  -> 1.33
  [5] 4 Why not do this?                           2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This follows the general principle that ranges are simply more convenient for users than iterators, because you only need the one object rather than two.
candidate 2 (found by 3 of 21 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 3 (found by 2 of 21 passes): Barry wrote a whole blog post several years about about how [`T*` makes for a poor `optional<T&>`](https://brevzin.github.io/c++/2021/12/13/optional-ref-ptr/) responding to this claim.
candidate 4 (found by 1 of 21 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

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
candidate 1 (found by 3 of 21 passes): There are several significant benefits to `optional<T&>` when it comes to the return type here, which we will enumerate.

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/1  -> 0.33
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): When [[P0843R14] (inplace_vector)](https://wg21.link/p0843r14) was adopted, the only sensible choice for the return type was `T*`: either a pointer that points to the new element or a null pointer.

## insufficiency - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            1/1/0  -> 0.67
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): There are simply no benefits to returning `T*`.

## implementation - grade 0.67  [binary: max] (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      0/0/0  -> 0.00
  [5] 4 Why not do this?                           1/0/1  -> 0.67
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
