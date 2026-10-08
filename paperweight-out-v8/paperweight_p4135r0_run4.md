Verdict: Adequate to Strong (7/14)

The paper offers a reasonably strong case for why consteval-only types matter and why the standard is the right place to address them, but it leaves several important parts of the standardization argument largely unspoken. The thinnest areas are the absence of any clear account of who is affected, how the feature would coordinate with existing or in-flight work, and whether real implementation experience supports the claimed simplicity.

- The paper most convincingly establishes the need for standardization by tying consteval-only types to already-adopted C++26 machinery and to a concrete failure mode in P3603’s allocation model.
- It also does well in showing that prior art and alternatives have been considered, including the committee’s existing direction and the comparison with P4101R0.
- The weakest part of the case is the lack of any established audience or affected-user analysis, leaving the practical urgency of the proposal unclear.
- The claims about implementation experience and about a library-only solution being insufficient are asserted rather than demonstrated, so the paper does not yet close those gaps.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 6.67   accumulate 7.33   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 2.00  coordination 0.00  insufficiency 0.33  implementation 1.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 7.50 / 6.50   (all 3 samples: 6.83)
headings: h2 7
on threshold: prior_art
splits: prior_art[5] 1/0/0  insufficiency[8] 0/2/0  implementation[6] 1/1/0
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
candidate 2 (found by 3 of 27 passes): This is a notable improvement in diagnostic clarity and tells the user *exactly* what they need to do.
candidate 3 (found by 3 of 27 passes): This has proven to be a hard problem to solve generally; meanwhile cases of common data structures like vectors and maps that are pain points.
candidate 4 (found by 3 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.

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

## prior_art - grade 1.50 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                1/0/0  -> 0.33
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   1/1/1  -> 1.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): This committee has voted into C++26 the notion of a **std::meta::info** type.
candidate 2 (found by 3 of 27 passes): built on top of what’s shipping in C++26 into account
candidate 3 (found by 3 of 27 passes): To address CWG3150 “ Incomplete consteval-only class types”, we should adopt the delayed consteval-only type decision approach.
candidate 4 (found by 2 of 27 passes): P4101R0 prescribes consteval-only values as a solution that is superior to consteval-only types.

## vehicle - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   2/2/2  -> 2.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper looks to make the case that this distinction is meaningful in a way that should be captured formally in the type system.
candidate 2 (found by 2 of 27 passes): It is tempting to say that we could have these types without consteval-only types (perhaps as a category of types known as builtin interpreter types) and that only those types would be special.
candidate 3 (found by 2 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.
candidate 4 (found by 1 of 27 passes): Consteval-only types provide a very clean and sound model for compile time only non-transient allocations as by definition all values with a given consteval-only type are consteval-only values.

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

## insufficiency - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                0/2/0  -> 0.67
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.

## implementation - grade 1.00  [binary: max] (fired in 3 of 9 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   1/1/0  -> 0.67
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                1/1/1  -> 1.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): Back in the Lock3 days we implemented an innocent pattern where we wanted to specialize a type with a consteval function to implement our iterator type.
candidate 2 (found by 2 of 27 passes): In fact, Andrew Sutton gave a talk at CppCon 2019 (https://www.youtube.com/watch?v=ARxj3dfF_h0); as part of this talk, he presented “Nemesis: a library for runtime introspection” (starting at ~45:50).
candidate 3 (found by 2 of 27 passes): the suggested approach has trivial implementation implications
candidate 4 (found by 1 of 27 passes): the suggested approach has trivial implementation implications.

-->
