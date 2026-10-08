Verdict: Adequate (7/14)

The paper gives a reasonably clear account of why constexpr synchronization primitives would be useful and shows some implementation exploration, but it does not adequately establish who is affected or how the proposed facility would fit with existing standardization efforts. The thinnest parts concern the necessity of standardizing this rather than leaving it to implementations, and the absence of any discussion of coordination or interoperability.

- The strongest support is the concrete implementation experience, with links to Compiler Explorer demonstrating working functions, member functions, and destructors.
- The paper also establishes why the problem matters by explaining the difficulty of conditionally avoiding non-constexpr types in constexpr-compatible code.
- Prior art and alternatives are addressed through the connection to P3309R3 and the discussion of an alternative implementation approach using `__shared_mutex_base::__state_`.
- The most glaring omission is the lack of any established audience or affected-user analysis, leaving unclear who would rely on the proposed standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.50   max 8.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.50  implementation 2.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 9
on threshold: motivation, implementation
splits: prior_art[4] 2/2/1
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
candidate 3 (found by 2 of 33 passes): There is not observable time during constant evaluation
candidate 4 (found by 1 of 33 passes): forcing users to `if consteval` such code away, which is against motivation of this paper

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
  [4] Motivation                                   2/2/1  -> 1.67
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

## vehicle - grade 1.00 (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Timeline                                     0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Design                                       0/0/0  -> 0.00
  [6] Implementation                               1/1/1  -> 1.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] 7.7 Constant expressions [expr.const]        0/0/0  -> 0.00
  [9] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [10] 32.6 Mutual exclusion [thread.mutex]  (pa... 0/0/0  -> 0.00
  [11] 32.7 Condition variables [thread.condition]  0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): I'm not sure if this should be standard provided, as it solves problem which lies beyond the standard in implementations, but I think implementatins should have something similar available.
candidate 2 (found by 2 of 33 passes): One possibility to make this work without this paper would look like this:
candidate 3 (found by 1 of 33 passes): This paper fixes it by making these types (and algorithms) `constexpr` compatible.

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

## insufficiency - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 2 (found by 2 of 33 passes): You can experiment with this on [the compiler explorer](https://compiler-explorer.com/z/1McjbzdWa) (functions, member functions, and destructors are working, constructors are work-in-progress.)
candidate 3 (found by 1 of 33 passes): You can experiment with this on [the compiler explorer](https://compiler-explorer.com/z/1McjbzdWa)

-->
