Verdict: Adequate (4/14)

The paper offers only partial support for its own standardization, with the strongest evidence being that the feature already exists in major implementations. Beyond that, most of the case rests on assertions about user expectations and taxonomy coherence rather than demonstrated need, and several required dimensions are entirely unaddressed.

- The paper does establish implementation experience, since GCC and Clang already provide the feature with a documented maximum width.
- The paper claims but does not establish why the change matters, leaning on assertions about learnability and user expectations without supporting evidence.
- The paper does not establish who is affected, leaving the scope and impact of the proposed change unclear.
- The most glaring omission is the absence of any discussion of coordination and interoperability, prior art, or why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 4 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 4.33   accumulate 6.17   max 4.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.50 / 4.50 / 4.50   (all 3 samples: 4.17)
headings: h3 13   <- NOT h2, check the unit list
on threshold: implementation
splits: motivation[9] 0/1/1  motivation[14] 0/0/1  prior_art[6] 1/0/1  prior_art[8] 1/0/1
        vehicle[7] 0/1/1  vehicle[12] 1/0/0  implementation[2] 1/2/2
## END SUMMARY

## motivation - grade 1.00 (fired in 8 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    1/1/1  -> 1.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/1/1  -> 1.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/1/1  -> 0.67
  [10] Most code handles the change fine            1/1/1  -> 1.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/1/1  -> 1.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/1  -> 0.33
candidate 1 (found by 3 of 42 passes): A bit-precise integer is an integer.
candidate 2 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 3 (found by 3 of 42 passes): users likely expect `int`, `unsigned long`, etc. instead
candidate 4 (found by 3 of 42 passes): edge case: promotion to `int` can prevent some UB … but also introduce UB (e.g. `T = unsigned short`)

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

## prior_art - grade 1.00 (fired in 7 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            1/0/1  -> 0.67
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/0/1  -> 0.67
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            1/1/1  -> 1.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    1/1/1  -> 1.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 42 passes): P3666R4 mostly matches C2y taxonomy
candidate 3 (found by 2 of 42 passes): e.g. `std::is_class_v` is false for unions (but unions are class types)
candidate 4 (found by 2 of 42 passes): existing `std::is_integral` constraints would change

## vehicle - grade 0.50 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/1/1  -> 0.67
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/0/0  -> 0.33
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 2 (found by 1 of 42 passes): This is our *only* chance to make it true.

## coordination - grade 0.00 (fired in 0 of 14 sections, strong in 0)
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

## implementation - grade 1.67  [binary: max] (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/2/2  -> 1.67
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
