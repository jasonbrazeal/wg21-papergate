Verdict: Adequate (5/14)

The paper offers a narrow but concrete basis for its standardization case: it identifies a real interaction problem and shows that a reference implementation exists. Beyond that, the support is thin, with most of the necessary framing—affected users, standardization rationale, interoperability, and why a library solution is insufficient—left unaddressed.

- The strongest support is the demonstrated implementation in `stdexec`, which gives the proposal a concrete existence outside the paper.
- The paper clearly explains why the current `task_scheduler` behavior matters for users composing parallel work through type-erased wrappers.
- The discussion of prior art gestures toward `parallel_scheduler` and P3941R3, but does not establish how the proposed approach compares to or improves upon alternatives.
- The most glaring omission is any account of why this change belongs in the standard rather than remaining a library-level fix.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.00   accumulate 5.00   max 5.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 4.50 / 4.50   (all 3 samples: 4.50)
headings: h2 6
on threshold: motivation, implementation
splits: prior_art[2] 2/0/0  prior_art[5] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   2/2/2  -> 2.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/1/1  -> 1.00
  [5] 4 Implementation Experience                  0/0/0  -> 0.00
  [6] 5 Proposed Wording                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): if a `task_scheduler` wraps a `parallel_scheduler` and is used to launch parallel work with a `bulk` sender, the work is not parallelized as it would be had a `parallel_scheduler` been used directly.
candidate 2 (found by 2 of 21 passes): These are precisely the operations we would like `task_scheduler` to handle.
candidate 3 (found by 1 of 21 passes): Currently, `task_scheduler` is specified to have an exposition-only member *`sch_`* of type `shared_ptr&lt;void>`.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Implementation Experience                  0/0/0  -> 0.00
  [6] 5 Proposed Wording                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 4 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   2/0/0  -> 0.67
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/1/1  -> 1.00
  [5] 4 Implementation Experience                  0/1/0  -> 0.33
  [6] 5 Proposed Wording                           1/1/1  -> 1.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Like `task_scheduler`, the `parallel_scheduler` is a type-erased wrapper for a scheduler-like object.
candidate 2 (found by 2 of 21 passes): This paragraph is taken from [[P3941R3]](https://isocpp.org/files/papers/P3941R3.html).
candidate 3 (found by 1 of 21 passes): if a `task_scheduler` wraps a `parallel_scheduler` and is used to launch parallel work with a `bulk` sender, the work is not parallelized as it would be had a `parallel_scheduler` been used directly.
candidate 4 (found by 1 of 21 passes): The proposed solution has been implemented in [`stdexec`](https://github.com/NVIDIA/stdexec), the `std::execution` reference implementation, as of 2026-01-22.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Implementation Experience                  0/0/0  -> 0.00
  [6] 5 Proposed Wording                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Implementation Experience                  0/0/0  -> 0.00
  [6] 5 Proposed Wording                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Implementation Experience                  0/0/0  -> 0.00
  [6] 5 Proposed Wording                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Synopsis                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Implementation Experience                  2/2/2  -> 2.00
  [6] 5 Proposed Wording                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The proposed solution has been implemented in [`stdexec`](https://github.com/NVIDIA/stdexec), the `std::execution` reference implementation, as of 2026-01-22.

-->
