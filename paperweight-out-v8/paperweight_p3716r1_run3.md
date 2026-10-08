Verdict: Adequate (4/14)

The paper gives a partial account of why the feature area matters and gestures toward some relevant prior work, but it leaves the core standardization rationale largely unargued. The strongest material concerns the motivating problem, while the case for a standard mechanism is thin where it matters most: there is no developed argument for why the standard should act, how the feature would interoperate, or what implementation experience supports it.

- The paper clearly establishes that pointer arithmetic and dynamic allocation are real concerns in hard-embedded environments.
- The discussion of affected users and prior art is suggestive but remains asserted rather than demonstrated with enough detail to carry the standardization argument.
- The paper does not establish why standardization is the right venue, as opposed to a vendor mode or profile outside the standard.
- The absence of any implementation experience or interoperability discussion is the most glaring omission for a proposal of this kind.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.00   accumulate 4.67   max 5.00

## SUMMARY
grades: motivation 1.50  audience 1.17  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.50 / 3.50 / 4.00   (all 3 samples: 3.67)
headings: h2 8
on threshold: motivation, audience
splits: audience[5] 0/0/1
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

## audience - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 0/0/1  -> 0.33
  [6] 5 How to subset                              0/0/0  -> 0.00
  [7] 6 Rules that can be removed under this pr... 2/2/2  -> 2.00
  [8] 7 Combining multiple removal rules under ... 0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): sampled in 2014, code base of 7M lines, contained 128 dynamic_cast's of which 123 were upcasts or guaranteed downcasts, 4 checked downcasts and 1 crosscast
candidate 2 (found by 1 of 27 passes): Many people want to use the "without-C" subset of C++

## prior_art - grade 1.00 (fired in 5 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Prior art                                  0/0/0  -> 0.00
  [4] 3 Revision history                           0/0/0  -> 0.00
  [5] 4 Existing subsetting of C++                 1/1/1  -> 1.00
  [6] 5 How to subset                              1/1/1  -> 1.00
  [7] 6 Rules that can be removed under this pr... 1/1/1  -> 1.00
  [8] 7 Combining multiple removal rules under ... 1/1/1  -> 1.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As part of [Profiles](https://wg21.link/P4300) we should have the ability to express a particular feature to be removed from the language or library in a given environment, under a particular profile.
candidate 2 (found by 3 of 27 passes): IAR long shipped a mode called "Embedded C++" that omitted half of C++
candidate 3 (found by 3 of 27 passes): P3589 is the leading proposal for tackling this problem.
candidate 4 (found by 2 of 27 passes): It is a better idea to define one removal, and to have multiple profiles indirect to the name under which it is removed.

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
