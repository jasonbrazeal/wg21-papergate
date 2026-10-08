Verdict: Adequate (6/14)

The paper offers a mixed case for its own standardization, with the strongest support coming from its discussion of alternatives and its implementation experience, while the argument for why this belongs in the standard rather than in a library remains largely unaddressed. The thinnest areas are the lack of any coordination or interoperability discussion and the absence of a clear explanation for why a library solution would not suffice.

- The paper does establish that coroutines have meaningful compile-time use cases and that existing alternatives impose real costs on users.
- The availability of a partial Clang implementation gives the proposal some grounding in practical experience.
- The claim that this limitation is a main factor holding back coroutine adoption is asserted but not backed by evidence.
- The paper never explains why the standard is the right venue or how the feature would coordinate with existing constexpr and coroutine machinery, and it offers no argument against a library-based approach.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 5 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.50  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.50 / 6.00 / 5.00   (all 3 samples: 5.50)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: motivation[7] 1/0/1  audience[4] 0/1/0  vehicle[1] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Evaluation of constexpr coroutines           1/1/1  -> 1.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      1/0/1  -> 0.67
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Even when most of use-cases for coroutines are based on I/O and event based, coroutines are still useful for compile-time based computation, eg. `std::generator`.
candidate 2 (found by 3 of 30 passes): Based on anecdotal evidence people don't use coroutines for two reasons: one is missing standard library support (which is partially resolved with `std::generator`) and second is mutual exclusivity with much more popular constant evaluated code.
candidate 3 (found by 3 of 30 passes): This limitation forces users to choose between having `constexpr` compatible library or (maybe) simpler coroutine interface.
candidate 4 (found by 3 of 30 passes): Implementation must make sure to avoid stack exhaustion and store evaluation state and coroutine's local variables in a way to avoid it.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): I think this limitation and weak library support for coroutines are main limiting factors for bigger adoption of coroutines.

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Evaluation of constexpr coroutines           1/1/1  -> 1.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because AST walk is unbounded, obvious first choice is a stackfull coroutine (fiber, not a thread!).
candidate 2 (found by 2 of 30 passes): I think this limitation and weak library support for coroutines are main limiting factors for bigger adoption of coroutines.
candidate 3 (found by 2 of 30 passes): Following subpart of paper shows alternative approaches which can model coroutines. All of them have same expressive ability and model coroutines well. These implementation has various advantages and costs.
candidate 4 (found by 1 of 30 passes): This limitation forces users to choose between having `constexpr` compatible library or (maybe) simpler coroutine interface.

## vehicle - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Even when most of use-cases for coroutines are based on I/O and event based, coroutines are still useful for compile-time based computation, eg. `std::generator`.

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Partially implemented in clang available on my [github](https://github.com/hanickadot/llvm-project/tree/P3367-constexpr-coroutines)
candidate 2 (found by 1 of 30 passes): Partially implemented in clang available on my [github](https://github.com/hanickadot/llvm-project/tree/P3367-constexpr-coroutines), implementation should be ready for its presentation at Wroclaw meeting, and also will be soon available on compiler explorer (thanks Matt!).

-->
