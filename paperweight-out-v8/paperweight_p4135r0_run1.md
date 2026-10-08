Verdict: Adequate (7/14)

The paper gives a reasonably clear account of why consteval-only types would improve diagnostics and support related C++26 work, but it leaves several practical parts of the standardization case largely unargued. The strongest material concerns motivation and prior art, while the discussion of affected users, interoperability, and real implementation experience is thin or absent.

- The paper establishes a meaningful motivation by connecting consteval-only types to better diagnostics and to the viability of P3603’s non-transient allocation model.
- It situates the proposal credibly within existing committee direction, including C++26’s std::meta::info and the handling of CWG3150.
- The case for why this must be a language feature rather than a library solution is asserted mainly through one dependency claim, without enough supporting argument.
- The paper does not establish who would be affected or how the feature would coordinate with existing and adjacent language features, leaving the standardization audience without a clear picture of practical impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.00   accumulate 7.33   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.33  coordination 0.00  insufficiency 0.67  implementation 1.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.00 / 6.00 / 7.00   (all 3 samples: 6.50)
headings: h2 7
on threshold: prior_art, vehicle
splits: motivation[7] 1/0/1  prior_art[3] 0/1/1  vehicle[6] 0/2/0  vehicle[8] 2/1/2
        insufficiency[8] 2/0/2  implementation[6] 0/1/0  implementation[9] 1/1/0
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
  [7] Formal Consteval-only Types  (part 2 of 2)   1/0/1  -> 0.67
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): It is through that solid foundation, that we are able to prevent leakage of meaningless scalar values to runtime (with a 100% success rate) and improve diagnostics using consteval-only types for C++26.
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
  [3] Introduction                                 0/1/1  -> 0.67
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   1/1/1  -> 1.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): To address CWG3150 “ Incomplete consteval-only class types”, we should adopt the delayed consteval-only type decision approach.
candidate 2 (found by 2 of 27 passes): built on top of what’s shipping in C++26 into account
candidate 3 (found by 2 of 27 passes): P4101R0 prescribes consteval-only values as a solution that is superior to consteval-only types.
candidate 4 (found by 1 of 27 passes): This committee has voted into C++26 the notion of a **std::meta::info** type.

## vehicle - grade 1.33 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/2/0  -> 0.67
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                2/1/2  -> 1.67
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper looks to make the case that this distinction is meaningful in a way that should be captured formally in the type system.
candidate 2 (found by 2 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.
candidate 3 (found by 1 of 27 passes): Consteval-only types provide a very clean and sound model for compile time only non-transient allocations as by definition all values with a given consteval-only type are consteval-only values.
candidate 4 (found by 1 of 27 passes): It is much easier if the language simply tells us the variable declaration is invalid.

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

## insufficiency - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                2/0/2  -> 1.33
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.

## implementation - grade 1.00  [binary: max] (fired in 3 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/1/0  -> 0.33
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                1/1/1  -> 1.00
  [9] Conclusion                                   1/1/0  -> 0.67
candidate 1 (found by 3 of 27 passes): Back in the Lock3 days we implemented an innocent pattern where we wanted to specialize a type with a consteval function to implement our iterator type.
candidate 2 (found by 2 of 27 passes): the suggested approach has trivial implementation implications
candidate 3 (found by 1 of 27 passes): In fact, Andrew Sutton gave a talk at CppCon 2019 (https://www.youtube.com/watch?v=ARxj3dfF_h0); as part of this talk, he presented “Nemesis: a library for runtime introspection” (starting at ~45:50).

-->
