Verdict: Weak (2/14)

The paper offers only a thin, largely asserted case for its own standardization. Its strongest material concerns the motivation, but even that rests on claims about design lock-in and allocator propagation that are not substantiated in the text. Beyond that, the document is almost entirely silent on the affected users, prior art, standardization need, interoperability, implementability, and experience.

- The clearest support appears in the motivation, where the paper asserts that shipping without propagation would foreclose transparent allocator injection through the coroutine call tree.
- The discussion of prior art gestures at P4007R0 and the allocator_arg mechanism, but it does not establish how those alternatives compare or why they are insufficient.
- The paper provides no account of who is affected by the problem or what practical burden the current design imposes.
- Most notably, the document offers nothing on implementation experience, why a library solution would not suffice, or how the proposal would coordinate with existing sender and coroutine machinery.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.33/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 2.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.33   corroborated 2.00   accumulate 2.33   max 3.33

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.17  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 2.00 / 2.50 / 2.50   (all 3 samples: 2.33)
headings: h2 5
on threshold: motivation
splits: motivation[3] 0/1/0  prior_art[4] 1/1/2
## END SUMMARY

## motivation - grade 1.17 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/1/0  -> 0.33
  [4] 3. Not Fixable Post-Ship                     2/2/2  -> 2.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): Shipping without propagation locks in a design where every launch site must specify its allocator explicitly, foreclosing transparent propagation through the coroutine call tree.
candidate 2 (found by 1 of 18 passes): `std::execution::task` ([P3552R3](https://wg21.link/p3552r3)[1]) has open issues identified by national ballot comments, LWG issues, and published papers.
candidate 3 (found by 1 of 18 passes): task does not allow the user to specify an allocator at the launch site for coroutine frame allocation. The coroutine frame is allocated by operator new at the call site, before any sender connect / start machinery runs.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 3. Not Fixable Post-Ship                     0/0/0  -> 0.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] 3. Not Fixable Post-Ship                     1/1/2  -> 1.33
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The authors developed P4007R0[2] (“Senders and Coroutines”). The classification below holds regardless of whether any alternative design exists.
candidate 2 (found by 3 of 18 passes): The `allocator_arg` mechanism in [P3552R3](https://wg21.link/p3552r3)[1] works around this by requiring the allocator in the coroutine’s parameter list, but that locks in a caller-specified approach and forecloses environment-based injection.

## vehicle - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 3. Not Fixable Post-Ship                     0/0/0  -> 0.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 3. Not Fixable Post-Ship                     0/0/0  -> 0.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 3. Not Fixable Post-Ship                     0/0/0  -> 0.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 3. Not Fixable Post-Ship                     0/0/0  -> 0.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
