Verdict: Adequate to Strong (7/14)

The paper offers some concrete support for its standardization, chiefly through a reference implementation and a clear statement of the motivating use cases, but much of the surrounding case is asserted rather than demonstrated. The thinnest areas are the absence of any identified affected audience and the reliance on claims about portability, implementation divergence, and the insufficiency of library solutions without supporting evidence.

- The strongest support is the existence of an implementation, which grounds the proposal in practical experience.
- The paper clearly articulates why the separation of extraction and insertion matters for key modification and transferability.
- The discussion of prior art and alternatives gestures toward consistency concerns and implementation freedom, but does not establish how the proposed design resolves them.
- The most glaring omission is the lack of any established audience or demonstrated need among users, leaving the proposal’s relevance largely assumed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.33   accumulate 7.17   max 9.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 1.17  coordination 0.17  insufficiency 0.67  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.00 / 8.00 / 5.50   (all 3 samples: 6.83)
headings: h2 9
on threshold: motivation, prior_art, vehicle, implementation
splits: motivation[3] 1/0/0  prior_art[6] 0/2/0  prior_art[8] 0/1/0  vehicle[5] 1/0/0
        coordination[5] 0/1/0  insufficiency[6] 2/2/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   1/0/0  -> 0.33
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design Space                                 1/1/1  -> 1.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): As we can’t come up with a convincing use-case for such a facility, we don’t propose them and suggest future proposals on this topic to introduce a dedicated `multi-node-handle` instead of changing the conceptual design of `node-handle`.
candidate 2 (found by 2 of 30 passes): Separation of extraction and insertion (compared to the traditional splice-API), thereby enabling: Modifications of the otherwise immutable key.
candidate 3 (found by 1 of 30 passes): // =&gt; extraction and insertion can be separated
candidate 4 (found by 1 of 30 passes): Separation of extraction and insertion (compared to the traditional splice-API), thereby enabling: - Modifications of the otherwise immutable key. - Adding custom logic running between extraction and insertion. - Transferability between compatible containers. - Isolation of source- and target-container.

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

## prior_art - grade 1.33 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design Space                                 0/2/0  -> 0.67
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/1/0  -> 0.33
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): We agree with the criticism that there is a lack of consistency with other node-based sequences, but think the advantages of this new API are very clear:
candidate 2 (found by 1 of 30 passes): As only forward iterators are required, there is sufficient leeway for implementation divergence: MS-STL uses doubly-linked bucket lists whereas libstdc++ uses a singly-linked ones.
candidate 3 (found by 1 of 30 passes): The proposed design has been implemented at https://github.com/MFHava/STL/tree/P3049.

## vehicle - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   1/0/0  -> 0.33
  [6] Design Space                                 2/2/2  -> 2.00
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Therefore we maintain a dedicated `node-handle` type is necessary 5 for portable code.
candidate 2 (found by 1 of 30 passes): As several of these are equally relevant for lists, we propose adding a suitable subset of the `nodehandle` API to the remaining node-based sequence containers, namely `list` and `forward_list`.

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
candidate 1 (found by 1 of 30 passes): Transferability between compatible containers.

## insufficiency - grade 0.67 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Tony Table                                   0/0/0  -> 0.00
  [4] Revisions                                    0/0/0  -> 0.00
  [5] Motivation                                   0/0/0  -> 0.00
  [6] Design Space                                 2/2/0  -> 1.33
  [7] Impact on the Standard                       0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Proposed Wording                             0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Neither of which is mandated for `list` per the standard and at east one implementation does not provide said guarantees due to the usage of sentinel nodes.
candidate 2 (found by 1 of 30 passes): Neither of which is mandated for `list` per the standard and at east one implementation does not provide said guarantees due to the usage of sentinel nodes .

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
candidate 1 (found by 3 of 30 passes): The proposed design has been implemented at https://github.com/MFHava/STL/tree/P3049.

-->
