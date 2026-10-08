Verdict: Adequate (5/14)

The paper offers only a narrow, concrete basis for standardization: the feature exists in GCC and Clang with a documented maximum width. Nearly everything else about the need for standardization is asserted rather than demonstrated, leaving the motivation, audience, alternatives, and standardizing rationale largely unsupported. The thinnest areas are the absence of any coordination or interoperability discussion and the failure to explain why a library solution would not suffice.

- The strongest support is implementation experience, since the paper establishes that GCC and Clang already implement the feature, including a maximum width of `_BitInt(8'388'608)`.
- The paper claims relevance by pointing to C23’s `_BitInt` and the difficulty of learning two different taxonomies, but it does not establish who is actually affected or how severe the problem is in practice.
- The paper does not establish why standardization is necessary rather than leaving the feature as an implementation extension.
- The most glaring omission is the complete lack of any coordination and interoperability discussion, leaving open how this would interact with existing C++ integer types, ABIs, or the C standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 5 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.33   accumulate 7.00   max 5.33

## SUMMARY
grades: motivation 1.00  audience 0.17  prior_art 1.00  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 5.00 / 4.50 / 5.50   (all 3 samples: 5.00)
headings: h3 13   <- NOT h2, check the unit list
on threshold: implementation
splits: motivation[2] 1/0/0  motivation[4] 0/1/0  motivation[5] 0/1/1  motivation[9] 1/0/1
        audience[8] 0/0/1  prior_art[6] 1/0/1  prior_art[10] 1/1/0  prior_art[13] 1/0/1
        vehicle[12] 1/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 9 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/0/0  -> 0.33
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/1/0  -> 0.33
  [5] Intuition                                    0/1/1  -> 0.67
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/1/1  -> 1.00
  [9] std::isintegralv<BitInt(N)> is already tr... 1/0/1  -> 0.67
  [10] Most code handles the change fine            1/1/1  -> 1.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/1/1  -> 1.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 2 (found by 3 of 42 passes): users likely expect `int`, `unsigned long`, etc. instead
candidate 3 (found by 3 of 42 passes): problems usually arise only for *huge* widths
candidate 4 (found by 3 of 42 passes): If the implementation can arbitrarily extend integral type, why can't we extend it with `_BitInt`?

## audience - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/0/0  -> 0.00
  [8] std::isintegral is underconstraining         0/0/1  -> 0.33
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 42 passes): users likely expect `int`, `unsigned long`, etc. instead

## prior_art - grade 1.00 (fired in 6 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            1/0/1  -> 0.67
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            1/1/0  -> 0.67
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    1/0/1  -> 0.67
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 42 passes): P3666R4 mostly matches C2y taxonomy
candidate 3 (found by 3 of 42 passes): implementation can add `_ExtInt(N)` as extended integer type with same properties as `_BitInt(N)`
candidate 4 (found by 2 of 42 passes): e.g. `std::is_class_v` is false for unions (but unions are class types)

## vehicle - grade 0.83 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            0/0/0  -> 0.00
  [11] Extended integer types                       0/0/0  -> 0.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/0/1  -> 0.67
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 2 (found by 2 of 42 passes): This is our *only* chance to make it true.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/2/2  -> 2.00
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
