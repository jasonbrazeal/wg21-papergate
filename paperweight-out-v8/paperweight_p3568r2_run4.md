Verdict: Excellent (12/14)

The paper offers substantial support for standardizing labeled `break` and `continue`, particularly through its alignment with C2y, evidence of user interest, and clear motivation around nested control flow. The case is thinnest where it relies on claims about implementation experience and the inadequacy of library alternatives without demonstrating those points in the proposal itself.

- The strongest support comes from the established compatibility story: C2y has already adopted the syntax, WG14 will not revisit it, and C++ consensus favors matching C.
- The paper also clearly establishes why the feature matters and who is affected, citing both widespread user interest and the macro-related label restriction problem.
- The most glaring omission is implementation experience, which is only claimed through a GCC commit and not established as evidence of feasibility or maturity.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (12.00/14)

Provisionally addressed: 7 of 7. Provisional points: 12.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 12.00   corroborated 12.00   accumulate 12.00   max 13.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 1.00  implementation 1.00
sample agreement: 77 of 77 section-criterion pairs unanimous (100%)
single-sample totals would have been: 12.00 / 12.00 / 12.00   (all 3 samples: 12.00)
headings: h2 10
on threshold: insufficiency
splits: none
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): While C++ already has a broad selection of control flow constructs, one construct commonly found in other languages is notably absent: the ability to apply `break` or `continue` to a loop or `switch` when this isn’t the innermost enclosing statement.
candidate 2 (found by 3 of 33 passes): `break label` and `continue label` are largely motivated by the ability to control nested loops. This is a highly popular feature in other languages, and C++ could use it too, since it has no good alternative.
candidate 3 (found by 2 of 33 passes): Notably, the restriction that a label can be used only once per function is not usually present in other languages that support `break label`.
candidate 4 (found by 1 of 33 passes): This restriction is especially bad for C and C++ because if `label:` was used in a macro, that macro could only be expanded once per function:

## audience - grade 2.00 (fired in 2 of 11 sections, strong in 2)
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
candidate 1 (found by 3 of 33 passes): [StackOverflow] *"Can I use break to exit multiple nested `for` loops?"* shows that there is interest in this feature (393K views at the time of writing).
candidate 2 (found by 2 of 33 passes): WG21 *overwhelmingly* agrees (based on polls, reflector discussions, and personal conversations) that the design should be compatible with C.
candidate 3 (found by 1 of 33 passes): WG21 *overwhelmingly* agrees (based on polls, reflector discussions, and personal conversations) that the design should be compatible with C. This is also reflected by a poll at Hagenberg 2025:

## prior_art - grade 2.00 (fired in 3 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): We bring that syntax into C++ and relax restrictions on labels to make it more powerful, and to address concerns in a follow-up proposal [N3377].
candidate 2 (found by 2 of 33 passes): `goto` is similar in complexity and even readability here, however there are some issues:
candidate 3 (found by 2 of 33 passes): While the proposed `for name (...)` syntax of [N3377] was de-facto rejected at Graz, the paper brings up legitimate issues with C2y `break label` after [N3355].
candidate 4 (found by 1 of 33 passes): The `break label` and `continue label` syntax is identical to that in [N3355] and has been accepted into C2y (see working draft at [N3435]).

## vehicle - grade 2.00 (fired in 2 of 11 sections, strong in 2)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 33 passes): C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.
candidate 2 (found by 3 of 33 passes): There is *only* one way forward that has a chance of finding consensus: **do what C does.**

## coordination - grade 2.00 (fired in 2 of 11 sections, strong in 2)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 33 passes): C2y code is much easier to port to C++ (and vice-versa) if both languages support the same control flow constructs.
candidate 2 (found by 2 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax, as voted at Graz 2025.
candidate 3 (found by 1 of 33 passes): C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.
candidate 4 (found by 1 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax

## insufficiency - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
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
