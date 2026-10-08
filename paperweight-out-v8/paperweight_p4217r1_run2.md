Verdict: Adequate (6/14)

The paper offers meaningful support in the areas of motivation, prior art, and implementation experience, but it leaves several essential parts of the standardization case entirely unaddressed. The thinnest support concerns why this belongs in the standard, how it coordinates with existing specifications, and why a library solution would be insufficient.

- The paper clearly establishes why the current restriction matters and that a viable alternative has been implemented and used in practice.
- It shows credible implementation experience through both a reference implementation and reported use in real code.
- The paper does not establish why the standard itself must change rather than leaving this to a library or vendor extension.
- It is silent on coordination and interoperability with the broader execution model or related proposals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 4 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 6.00   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.50 / 6.00 / 5.00   (all 3 samples: 5.50)
headings: h2 9
on threshold: motivation, prior_art, implementation
splits: audience[4] 1/2/0  implementation[10] 0/2/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): If this restriction were not present the asynchronous operation which results from connecting the result of `std::execution::when_all()` and starting the operation state yielded thereby would hang
candidate 2 (found by 3 of 30 passes): Banning `std::execution::when_all()` (i.e. the status quo) unnecessarily creates a special case when writing generic algorithms.

## audience - grade 0.50 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/2/0  -> 1.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Implementation Experience                    0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.*

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
candidate 2 (found by 3 of 30 passes): The coalescing option has been implemented against nVidia’s reference implementation of `std::execution` [2].
candidate 3 (found by 2 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.*
candidate 4 (found by 2 of 30 passes): The following change represents the coalesce-to-`std::execution::just()` approach (forwarded to LEWG by SG1):

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
  [10] References                                   0/2/0  -> 0.67
candidate 1 (found by 3 of 30 passes): The coalescing option has been implemented against nVidia’s reference implementation of `std::execution` [2].
candidate 2 (found by 1 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.*
candidate 3 (found by 1 of 30 passes): *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect.*
candidate 4 (found by 1 of 30 passes): Ben Deane provided the following: *“a) Yes* `when_all()` *is well-formed for us and completes immediately and synchronously on the* *value channel as you would expect."

-->
