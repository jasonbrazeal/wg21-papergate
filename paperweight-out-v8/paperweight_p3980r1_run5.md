Verdict: Weak (3/14)

The paper offers a narrow but real basis for its request, anchored in specific national body comments and a recorded LEWG preference, but it leaves most of the case for standardization unargued. The strongest material concerns the problem’s relevance and the chosen direction among alternatives; the thinnest concerns who is concretely affected and why existing practice or non-standard mechanisms cannot suffice.

- The paper clearly ties its motivation to pending NB comments and identifies the practical benefit of supporting an optional allocator through a trailing parameter pack.
- It documents prior art and the alternative considered, including the LEWG preference for placing `allocator_arg` first and the Kona conclusion about which allocator should be forwarded.
- It does not establish who is affected by the current specification or what implementation experience supports the change.
- It offers no argument for why the standard must address this rather than a library solution, nor any coordination or interoperability analysis.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.00   accumulate 4.00   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 4
on threshold: motivation, prior_art
splits: motivation[1] 1/1/2  motivation[4] 2/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/2  -> 1.33
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/1  -> 1.00
  [4] 3 Allocator Argument Position                2/2/1  -> 1.67
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 2 (found by 3 of 15 passes): The main benefit is that support of an optional allocator can be supported by having a trailing `, auto&&...` on the parameter list.
candidate 3 (found by 2 of 15 passes): There are a few NB comments about `task`’s use of allocators
candidate 4 (found by 1 of 15 passes): The status quo is anywhere, and the request is to require that it goes first.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 4 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Allocator Argument Position                1/1/1  -> 1.00
  [5] 4 Use Allocator From Environment             1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): This paper addresses [US 254-385](https://github.com/cplusplus/nbballot/issues/960), [US 253-386](https://github.com/cplusplus/nbballot/issues/961), [US 255-384](https://github.com/cplusplus/nbballot/issues/959), and [US 261-391](https://github.com/cplusplus/nbballot/issues/966).
candidate 2 (found by 3 of 15 passes): The status quo is anywhere, and the request is to require that it goes first. However, to support optionally passing an allocator, having it go anywhere is easier to do.
candidate 3 (found by 3 of 15 passes): At the LEWG meeting on 2026-02-03 the first approach (putting the `allocator_arg` first, Wording Change A) was preferred ([notes](https://wiki.isocpp.org/2026-02-03_LEWG_Telecon)).
candidate 4 (found by 3 of 15 passes): During the discussion at Kona the conclusion was that the allocator forwarded by `task`’s environment to child senders should be the allocator from `get_allocator` on the receiver `task` gets `connect`ed to.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

-->
