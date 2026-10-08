Verdict: Adequate (5/14)

The paper offers some useful groundwork in its discussion of prior art and its report of implementation behavior, but it does not yet make a complete case for standardization. The support is thinnest around the affected audience, the need for a standard change rather than another remedy, and the absence of a library-based alternative.

- The strongest support comes from the implementation experience, where compiler agreement is documented across most of the examined cases.
- The paper also establishes prior art by tracing the intent behind ref-qualifiers back to N1821 and engaging with CWG3103.
- The rationale for why the issue matters is only claimed, resting on observations about overload behavior without fully demonstrating the practical impact.
- The most glaring omission is the lack of any established discussion of who is affected or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 4 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 4.67   accumulate 6.33   max 6.00

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.00 / 6.00 / 4.50   (all 3 samples: 5.17)
headings: h2 8
on threshold: prior_art
splits: motivation[6] 1/2/1  motivation[8] 0/1/0  prior_art[5] 2/1/1  prior_art[6] 0/1/0
        coordination[5] 0/2/0
## END SUMMARY

## motivation - grade 1.17 (fired in 5 of 9 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 1/1/1  -> 1.00
  [5] 4 Status quo                                 1/1/1  -> 1.00
  [6] 5 Not all ✅ are created equal              1/2/1  -> 1.33
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/1/0  -> 0.33
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): it doesn’t make much sense to overload member functions with explicit object parameter of non-reference type with member functions of any other kind of object parameter with the same type, ignoring references.
candidate 2 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases
candidate 3 (found by 2 of 27 passes): This, and the obvious rule that object parameters of the same type correspond, shape the status quo of the wording.
candidate 4 (found by 2 of 27 passes): While it’s possible to get ahold of functions #1 and #3 (via address of an overload set) and call them, it’s not clear why they need to be a part of their respective overload sets in the first place.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 2/2/2  -> 2.00
  [5] 4 Status quo                                 2/1/1  -> 1.33
  [6] 5 Not all ✅ are created equal              0/1/0  -> 0.33
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): While looking at [CWG3103](https://cplusplus.github.io/CWG/issues/3103.html), I got interested how we arrived at status quo
candidate 2 (found by 3 of 27 passes): Clang sometimes considers `(this) + (this D&)` and `(this) + () &` cases to correspond, but this might be a desirable direction as discussed in section.
candidate 3 (found by 2 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifier:
candidate 4 (found by 1 of 27 passes): The intent to give member functions with no ref-qualifier special treatment can be tracked all the way to [[N1821] (Extending Move Semantics To *this (Revision 2))](https://wg21.link/n1821), which introduced ref-qualifier

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/2/0  -> 0.67
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n)):

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 0/0/0  -> 0.00
  [6] 5 Not all ✅ are created equal              0/0/0  -> 0.00
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Background                                 0/0/0  -> 0.00
  [5] 4 Status quo                                 2/2/2  -> 2.00
  [6] 5 Not all ✅ are created equal              2/2/2  -> 2.00
  [7] 6 Proposed approach                          0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Implementations agree on 18 out of 21 cases ([Compiler Explorer](https://godbolt.org/z/aM963qh8n))
candidate 2 (found by 3 of 27 passes): All implementations [agree](https://godbolt.org/z/baPGKKq39), with an exception of Clang, which considers more cases conflicting, as described in the previous section.

-->
