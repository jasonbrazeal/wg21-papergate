Verdict: Adequate (6/14)

The paper gives a partial account of why constant-evaluated coroutines would be useful and shows that a prototype exists, but it leaves the central standardization questions largely unaddressed. The thinnest parts concern why this belongs in the standard, how it would interact with existing rules, and why a library solution cannot suffice.

- The strongest support is the implementation experience, with a partial Clang implementation available for inspection.
- The paper also establishes that coroutines have plausible compile-time uses and that alternative modeling approaches exist.
- The most glaring omission is the absence of any case for why the standard should change rather than relying on library or implementation-specific mechanisms.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.67   accumulate 6.33   max 6.67

## SUMMARY
grades: motivation 1.83  audience 0.33  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.50 / 6.00 / 5.50   (all 3 samples: 5.67)
headings: h2 8
on threshold: prior_art, implementation
splits: motivation[5] 2/2/1  audience[1] 0/1/1
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 10 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Evaluation of constexpr coroutines           2/2/1  -> 1.67
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      1/1/1  -> 1.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Even when most of use-cases for coroutines are based on I/O and event based, coroutines are still useful for compile-time based computation, eg. `std::generator`.
candidate 2 (found by 3 of 30 passes): Based on anecdotal evidence people don't use coroutines for two reasons: one is missing standard library support (which is partially resolved with `std::generator`) and second is mutual exclusivity with much more popular constant evaluated code.
candidate 3 (found by 3 of 30 passes): This limitation forces users to choose between having `constexpr` compatible library or (maybe) simpler coroutine interface.
candidate 4 (found by 3 of 30 passes): Implementation must make sure to avoid stack exhaustion and store evaluation state and coroutine's local variables in a way to avoid it.

## audience - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): coroutines are still useful for compile-time based computation, eg. `std::generator`.

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
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
candidate 1 (found by 3 of 30 passes): Following subpart of paper shows alternative approaches which can model coroutines. All of them have same expressive ability and model coroutines well.
candidate 2 (found by 2 of 30 passes): I think this limitation and weak library support for coroutines are main limiting factors for bigger adoption of coroutines.
candidate 3 (found by 2 of 30 passes): To avoid this situation the easiest way to model a coroutine is to use coroutine (or coroutine-like functionality) to store the state (represented with values on stack) somewhere else.
candidate 4 (found by 1 of 30 passes): I personally want to be able to write CTRE coroutine interface which allows partially process input on a regular expression state and continue later when it will be resumed.

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
candidate 1 (found by 3 of 30 passes): Partially implemented in clang available on my [github](https://github.com/hanickadot/llvm-project/tree/P3367-constexpr-coroutines)

-->
