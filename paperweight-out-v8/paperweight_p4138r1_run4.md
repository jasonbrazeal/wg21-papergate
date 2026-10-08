Verdict: Adequate (5/14)

The paper offers some useful grounding in implementation behavior and prior discussion, but it leaves much of the standardization rationale implicit rather than argued. The strongest material concerns what existing compilers do, while the case for who is affected, why the standard is the right venue, and how the change would coordinate with other work is largely absent.

- The paper’s implementation experience is its best-supported element, with compiler agreement documented across most of the examined cases and a noted Clang divergence.
- The prior art and alternatives section is credited as established, tracing the relevant history and linking the question to CWG3103 and earlier ref-qualifier work.
- The paper only claims, rather than establishes, why the change matters, resting on examples and assertions about overload behavior without a fuller motivating argument.
- The most glaring omissions are the absence of any established discussion of who is affected, why standardization is necessary, coordination and interoperability concerns, or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 3 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.00   accumulate 5.83   max 5.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 55 of 63 section-criterion pairs unanimous (87%)
single-sample totals would have been: 5.00 / 4.50 / 5.00   (all 3 samples: 4.83)
headings: h2 8
on threshold: none
splits: motivation[2] 0/1/0  motivation[5] 0/0/1  motivation[7] 0/1/1  motivation[8] 1/0/0
        prior_art[2] 0/1/1  prior_art[4] 2/1/2  prior_art[6] 1/0/1  prior_art[7] 1/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 6 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/0  -> 0.33
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 1/1/1  -> 1.00
  [5] 4 Status quo                                 0/0/1  -> 0.33
  [6] 5 Not all ✅ are created equal              1/1/1  -> 1.00
  [7] 6 Proposed changes                           0/1/1  -> 0.67
  [8] 7 Proposed wording                           1/0/0  -> 0.33
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This, and the obvious rule that object parameters of the same type correspond, shape the status quo of the wording.
candidate 2 (found by 3 of 27 passes): Note how adding a `this D` overload to an existing member function *F* flips the set of well-formed calls to its complement, because `this D` is best viable function in all cases, rendering *F* obsolete.
candidate 3 (found by 2 of 27 passes): This will render the second example in [[CWG3103]](https://wg21.link/cwg3103) ill-formed as requested.
candidate 4 (found by 1 of 27 passes): it doesn’t make much sense to overload member functions with explicit object parameter of non-reference type with member functions of any other kind of object parameter with the same type, ignoring references.

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

## prior_art - grade 1.83 (fired in 5 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/1  -> 0.67
  [3] 2 Revision History                           0/0/0  -> 0.00
  [4] 3 Background                                 2/1/2  -> 1.67
  [5] 4 Status quo                                 2/2/2  -> 2.00
  [6] 5 Not all ✅ are created equal              1/0/1  -> 0.67
  [7] 6 Proposed changes                           1/1/0  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Clang considers `this D` and `this D&` to correspond (but this might be a desirable direction as discussed in Proposed changes section).
candidate 2 (found by 2 of 27 passes): While looking at [[CWG3103]](https://wg21.link/cwg3103), I got interested how we arrived at status quo
candidate 3 (found by 2 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifiers
candidate 4 (found by 2 of 27 passes): All implementations [agree](https://godbolt.org/z/WMz5e6s89), with an exception of Clang, which consider `this D` and `this D&` to be corresponding object parameters.

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
