Verdict: Adequate (6/14)

The paper makes a genuine case that the proposed return-type changes would be useful and that similar designs have succeeded elsewhere, but it leaves several parts of the standardization argument largely unaddressed. The thinnest support concerns who is actually affected, how the change would interoperate with existing code and adjacent proposals, and why the same result cannot be achieved in a library.

- The strongest support is the discussion of prior art and alternatives, which grounds the proposal in existing practice and explains why the current return types are inconvenient.
- The paper also establishes why the change matters by laying out concrete benefits of `optional<T&>` and borrowed subranges over the status quo.
- The claim that there are no benefits to returning `T*` is asserted rather than demonstrated, so the case for standardizing rests partly on an unsupported comparison.
- The most glaring omissions are the absence of any account of affected users, interoperability concerns, or why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 5.67)
headings: h2 6
on threshold: prior_art, vehicle
splits: motivation[5] 2/1/1  prior_art[2] 0/2/2  prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 T makes for a poor optional<T&>            2/2/2  -> 2.00
  [4] 3 Iterator or Subrange?                      2/2/2  -> 2.00
  [5] 4 Why not do this?                           2/1/1  -> 1.33
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

## prior_art - grade 1.67 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/2/2  -> 1.33
  [3] 2 T makes for a poor optional<T&>            0/0/0  -> 0.00
  [4] 3 Iterator or Subrange?                      2/1/1  -> 1.33
  [5] 4 Why not do this?                           2/2/2  -> 2.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The Rust standard library returns optional references from many APIs quite liberally.
candidate 2 (found by 2 of 21 passes): We are aware that [[P3739R4] (Standard Library Hardening - using std::optional)](https://wg21.link/p3739r4) exists, but we feel that this is an important change to make, and that paper’s motivation is weak
candidate 3 (found by 2 of 21 passes): This follows the general principle that ranges are simply more convenient for users than iterators, because you only need the one object rather than two.
candidate 4 (found by 1 of 21 passes): This API is quite unlike a few algorithms which return an iterator, like `std::find`, where the iterator itself is specifically desired.

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
candidate 1 (found by 2 of 21 passes): There are simply no benefits to returning `T*`.
candidate 2 (found by 1 of 21 passes): These are very significant benefits to returning `optional<T&>`. There are simply no benefits to returning `T*`.

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

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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
candidate 1 (found by 2 of 21 passes): But the notion of an optional reference in general is not new, and we have a lot of experience with it outside of the standard library — and even outside of C++.
candidate 2 (found by 1 of 21 passes): we have a lot of experience with it outside of the standard library — and even outside of C++.

-->
