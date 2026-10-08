Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why the feature would matter and how it relates to prior work, but it leaves several parts of the standardization case underdeveloped, particularly around who is affected and how the proposal would coordinate with existing or future library and language facilities.

- The strongest support is the motivation, which explains concretely why avoiding non-`constexpr` types in `constexpr`-compatible code is difficult and why preventing already-locked synchronization objects from leaking into runtime code matters.
- The paper also establishes useful prior art and alternatives by connecting the proposal to P3309R3 and P3037R6, and by discussing an implementation-level alternative and its diagnostic limitations.
- The weakest areas are the absence of any identified affected user group and the lack of coordination or interoperability discussion, leaving the audience and ecosystem impact unclear.
- The claims about why this belongs in the standard and why a library-only solution is insufficient are asserted but not backed by enough reasoning or evidence to be persuasive.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 5 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.00   accumulate 6.67   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 6.50 / 6.00   (all 3 samples: 6.17)
headings: h2 9
on threshold: motivation, implementation
splits: vehicle[4] 0/1/0  vehicle[6] 0/0/1  insufficiency[4] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design                                       1/1/1  -> 1.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      1/1/1  -> 1.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): It's really hard to conditionally avoid non-`constexpr` types in a code which is supposed to be `constexpr` compatible.
candidate 2 (found by 3 of 33 passes): Purpose of this change is to disallow creation of already locked synchronization objects and their subsequent leakage into runtime code.
candidate 3 (found by 1 of 33 passes): And there is no way how to observe time during constant evaluation anyway.
candidate 4 (found by 1 of 33 passes): There is not observable time during constant evaluation, there are three possible options:

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 11 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design                                       2/2/2  -> 2.00
  [6] Implementation                               2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper is a continuation of paper [P3309R3: `constexpr atomic & atomic_ref`](https://wg21.link/P3309R3) and makes a lot of library code reusable in `constexpr` world.
candidate 2 (found by 3 of 33 passes): This paper also proposes making `constexpr` free functions implementing interruptable waits, and we can do so as `stop_token` is already `constexpr` default constructible thanks to making `shared_ptr` constexpr in [P3037R6](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3037r6.pdf).
candidate 3 (found by 3 of 33 passes): Alternative approach would be use `__shared_mutex_base::__state_` for it, and use library functionality to provide error messages in case of deadlock, but this approach doesn't allow us easily to diagnose where the lock was previously obtained.

## vehicle - grade 0.33 (fired in 2 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/1/0  -> 0.33
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/1  -> 0.33
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Main objective is being able to reuse same code in any environment (runtime, GPU, and now also constant evaluated).
candidate 2 (found by 1 of 33 passes): I'm not sure if this should be standard provided, as it solves problem which lies beyond the standard in implementations, but I think implementatins should have something similar available.

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/0  -> 0.67
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): One possibility to make this work without this paper would look like this:

## implementation - grade 2.00  [binary: max] (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): You can experiment with this on [the compiler explorer](https://compiler-explorer.com/z/1McjbzdWa) (functions, member functions, and destructors are working, constructors are work-in-progress.)

-->
