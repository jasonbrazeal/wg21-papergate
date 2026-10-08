Verdict: Adequate to Strong (7/14)

The paper offers solid support for the existence of a real design problem and for the fact that prior standardization efforts have stalled over fundamental disagreements, but it is much thinner when it comes to showing why the proposed direction belongs in the standard rather than in a library or existing practice. The weakest areas are the absence of a direct case for standardization itself and only asserted, rather than demonstrated, relevance to affected users and implementations.

- The strongest support is the paper’s account of prior art and competing proposals, which clearly establishes that trivial relocation has been seriously considered and remains unresolved.
- The paper also establishes why the topic matters by framing relocate-only types as an unfinished part of C++’s value-type story.
- The case for who is affected rests on named libraries but does not show concretely how they would adopt or benefit from the standardized feature.
- The most glaring omission is any direct argument for why this needs to be in the standard, as opposed to remaining a library-level or vendor-specific technique.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 6.67   max 8.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.00  coordination 0.50  insufficiency 0.17  implementation 1.00
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 7.50 / 6.00 / 6.50   (all 3 samples: 6.67)
headings: h2 9
on threshold: audience
splits: prior_art[7] 2/2/0  prior_art[8] 0/0/1  coordination[5] 2/0/0  coordination[7] 1/0/0
        insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. The semantics of trivial relocation       2/2/2  -> 2.00
  [6] 4. Relocation and the type system            2/2/2  -> 2.00
  [7] 5. The scope of a relocation proposal        2/2/2  -> 2.00
  [8] 6. Summary of design questions               0/0/0  -> 0.00
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Trivial relocation was removed from C++26 due to a number of fundamental design disagreements.
candidate 2 (found by 3 of 30 passes): We believe that the failure to reach consensus was not merely a matter of details, but the result of **fundamental disagreements on several core aspects** of what a relocation feature should look like.
candidate 3 (found by 3 of 30 passes): There is no general relocation primitive in C++ today, and the attempts to add one have stalled (see [P2839R0] and [P2785R3]).
candidate 4 (found by 3 of 30 passes): Extending the scope of a trivial relocation proposal to this position finishes the story: relocate-only types become first-class value types.

## audience - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. The semantics of trivial relocation       2/2/2  -> 2.00
  [6] 4. Relocation and the type system            0/0/0  -> 0.00
  [7] 5. The scope of a relocation proposal        0/0/0  -> 0.00
  [8] 6. Summary of design questions               0/0/0  -> 0.00
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Libraries such as Qt, folly, and BSL have all relied on `memmove`, `realloc`, and related byte-level facilities to implement something equivalent to trivial relocation (in the absence of any Standard-provided primitive).

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. The semantics of trivial relocation       2/2/2  -> 2.00
  [6] 4. Relocation and the type system            2/2/2  -> 2.00
  [7] 5. The scope of a relocation proposal        2/2/0  -> 1.33
  [8] 6. Summary of design questions               0/0/1  -> 0.33
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Trivial relocation was removed from C++26 due to a number of fundamental design disagreements.
candidate 2 (found by 3 of 30 passes): The two main competing proposals for trivial relocation have been [P1144R12] ("std::is_trivially_relocatable") and [P2786R13] ("Trivial Relocatability For C++26").
candidate 3 (found by 3 of 30 passes): [P2786R13] introduced one such operation, and [P3858R0] argued that a lower-level primitive was more appropriate.
candidate 4 (found by 3 of 30 passes): This question was framed in the design of [P1144R12] and [P2786R13] as "sharp-knife" versus "dull-knife" semantics, and the two papers picked opposite answers.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. The semantics of trivial relocation       0/0/0  -> 0.00
  [6] 4. Relocation and the type system            0/0/0  -> 0.00
  [7] 5. The scope of a relocation proposal        0/0/0  -> 0.00
  [8] 6. Summary of design questions               0/0/0  -> 0.00
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.50 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. The semantics of trivial relocation       2/0/0  -> 0.67
  [6] 4. Relocation and the type system            0/0/0  -> 0.00
  [7] 5. The scope of a relocation proposal        1/0/0  -> 0.33
  [8] 6. Summary of design questions               0/0/0  -> 0.00
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Qt, for example, uses `realloc` to grow its container buffers; if the standardized operation does not permit this, Qt will continue to rely on its own mechanism and ignore the Standard feature.
candidate 2 (found by 1 of 30 passes): Extending the scope of a trivial relocation proposal to this position finishes the story: relocate-only types become first-class value types.

## insufficiency - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. The semantics of trivial relocation       0/0/1  -> 0.33
  [6] 4. Relocation and the type system            0/0/0  -> 0.00
  [7] 5. The scope of a relocation proposal        0/0/0  -> 0.00
  [8] 6. Summary of design questions               0/0/0  -> 0.00
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Libraries such as Qt, folly, and BSL have all relied on `memmove`, `realloc`, and related byte-level facilities to implement something equivalent to trivial relocation (in the absence of any Standard-provided primitive).

## implementation - grade 1.00  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. The semantics of trivial relocation       1/1/1  -> 1.00
  [6] 4. Relocation and the type system            1/1/1  -> 1.00
  [7] 5. The scope of a relocation proposal        0/0/0  -> 0.00
  [8] 6. Summary of design questions               0/0/0  -> 0.00
  [9] 7. Acknowledgements                          0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Libraries such as Qt, folly, and BSL have all relied on `memmove`, `realloc`, and related byte-level facilities to implement something equivalent to trivial relocation (in the absence of any Standard-provided primitive).
candidate 2 (found by 3 of 30 passes): Every deployed use of trivial relocation today (as found in third-party libraries) is in effect an optimization of move+destroy.

-->
