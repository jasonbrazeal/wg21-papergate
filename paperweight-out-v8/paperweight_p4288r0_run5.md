Verdict: Adequate (6/14)

The paper makes a plausible conceptual case that asynchronous operations should be able to return references, and it points to the earlier `std::execution::split` design as relevant prior art. However, the support is thin where standardization proposals usually need to be strongest: there is no demonstrated affected user base, no interoperability or library-only analysis, and no public implementation experience.

- The strongest support is the established motivation that synchronous functions routinely return references, so asynchronous functions should have a coherent way to do the same.
- The paper also credibly establishes relevant prior art through the previously standardized `std::execution::split`, including its removal and the associated dangling-reference concern.
- The argument for why this belongs in the standard rather than a library is only claimed, resting on general appeals to zero-cost abstraction and destructor behavior without concrete standardization rationale.
- The most glaring omission is the absence of any established affected audience, coordination story, or evidence that a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 4 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 6.00   accumulate 5.83   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 6.50 / 5.50   (all 3 samples: 5.83)
headings: h2 8
on threshold: none
splits: motivation[2] 1/0/0  motivation[4] 0/0/2  prior_art[9] 0/0/1  vehicle[4] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion  (part 1 of 2)                    0/0/2  -> 0.67
  [5] Discussion  (part 2 of 2)                    2/2/2  -> 2.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Synchronous functions are capable of returning references. This is uncontroversial. Some of the first functions new C++ developers interact with return references (e.g. `std::vector::operator[]`). Therefore it stands to reason that asynchronous functions should have this capability as well.
candidate 2 (found by 3 of 33 passes): While `complete` is convenient as an API it admits only one modality by which the stored completion (if any) can be consumed: Completing an asynchronous operation by sending a completion signal to a receiver.
candidate 3 (found by 1 of 33 passes): This paper proposes that `std::execution` algorithms pass through by-reference result datums from child operations rather than uniformly decay-copying them.
candidate 4 (found by 1 of 33 passes): This should be changed. Not only is there value in the standard mandating consistency here, but there’s also value in reserving syntactic space for operations which truly send rvalue references

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    0/0/0  -> 0.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion  (part 1 of 2)                    2/2/2  -> 2.00
  [5] Discussion  (part 2 of 2)                    2/2/2  -> 2.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/1  -> 0.33
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): It was removed before C++26 shipped [6] (note that the fact `std::execution::split` completed with references meant that it was the asynchronous analogue of a function which returns a reference to a local variable
candidate 2 (found by 2 of 33 passes): Consider the previously-standard [6] algorithm which advertised and sent lvalue references: `std::execution::split` [5].
candidate 3 (found by 2 of 33 passes): This pattern is seen in the synchronous domain when destructors are run on exit from a function.
candidate 4 (found by 1 of 33 passes): The previously-standard [6] algorithm which advertised and sent lvalue references: `std::execution::split` [5].

## vehicle - grade 0.83 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/2/0  -> 0.67
  [5] Discussion  (part 2 of 2)                    1/1/1  -> 1.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Bolsters the argument made by this paper as a whole, since running destructors while returning from a function does not alter or interfere with the return modality
candidate 2 (found by 1 of 33 passes): Moreover baking such a requirement into C++’s standardized approach to asynchrony would violate C++’s core value proposition: Zero-cost abstractions.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    0/0/0  -> 0.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    0/0/0  -> 0.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    0/0/0  -> 0.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` although that implementation is not yet available publicly.

-->
