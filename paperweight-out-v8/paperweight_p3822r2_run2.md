Verdict: Adequate (4/14)

The paper offers only a narrow slice of the support needed to justify standardization: it demonstrates that the feature can be implemented, but leaves most of the surrounding case—who needs it, why the standard is the right venue, and how it fits with existing practice—largely unargued. The thinnest areas are the absence of any identified user constituency and the lack of discussion about why a library-level solution would be inadequate.

- The strongest support is the implementation experience, with a working Clang fork and Compiler Explorer examples showing the feature in use.
- The paper gestures at prior art by noting the inconsistency with conditional noexcept in function declarations, but does not develop that into a substantive comparison or alternative analysis.
- The motivation is asserted rather than demonstrated, with no concrete examples of generic code that is currently blocked or made significantly harder.
- The most glaring omission is the complete silence on who is affected and why the standard, rather than a library or existing workaround, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 3 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 4.00   accumulate 4.33   max 5.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 9
on threshold: motivation
splits: prior_art[7] 0/1/1
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Requires-expressions can be used to assert that an expression is non-throwing, but do not provide a way to do so conditionally, which is sometimes needed in generic programming.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 3 of 10 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 History                                    1/1/1  -> 1.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  0/1/1  -> 0.67
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The lack of support for this syntax is also inconsistent with function declarations, which have had conditional noexcept specifiers since C++11.
candidate 2 (found by 3 of 30 passes): The current syntax for unconditional noexcept specifiers in requirements appears to originate from [[N3701]](https://wg21.link/n3701).
candidate 3 (found by 2 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang fork

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  0/0/0  -> 0.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  2/2/2  -> 2.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   2/2/2  -> 2.00
  [10] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang [fork](https://github.com/yuxuanchen1997/llvm-project/tree/users/yuxuanchen1997/p3822r0-requirements-noexcept), which is available on Compiler Explorer at [https://godbolt.org/z/saYoeWPM9](https://godbolt.org/z/saYoeWPM9).
candidate 2 (found by 2 of 30 passes): A more complete example using this to implement type erasure ([link](https://godbolt.org/z/4rvPMEvdf)):
candidate 3 (found by 1 of 30 passes): A more complete example using this to implement type erasure ([link](https://godbolt.org/z/4rvPMEvdf))

-->
