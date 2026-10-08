Verdict: Strong to Excellent (11/14)

The paper offers solid support in several areas, particularly by showing prior art in C2y, implementation experience in GCC, and broad agreement on compatibility with C. The case is thinnest where it needs to explain why standardization is necessary rather than merely convenient, and why a library-level or existing language solution would not suffice.

- The strongest support comes from the feature’s acceptance into C2y and the existence of a committed GCC implementation, which grounds the proposal in both specification and practice.
- The paper clearly identifies the affected audience and the absence of a good alternative in C++ for controlling nested loops.
- The argument for why this belongs in the standard is asserted mainly through C compatibility and portability, but the paper does not develop that into a fuller justification.
- The claim that a library cannot address the need rests only on the observation that `goto` is unavailable in constant expressions, leaving the broader case for language support underdeveloped.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.33   corroborated 11.67   accumulate 11.33   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.83  prior_art 2.00  vehicle 0.83  coordination 2.00  insufficiency 1.00  implementation 1.67
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 12.00 / 11.50 / 10.50   (all 3 samples: 11.33)
headings: h2 10
on threshold: vehicle, insufficiency, implementation
splits: motivation[2] 1/0/0  audience[6] 2/1/2  prior_art[8] 1/0/1  vehicle[5] 2/2/1
        implementation[8] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): `break label` and `continue label` are largely motivated by the ability to control nested loops. This is a highly popular feature in other languages, and C++ could use it too, since it has no good alternative.
candidate 2 (found by 2 of 33 passes): While C++ already has a broad selection of control flow constructs, one construct commonly found in other languages is notably absent: the ability to apply `break` or `continue` to a loop or `switch` when this isn’t the innermost enclosing statement.
candidate 3 (found by 1 of 33 passes): Introduce `break label` and `continue label` to `break` and `continue` out of nested loops and `switch`es as accepted into C2y, and relax label restrictions.
candidate 4 (found by 1 of 33 passes): one construct commonly found in other languages is notably absent: the ability to apply `break` or `continue` to a loop or `switch` when this isn’t the innermost enclosing statement.

## audience - grade 1.83 (fired in 2 of 11 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/1/2  -> 1.67
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The following table counts only control statements with a label, *not* plain `break;`, `continue;`, etc.
candidate 2 (found by 3 of 33 passes): WG21 *overwhelmingly* agrees (based on polls, reflector discussions, and personal conversations) that the design should be compatible with C.

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
  [8] 6. Implementation experience                 1/0/1  -> 0.67
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The `break label` and `continue label` syntax is identical to that in [N3355] and has been accepted into C2y (see working draft at [N3435]).
candidate 2 (found by 3 of 33 passes): There are alternative ways to write this, but all of them have various issues.
candidate 3 (found by 3 of 33 passes): All of these have been discussed in great detail in the first revision of this paper, [P3568R0].
candidate 4 (found by 2 of 33 passes): A GCC implementation of [N3355] has also been committed at [GCC].

## vehicle - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/1  -> 1.67
  [6] 4. Design Considerations                     0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.
candidate 2 (found by 1 of 33 passes): C2y code is much easier to port to C++ (and vice-versa) if both languages support the same control flow constructs.

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
candidate 1 (found by 3 of 33 passes): C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.
candidate 2 (found by 2 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax
candidate 3 (found by 1 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax, as voted at Graz 2025.

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
candidate 1 (found by 3 of 33 passes): `goto` cannot be used in constant expressions.

## implementation - grade 1.67  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design Considerations                     0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 2/2/1  -> 1.67
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): A GCC implementation of [N3355] has also been committed at [GCC].

-->
