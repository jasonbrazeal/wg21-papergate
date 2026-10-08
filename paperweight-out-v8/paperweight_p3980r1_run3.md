Verdict: Weak (3/14)

The paper offers only a thin account of why its requested change should be standardized, leaning on meeting sentiment and a narrow design preference rather than building a broader case. The strongest material concerns the choice among wording approaches, but the document is largely silent on the affected audience, implementation experience, and why a library solution would be insufficient.

- The clearest support is the record of committee discussion, including LEWG’s preference for putting `allocator_arg` first and the Kona direction on forwarding the receiver’s allocator.
- The paper gestures at a practical benefit by noting that an optional allocator could be supported with a trailing `auto&&...` parameter list.
- The most glaring omission is the absence of any implementation experience or evidence about how the change would affect real users and existing code.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.50/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.50   corroborated 2.00   accumulate 3.67   max 2.67

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 2.50 / 2.00 / 3.00   (all 3 samples: 2.50)
headings: h2 4
on threshold: none
splits: motivation[1] 2/1/1  prior_art[3] 1/1/2  prior_art[4] 1/1/2
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 2/1/1  -> 1.33
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/1  -> 1.00
  [4] 3 Allocator Argument Position                1/1/1  -> 1.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 2 (found by 3 of 15 passes): The main benefit is that support of an optional allocator can be supported by having a trailing `, auto&&...` on the parameter list.
candidate 3 (found by 2 of 15 passes): The status quo is anywhere, and the request is to require that it goes first.
candidate 4 (found by 1 of 15 passes): There are a few NB comments about `task`’s use of allocators

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 4 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/2  -> 1.33
  [4] 3 Allocator Argument Position                1/1/2  -> 1.33
  [5] 4 Use Allocator From Environment             1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 2 (found by 3 of 15 passes): At the LEWG meeting on 2026-02-03 the first approach (putting the `allocator_arg` first, Wording Change A) was preferred ([notes](https://wiki.isocpp.org/2026-02-03_LEWG_Telecon)).
candidate 3 (found by 3 of 15 passes): During the discussion at Kona the conclusion was that the allocator forwarded by `task`’s environment to child senders should be the allocator from `get_allocator` on the receiver `task` gets `connect`ed to.
candidate 4 (found by 2 of 15 passes): The discussion in Kona favored this direction.

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
