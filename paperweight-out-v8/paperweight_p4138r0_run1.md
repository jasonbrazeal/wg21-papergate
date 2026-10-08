Verdict: Adequate (5/14)

The paper offers some useful historical and implementation grounding, but it leaves the core rationale for standardization largely asserted rather than demonstrated. The thinnest parts concern who is actually affected, why a language change is necessary, and why a library-level solution would not suffice.

- The strongest support comes from implementation experience, with compiler agreement documented across most of the examined cases and a concrete divergence identified in Clang.
- The paper also establishes prior art by tracing the relevant intent back through CWG3103 and N1821, showing the question has a real history.
- The claim that the change matters rests mainly on assertions about overload behavior and obsolescence, without evidence of practical impact on users.
- The most glaring omission is the absence of any established case for why the standard must change, who is affected, or why a library cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.33   accumulate 6.33   max 6.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 6.00 / 5.50 / 4.50   (all 3 samples: 5.33)
headings: h2 8
on threshold: motivation
splits: motivation[4] 1/0/1  motivation[6] 2/2/1  motivation[8] 1/0/0  prior_art[4] 2/2/1
        prior_art[5] 1/2/2  prior_art[6] 1/0/0  coordination[5] 2/0/0
## END SUMMARY

## motivation - grade 1.33 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/0/1  -> 0.67
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              2/2/1  -> 1.67
  [7] 6 Proposed changes                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           1/0/0  -> 0.33
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): it doesn’t make much sense to overload member functions with explicit object parameter of non-reference type with member functions of any other kind of object parameter with the same type, ignoring references.
candidate 2 (found by 3 of 27 passes): This will render the second example in [[CWG3103]](https://wg21.link/cwg3103) ill-formed as requested.
candidate 3 (found by 2 of 27 passes): This, and the obvious rule that object parameters of the same type correspond, shape the status quo of the wording.
candidate 4 (found by 2 of 27 passes): adding a `this D` overload to an existing member function *F* flips the set of well-formed calls to its complement, because `this D` is best viable function in all cases, rendering *F* obsolete.

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

## prior_art - grade 1.67 (fired in 4 of 9 sections, strong in 2)
under each rule: top2 1.67   corroborated 1.67   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 2/2/1  -> 1.67
  [5] 4 Status quo                                 1/2/2  -> 1.67
  [6] 5 Not all ✅ are created equal              1/0/0  -> 0.33
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): While looking at [[CWG3103]](https://wg21.link/cwg3103), I got interested how we arrived at status quo
candidate 2 (found by 3 of 27 passes): Clang considers `this D` and `this D&` to correspond (but this might be a desirable direction as discussed in Proposed changes section).
candidate 3 (found by 2 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers:
candidate 4 (found by 1 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers

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

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 2/0/0  -> 0.67
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n))

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
