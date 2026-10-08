Verdict: Adequate (5/14)

The paper offers solid grounding in implementation behavior and some historical intent, but it leaves the standardization case largely incomplete: it does not identify an affected audience, explain why the standard must change rather than a library or user-side workaround, or address coordination and interoperability concerns.

- The strongest support comes from compiler evidence, with implementations agreeing on 18 of 21 cases and Clang’s divergent treatment of `this D` and `this D&` documented concretely.
- The paper also establishes relevant prior art and historical intent by tracing the special treatment of unqualified member functions back to N1821 and CWG3103.
- The most glaring omission is the absence of any discussion of who is affected by the current wording or the proposed change.
- The paper likewise never establishes why a library solution would not suffice or how the change would coordinate with existing practice and adjacent features.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 3 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 4.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 5.50 / 5.50   (all 3 samples: 5.33)
headings: h2 8
on threshold: motivation, prior_art
splits: motivation[4] 1/1/2  prior_art[4] 1/2/1  prior_art[7] 1/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/1/2  -> 1.33
  [5] 4 Status quo                                 1/1/1  -> 1.00
  [6] 5 Not all ✅ are created equal              2/2/2  -> 2.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases
candidate 2 (found by 2 of 27 passes): This, and the obvious rule that object parameters of the same type correspond, shape the status quo of the wording.
candidate 3 (found by 2 of 27 passes): adding a `this D` overload to an existing member function *F* flips the set of well-formed calls to its complement, because `this D` is best viable function in all cases, rendering *F* obsolete.
candidate 4 (found by 1 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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

## prior_art - grade 1.67 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/2/1  -> 1.33
  [5] 4 Status quo                                 2/2/2  -> 2.00
  [6] 5 Not all ✅ are created equal              1/1/1  -> 1.00
  [7] 6 Proposed changes                           1/0/1  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Clang considers `this D` and `this D&` to correspond (but this might be a desirable direction as discussed in Proposed changes section).
candidate 2 (found by 3 of 27 passes): All implementations [agree](https://godbolt.org/z/WMz5e6s89), with an exception of Clang, which consider `this D` and `this D&` to be corresponding object parameters.
candidate 3 (found by 2 of 27 passes): While looking at [[CWG3103]](https://wg21.link/cwg3103), I got interested how we arrived at status quo
candidate 4 (found by 2 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers:

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

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
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
candidate 1 (found by 3 of 27 passes): All implementations [agree](https://godbolt.org/z/WMz5e6s89), with an exception of Clang, which consider `this D` and `this D&` to be corresponding object parameters.
candidate 2 (found by 3 of 27 passes): Worth mentioning that Clang already [rejects](https://godbolt.org/z/Ger8dhheW) `this D` and `this D&` overloads.
candidate 3 (found by 2 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n))
candidate 4 (found by 1 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n)):

-->
