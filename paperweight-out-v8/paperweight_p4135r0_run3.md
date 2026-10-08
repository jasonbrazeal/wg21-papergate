Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why consteval-only types matter and how the idea relates to recent committee work, but it leaves several practical questions about affected users, library alternatives, and interoperability largely unanswered. The strongest support is conceptual, while the thinnest support concerns evidence that the feature has been implemented and that standardization is the necessary path.

- The paper establishes a coherent motivation by tying consteval-only types to diagnostic clarity, static analysis, and the non-transient allocation model in P3603.
- It also grounds the proposal in existing C++26 features and prior alternatives, including std::meta::info and CWG3150.
- The weakest established area is implementation experience, where the cited examples are historical or indirect rather than evidence from a current implementation of the proposed design.
- The most glaring omissions are any discussion of who is affected, how the feature coordinates with other proposals, and why a library solution cannot suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 4 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.00   accumulate 6.33   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.33  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 5.50 / 6.00   (all 3 samples: 5.83)
headings: h2 7
on threshold: prior_art, vehicle
splits: vehicle[6] 1/0/1  implementation[6] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   1/1/1  -> 1.00
  [5] Informal Consteval-only Types                2/2/2  -> 2.00
  [6] Formal Consteval-only Types  (part 1 of 2)   2/2/2  -> 2.00
  [7] Formal Consteval-only Types  (part 2 of 2)   1/1/1  -> 1.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): As designers of the language: we must look out for these opportunities to empower static analysis and not create holes in the type system that undermine its ability to catch our mistakes.
candidate 2 (found by 3 of 27 passes): This is a notable improvement in diagnostic clarity and tells the user *exactly* what they need to do.
candidate 3 (found by 3 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.
candidate 4 (found by 3 of 27 passes): Consteval-only types are a strong start towards expanding the language’s understanding of compile-time only values incrementally (in a way that allows the committee and community to gain usage experience and thus make more informed decisions).

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                0/0/0  -> 0.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   1/1/1  -> 1.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): built on top of what’s shipping in C++26 into account
candidate 2 (found by 3 of 27 passes): To address CWG3150 “ Incomplete consteval-only class types”, we should adopt the delayed consteval-only type decision approach.
candidate 3 (found by 2 of 27 passes): This committee has voted into C++26 the notion of a **std::meta::info** type.
candidate 4 (found by 2 of 27 passes): P4101R0 prescribes consteval-only values as a solution that is superior to consteval-only types. P3603 expands upon the functionality proposed to allow for various forms of escalation from a constexpr variable to a consteval (immediate) variable.

## vehicle - grade 1.33 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   1/0/1  -> 0.67
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It is much easier if the language simply tells us the variable declaration is invalid.
candidate 2 (found by 2 of 27 passes): Consteval-only types provide a very clean and sound model for compile time only non-transient allocations as by definition all values with a given consteval-only type are consteval-only values.

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                0/0/0  -> 0.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                0/0/0  -> 0.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   1/0/0  -> 0.33
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                1/1/1  -> 1.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Back in the Lock3 days we implemented an innocent pattern where we wanted to specialize a type with a consteval function to implement our iterator type.
candidate 2 (found by 1 of 27 passes): In fact, Andrew Sutton gave a talk at CppCon 2019 (https://www.youtube.com/watch?v=ARxj3dfF_h0); as part of this talk, he presented “Nemesis: a library for runtime introspection” (starting at ~45:50).

-->
