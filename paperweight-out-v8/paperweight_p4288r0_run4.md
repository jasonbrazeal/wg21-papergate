Verdict: Adequate (5/14)

The paper offers a partial case for standardization, with its clearest support concentrated in motivation and prior art, but it leaves several essential questions about affected users, interoperability, and why a library solution would be insufficient essentially unaddressed. The thinnest areas are those that would normally anchor a proposal in real-world need and integration.

- The paper establishes a clear conceptual motivation by pointing to the ordinary expectation that synchronous functions can return references and that asynchronous functions should be able to do the same.
- It grounds the design discussion in relevant prior art, including the removal of a reference-completing algorithm from the C++26 draft and implementation work against a reference implementation of `std::execution`.
- The argument for why this belongs in the standard is only claimed, resting on a narrow technical observation rather than a broader demonstration of standardization need.
- The paper does not establish who is affected, how the feature would coordinate with existing or planned facilities, or why a library-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 4 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.33   accumulate 5.17   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.00 / 5.00 / 5.50   (all 3 samples: 5.17)
headings: h2 8
on threshold: none
splits: motivation[4] 2/0/2  vehicle[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion  (part 1 of 2)                    2/0/2  -> 1.33
  [5] Discussion  (part 2 of 2)                    2/2/2  -> 2.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Synchronous functions are capable of returning references. This is uncontroversial. Some of the first functions new C++ developers interact with return references (e.g. `std::vector::operator[]`). Therefore it stands to reason that asynchronous functions should have this capability as well.
candidate 2 (found by 3 of 33 passes): While `complete` is convenient as an API it admits only one modality by which the stored completion (if any) can be consumed: Completing an asynchronous operation by sending a completion signal to a receiver.
candidate 3 (found by 2 of 33 passes): The distinction between a by-value completion and an rvalue-reference completion is not what will be deduced by a generic/forwarding `set_value` member function of the receiver, but rather what the ownership model is for that particular argument to the completion.

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

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
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
  [9] Implementation Experience                    1/1/1  -> 1.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Consider the previously-standard [6] algorithm which advertised and sent lvalue references: `std::execution::split` [5].
candidate 2 (found by 3 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` although that implementation is not yet available publicly.
candidate 3 (found by 2 of 33 passes): As adopted into the C++26 working draft in St. Louis `std::execution` had a single asynchronous algorithm which completed with one or more references. It was removed before C++26 shipped [6]
candidate 4 (found by 2 of 33 passes): This suggests an interface similar to `std::visit` over `std::variant`.

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    0/0/1  -> 0.33
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Bolsters the argument made by this paper as a whole, since running destructors while returning from a function does not alter or interfere with the return modality

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
