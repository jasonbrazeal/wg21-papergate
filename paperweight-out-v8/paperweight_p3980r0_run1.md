Verdict: Weak to Adequate (3/14)

The paper offers only partial support for its own standardization, with the strongest material concentrated in prior art and the record of committee discussion. The case is thinnest around the basic rationale for standardizing this behavior rather than leaving it to a library, and around who would actually be affected by the change.

- The paper does establish that the direction has prior committee support, citing both the LEWG preference for one wording approach and the Kona discussion favoring the receiver’s allocator.
- The paper claims, but does not fully establish, why the change matters, resting mainly on the observation that the current specification uses one allocator for both the coroutine frame and child environments.
- The paper does not establish why the standard is the right place for this change, nor why a library solution would be insufficient.
- The paper offers no implementation experience, no account of who is affected, and no substantive interoperability or coordination evidence beyond the single allocator observation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.33   accumulate 4.00   max 3.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 0.00
sample agreement: 31 of 35 section-criterion pairs unanimous (89%)
single-sample totals would have been: 3.00 / 2.50 / 4.00   (all 3 samples: 3.17)
headings: h2 4
on threshold: prior_art
splits: motivation[3] 2/1/1  motivation[4] 1/1/2  prior_art[3] 1/1/2  coordination[1] 0/0/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        2/1/1  -> 1.33
  [4] 3 Allocator Argument Position                1/1/2  -> 1.33
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 2 (found by 3 of 15 passes): The main benefit is that support of an optional allocator can be supported by having a trailing `, auto&&...` on the parameter list.
candidate 3 (found by 2 of 15 passes): There are a few NB comments about `task`’s use of allocators
candidate 4 (found by 1 of 15 passes): The allocator constraints for allocating the coroutine frame are due to the use of the same allocator for the environment of child senders.

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
  [3] 2 Overview of Changes                        1/1/2  -> 1.33
  [4] 3 Allocator Argument Position                2/2/2  -> 2.00
  [5] 4 Use Allocator From Environment             1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.
candidate 2 (found by 3 of 15 passes): At the LEWG meeting on 2026-02-03 the first approach (putting the `allocator_arg` first, Wording Change A) was preferred ([notes](https://wiki.isocpp.org/2026-02-03_LEWG_Telecon)).
candidate 3 (found by 3 of 15 passes): During the discussion at Kona the conclusion was that the allocator forwarded by `task`’s environment to child senders should be the allocator from `get_allocator` on the receiver `task` gets `connect`ed to.
candidate 4 (found by 1 of 15 passes): The discussion in Kona favored this direction.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] 1 Change History                             0/0/0  -> 0.00
  [3] 2 Overview of Changes                        0/0/0  -> 0.00
  [4] 3 Allocator Argument Position                0/0/0  -> 0.00
  [5] 4 Use Allocator From Environment             0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): The current specification uses the same allocator for coroutine frame and the child environments.

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
