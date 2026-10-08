Verdict: Adequate (6/14)

The paper offers a solid foundation in some areas, particularly in demonstrating prior art and implementation experience, but it leaves several essential parts of the standardization case unaddressed. The thinnest support concerns why this work belongs in the standard, how it coordinates with existing or future features, and why a library solution cannot suffice.

- The strongest support is the concrete implementation experience, with working prototypes in both GCC and Clang and a clear statement that the approach was straightforward to implement.
- The paper also establishes prior art and alternatives by referencing existing mechanisms like P3400R4 and the Clang contract group attribute.
- The case for why the feature matters is established through discussion of compiler bugs, code generation tradeoffs, and the need for fine-grained semantic control.
- The most glaring omission is the absence of any established argument for why the standard, rather than a library or implementation-specific configuration, is the right vehicle for this work.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.50   max 6.67

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 8
on threshold: motivation
splits: motivation[4] 2/0/2  motivation[5] 2/2/1  implementation[4] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/0/2  -> 1.33
  [5] 2 Proposal                                   2/2/1  -> 1.67
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 1/1/1  -> 1.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Sometimes, an assertion might trigger a compiler bug with some semantics — providing a workaround to that sort of problem is essential.
candidate 2 (found by 2 of 27 passes): The more information we can pin down at compile time about the chosen semantic, the better the code we can generate; however there remain use cases for deferring the final selection of semantics until link-time or even run-time.
candidate 3 (found by 2 of 27 passes): Most importantly, by doing this now we also will have enabled satisfying a vast range of use cases that have previously not been directly addressed by ad-hoc configuration options that initial contracts implementations inevitably begin with.
candidate 4 (found by 1 of 27 passes): For 2, we need to make careful provision; the processing that is implied could be required at every call-site, and for each `pre` and `post` condition of the callee.

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 4 Implementation Experience                  0/0/0  -> 0.00
  [7] 5 Conclusion                                 1/1/1  -> 1.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Most importantly, by doing this now we also will have enabled satisfying a vast range of use cases that have previously not been directly addressed
candidate 2 (found by 1 of 27 passes): satisfying a vast range of use cases that have previously not been directly addressed

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Proposal                                   2/2/2  -> 2.00
  [6] 4 Implementation Experience                  2/2/2  -> 2.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): To augment the C++26 Contracts baseline, mechanisms have been proposed that allow code authors to specify the finer granularity in the source code [P3400R4].
candidate 2 (found by 3 of 27 passes): The Clang `[[clang::contract_group(...)]]` attribute, or group labels as specified in [P3400R4], both specify a group (that is a string) that can be attached to a contract assertion.
candidate 3 (found by 3 of 27 passes): Integration with the implementation of [P3097R3], to support contract assertions on virtual functions, also took some extra considerations resulting in treating the seemingly caller-side static type check as callee-side.

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
  [4] 1 Introduction                               1/0/1  -> 0.67
  [5] 2 Proposal                                   2/2/2  -> 2.00
  [6] 4 Implementation Experience                  2/2/2  -> 2.00
  [7] 5 Conclusion                                 0/0/0  -> 0.00
  [8] Acknowledgments                              0/0/0  -> 0.00
  [9] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Prototype implementations in both GCC and Clang have been made available.
candidate 2 (found by 3 of 27 passes): Implementation of this strategy was fairly straightforward in both Clang and GCC.
candidate 3 (found by 3 of 27 passes): This configuration system has been partially implemented in branches of GCC and Clang that are available on compiler explorer.
candidate 4 (found by 2 of 27 passes): Currently, experimental implementations of C++26 Contracts provide much simpler controls over the semantic (which do not implement the fine-grained selection but, rather, express semantics at the TU, or higher, level).

-->
