Verdict: Weak (3/14)

The paper offers a narrow but real foundation for revisiting `std::execution::task`’s handling of stopped completion, grounded in the recent acceptance of P3950 and the prior restriction on `co_await std::execution::just_stopped()`. Beyond that motivating change, however, the case for standardization is largely undeveloped, with no discussion of affected users, the need for a standard rather than a library solution, coordination with related facilities, or implementation experience.

- The strongest support is the paper’s identification of a concrete gap in the current `std::execution::task` promise type and its connection to the now-accepted P3950 as the enabling change.
- The paper also establishes a clear prior-art and alternatives context by explaining the earlier ban on `co_await std::execution::just_stopped()` and the resulting reliance on `co_yield`.
- The most glaring omission is the absence of any account of who is affected by the current limitation or how the proposed change would address their needs in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.00   accumulate 3.33   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 8
on threshold: motivation, prior_art
splits: prior_art[2] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): While `std::execution::task` supports stopped completion signals the promise type has no bona fide manner in which the coroutine body can emit them.
candidate 2 (found by 2 of 27 passes): Previously if the author of a coroutine body which uses `std::execution::task` wished to end the asynchronous operation with stopped they had to write `co_await` `std::execution::just_stopped()`.
candidate 3 (found by 1 of 27 passes): This was banned before P3950 and therefore `co_yield` was the only viable, general option.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): P3950 [1] proposed changing the above.
candidate 2 (found by 3 of 27 passes): P3950 has now been accepted into the C++29 working draft and therefore the above can be revisited.
candidate 3 (found by 2 of 27 passes): This paper updates the design and wording of `std::execution::task` given the adoption of P3950 [1].

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] Implementation Experience                    0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
