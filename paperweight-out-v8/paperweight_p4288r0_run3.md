Verdict: Adequate (5/14)

The paper offers a solid conceptual case for why reference-returning asynchronous operations matter and shows awareness of prior art, but it leaves several practical and procedural questions largely unaddressed. The thinnest areas are the absence of evidence about who is affected, how the feature would coordinate with existing practice, and why a library solution would be insufficient.

- The strongest support is the motivation, which clearly ties the proposal to ordinary C++ reference-returning behavior and to a capability that existed briefly in the C++26 draft before removal.
- The paper also credibly establishes prior art by discussing the earlier `split` algorithm and the St. Louis draft, and by noting an implementation against nVidia’s reference library.
- The case for why this must be standardized rather than provided as a library is not established, leaving a central justification for standardization missing.
- The most glaring omission is the lack of any established account of who is affected, which makes the practical reach and urgency of the proposal hard to assess.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.33   accumulate 5.33   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 5.33)
headings: h2 8
on threshold: none
splits: motivation[2] 0/1/0  prior_art[9] 1/0/1  vehicle[4] 0/0/1  vehicle[5] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    2/2/2  -> 2.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): While `complete` is convenient as an API it admits only one modality by which the stored completion (if any) can be consumed: Completing an asynchronous operation by sending a completion signal to a receiver.
candidate 2 (found by 2 of 33 passes): Synchronous functions are capable of returning references. This is uncontroversial. Some of the first functions new C++ developers interact with return references (e.g. `std::vector::operator[]`). Therefore it stands to reason that asynchronous functions should have this capability as well.
candidate 3 (found by 1 of 33 passes): This paper proposes that `std::execution` algorithms pass through by-reference result datums from child operations rather than uniformly decay-copying them.
candidate 4 (found by 1 of 33 passes): As adopted into the C++26 working draft in St. Louis `std::execution` had a single asynchronous algorithm which completed with one or more references. It was removed before C++26 shipped

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
  [9] Implementation Experience                    1/0/1  -> 0.67
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Consider the previously-standard [6] algorithm which advertised and sent lvalue references: `std::execution::split` [5].
candidate 2 (found by 3 of 33 passes): At first mirroring the interface of `std::visit` seems appropriate with no completion represented by `std::monostate`. However this falls apart as we once again consider application of this primitive to `std::execution::when_all`.
candidate 3 (found by 2 of 33 passes): As adopted into the C++26 working draft in St. Louis `std::execution` had a single asynchronous algorithm which completed with one or more references. It was removed before C++26 shipped [6]
candidate 4 (found by 2 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` although that implementation is not yet available publicly.

## vehicle - grade 0.33 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/1  -> 0.33
  [5] Discussion  (part 2 of 2)                    0/1/0  -> 0.33
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Moreover baking such a requirement into C++’s standardized approach to asynchrony would violate C++’s core value proposition: Zero-cost abstractions.
candidate 2 (found by 1 of 33 passes): Bolsters the argument made by this paper as a whole, since running destructors while returning from a function does not alter or interfere with the return modality

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
