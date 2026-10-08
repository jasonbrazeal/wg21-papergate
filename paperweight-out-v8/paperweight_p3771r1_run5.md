Verdict: Adequate (6/14)

The paper gives a reasonably grounded account of why constexpr synchronization primitives would be useful and shows some implementation progress, but it leaves several parts of the standardization case underdeveloped, particularly around affected users and interoperability with existing practice.

- The strongest support comes from the concrete motivation that avoiding non-constexpr types in constexpr-compatible code is difficult, and that constexpr evaluation has no observable time during which a lock could be meaningfully held.
- The paper also credibly situates itself as a continuation of prior constexpr atomic and shared_ptr work, with a working compiler explorer implementation for much of the proposed functionality.
- The thinnest parts are the absence of any discussion of who is affected and how the feature coordinates with existing synchronization or constexpr facilities.
- The claim that a library-only solution would not suffice is asserted through a single possible workaround rather than established as a general limitation.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.33  implementation 2.00
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 6.00 / 5.50 / 6.50   (all 3 samples: 6.00)
headings: h2 9
on threshold: motivation, implementation
splits: motivation[6] 0/0/1  vehicle[4] 0/0/1  insufficiency[4] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   2/2/2  -> 2.00
  [5] Design                                       1/1/1  -> 1.00
  [6] Implementation                               0/0/1  -> 0.33
  [7] Wording                                      1/1/1  -> 1.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): It's really hard to conditionally avoid non-`constexpr` types in a code which is supposed to be `constexpr` compatible.
candidate 2 (found by 3 of 33 passes): Purpose of this change is to disallow creation of already locked synchronization objects and their subsequent leakage into runtime code.
candidate 3 (found by 2 of 33 passes): forcing users to `if consteval` such code away, which is against motivation of this paper
candidate 4 (found by 1 of 33 passes): There is not observable time during constant evaluation

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

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   0/0/1  -> 0.33
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): This makes C++ programs much easier to read and write and more bug-prone as someone wise once said "for every line there is a bug".

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
  [4] Motivation                                   1/0/1  -> 0.67
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): One possibility to make this work without this paper would look like this:

## implementation - grade 2.00  [binary: max] (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): link to compiler explorer
candidate 2 (found by 3 of 33 passes): You can experiment with this on [the compiler explorer](https://compiler-explorer.com/z/1McjbzdWa) (functions, member functions, and destructors are working, constructors are work-in-progress.)

-->
