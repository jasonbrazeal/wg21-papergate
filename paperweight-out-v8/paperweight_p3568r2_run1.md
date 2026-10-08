Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing labeled `break` and `continue`, particularly in establishing motivation, affected users, prior art, the need for a language feature, and interoperability with C. The case is thinnest where it relies on claims about implementation experience and the inadequacy of library alternatives, since those points are asserted rather than demonstrated.

- The strongest support comes from the paper’s alignment with C2y and WG14’s accepted syntax, which gives the proposal a clear interoperability and coordination foundation.
- The paper also convincingly shows that the feature addresses a real gap in C++ control flow, with evidence of user demand and the macro-related label restriction problem.
- The discussion of why a library cannot substitute is less convincing, because the cited limitations of `goto` are mentioned but not developed into a full argument against library-based workarounds.
- The most glaring omission is implementation experience, where the paper cites a GCC implementation but does not establish what that experience demonstrates about feasibility, performance, or design stability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 10.00   accumulate 11.50   max 13.00

## SUMMARY
grades: motivation 1.67  audience 2.00  prior_art 2.00  vehicle 1.50  coordination 2.00  insufficiency 1.00  implementation 1.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 11.00 / 11.50 / 11.50   (all 3 samples: 11.17)
headings: h2 10
on threshold: motivation, vehicle, insufficiency
splits: motivation[4] 1/2/1  motivation[6] 1/1/2  audience[4] 1/1/0  prior_art[8] 0/1/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/2/1  -> 1.33
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     1/1/2  -> 1.33
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): While C++ already has a broad selection of control flow constructs, one construct commonly found in other languages is notably absent: the ability to apply `break` or `continue` to a loop or `switch` when this isn’t the innermost enclosing statement.
candidate 2 (found by 3 of 33 passes): `break label` and `continue label` are largely motivated by the ability to control nested loops. This is a highly popular feature in other languages, and C++ could use it too, since it has no good alternative.
candidate 3 (found by 2 of 33 passes): Notably, the restriction that a label can be used only once per function is not usually present in other languages that support `break label`.
candidate 4 (found by 1 of 33 passes): This restriction is especially bad for C and C++ because if `label:` was used in a macro, that macro could only be expanded once per function:

## audience - grade 2.00 (fired in 3 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/0  -> 0.67
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The following table counts only control statements with a label, *not* plain `break;`, `continue;`, etc.
candidate 2 (found by 2 of 33 passes): This feature is popular, simple, and quite useful:
candidate 3 (found by 2 of 33 passes): WG21 *overwhelmingly* agrees (based on polls, reflector discussions, and personal conversations) that the design should be compatible with C.
candidate 4 (found by 1 of 33 passes): WG21 *overwhelmingly* agrees (based on polls, reflector discussions, and personal conversations) that the design should be compatible with C. This is also reflected by a poll at Hagenberg 2025:

## prior_art - grade 2.00 (fired in 4 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/1/1  -> 0.67
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): We bring that syntax into C++ and relax restrictions on labels to make it more powerful, and to address concerns in a follow-up proposal [N3377].
candidate 2 (found by 3 of 33 passes): While the proposed `for name (...)` syntax of [N3377] was de-facto rejected at Graz, the paper brings up legitimate issues with C2y `break label` after [N3355].
candidate 3 (found by 1 of 33 passes): `goto` is similar in complexity and even readability here, however there are some issues:
candidate 4 (found by 1 of 33 passes): `goto` cannot cross (non-vacuous) initialization, which would be an issue if some variable was initialized prior to `std::println`.

## vehicle - grade 1.50 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                1/1/1  -> 1.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): There is *only* one way forward that has a chance of finding consensus: **do what C does.**
candidate 2 (found by 2 of 33 passes): C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.
candidate 3 (found by 1 of 33 passes): Last but not least, C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.

## coordination - grade 2.00 (fired in 2 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): C2y code is much easier to port to C++ (and vice-versa) if both languages support the same control flow constructs.
candidate 2 (found by 2 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax, as voted at Graz 2025.
candidate 3 (found by 1 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax

## insufficiency - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): `goto` cannot cross (non-vacuous) initialization, which would be an issue if some variable was initialized prior to `std::println`.
candidate 2 (found by 1 of 33 passes): `goto` cannot be used in constant expressions.

## implementation - grade 1.00  [binary: max] (fired in 1 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design Considerations                     0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 1/1/1  -> 1.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): A GCC implementation of [N3355] has also been committed at [GCC].

-->
