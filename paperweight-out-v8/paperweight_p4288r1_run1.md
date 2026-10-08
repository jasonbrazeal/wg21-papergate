Verdict: Adequate (5/14)

The paper offers some grounding for its central concern, particularly in showing that reference-returning asynchronous completions raise real specification questions and that prior art exists, but it leaves the standardization case largely unbuilt. The thinnest support is around who is affected, why the standard is the right venue, and whether a library solution would suffice.

- The strongest support is the paper’s identification of a genuine ambiguity in `std::execution`’s handling of reference completions and its connection to removed prior art.
- The discussion of alternatives shows awareness of design trade-offs, though it does not by itself justify standardization.
- The paper does not establish who is affected by the problem or what practical code is blocked without a standard change.
- The most glaring omission is the absence of any argument for why this cannot be addressed as a library or why standardization is necessary now.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.00   accumulate 5.00   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 82 of 84 section-criterion pairs unanimous (98%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h2 9
on threshold: none
splits: prior_art[5] 2/0/2  prior_art[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 12 sections, strong in 3)
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
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Synchronous functions are capable of returning references. This is uncontroversial. Some of the first functions new C++ developers interact with return references (e.g. `std::vector::operator[]`). Therefore it stands to reason that asynchronous functions should have this capability as well.
candidate 2 (found by 3 of 36 passes): While `complete` is convenient as an API it admits only one modality by which the stored completion (if any) can be consumed: Completing an asynchronous operation by sending a completion signal to a receiver.
candidate 3 (found by 2 of 36 passes): The distinction between a by-value completion and an rvalue-reference completion is not what will be deduced by a generic/forwarding `set_value` member function of the receiver, but rather what the ownership model is for that particular argument to the completion.
candidate 4 (found by 1 of 36 passes): The above brings into focus a problematic flexibility/ambiguity in the specification of `std::execution`.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion  (part 1 of 2)                    2/2/2  -> 2.00
  [5] Discussion  (part 2 of 2)                    2/0/2  -> 1.33
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/1/0  -> 0.33
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Consider the previously-standard [6] algorithm which advertised and sent lvalue references: `std::execution::split` [5].
candidate 2 (found by 2 of 36 passes): As adopted into the C++26 working draft in St. Louis `std::execution` had a single asynchronous algorithm which completed with one or more references. It was removed before C++26 shipped [6]
candidate 3 (found by 1 of 36 passes): It was removed before C++26 shipped [6] (note that the fact `std::execution::split` completed with references meant that it was the asynchronous analogue of a function which returns a reference to a local variable
candidate 4 (found by 1 of 36 passes): At first mirroring the interface of `std::visit` seems appropriate with no completion represented by `std::monostate`. However this falls apart as we once again consider application of this primitive to `std::execution::when_all`.

## vehicle - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 12 sections, strong in 0)
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
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 12 sections, strong in 0)
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
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [?].

-->
