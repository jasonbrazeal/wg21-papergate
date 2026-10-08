Verdict: Adequate (5/14)

The paper offers a mixed case for standardization, with its strongest material concentrated in the problem description, prior art, and a partial implementation, while the argument for why this belongs in the standard rather than in a library is essentially absent. The support thins considerably around the affected audience and the coordination and interoperability questions, leaving the proposal’s standardization rationale incomplete.

- The paper clearly establishes why the limitation matters, including the tension between coroutine use and constant-evaluated code, and it points to a concrete partial implementation in Clang.
- The discussion of prior art and alternatives is credited as established, showing that the author has considered other ways to model coroutine-like behavior and their costs.
- The claim about who is affected remains only asserted, with a brief mention of compile-time computation but no evidence that this represents a real user population.
- The paper does not establish why the standard should address this, how it would coordinate with existing features, or why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 4 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 4.33   accumulate 6.00   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 5.00 / 5.00 / 5.50   (all 3 samples: 5.17)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: audience[1] 0/0/1  prior_art[4] 1/1/0  implementation[5] 0/1/0
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
  [7] Impact on existing code                      1/1/1  -> 1.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Based on anecdotal evidence people don't use coroutines for two reasons: one is missing standard library support (which is partially resolved with `std::generator`) and second is mutual exclusivity with much more popular constant evaluated code.
candidate 2 (found by 3 of 30 passes): This limitation forces users to choose between having `constexpr` compatible library or (maybe) simpler coroutine interface.
candidate 3 (found by 3 of 30 passes): Implementation must make sure to avoid stack exhaustion and store evaluation state and coroutine's local variables in a way to avoid it.
candidate 4 (found by 3 of 30 passes): None, this is a pure extension, it allows code to be constexpr which wasn't case before.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/1  -> 0.33
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Even when most of use-cases for coroutines are based on I/O and event based, coroutines are still useful for compile-time based computation, eg. `std::generator`.

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/0  -> 0.67
  [5] Evaluation of constexpr coroutines           1/1/1  -> 1.00
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Because AST walk is unbounded, obvious first choice is a stackfull coroutine (fiber, not a thread!).
candidate 2 (found by 2 of 30 passes): Following subpart of paper shows alternative approaches which can model coroutines. All of them have same expressive ability and model coroutines well. These implementation has various advantages and costs.
candidate 3 (found by 1 of 30 passes): I personally want to be able to write CTRE coroutine interface which allows partially process input on a regular expression state and continue later when it will be resumed.
candidate 4 (found by 1 of 30 passes): This limitation forces users to choose between having `constexpr` compatible library or (maybe) simpler coroutine interface.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/1/0  -> 0.33
  [6] Implementation experience                    2/2/2  -> 2.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Partially implemented in clang available on my [github](https://github.com/hanickadot/llvm-project/tree/P3367-constexpr-coroutines)
candidate 2 (found by 1 of 30 passes): Implementation must make sure to avoid stack exhaustion and store evaluation state and coroutine's local variables in a way to avoid it.

-->
