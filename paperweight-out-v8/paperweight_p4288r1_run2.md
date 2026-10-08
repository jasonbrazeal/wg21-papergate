Verdict: Adequate (5/14)

The paper offers a narrow but real foundation for its case, centered on the conceptual need for asynchronous functions to return references and on relevant prior art, but it leaves several essential standardization questions essentially unaddressed. The thinnest areas are the lack of evidence about who is affected, why a library solution is insufficient, and how the proposal would coordinate with existing practice.

- The strongest support is the argument that reference-returning synchronous functions are common and that asynchronous functions should have comparable capability.
- The paper also credibly grounds itself in prior art, including an earlier standardized algorithm that advertised lvalue references and an implementation against a reference implementation.
- The most glaring omission is the absence of any established case for why this cannot be done as a library rather than through standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 6.00   accumulate 5.50   max 6.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 80 of 84 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.50 / 5.00 / 5.50   (all 3 samples: 5.33)
headings: h2 9
on threshold: none
splits: motivation[2] 0/0/1  motivation[4] 2/0/2  motivation[5] 2/1/2  prior_art[3] 0/2/2
## END SUMMARY

## motivation - grade 1.83 (fired in 4 of 12 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion  (part 1 of 2)                    2/0/2  -> 1.33
  [5] Discussion  (part 2 of 2)                    2/1/2  -> 1.67
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): Synchronous functions are capable of returning references. This is uncontroversial. Some of the first functions new C++ developers interact with return references (e.g. `std::vector::operator[]`). Therefore it stands to reason that asynchronous functions should have this capability as well.
candidate 2 (found by 3 of 36 passes): While `complete` is convenient as an API it admits only one modality by which the stored completion (if any) can be consumed: Completing an asynchronous operation by sending a completion signal to a receiver.
candidate 3 (found by 1 of 36 passes): This paper proposes that `std::execution` algorithms pass through by-reference result datums from child operations rather than uniformly decay-copying them.
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

## prior_art - grade 2.00 (fired in 4 of 12 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/2/2  -> 1.33
  [4] Discussion  (part 1 of 2)                    2/2/2  -> 2.00
  [5] Discussion  (part 2 of 2)                    2/2/2  -> 2.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    1/1/1  -> 1.00
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [?].
candidate 2 (found by 2 of 36 passes): As adopted into the C++26 working draft in St. Louis `std::execution` had a single asynchronous algorithm which completed with one or more references. It was removed before C++26 shipped [6]
candidate 3 (found by 2 of 36 passes): Now let’s consider the previously-standard [6] algorithm which advertised and sent lvalue references: `std::execution::split` [5].
candidate 4 (found by 2 of 36 passes): At first mirroring the interface of `std::visit` seems appropriate with no completion represented by `std::monostate`. However this falls apart as we once again consider application of this primitive to `std::execution::when_all`.

## vehicle - grade 0.50 (fired in 1 of 12 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion  (part 1 of 2)                    0/0/0  -> 0.00
  [5] Discussion  (part 2 of 2)                    1/1/1  -> 1.00
  [6] Proposal  (part 1 of 2)                      0/0/0  -> 0.00
  [7] Proposal  (part 2 of 2)                      0/0/0  -> 0.00
  [8] Open Design Questions                        0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Revision History                             0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 36 passes): Bolsters the argument made by this paper as a whole, since running destructors while returning from a function does not alter or interfere with the return modality
candidate 2 (found by 1 of 36 passes): The fact that the return must be “suspended” so that one or more intervening synchronous operations (i.e. one or more destructors) may run:

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

## implementation - grade 1.00  [binary: max] (fired in 1 of 12 sections, strong in 0)  (SHARED PASSAGE)
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
