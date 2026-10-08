Verdict: Adequate to Strong (7/14)

The paper offers a reasonably grounded motivation for defaulted postfix increment and decrement, but its case for standardization leans heavily on assertion rather than demonstrated need, especially where affected users, standard-library interaction, and practical experience are concerned. The strongest material is the discussion of why the operation is canonical and why existing library-based alternatives fall short, while the thinnest is the absence of any implementation experience or evidence about the scale and nature of real-world impact.

- The paper clearly establishes why the feature matters by tying it to a near-universal canonical definition and to reduced user error in ordinary classes.
- The discussion of prior art and alternatives is substantive, particularly in explaining why a rewrite rule is unsuitable and how the proposal follows the C++20 defaulted-comparison model.
- The claims about who is affected and why a library solution will not do are plausible but not backed by concrete evidence of existing practice or user demand.
- The most glaring omission is implementation experience, for which the paper provides nothing to show feasibility, compiler cost, or real-world validation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 7.33   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 1.17  coordination 1.00  insufficiency 0.50  implementation 0.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.50 / 8.00 / 6.50   (all 3 samples: 7.33)
headings: h2 12
on threshold: vehicle, coordination
splits: audience[2] 0/0/1  audience[4] 1/2/0  vehicle[4] 1/0/0  insufficiency[6] 1/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 2/2/2  -> 2.00
  [7] 5. Alternatives Considered                   2/2/2  -> 2.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Postfix increment and decrement operators have a near-universal canonical definition.
candidate 2 (found by 3 of 39 passes): The issue with a rewrite rule is that increment and decrement operators are not as suitable for implicit operations as equality and comparison ones.
candidate 3 (found by 2 of 39 passes): It reduces the possibility for user error when writing such operators - typical classes won’t need their implementation of such functions checked and debugged; and atypical ones will have their explicitly-defined operators stand out by virtue of not being defaulted.
candidate 4 (found by 2 of 39 passes): There are several existing approaches to attempt a similar reduction in boilerplate. Our position is that none of them quite find the best way to express user intent in code, and will examine them here.

## audience - grade 0.67 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/2/0  -> 1.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): Postfix increment and decrement operators have a near-universal canonical definition.
candidate 2 (found by 1 of 39 passes): The majority of classes written with postfix operations can now simply default them and get an operator which does the right thing.
candidate 3 (found by 1 of 39 passes): The authors have identified 53 candidate operations which could be defaulted and remain semantically equivalent to their current behaviour, and have written [P3785] to explore defaulting them.

## prior_art - grade 2.00 (fired in 4 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Alternatives Considered                   2/2/2  -> 2.00
  [8] 6. Other Papers in this Space                2/2/2  -> 2.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         2/2/2  -> 2.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The authors have identified 53 candidate operations which could be defaulted and remain semantically equivalent to their current behaviour, and have written [P3785] to explore defaulting them.
candidate 2 (found by 3 of 39 passes): We do not believe that there is any incompatibility between this paper and P3662.
candidate 3 (found by 3 of 39 passes): This follows the lead of the C++20 comparison changes to defaulted functions, which were largely defined in their own [[class.compare.default]] clause.
candidate 4 (found by 2 of 39 passes): One alternative we considered for this change would be a rewrite rule, similar to the C++20 equality and comparison operator changes, such that `a++` could generate a rewritten candidate equivalent to `[&a]{auto copy{a}; ++a; return copy;}()`.

## vehicle - grade 1.17 (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/0/0  -> 0.33
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 2/2/2  -> 2.00
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): There is also benefit in standardising the way to retrieve this default - multiple libraries might all ship their own `incrementable` or `postfix_increment()` variants, which may make slightly different design choices.
candidate 2 (found by 1 of 39 passes): Standardising a "default" behaviour for postfix operations would also allow us to shrink the library specification, by expressing operations which are specified to be equivalent to the canonical implementation as being default.

## coordination - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 2/2/2  -> 2.00
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): multiple libraries might all ship their own `incrementable` or `postfix_increment()` variants, which may make slightly different design choices.

## insufficiency - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 1/2/0  -> 1.00
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): Mixins open the door to potentially confusing semantics, such as my_class being pointer-interconvertible with incrementable
candidate 2 (found by 1 of 39 passes): This approach is opt-out, rather than opt-in, with every copyable and prefix-incrementable class automatically gaining postfix operations whether they make sense or not; and so opens the door to additional surprise features.

## implementation - grade 0.00  [binary: max] (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
