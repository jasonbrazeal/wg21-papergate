Verdict: Adequate (5/14)

The paper offers some concrete implementation evidence and a reasonably clear account of prior art, but its central rationale for standardization rests largely on assertion rather than demonstrated need. The thinnest parts are the absence of any discussion of coordination with existing features or why a library solution cannot provide the behavior, which leaves the standardization case incomplete.

- The strongest support is the implementation experience, with working branches in both GCC and Clang and a description of how the feature integrates with existing contracts machinery.
- The discussion of prior art and alternatives is also established, showing how the proposal relates to other contracts papers and existing evaluation-semantic infrastructure.
- The paper only claims, without establishing, why the feature matters and who is affected, relying on general statements about domains and concerns rather than concrete motivating cases.
- The most glaring omission is the lack of any coordination and interoperability analysis or any argument for why a library cannot provide the semantics, leaving key standardization questions unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.33/14)

Provisionally addressed: 5 of 7. Provisional points: 5.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.33   corroborated 5.67   accumulate 6.67   max 6.67

## SUMMARY
grades: motivation 1.00  audience 0.33  prior_art 1.50  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 88 of 91 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.00 / 6.50 / 5.50   (all 3 samples: 5.33)
headings: h2 9 + bold numbered 3
on threshold: prior_art, implementation
splits: motivation[4] 0/2/0  audience[7] 0/2/0  prior_art[7] 0/0/2
## END SUMMARY

## motivation - grade 1.00 (fired in 4 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/2/0  -> 0.67
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 3 Additional Rationale                       1/1/1  -> 1.00
  [7] 4 Implementation Experience                  0/0/0  -> 0.00
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            1/1/1  -> 1.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This essential behavior is needed in many domains, but introduces concerns in others where no exception could escape safely or without the need for significant additional overhead.
candidate 2 (found by 3 of 39 passes): Because we have chosen to name the new semantics with the use of `noexcept` as an adverb, the choice with the least surprise for users is to invoke `std::terminate()`.
candidate 3 (found by 3 of 39 passes): This small addition to C++26 Contracts will enable fine-grained control over the support for exceptions, allowing people to mitigate many of the concerns that have been expressed with throwing violation handlers.
candidate 4 (found by 1 of 39 passes): When an exception emanates from undefined behavior there is no onus on the compiler and runtime to make that exception propagate properly.

## audience - grade 0.33 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 3 Additional Rationale                       0/0/0  -> 0.00
  [7] 4 Implementation Experience                  0/2/0  -> 0.67
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): A variant of this proposal was originally suggested and implemented by Ville Voutilainen. It has since been implemented in this form in the P3850 branches of both GCC and Clang that are available on Compiler Explorer.

## prior_art - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Proposal                                   1/1/1  -> 1.00
  [6] 3 Additional Rationale                       2/2/2  -> 2.00
  [7] 4 Implementation Experience                  0/0/2  -> 0.67
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): With the potential adoption of [P3400R4], assertion-control objects (i.e., labels) could allow for selecting locally whether a given contract assertion should support exceptions escaping from a violation of a particular assertion.
candidate 2 (found by 3 of 39 passes): Then, if [P3290R6] is adopted first, update its behavior to pass through the new semantics when using the `noexcept` entry points:
candidate 3 (found by 3 of 39 passes): Unlike when a violation handler throws from the `assert` macro (as proposed in [P3290R6]) we propose that an exception from the contract-violation handler where one of the new semantics has been used results in invoking `std::terminate()`.
candidate 4 (found by 1 of 39 passes): The two new semantics were added as ordinary `evaluation_semantic` enumerators, which let them flow through the entire existing resolution pipeline — the `-fcontract-evaluation-semantic=` default, per-group configuration, JSON configuration files, and the assertion-control labels of [P3400R4]

## vehicle - grade 0.50 (fired in 1 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 3 Additional Rationale                       1/1/1  -> 1.00
  [7] 4 Implementation Experience                  0/0/0  -> 0.00
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Because we have chosen to name the new semantics with the use of `noexcept` as an adverb, the choice with the least surprise for users is to invoke `std::terminate()`.

## coordination - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 3 Additional Rationale                       0/0/0  -> 0.00
  [7] 4 Implementation Experience                  0/0/0  -> 0.00
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 3 Additional Rationale                       0/0/0  -> 0.00
  [7] 4 Implementation Experience                  0/0/0  -> 0.00
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Proposal                                   1/1/1  -> 1.00
  [6] 3 Additional Rationale                       0/0/0  -> 0.00
  [7] 4 Implementation Experience                  2/2/2  -> 2.00
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In practice, prototype implementations all use a separate function for this purpose as it minimizes the code needed for the assertion itself.
candidate 2 (found by 3 of 39 passes): It has since been implemented in this form in the P3850 branches of both GCC and Clang that are available on Compiler Explorer, including the interactions with the other contracts extensions those branches carry.

-->
