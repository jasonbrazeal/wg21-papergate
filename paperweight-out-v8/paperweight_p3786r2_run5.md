Verdict: Adequate (5/14)

The paper offers some concrete support for its standardization case, chiefly through implementation experience and engagement with existing proposals, but it leaves several foundational questions about affected users, the need for a standard mechanism, and interoperability largely unaddressed. The thinnest part of the argument is the absence of any discussion of who is affected or why a library solution would be insufficient.

- The strongest support comes from the demonstrated implementation experience, including a Godbolt prototype and a libstdc++ implementation by Tomasz Kamiński.
- The paper also establishes prior art and alternatives by connecting the design to pattern matching work in P2688R5 and the tuplelike concept from P2165.
- The most glaring omission is the lack of any established case for who is affected by the current absence of the feature or why standardization, rather than a library solution, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 3 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.00   accumulate 5.67   max 6.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 5.33)
headings: h2 9
on threshold: prior_art, implementation
splits: motivation[3] 1/2/2  prior_art[8] 0/1/0
## END SUMMARY

## motivation - grade 1.83 (fired in 4 of 10 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Tony Table                                   1/2/2  -> 1.67
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design Space                                 1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): enabling structured binding, integration with `views::elements` and pattern matching once it is approved.
candidate 2 (found by 3 of 30 passes): ❌ span is not compatible with pattern matching
candidate 3 (found by 3 of 30 passes): At the time of writing the only fixed-size library types that do not support structured binding are: `bitset`, `integer_sequence` and `span`.
candidate 4 (found by 2 of 30 passes): Extending the *tuple-protocol* has one unfortunate side effect: It renders the following previously valid code ambiguous.

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
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   1/1/1  -> 1.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/1/0  -> 0.33
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): //interaction with pattern matching proposal P2688R5
candidate 2 (found by 3 of 30 passes): This type of breakage was already explicitly pointed out in P2165 which introduced the tuplelike concept.
candidate 3 (found by 1 of 30 passes): The proposed design has been implemented on Godbolt (https://godbolt.org/z/vrKffnMWr) and by Tomasz Kamiński at https://gcc.gnu.org/pipermail/libstdc++/2025-October/063762.html.

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

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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
