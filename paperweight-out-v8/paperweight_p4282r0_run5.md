Verdict: Weak to Adequate (3/14)

The paper offers a narrow but real basis for its standardization, centered on a concrete gap in `std::execution::task` and the fact that a prior proposal has already been accepted into the working draft. Beyond that motivating change, however, the paper provides almost no supporting case: it does not identify affected users, explain why the standard is the right venue, address interoperability, or show implementation experience.

- The strongest support is the established motivation: the current `task` promise type gives coroutine bodies no direct way to emit a stopped completion signal.
- The paper also credibly grounds itself in prior art by pointing to P3950 and its acceptance into the C++29 working draft.
- The thinnest area is the absence of any established audience or impact, leaving it unclear who would benefit from the change.
- The most glaring omission is the lack of implementation experience, which leaves the proposal without evidence that the design works in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.00   accumulate 3.33   max 4.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.00 / 3.00 / 3.50   (all 3 samples: 3.17)
headings: h2 6
on threshold: motivation, prior_art
splits: motivation[3] 1/1/2  prior_art[2] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/2  -> 1.33
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): While `std::execution::task` supports stopped completion signals the promise type has no bona fide manner in which the coroutine body can emit them.
candidate 2 (found by 3 of 21 passes): Previously if the author of a coroutine body which uses `std::execution::task` wished to end the asynchronous operation with stopped they had to write `co_await` `std::execution::just_stopped()`.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): P3950 [1] proposed changing the above.
candidate 2 (found by 3 of 21 passes): P3950 has now been accepted into the C++29 working draft and therefore the above can be revisited.
candidate 3 (found by 1 of 21 passes): This paper updates the design and wording of `std::execution::task` given the adoption of P3950 [1].

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Acknowledgments                              0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
