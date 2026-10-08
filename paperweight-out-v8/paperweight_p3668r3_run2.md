Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of why defaulted postfix operators would be useful and why a language feature is preferable to a rewrite rule, but it leaves several practical questions about users, library sufficiency, and real-world validation largely unanswered. The strongest material concerns motivation and prior art, while the thinnest support is the complete absence of implementation experience and only asserted claims about who would benefit or why existing library techniques are inadequate.

- The paper establishes a solid motivation by tying the proposal to the near-universal canonical definition of postfix increment and decrement and the boilerplate required to expose it through inheritance.
- The discussion of alternatives is well supported, particularly the rejection of a rewrite rule and the alignment with the C++20 comparison defaulting approach.
- The claim that a library solution will not do is only asserted through a brief example, without showing why such a template cannot adequately serve the affected cases.
- The paper offers no implementation experience, leaving the practical viability and integration cost of the feature entirely unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.67   accumulate 7.83   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 1.67  coordination 1.00  insufficiency 0.33  implementation 0.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 7.50 / 8.00   (all 3 samples: 7.50)
headings: h2 12
on threshold: vehicle, coordination
splits: motivation[7] 2/1/1  vehicle[7] 2/2/0  insufficiency[6] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      2/2/2  -> 2.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 2/2/2  -> 2.00
  [7] 5. Alternatives Considered                   2/1/1  -> 1.33
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Postfix increment and decrement operators have a near-universal canonical definition.
candidate 2 (found by 3 of 39 passes): This reduces boilerplate code while still expressing the universally-known meaning of the function.
candidate 3 (found by 2 of 39 passes): Every parent class which inherits from incrementable must explicitly make the postfix operator visible with a using expression, as the prefix operator in my_class shadows the postfix in incrementable.
candidate 4 (found by 2 of 39 passes): The issue with a rewrite rule is that increment and decrement operators are not as suitable for implicit operations as equality and comparison ones.

## audience - grade 0.50 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/0  -> 0.00
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): The majority of classes written with postfix operations can now simply default them and get an operator which does the right thing.

## prior_art - grade 2.00 (fired in 4 of 13 sections, strong in 3)
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
candidate 2 (found by 3 of 39 passes): One alternative we considered for this change would be a rewrite rule, similar to the C++20 equality and comparison operator changes, such that `a++` could generate a rewritten candidate equivalent to `[&a]{auto copy{a}; ++a; return copy;}()`.
candidate 3 (found by 3 of 39 passes): We do not believe that there is any incompatibility between this paper and P3662.
candidate 4 (found by 3 of 39 passes): This follows the lead of the C++20 comparison changes to defaulted functions, which were largely defined in their own [[class.compare.default]] clause.

## vehicle - grade 1.67 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      1/1/1  -> 1.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 2/2/2  -> 2.00
  [7] 5. Alternatives Considered                   2/2/0  -> 1.33
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Standardising a "default" behaviour for postfix operations would also allow us to shrink the library specification, by expressing operations which are specified to be equivalent to the canonical implementation as being default.
candidate 2 (found by 3 of 39 passes): multiple libraries might all ship their own `incrementable` or `postfix_increment()` variants, which may make slightly different design choices.
candidate 3 (found by 2 of 39 passes): The issue with a rewrite rule is that increment and decrement operators are not as suitable for implicit operations as equality and comparison ones.

## coordination - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## insufficiency - grade 0.33 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Motivation and Scope                      0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 4. Prior Art                                 0/0/2  -> 0.67
  [7] 5. Alternatives Considered                   0/0/0  -> 0.00
  [8] 6. Other Papers in this Space                0/0/0  -> 0.00
  [9] 7. Effect on Existing Code                   0/0/0  -> 0.00
  [10] 8. Implementation Experience                 0/0/0  -> 0.00
  [11] 9. Polls                                     0/0/0  -> 0.00
  [12] 10. Proposed Wording                         0/0/0  -> 0.00
  [13] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): It would be possible to define a free function template postfix operator, which automatically generates the correct operator overloads for the class, for example:

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
