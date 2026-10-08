Verdict: Adequate (5/14)

The paper offers meaningful support in a few areas, particularly in showing that the current restriction creates a real generic-programming problem and that a coalescing alternative has been implemented and exercised. The case is much thinner, however, on the broader standardization questions: it does not establish why the standard is the right venue, how the change coordinates with related facilities, or why a library-level solution would be insufficient.

- The strongest support is the implementation experience, with the coalescing approach tested against NVIDIA’s reference implementation and corroborated by Intel’s bare-metal senders and receivers.
- The paper also clearly establishes why the issue matters, since the status quo creates an avoidable special case and can lead to hanging asynchronous operations in generic code.
- Prior art and alternatives are adequately covered, including the current ill-formed specification and the SG1-requested feedback from relevant maintainers.
- The most glaring omission is the absence of any established case for why this needs to be in the standard rather than addressed through a library facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.67   accumulate 5.83   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 5.33)
headings: h2 9
on threshold: motivation, prior_art
splits: motivation[3] 2/0/2  motivation[4] 1/2/2  audience[4] 0/2/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/0/2  -> 1.33
  [4] Discussion                                   1/2/2  -> 1.67
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Banning `std::execution::when_all()` (i.e. the status quo) unnecessarily creates a special case when writing generic algorithms.
candidate 2 (found by 2 of 30 passes): If this restriction were not present the asynchronous operation which results from connecting the result of `std::execution::when_all()` and starting the operation state yielded thereby would hang

## audience - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/2/0  -> 0.67
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.

## prior_art - grade 1.50 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Proposal                                     1/1/1  -> 1.00
  [6] Implementation Experience                    1/1/1  -> 1.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The standard currently specifies, by fiat, that `std::execution::when_all()` is ill-formed (§33.9.12.12 [exec.when.all])
candidate 2 (found by 3 of 30 passes): During SG1 review in Brno 2026 SG1 requested that the author solicit feedback on this issue from Ben Deane and/or Michael Caisse, maintainers of Intel’s “Bare Metal Senders and Receivers” [1].
candidate 3 (found by 3 of 30 passes): The following change represents the coalesce-to-`std::execution::just()` approach (forwarded to LEWG by SG1):
candidate 4 (found by 3 of 30 passes): The coalescing option has been implemented against nVidia’s reference implementation of `std::execution` [2].

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    1/1/1  -> 1.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): The coalescing option has been implemented against nVidia’s reference implementation of `std::execution` [2].
candidate 2 (found by 3 of 30 passes): [1] https://github.com/intel/cpp-baremetal-senders-and-receivers [2] https://github.com/NVIDIA/stdexec/pull/2124
candidate 3 (found by 2 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.
candidate 4 (found by 1 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.*

-->
