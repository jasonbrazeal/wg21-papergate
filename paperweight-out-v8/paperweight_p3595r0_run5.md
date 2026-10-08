Verdict: Adequate (5/14)

The paper offers concrete evidence of implementability, with working prototypes in both GCC and Clang, but its broader rationale remains largely asserted rather than demonstrated. The thinnest parts of the case concern why this belongs in the standard at all, how it would coordinate with existing or future mechanisms, and why a library-level solution would be insufficient.

- The strongest support is the implementation experience, with prototype implementations in both major compilers and a straightforward integration path described.
- The paper establishes that prior art and alternatives exist, including Clang attributes and group-label mechanisms from P3400R4.
- The claimed motivation and affected audience rest on vague references to “a vast range of use cases” without concrete examples or evidence of demand.
- The most glaring omission is the absence of any argument for why standardization is necessary or why a library cannot provide the same capability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 4 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 1.17  audience 0.33  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 5.00 / 5.50   (all 3 samples: 5.33)
headings: h2 8
on threshold: none
splits: motivation[4] 2/2/0  audience[7] 1/0/1  prior_art[5] 2/1/2  implementation[4] 0/0/1
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/0  -> 1.33
  [5] 2 Proposal                                   1/1/1  -> 1.00
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 1/1/1  -> 1.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The more information we can pin down at compile time about the chosen semantic, the better the code we can generate; however there remain use cases for deferring the final selection of semantics until link-time or even run-time.
candidate 2 (found by 2 of 27 passes): Sometimes, an assertion might trigger a compiler bug with some semantics — providing a workaround to that sort of problem is essential.
candidate 3 (found by 2 of 27 passes): Most importantly, by doing this now we also will have enabled satisfying a vast range of use cases that have previously not been directly addressed by ad-hoc configuration options that initial contracts implementations inevitably begin with.
candidate 4 (found by 1 of 27 passes): by doing this now we also will have enabled satisfying a vast range of use cases that have previously not been directly addressed by ad-hoc configuration options

## audience - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 1/0/1  -> 0.67
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Most importantly, by doing this now we also will have enabled satisfying a vast range of use cases that have previously not been directly addressed by ad-hoc configuration options that initial contracts implementations inevitably begin with.

## prior_art - grade 1.83 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Proposal                                   2/1/2  -> 1.67
  [6] 4 Implementation Experience                  2/2/2  -> 2.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The Clang `[[clang::contract_group(...)]]` attribute, or group labels as specified in [P3400R4], both specify a group (that is a string) that can be attached to a contract assertion.
candidate 2 (found by 2 of 27 passes): mechanisms have been proposed that allow code authors to specify the finer granularity in the source code [P3400R4].
candidate 3 (found by 2 of 27 passes): Integration with [P3400R4] was straightforward as well, capturing the group names and allowed semantics at contract parsing time so that they could be used when the evaluation semantic was needed.
candidate 4 (found by 1 of 27 passes): To augment the C++26 Contracts baseline, mechanisms have been proposed that allow code authors to specify the finer granularity in the source code [P3400R4].

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/1  -> 0.33
  [5] 2 Proposal                                   2/2/2  -> 2.00
  [6] 4 Implementation Experience                  2/2/2  -> 2.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Prototype implementations in both GCC and Clang have been made available.
candidate 2 (found by 3 of 27 passes): Implementation of this strategy was fairly straightforward in both Clang and GCC.
candidate 3 (found by 3 of 27 passes): This configuration system has been partially implemented in branches of GCC and Clang that are available on compiler explorer.
candidate 4 (found by 1 of 27 passes): Currently, experimental implementations of C++26 Contracts provide much simpler controls over the semantic (which do not implement the fine-grained selection but, rather, express semantics at the TU, or higher, level).

-->
