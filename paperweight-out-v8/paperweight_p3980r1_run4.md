Verdict: Weak to Adequate (3/14)

The paper offers only a narrow slice of the case for standardization: it can point to a recorded committee preference and some discussion history, but it does not establish who is affected, why the standard is the right venue, how the change would interoperate, why a library solution is insufficient, or whether anyone has implemented it. The thinnest support is around the basic motivation and the affected audience, leaving the proposal largely dependent on procedural precedent rather than demonstrated need.

- The strongest support is the documented LEWG preference for putting `allocator_arg` first, which anchors the proposed direction in committee discussion.
- The paper also establishes that alternatives were considered, since it contrasts a fixed first position with the status quo of allowing the allocator anywhere.
- The most glaring omission is the absence of any account of who is affected by the current behavior or the proposed change.
- The paper likewise offers no implementation experience, no interoperability analysis, and no argument for why this cannot be handled outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 3.00   accumulate 3.83   max 3.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 3.00 / 3.00 / 3.50   (all 3 samples: 3.17)
headings: h2 4
on threshold: motivation
splits: motivation[4] 2/1/2  prior_art[1] 0/1/1  prior_art[4] 1/2/2
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        1/1/1  -> 1.00
  [4] 3 Allocator Argument Position                2/1/2  -> 1.67
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

## prior_art - grade 1.83 (fired in 4 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/2/2  -> 2.00
  [4] 3 Allocator Argument Position                1/2/2  -> 1.67
  [5] 4 Use Allocator From Environment             1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): At the LEWG meeting on 2026-02-03 the first approach (putting the `allocator_arg` first, Wording Change A) was preferred ([notes](https://wiki.isocpp.org/2026-02-03_LEWG_Telecon)).
candidate 2 (found by 3 of 15 passes): During the discussion at Kona the conclusion was that the allocator forwarded by `task`’s environment to child senders should be the allocator from `get_allocator` on the receiver `task` gets `connect`ed to.
candidate 3 (found by 2 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 4 (found by 1 of 15 passes): The options are a fixed location (which would fit first for consistency with existing use) and anywhere. The status quo is anywhere, and the request is to require that it goes first.

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
