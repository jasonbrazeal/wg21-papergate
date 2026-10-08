Verdict: Adequate (6/14)

The paper’s strongest support comes from compiler behavior, which is the one area it actually establishes, but most of the surrounding case rests on assertions rather than demonstrated need. The thinnest parts are the absence of any argument for why the standard is the right venue and why a library solution cannot suffice.

- The paper establishes implementation experience through concrete compiler agreement and a noted Clang divergence.
- The paper claims relevance and affected users by pointing to implementation agreement, but does not show who depends on the behavior or why the inconsistency matters in practice.
- The paper gestures at prior intent and alternatives but does not develop them into a comparison that justifies the proposed direction.
- The paper offers no case for standardization itself or for why a library-level solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 5 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.67   accumulate 6.67   max 7.67

## SUMMARY
grades: motivation 1.00  audience 0.33  prior_art 1.33  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.00 / 6.50 / 5.50   (all 3 samples: 5.67)
headings: h2 8
on threshold: prior_art, coordination
splits: motivation[2] 0/1/0  motivation[4] 1/0/1  motivation[8] 1/1/0  audience[5] 0/2/0
        prior_art[7] 0/1/1
## END SUMMARY

## motivation - grade 1.00 (fired in 6 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/0  -> 0.33
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/0/1  -> 0.67
  [5] 4 Status quo                                 1/1/1  -> 1.00
  [6] 5 Not all ✅ are created equal              1/1/1  -> 1.00
  [7] 6 Proposed changes                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           1/1/0  -> 0.67
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases
candidate 2 (found by 3 of 27 passes): Note how adding a `this D` overload to an existing member function *F* flips the set of well-formed calls to its complement, because `this D` is best viable function in all cases, rendering *F* obsolete.
candidate 3 (found by 3 of 27 passes): This will render the second example in [[CWG3103]](https://wg21.link/cwg3103) ill-formed as requested.
candidate 4 (found by 2 of 27 passes): This, and the obvious rule that object parameters of the same type correspond, shape the status quo of the wording.

## audience - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/2/0  -> 0.67
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n))

## prior_art - grade 1.33 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 2/2/2  -> 2.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed changes                           0/1/1  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers:
candidate 2 (found by 2 of 27 passes): Worth mentioning that Clang already [rejects](https://godbolt.org/z/Ger8dhheW) `this D` and `this D&` overloads.
candidate 3 (found by 1 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 2/2/2  -> 2.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n)):

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 2/2/2  -> 2.00
  [6] 5 Not all ✅ are created equal              2/2/2  -> 2.00
  [7] 6 Proposed changes                           2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n))
candidate 2 (found by 3 of 27 passes): All implementations [agree](https://godbolt.org/z/WMz5e6s89), with an exception of Clang, which consider `this D` and `this D&` to be corresponding object parameters.
candidate 3 (found by 3 of 27 passes): Worth mentioning that Clang already [rejects](https://godbolt.org/z/Ger8dhheW) `this D` and `this D&` overloads.

-->
