Verdict: Adequate (4/14)

The paper offers a narrow but concrete motivation for its problem, centered on hard-embedded constraints and the risks of pointer arithmetic, but it leaves most of the case for standardization unbuilt. The strongest material concerns why the issue matters; beyond that, the affected audience, prior work, and alternatives are asserted rather than demonstrated, while the need for a standard, interoperability, library inadequacy, and implementation experience are essentially absent.

- The paper does establish a real and clearly stated motivation in environments where dynamic allocation is forbidden and pointer arithmetic can silently escape object bounds.
- Its claims about who is affected rest on a single dated codebase sample, with no evidence that the pattern generalizes or persists.
- The discussion of prior art and alternatives gestures at Profiles, Embedded C++, and P3589, but does not show how those efforts compare with or fail to meet the paper’s specific need.
- The most glaring omission is any argument for why this requires standardization at all, including why a library solution would not suffice or how implementations and ecosystems would coordinate around it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.00   accumulate 4.50   max 5.00

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h2 8
on threshold: motivation, audience
splits: prior_art[6] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 1/1/1  -> 1.00
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 2/2/2  -> 2.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In hard-embedded setups, dynamic allocations are not allowed
candidate 2 (found by 3 of 27 passes): Pointer arithmetic can easily result in pointers outside the bounds of the original value, and is often unintended.

## audience - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 0/0/0  -> 0.00
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 2/2/2  -> 2.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): sampled in 2014, code base of 7M lines, contained 128 dynamic_cast's of which 123 were upcasts or guaranteed downcasts, 4 checked downcasts and 1 crosscast

## prior_art - grade 1.00 (fired in 5 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 1/1/1  -> 1.00
  [6] 5 How to subset                              1/0/0  -> 0.33
  [7] 6 Rules that can be removed under this pr... 1/1/1  -> 1.00
  [8] 7 Combining multiple removal rules under ... 1/1/1  -> 1.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As part of [Profiles](https://wg21.link/P4300) we should have the ability to express a particular feature to be removed from the language or library in a given environment, under a particular profile.
candidate 2 (found by 3 of 27 passes): IAR long shipped a mode called "Embedded C++" that omitted half of C++
candidate 3 (found by 3 of 27 passes): P3589 is the leading proposal for tackling this problem.
candidate 4 (found by 2 of 27 passes): In "Modern C++" it is possible to write code that only uses types that manage heap allocations for you, keeping your own code base free of any new or delete calls.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 0/0/0  -> 0.00
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 0/0/0  -> 0.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 0/0/0  -> 0.00
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 0/0/0  -> 0.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 0/0/0  -> 0.00
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 0/0/0  -> 0.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 0/0/0  -> 0.00
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 0/0/0  -> 0.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidates: (none validated)

-->
