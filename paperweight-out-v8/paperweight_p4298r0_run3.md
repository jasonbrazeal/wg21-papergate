Verdict: Adequate (5/14)

The paper offers some meaningful support for its standardization case, particularly around motivation, alternatives, and implementation experience, but it leaves several essential justifications almost entirely unaddressed. The thinnest areas concern who would be affected, why the feature belongs in the standard rather than a library, and how it would coordinate with existing or forthcoming specifications.

- The strongest support is the concrete implementation experience in GCC and Clang branches, which shows the feature is buildable and has been exercised in prototype form.
- The paper also establishes a clear rationale by connecting the proposal to existing concerns about exception-throwing violation handlers and by discussing plausible alternative designs.
- The most glaring omission is the absence of any established case for why this cannot be provided as a library facility rather than a core language or standard library change.
- The paper likewise does not establish who is affected or how the feature would interoperate with the broader contracts and assertions ecosystem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 3 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 4.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 87 of 91 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 5.00 / 5.50   (all 3 samples: 5.17)
headings: h2 9 + bold numbered 3
on threshold: motivation, prior_art, implementation
splits: motivation[6] 0/1/0  prior_art[4] 2/1/1  prior_art[5] 2/1/1  prior_art[7] 0/0/2
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Proposal                                   0/0/0  -> 0.00
  [6] 3 Additional Rationale                       0/1/0  -> 0.33
  [7] 4 Implementation Experience                  0/0/0  -> 0.00
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            1/1/1  -> 1.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): This essential behavior is needed in many domains, but introduces concerns in others where no exception could escape safely or without the need for significant additional overhead.
candidate 2 (found by 3 of 39 passes): Undefined behavior can unquestionably throw an exception — it can do anything.
candidate 3 (found by 3 of 39 passes): This small addition to C++26 Contracts will enable fine-grained control over the support for exceptions, allowing people to mitigate many of the concerns that have been expressed with throwing violation handlers.
candidate 4 (found by 1 of 39 passes): Because we have chosen to name the new semantics with the use of `noexcept` as an adverb, the choice with the least surprise for users is to invoke `std::terminate()`.

## audience - grade 0.00 (fired in 0 of 13 sections, strong in 0)
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

## prior_art - grade 1.67 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/1/1  -> 1.33
  [5] 2 Proposal                                   2/1/1  -> 1.33
  [6] 3 Additional Rationale                       2/2/2  -> 2.00
  [7] 4 Implementation Experience                  0/0/2  -> 0.67
  [8] 5 Wording Changes                            0/0/0  -> 0.00
  [9] 6 Basics [basic]                             0/0/0  -> 0.00
  [10] 14 Exception handling [except]               0/0/0  -> 0.00
  [11] 15 Preprocessing directives [cpp]            0/0/0  -> 0.00
  [12] Acknowledgments                              0/0/0  -> 0.00
  [13] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): With the potential adoption of [P3400R4], assertion-control objects (i.e., labels) could allow for selecting locally whether a given contract assertion should support exceptions escaping from a violation of a particular assertion.
candidate 2 (found by 3 of 39 passes): Unlike when a violation handler throws from the `assert` macro (as proposed in [P3290R6]) we propose that an exception from the contract-violation handler where one of the new semantics has been used results in invoking `std::terminate()`.
candidate 3 (found by 2 of 39 passes): Then, if [P3290R6] is adopted first, update its behavior to pass through the new semantics when using the `noexcept` entry points:
candidate 4 (found by 1 of 39 passes): Then, if [P3290R6] is adopted first, update its behavior to pass through the new semantics when using the `noexcept` entry points

## vehicle - grade 0.00 (fired in 0 of 13 sections, strong in 0)
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
