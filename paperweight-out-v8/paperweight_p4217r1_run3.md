Verdict: Adequate (4/14)

The paper offers only a narrow basis for its standardization case: it can point to one concrete implementation, but most of the surrounding argument—who is affected, why the standard should change, and how the change fits with existing practice—is asserted rather than demonstrated. The thinnest support is in the areas that would normally carry the burden for a language or library change, namely the rationale for standardizing at all and the reason a library solution would not suffice.

- The strongest support is implementation experience, with a working change against NVIDIA’s reference implementation and confirmation from Intel’s maintainer that `when_all()` is already well-formed in that codebase.
- The paper claims prior art and alternatives by citing the current standard’s ill-formed status and the coalescing implementation, but it does not establish that these amount to a considered range of options.
- The paper’s statements about who is affected and about coordination with other implementations rest on a request to solicit feedback, not on evidence that the affected community has actually weighed in.
- The paper offers no established case for why the standard should address this rather than a library, and no established account of why the change matters beyond a generic-algorithms special case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 5 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 5.67   accumulate 5.17   max 5.67

## SUMMARY
grades: motivation 0.50  audience 0.50  prior_art 1.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.50 / 5.00 / 4.00   (all 3 samples: 4.33)
headings: h2 9
on threshold: implementation
splits: prior_art[4] 2/0/0  coordination[4] 0/2/0  implementation[4] 2/0/0
## END SUMMARY

## motivation - grade 0.50 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Banning `std::execution::when_all()` (i.e. the status quo) unnecessarily creates a special case when writing generic algorithms.

## audience - grade 0.50 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): During SG1 review in Brno 2026 SG1 requested that the author solicit feedback on this issue from Ben Deane and/or Michael Caisse, maintainers of Intel’s “Bare Metal Senders and Receivers” [1].

## prior_art - grade 1.00 (fired in 4 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/0/0  -> 0.67
  [5] Proposal                                     1/1/1  -> 1.00
  [6] Implementation Experience                    1/1/1  -> 1.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The standard currently specifies, by fiat, that `std::execution::when_all()` is ill-formed (§33.9.12.12 [exec.when.all])
candidate 2 (found by 3 of 30 passes): The coalescing option has been implemented against nVidia’s reference implementation of `std::execution` [2].
candidate 3 (found by 2 of 30 passes): The following change represents the coalesce-to-`std::execution::just()` approach (forwarded to LEWG by SG1):
candidate 4 (found by 1 of 30 passes): During SG1 review in Brno 2026 SG1 requested that the author solicit feedback on this issue from Ben Deane and/or Michael Caisse, maintainers of Intel’s “Bare Metal Senders and Receivers” [1].

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

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 1 of 30 passes): During SG1 review in Brno 2026 SG1 requested that the author solicit feedback on this issue from Ben Deane and/or Michael Caisse, maintainers of Intel’s “Bare Metal Senders and Receivers” [1].

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/0/0  -> 0.67
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    1/1/1  -> 1.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): The coalescing option has been implemented against nVidia’s reference implementation of `std::execution` [2].
candidate 2 (found by 3 of 30 passes): [1] https://github.com/intel/cpp-baremetal-senders-and-receivers [2] https://github.com/NVIDIA/stdexec/pull/2124
candidate 3 (found by 1 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.

-->
