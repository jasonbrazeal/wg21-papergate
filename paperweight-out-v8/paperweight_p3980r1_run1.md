Verdict: Weak to Adequate (3/14)

The paper offers some useful context for the change, particularly around prior discussion and the preference expressed in LEWG, but it does not build a complete case for standardization. The thinnest areas are the absence of any account of who is affected, why the standard is the right venue, or how the change would work in practice.

- The strongest support is the record of prior art and alternatives, including the LEWG preference for placing `allocator_arg` first and the existing status quo.
- The paper asserts that the change matters because it would make allocator support more consistent, but it does not substantiate that benefit beyond a brief rationale.
- The most glaring omission is the lack of implementation experience, leaving no evidence that the proposed wording has been tried or validated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.00   accumulate 3.83   max 3.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 3.50 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 4
on threshold: motivation, prior_art
splits: motivation[1] 2/1/0  motivation[4] 1/2/2  prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 2/1/0  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/1  -> 1.00
  [4] 3 Allocator Argument Position                1/2/2  -> 1.67
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The main benefit is that support of an optional allocator can be supported by having a trailing `, auto&&...` on the parameter list.
candidate 2 (found by 2 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
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

## prior_art - grade 1.67 (fired in 4 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Allocator Argument Position                2/1/1  -> 1.33
  [5] 4 Use Allocator From Environment             1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 2 (found by 3 of 15 passes): At the LEWG meeting on 2026-02-03 the first approach (putting the `allocator_arg` first, Wording Change A) was preferred ([notes](https://wiki.isocpp.org/2026-02-03_LEWG_Telecon)).
candidate 3 (found by 3 of 15 passes): During the discussion at Kona the conclusion was that the allocator forwarded by `task`’s environment to child senders should be the allocator from `get_allocator` on the receiver `task` gets `connect`ed to.
candidate 4 (found by 2 of 15 passes): The options are a fixed location (which would fit first for consistency with existing use) and anywhere. The status quo is anywhere, and the request is to require that it goes first.

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
