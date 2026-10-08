Verdict: Strong to Excellent (11/14)

The paper offers solid support for the need to standardize labeled `break` and `continue` in C++, particularly through its arguments about C compatibility, prior art, and the absence of good alternatives. The thinnest parts of the case concern evidence about who is affected, why a library solution is insufficient, and whether there is meaningful implementation experience.

- The strongest support is the coordination argument: WG14 has already accepted the syntax into C2y and is unwilling to revisit it, making C++ alignment the only realistic path to consensus.
- The paper also clearly establishes why the feature matters and why existing alternatives are inadequate, with the C2y portability concern reinforcing the standardization rationale.
- The most glaring omission is the lack of established evidence about who is affected, since the cited poll and usage counts are presented as claims rather than demonstrated need.
- The case against a library solution is also thin, resting on a single observation about `goto` in constant expressions without broader justification.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 10.67   accumulate 10.83   max 12.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.67  coordination 2.00  insufficiency 1.00  implementation 1.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 11.00 / 11.50 / 10.00   (all 3 samples: 10.83)
headings: h2 10
on threshold: audience, insufficiency
splits: audience[4] 0/1/0  prior_art[4] 2/0/2  vehicle[5] 2/2/1  vehicle[6] 2/2/1
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
candidate 3 (found by 3 of 33 passes): Notably, the restriction that a label can be used only once per function is not usually present in other languages that support `break label`.

## audience - grade 1.17 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     0/0/0  -> 0.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The following table counts only control statements with a label, *not* plain `break;`, `continue;`, etc.
candidate 2 (found by 1 of 33 passes): This feature is popular, simple, and quite useful:
candidate 3 (found by 1 of 33 passes): The following is a committee-style poll (source: [TCCPP]) from the Discord server [Together C & C++](https://discord.gg/tccpp), which is the largest server in terms of C++-focused message activity:

## prior_art - grade 2.00 (fired in 3 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/0/2  -> 1.33
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design Considerations                     2/2/2  -> 2.00
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): There are alternative ways to write this, but all of them have various issues.
candidate 2 (found by 3 of 33 passes): All of these have been discussed in great detail in the first revision of this paper, [P3568R0].
candidate 3 (found by 2 of 33 passes): The `break label` and `continue label` syntax is identical to that in [N3355] and has been accepted into C2y (see working draft at [N3435]).

## vehicle - grade 1.67 (fired in 2 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/1  -> 1.67
  [6] 4. Design Considerations                     2/2/1  -> 1.67
  [7] 5. Impact on existing code                   0/0/0  -> 0.00
  [8] 6. Implementation experience                 0/0/0  -> 0.00
  [9] 7. Proposed wording                          0/0/0  -> 0.00
  [10] 8. Acknowledgements                          0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): C2y code is much easier to port to C++ (and vice-versa) if both languages support the same control flow constructs.
candidate 2 (found by 2 of 33 passes): There is *only* one way forward that has a chance of finding consensus: **do what C does.**
candidate 3 (found by 1 of 33 passes): WG21 *overwhelmingly* agrees (based on polls, reflector discussions, and personal conversations) that the design should be compatible with C.

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
candidate 1 (found by 2 of 33 passes): C++ should have `break label` and `continue label` to increase the amount of code that has a direct equivalent in C.
candidate 2 (found by 2 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax
candidate 3 (found by 1 of 33 passes): C2y code is much easier to port to C++ (and vice-versa) if both languages support the same control flow constructs.
candidate 4 (found by 1 of 33 passes): WG14 has already accepted the `label: for` syntax of [N3355] into C2y, and WG14 is unwilling to revisit this syntax, as voted at Graz 2025.

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
