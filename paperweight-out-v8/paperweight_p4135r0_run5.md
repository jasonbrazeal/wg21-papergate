Verdict: Adequate to Strong (7/14)

The paper offers solid support for the core motivation and the need for a language-level distinction, but it leaves several practical questions about affected users, implementation experience, and interoperability largely asserted rather than demonstrated.

- The strongest support is for why the distinction matters, with clear examples of improved diagnostics and a foundation for future compile-time programming.
- The case for standardization is also well made, particularly in arguing that the type system should formally capture a distinction that is otherwise easy to get wrong.
- The thinnest support is around who is affected, which is not established at all, leaving the scope of the problem unclear.
- Implementation experience and interoperability are only claimed, with little concrete evidence that the approach has been tried or that it works across real boundaries.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 7.33   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 2.00  coordination 0.50  insufficiency 0.17  implementation 0.67
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 6.50 / 8.00   (all 3 samples: 7.33)
headings: h2 7
on threshold: none
splits: motivation[7] 0/1/1  insufficiency[8] 0/0/1  implementation[8] 1/0/1
        implementation[9] 0/0/1
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
  [7] Formal Consteval-only Types  (part 2 of 2)   0/1/1  -> 0.67
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): As users of the language: we do our best to use the facilities provided by the language to allow the language to help us catch a mistake.
candidate 2 (found by 3 of 27 passes): This is a notable improvement in diagnostic clarity and tells the user *exactly* what they need to do.
candidate 3 (found by 3 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.
candidate 4 (found by 2 of 27 passes): ensuring that C++26 sets a good foundation for everything we conceivably may want to do with interpreted types, empowering language evolution to solve the problems we’ll have in the coming decades with increasingly complicated compile time programming.

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

## prior_art - grade 2.00 (fired in 5 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   2/2/2  -> 2.00
  [7] Formal Consteval-only Types  (part 2 of 2)   1/1/1  -> 1.00
  [8] Other Options                                2/2/2  -> 2.00
  [9] Conclusion                                   1/1/1  -> 1.00
candidate 1 (found by 3 of 27 passes): This paper looks to make the case that this distinction is meaningful in a way that should be captured formally in the type system.
candidate 2 (found by 3 of 27 passes): P2996 introduces **define_aggregate** which allows a forward declaration to be turned into a class definition programatically.
candidate 3 (found by 3 of 27 passes): built on top of what’s shipping in C++26 into account
candidate 4 (found by 3 of 27 passes): P4101R0 prescribes consteval-only values as a solution that is superior to consteval-only types. P3603 expands upon the functionality proposed to allow for various forms of escalation from a constexpr variable to a consteval (immediate) variable.

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
candidate 2 (found by 3 of 27 passes): It is much easier if the language simply tells us the variable declaration is invalid.
candidate 3 (found by 2 of 27 passes): Consteval-only types provide a very clean and sound model for compile time only non-transient allocations as by definition all values with a given consteval-only type are consteval-only values.
candidate 4 (found by 1 of 27 passes): It is tempting to say that we could have these types without consteval-only types (perhaps as a category of types known as builtin interpreter types) and that only those types would be special.

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   1/1/1  -> 1.00
  [8] Other Options                                0/0/0  -> 0.00
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): non-transient allocations owned by values of consteval-only type can be serialized and deserialized across a module boundary.

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                0/0/1  -> 0.33
  [9] Conclusion                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Without consteval-only types P3603’s non-transient allocation model does not actually work generically.

## implementation - grade 0.67  [binary: max] (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Foreword                                     0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Invariants                                   0/0/0  -> 0.00
  [5] Informal Consteval-only Types                0/0/0  -> 0.00
  [6] Formal Consteval-only Types  (part 1 of 2)   0/0/0  -> 0.00
  [7] Formal Consteval-only Types  (part 2 of 2)   0/0/0  -> 0.00
  [8] Other Options                                1/0/1  -> 0.67
  [9] Conclusion                                   0/0/1  -> 0.33
candidate 1 (found by 2 of 27 passes): Back in the Lock3 days we implemented an innocent pattern where we wanted to specialize a type with a consteval function to implement our iterator type.
candidate 2 (found by 1 of 27 passes): the suggested approach has trivial implementation implications

-->
