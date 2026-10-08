Verdict: Adequate (6/14)

The paper offers solid support for the core motivation and the formal, language-level nature of the problem, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest areas are the lack of evidence about who is affected, how the feature would coordinate with existing or in-flight work, and why a library solution cannot suffice.

- The paper most clearly establishes why the distinction matters and why it belongs in the standard rather than remaining an informal convention.
- It also grounds the proposal in prior committee work and alternatives, including the relationship to C++26 reflection and the delayed consteval-only type decision approach.
- The most glaring omission is the absence of any established account of who is affected by the problem or who would benefit from the proposed change.
- The paper also does not establish coordination and interoperability concerns or make a case for why a library-based approach would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.00   accumulate 7.00   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.83  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 6.00 / 6.50   (all 3 samples: 6.33)
headings: h2 7
on threshold: prior_art
splits: prior_art[7] 0/1/1  vehicle[6] 2/1/2  implementation[6] 1/0/0  implementation[9] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 9 sections, strong in 3)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 27 passes): It is through that solid foundation, that we are able to prevent leakage of meaningless scalar values to runtime (with a 100% success rate) and improve diagnostics using consteval-only types for C++26.
candidate 2 (found by 3 of 27 passes): As designers of the language: we must look out for these opportunities to empower static analysis and not create holes in the type system that undermine its ability to catch our mistakes.
candidate 3 (found by 3 of 27 passes): Again, we have a type that is only whole when it’s at compile time; it is informally a consteval-only type.
candidate 4 (found by 3 of 27 passes): This is a notable improvement in diagnostic clarity and tells the user *exactly* what they need to do.

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
  [7] Formal Consteval-only Types  (part 2 of 2)   0/1/1  -> 0.67
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): This committee has voted into C++26 the notion of a **std::meta::info** type.
candidate 2 (found by 3 of 27 passes): To address CWG3150 “ Incomplete consteval-only class types”, we should adopt the delayed consteval-only type decision approach.
candidate 3 (found by 2 of 27 passes): built on top of what’s shipping in C++26 into account
candidate 4 (found by 2 of 27 passes): P4101R0 prescribes consteval-only values as a solution that is superior to consteval-only types.

## vehicle - grade 1.83 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   2/1/2  -> 1.67
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper looks to make the case that this distinction is meaningful in a way that should be captured formally in the type system.
candidate 2 (found by 3 of 27 passes): It is much easier if the language simply tells us the variable declaration is invalid.
candidate 3 (found by 2 of 27 passes): Consteval-only types provide a very clean and sound model for compile time only non-transient allocations as by definition all values with a given consteval-only type are consteval-only values.
candidate 4 (found by 1 of 27 passes): This is a notable improvement in diagnostic clarity and tells the user *exactly* what they need to do.

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

## implementation - grade 1.00  [binary: max] (fired in 3 of 9 sections, strong in 0)
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
  [9] Conclusion                                   1/1/0  -> 0.67
candidate 1 (found by 3 of 27 passes): Back in the Lock3 days we implemented an innocent pattern where we wanted to specialize a type with a consteval function to implement our iterator type.
candidate 2 (found by 1 of 27 passes): In fact, Andrew Sutton gave a talk at CppCon 2019 (https://www.youtube.com/watch?v=ARxj3dfF_h0); as part of this talk, he presented “Nemesis: a library for runtime introspection” (starting at ~45:50).
candidate 3 (found by 1 of 27 passes): the suggested approach has trivial implementation implications.
candidate 4 (found by 1 of 27 passes): the suggested approach has trivial implementation implications

-->
