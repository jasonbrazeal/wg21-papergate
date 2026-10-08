Verdict: Adequate to Strong (7/14)

The paper offers a useful historical account of executor unification and shows that the prior-art landscape was well understood, but it does not carry that analysis forward into a case for why the standard should adopt the proposed facility now. The support is thinnest where the paper needs to move from describing fragmentation and past committee activity to demonstrating that a library solution is insufficient and that standardization is the necessary next step.

- The paper is strongest in establishing prior art and alternatives, particularly through its account of unifying three executor models and the committee’s existing `task` precedent.
- The paper establishes why the general problem of executor fragmentation matters, even if the specific stakes for this proposal remain more asserted than shown.
- The paper claims but does not establish who is affected, leaning on poll results and organization names rather than concrete user or implementer impact.
- The most glaring omission is the absence of any established argument for why the standard is needed or why a library cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 19. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.00   accumulate 7.50   max 8.00

## SUMMARY
grades: motivation 1.83  audience 1.33  prior_art 2.00  vehicle 0.00  coordination 0.67  insufficiency 0.00  implementation 1.33
sample agreement: 74 of 84 section-criterion pairs unanimous (88%)
single-sample totals would have been: 7.00 / 7.50 / 7.00   (all 3 samples: 7.17)
headings: h2 11
on threshold: audience
splits: motivation[6] 2/2/0  motivation[9] 2/2/1  audience[6] 2/0/0  prior_art[4] 1/0/1
        prior_art[6] 2/0/2  coordination[5] 1/0/0  coordination[6] 1/1/0  coordination[9] 1/0/1
        implementation[5] 0/1/1  implementation[9] 0/2/2
## END SUMMARY

## motivation - grade 1.83 (fired in 6 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                1/1/1  -> 1.00
  [6] 3. The Rationale for Unification             2/2/0  -> 1.33
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   2/2/2  -> 2.00
  [9] 7. Questions About the Cost of Multiple M... 2/2/1  -> 1.67
  [10] 8. Anticipated Objections                    1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The unification of three working executor models had unanticipated downstream consequences.
candidate 2 (found by 3 of 36 passes): Each model worked. Each was deployed. Each served its domain.
candidate 3 (found by 3 of 36 passes): The coupling between networking and executors is documented in published papers. The timeline is observable. Is this a cost of unification, or would networking have been delayed regardless?
candidate 4 (found by 3 of 36 passes): Three executor concepts instead of one. Libraries must choose which to target. Interop requires bridges. Fragmentation is a real concern.

## audience - grade 1.33 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/0/0  -> 0.00
  [6] 3. The Rationale for Unification             2/0/0  -> 0.67
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   2/2/2  -> 2.00
  [9] 7. Questions About the Cost of Multiple M... 0/0/0  -> 0.00
  [10] 8. Anticipated Objections                    0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The October 2021 poll: "We believe we need one grand unified model for asynchronous execution" (SF:4 / WF:9 / N:5 / WA:5 / SA:1 - no consensus, leaning in favor).
candidate 2 (found by 1 of 36 passes): More than 100 papers and revisions. Organizations including Google, NVIDIA, Sandia National Labs, Codeplay, Facebook, Nasdaq, Clearpool.io, Microsoft, and RedHat.
candidate 3 (found by 1 of 36 passes): The polls are published. The deployments are published.

## prior_art - grade 2.00 (fired in 6 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                1/0/1  -> 0.67
  [5] 2. Background                                2/2/2  -> 2.00
  [6] 3. The Rationale for Unification             2/0/2  -> 1.33
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   0/0/0  -> 0.00
  [9] 7. Questions About the Cost of Multiple M... 2/2/2  -> 2.00
  [10] 8. Anticipated Objections                    1/1/1  -> 1.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): It unified the three models into a single executor concept with multiple categories (`OneWayExecutor`, `TwoWayExecutor`, `BulkOneWayExecutor`, `BulkTwoWayExecutor`) and customization points.
candidate 2 (found by 3 of 36 passes): The `task` precedent is the sharpest - the committee has already voted to ship a type that fuses two async models into one.
candidate 3 (found by 2 of 36 passes): This paper examines the published record for the evidence that supported the unification decision and documents a terminology shift that erased the continuation framing from the API surface of [P0443R14](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p0443r14.html) [3].
candidate 4 (found by 2 of 36 passes): The sender/receiver model provides structured concurrency, sender composition, completion signatures as type-level contracts, and a customization point model that enables heterogeneous dispatch.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/0/0  -> 0.00
  [6] 3. The Rationale for Unification             0/0/0  -> 0.00
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   0/0/0  -> 0.00
  [9] 7. Questions About the Cost of Multiple M... 0/0/0  -> 0.00
  [10] 8. Anticipated Objections                    0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.67 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                1/0/0  -> 0.33
  [6] 3. The Rationale for Unification             1/1/0  -> 0.67
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   0/0/0  -> 0.00
  [9] 7. Questions About the Cost of Multiple M... 1/0/1  -> 0.67
  [10] 8. Anticipated Objections                    0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): The cross product of N facilities and M algorithms grows without bound. Standard library maintainers who would implement N x M combinations had legitimate reason to want N + M.
candidate 2 (found by 2 of 36 passes): Three executor concepts instead of one. Libraries must choose which to target. Interop requires bridges. Fragmentation is a real concern.
candidate 3 (found by 1 of 36 passes): By 2014, three independent executor proposals existed, each deployed in its domain.

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/0/0  -> 0.00
  [6] 3. The Rationale for Unification             0/0/0  -> 0.00
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   0/0/0  -> 0.00
  [9] 7. Questions About the Cost of Multiple M... 0/0/0  -> 0.00
  [10] 8. Anticipated Objections                    0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 2 of 12 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1. Disclosure                                0/0/0  -> 0.00
  [5] 2. Background                                0/1/1  -> 0.67
  [6] 3. The Rationale for Unification             0/0/0  -> 0.00
  [7] 4. The Published Record                      0/0/0  -> 0.00
  [8] 5. Questions About the Cost of Unification   0/0/0  -> 0.00
  [9] 7. Questions About the Cost of Multiple M... 0/2/2  -> 1.33
  [10] 8. Anticipated Objections                    0/0/0  -> 0.00
  [11] Acknowledgments                              0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Deployed in production for over a decade.
candidate 2 (found by 2 of 36 passes): [P4092R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4092r0.pdf) [35] and [P4093R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2026/p4093r0.pdf) [36] demonstrate coroutine-to-sender and sender-to-coroutine bridges. The implementations exist.

-->
