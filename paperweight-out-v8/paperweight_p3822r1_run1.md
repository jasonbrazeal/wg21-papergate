Verdict: Adequate (4/14)

The paper offers only a narrow basis for its own standardization: it can point to a concrete implementation, but most of the surrounding case is asserted rather than demonstrated. The thinnest areas are the absence of any argument for why this belongs in the standard specifically, how it would interact with existing features, and why a library solution is insufficient.

- The strongest support is the existence of a Clang fork implementing the proposed syntax, including linked examples.
- The paper claims the feature matters for generic programming, but does not develop that motivation with substantive use cases or evidence of need.
- The discussion of affected users and alternatives leans on the implementation and an analogy to conditional noexcept in function declarations, without establishing broader impact or prior practice.
- The paper is silent on why the standard is the right venue, how the feature would coordinate with related rules, and why a library approach cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 4 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 4.33   accumulate 4.17   max 5.33

## SUMMARY
grades: motivation 1.00  audience 0.17  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 4.50 / 4.00 / 4.00   (all 3 samples: 4.17)
headings: h2 9
on threshold: motivation
splits: audience[7] 1/0/0
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

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  1/0/0  -> 0.33
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang fork, which should soon be available on Compiler Explorer.

## prior_art - grade 1.00 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Motivation                                 1/1/1  -> 1.00
  [5] 4 History                                    0/0/0  -> 0.00
  [6] 5 Proposal                                   0/0/0  -> 0.00
  [7] 6 Implementation experience                  1/1/1  -> 1.00
  [8] 7 Proposed wording                           0/0/0  -> 0.00
  [9] 8 Appendix                                   0/0/0  -> 0.00
  [10] 9 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The lack of support for this syntax is also inconsistent with function declarations, which have had conditional noexcept specifiers since C++11.
candidate 2 (found by 2 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang fork, which should soon be available on Compiler Explorer.
candidate 3 (found by 1 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang fork, which should soon be available on Compiler Explorer

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
candidate 1 (found by 2 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang [fork](https://github.com/yuxuanchen1997/llvm-project/tree/users/yuxuanchen1997/p3822r0-requirements-noexcept), which should soon be available on Compiler Explorer at [https://godbolt.org/z/saYoeWPM9](https://godbolt.org/z/saYoeWPM9).
candidate 2 (found by 2 of 30 passes): A more complete example using this to implement type erasure ([link](https://godbolt.org/z/4rvPMEvdf)):
candidate 3 (found by 1 of 30 passes): Yuxuan Chen provided an implementation of this proposal in a Clang [fork](https://github.com/yuxuanchen1997/llvm-project/tree/users/yuxuanchen1997/p3822r0-requirements-noexcept)
candidate 4 (found by 1 of 30 passes): A more complete example using this to implement type erasure ([link](https://godbolt.org/z/4rvPMEvdf))

-->
