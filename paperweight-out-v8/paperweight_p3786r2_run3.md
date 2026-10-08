Verdict: Adequate (5/14)

The paper offers real but uneven support for its own standardization, with the strongest evidence concentrated in implementation experience and prior art, while the rationale for why this belongs in the standard rather than a library is essentially absent. The thinnest areas are the failure to identify who is affected and the lack of any argument that a library solution would be insufficient.

- The paper establishes implementation experience through working examples on Godbolt and a libstdc++ implementation by Tomasz Kamiński.
- The paper establishes prior art and alternatives by referencing pattern matching proposal P2688R5 and the breakage already noted in P2165.
- The paper claims coordination and interoperability concerns around `span` but does not establish them, leaving the interaction with existing types under-argued.
- The paper does not establish why the standard is the right venue or why a library would not do, which is the most glaring omission for a standardization proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.33   accumulate 6.00   max 6.33

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 6.00 / 5.00   (all 3 samples: 5.33)
headings: h2 9
on threshold: motivation, prior_art, implementation
splits: motivation[3] 1/2/1  prior_art[8] 0/1/1  coordination[5] 0/1/0
## END SUMMARY

## motivation - grade 1.67 (fired in 4 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   1/2/1  -> 1.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design Space                                 1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): enabling structured binding, integration with `views::elements` and pattern matching once it is approved.
candidate 2 (found by 3 of 30 passes): ❌ span is not compatible with pattern matching
candidate 3 (found by 3 of 30 passes): Extending the *tuple-protocol* has one unfortunate side effect: It renders the following previously valid code ambiguous.
candidate 4 (found by 2 of 30 passes): At the time of writing the only fixed-size library types that do not support structured binding are: `bitset`, `integer_sequence` and `span`.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/1/1  -> 0.67
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): //interaction with pattern matching proposal P2688R5
candidate 2 (found by 3 of 30 passes): This type of breakage was already explicitly pointed out in P2165 which introduced the tuplelike concept.
candidate 3 (found by 2 of 30 passes): The proposed design has been implemented on Godbolt (https://godbolt.org/z/vrKffnMWr) and by Tomasz Kamiński at https://gcc.gnu.org/pipermail/libstdc++/2025-October/063762.html.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/1/0  -> 0.33
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): For `span` we lack such a clear rationale.

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 0/0/0  -> 0.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    2/2/2  -> 2.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The proposed design has been implemented on Godbolt (https://godbolt.org/z/vrKffnMWr) and by Tomasz Kamiński at https://gcc.gnu.org/pipermail/libstdc++/2025-October/063762.html.

-->
