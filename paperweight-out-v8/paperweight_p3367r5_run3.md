Verdict: Adequate (6/14)

The paper offers a partial case for its own standardization, with the strongest material going to motivation, alternatives, and a concrete implementation, but it leaves several essential justifications entirely unaddressed. The thinnest areas concern why this belongs in the standard, how it would interact with existing features, and why a library solution is insufficient.

- The paper clearly establishes why constant-evaluated coroutines would matter and points to a working partial implementation in Clang.
- It gives a reasonable account of alternative ways to model coroutines and why a coroutine-like state representation is desirable.
- The claim about who is affected rests mostly on the author’s belief and anecdotal reasoning rather than demonstrated user or ecosystem need.
- The paper does not establish why the standard should address this, how it would coordinate with existing coroutine or constant-evaluation machinery, or why a library cannot provide the capability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 4.67   accumulate 6.50   max 6.67

## SUMMARY
grades: motivation 1.67  audience 0.50  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 5.50 / 5.50   (all 3 samples: 5.67)
headings: h2 8
on threshold: motivation, prior_art, implementation
splits: motivation[5] 2/1/1  motivation[7] 0/1/0  audience[1] 1/1/0  audience[4] 0/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 5 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     1/1/1  -> 1.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Evaluation of constexpr coroutines           2/1/1  -> 1.33
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/1/0  -> 0.33
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Even when most of use-cases for coroutines are based on I/O and event based, coroutines are still useful for compile-time based computation, eg. `std::generator`.
candidate 2 (found by 3 of 30 passes): Based on anecdotal evidence people don't use coroutines for two reasons: one is missing standard library support (which is partially resolved with `std::generator`) and second is mutual exclusivity with much more popular constant evaluated code.
candidate 3 (found by 3 of 30 passes): This limitation forces users to choose between having `constexpr` compatible library or (maybe) simpler coroutine interface.
candidate 4 (found by 3 of 30 passes): Implementation must make sure to avoid stack exhaustion and store evaluation state and coroutine's local variables in a way to avoid it.

## audience - grade 0.50 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/1  -> 0.33
  [5] Evaluation of constexpr coroutines           0/0/0  -> 0.00
  [6] Implementation experience                    0/0/0  -> 0.00
  [7] Impact on existing code                      0/0/0  -> 0.00
  [8] Proposed wording changes                     0/0/0  -> 0.00
  [9] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
  [10] 17.12 Coroutines [support.coroutine]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Even when most of use-cases for coroutines are based on I/O and event based, coroutines are still useful for compile-time based computation, eg. `std::generator`.
candidate 2 (found by 1 of 30 passes): coroutines are still useful for compile-time based computation, eg. `std::generator`.
candidate 3 (found by 1 of 30 passes): I think this limitation and weak library support for coroutines are main limiting factors for bigger adoption of coroutines.

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
candidate 1 (found by 2 of 30 passes): I personally want to be able to write CTRE coroutine interface which allows partially process input on a regular expression state and continue later when it will be resumed.
candidate 2 (found by 2 of 30 passes): To avoid this situation the easiest way to model a coroutine is to use coroutine (or coroutine-like functionality) to store the state (represented with values on stack) somewhere else.
candidate 3 (found by 2 of 30 passes): Following subpart of paper shows alternative approaches which can model coroutines. All of them have same expressive ability and model coroutines well.
candidate 4 (found by 1 of 30 passes): I think this limitation and weak library support for coroutines are main limiting factors for bigger adoption of coroutines.

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
