Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why the change would matter for `constexpr` code reuse and shows that the direction has been explored in practice, but it leaves several parts of the standardization case thin, particularly around the affected audience and how the feature would fit with existing or future library and language work.

- The strongest support is the concrete implementation experience, with compiler explorer links demonstrating that much of the proposed functionality already works in some form.
- The paper also establishes meaningful prior art and alternatives by connecting the work to earlier proposals and explaining why a different implementation approach was set aside.
- The case for why this belongs in the standard rather than in a library is only asserted through a brief criticism of a workaround, without enough surrounding argument to establish it.
- The most glaring omission is the absence of any established discussion of who is affected, which leaves the practical reach and user impact of the proposal unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 5 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.67   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.83  vehicle 0.33  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 9
on threshold: motivation, implementation
splits: prior_art[4] 2/2/1  prior_art[5] 2/1/2  vehicle[4] 1/0/1  implementation[2] 1/0/0
        implementation[4] 1/0/1
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
candidate 3 (found by 2 of 33 passes): forcing users to `if consteval` such code away, which is against motivation of this paper
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

## prior_art - grade 1.83 (fired in 3 of 11 sections, strong in 3)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   2/2/1  -> 1.67
  [5] Design                                       2/1/2  -> 1.67
  [6] Implementation                               2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper is a continuation of paper [P3309R3: `constexpr atomic & atomic_ref`](https://wg21.link/P3309R3) and makes a lot of library code reusable in `constexpr` world.
candidate 2 (found by 3 of 33 passes): This paper also proposes making `constexpr` free functions implementing interruptable waits, and we can do so as `stop_token` is already `constexpr` default constructible thanks to making `shared_ptr` constexpr in [P3037R6](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3037r6.pdf).
candidate 3 (found by 2 of 33 passes): I have started completely new implementation approach, as this concern is similar as for other `constexpr` changes.
candidate 4 (found by 1 of 33 passes): Alternative approach would be use `__shared_mutex_base::__state_` for it, and use library functionality to provide error messages in case of deadlock, but this approach doesn't allow us easily to diagnose where the lock was previously obtained.

## vehicle - grade 0.33 (fired in 1 of 11 sections, strong in 0)
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
candidate 1 (found by 1 of 33 passes): This paper fixes it by making these types (and algorithms) `constexpr` compatible.
candidate 2 (found by 1 of 33 passes): Main objective is being able to reuse same code in any environment (runtime, GPU, and now also constant evaluated).

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

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): One possibility to make this work without this paper would look like this:
candidate 2 (found by 1 of 33 passes): This pattern is terrible and it creates opportunities for more bugs, and it makes testing harder (especially when test coverage mapping is used).

## implementation - grade 2.00  [binary: max] (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      1/0/0  -> 0.33
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/0/1  -> 0.67
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): You can experiment with this on [the compiler explorer](https://compiler-explorer.com/z/1McjbzdWa) (functions, member functions, and destructors are working, constructors are work-in-progress.)
candidate 2 (found by 2 of 33 passes): link to compiler explorer
candidate 3 (found by 1 of 33 passes): All examples got links to the compiler explorer to play with them.

-->
