Verdict: Adequate (4/14)

The paper offers only a thin evidentiary basis for its own standardization, resting most of its case on repeated assertions about taxonomy confusion rather than demonstrated need, affected users, or viable alternatives. The thinnest areas are the complete absence of discussion about who is affected and why a library solution would not suffice, along with only a passing claim of implementation experience.

- The strongest support is the claim that GCC and Clang have implemented the feature, with a reported maximum width for `_BitInt`.
- The paper gestures toward prior art in C23 and related proposals, but does not establish that these were adequately considered or compared.
- The argument for why the standard must change leans almost entirely on the unestablished claim that two different taxonomies are harder to learn.
- The most glaring omission is the lack of any account of who is affected by the current state of affairs or why a library approach cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 5 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 4.00   accumulate 5.67   max 4.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.17  coordination 0.17  insufficiency 0.00  implementation 1.33
sample agreement: 92 of 98 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 3.50 / 4.00   (all 3 samples: 3.67)
headings: h3 13   <- NOT h2, check the unit list
on threshold: none
splits: motivation[2] 0/1/0  motivation[4] 0/0/1  motivation[9] 1/0/0  vehicle[7] 0/1/0
        coordination[7] 1/0/0  implementation[2] 1/1/2
## END SUMMARY

## motivation - grade 1.00 (fired in 9 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/1/0  -> 0.33
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/1  -> 0.33
  [5] Intuition                                    1/1/1  -> 1.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/1/1  -> 1.00
  [9] std::isintegralv<BitInt(N)> is already tr... 1/0/0  -> 0.33
  [10] Most code handles the change fine            1/1/1  -> 1.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/1/1  -> 1.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 2 (found by 3 of 42 passes): users likely expect `int`, `unsigned long`, etc. instead
candidate 3 (found by 3 of 42 passes): If the implementation can arbitrarily extend integral type, why can't we extend it with `_BitInt`?
candidate 4 (found by 3 of 42 passes): This is our *only* chance to make it true.

## audience - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/0/0  -> 0.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 6 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            1/1/1  -> 1.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 1/1/1  -> 1.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    1/1/1  -> 1.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 42 passes): e.g. `std::is_class_v` is false for unions (but unions are class types)
candidate 3 (found by 3 of 42 passes): P3666R4 mostly matches C2y taxonomy
candidate 4 (found by 3 of 42 passes): this was *not* mentioned in LEWG

## vehicle - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/1/0  -> 0.33
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): two *radically* different taxonomies are harder to learn

## coordination - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/0/0  -> 0.33
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): two *radically* different taxonomies are harder to learn

## insufficiency - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/0/0  -> 0.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 1 of 14 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/2  -> 1.33
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/0/0  -> 0.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`

-->
