Verdict: Weak to Adequate (3/14)

The paper gives a partial account of why its design choices matter and what alternatives were considered, but it leaves several core justifications for standardization largely unaddressed. The thinnest areas are the absence of a clear affected audience, a rationale for why this belongs in the standard rather than a library, and any evidence of implementation experience.

- The strongest support comes from the explanation that shipping without propagation would lock in explicit allocator specification at every launch site and foreclose transparent propagation through coroutine call trees.
- The paper also credibly establishes prior art and alternatives by citing the authors’ earlier senders-and-coroutines work and contrasting it with the allocator_arg mechanism’s caller-specified approach.
- The claim that a library solution will not do is asserted mainly through the risk of foreclosing a symmetric-transfer completion protocol, but it is not backed up with enough detail to count as established.
- Most glaringly, the paper never establishes who is affected, why the standard is the right venue, how the feature coordinates with existing specifications, or that there is implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.33   accumulate 3.17   max 4.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 41 of 42 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.50 / 3.00 / 3.00   (all 3 samples: 3.17)
headings: h2 5
on threshold: motivation, prior_art
splits: insufficiency[4] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] 3. Not Fixable Post-Ship                     2/2/2  -> 2.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Shipping without propagation locks in a design where every launch site must specify its allocator explicitly, foreclosing transparent propagation through the coroutine call tree.
candidate 2 (found by 2 of 18 passes): task ’s promise_type is a class template instantiated in user code.
candidate 3 (found by 1 of 18 passes): task ’s promise_type is a class template instantiated in user code. Its operator new , allocator selection, stop token storage, environment forwarding, and destruction ordering can change between standard revisions without binary incompatibility.

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

## prior_art - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] 3. Not Fixable Post-Ship                     2/2/2  -> 2.00
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The authors developed P4007R0[2] (“Senders and Coroutines”).
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

## insufficiency - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision History                             0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] 3. Not Fixable Post-Ship                     1/0/0  -> 0.33
  [5] Acknowledgements                             0/0/0  -> 0.00
  [6] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): Shipping this protocol forecloses the `coroutine_handle<>` -returning completion protocol that would enable symmetric transfer.

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
