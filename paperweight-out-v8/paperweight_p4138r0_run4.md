Verdict: Adequate (5/14)

The paper offers some useful grounding in existing implementation behavior and historical intent, but it does not build a complete case for standardization. The thinnest parts are the absence of any discussion of who is affected, why a standard change is needed rather than a library solution, and how the change would coordinate with existing practice.

- The strongest support is the implementation evidence, including broad compiler agreement on most cases and Clang’s existing rejection of the relevant overloads.
- The paper also establishes prior art by tracing the current wording and intent back to N1821 and the introduction of ref-qualifiers.
- The motivation is only claimed, not established, because the paper asserts that the status quo is problematic without demonstrating the practical consequences.
- The most glaring omission is the lack of any account of who is affected by the change or why the standard, rather than a library or non-normative approach, is the right place to address it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.00   accumulate 5.83   max 5.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 4.50 / 4.50 / 4.50   (all 3 samples: 4.50)
headings: h2 8
on threshold: prior_art
splits: motivation[8] 0/1/0  prior_art[2] 0/1/1
## END SUMMARY

## motivation - grade 1.00 (fired in 5 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/1/1  -> 1.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              1/1/1  -> 1.00
  [7] 6 Proposed changes                           1/1/1  -> 1.00
  [8] 7 Proposed wording                           0/1/0  -> 0.33
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): it doesn’t make much sense to overload member functions with explicit object parameter of non-reference type with member functions of any other kind of object parameter with the same type, ignoring references.
candidate 2 (found by 3 of 27 passes): This, and the obvious rule that object parameters of the same type correspond, shape the status quo of the wording.
candidate 3 (found by 3 of 27 passes): Note how adding a `this D` overload to an existing member function *F* flips the set of well-formed calls to its complement, because `this D` is best viable function in all cases, rendering *F* obsolete.
candidate 4 (found by 3 of 27 passes): This will render the second example in [[CWG3103]](https://wg21.link/cwg3103) ill-formed as requested.

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

## prior_art - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/1  -> 0.67
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 2/2/2  -> 2.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              1/1/1  -> 1.00
  [7] 6 Proposed changes                           0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): All implementations [agree](https://godbolt.org/z/WMz5e6s89), with an exception of Clang, which consider `this D` and `this D&` to be corresponding object parameters.
candidate 2 (found by 2 of 27 passes): While looking at [[CWG3103]](https://wg21.link/cwg3103), I got interested how we arrived at status quo, specifically how [[basic.scope.scope]/3.1](https://eel.is/c++draft/basic.scope.scope#3.1) came to be
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
candidate 1 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n))
candidate 2 (found by 3 of 27 passes): All implementations [agree](https://godbolt.org/z/WMz5e6s89), with an exception of Clang, which consider `this D` and `this D&` to be corresponding object parameters.
candidate 3 (found by 3 of 27 passes): Worth mentioning that Clang already [rejects](https://godbolt.org/z/Ger8dhheW) `this D` and `this D&` overloads.

-->
