Verdict: Adequate (4/14)

The paper offers only intermittent support for its own standardization, with most of its key claims asserted rather than demonstrated. The thinnest areas are the absence of any identified affected users and the lack of a case for why a library solution would not suffice.

- The strongest support comes from implementation experience, where the paper notes that GCC and Clang already implement the feature with a documented maximum width.
- The paper gestures toward prior art by citing C23’s `_BitInt` and suggesting a matching extended integer type, but it does not establish how that prior work validates this proposal.
- The rationale for standardization leans heavily on the claim that two taxonomies are harder to learn, without showing who would actually be confused or how the standard would resolve that confusion.
- The most glaring omission is the complete absence of any discussion of who is affected, leaving the proposal without a demonstrated constituency or use case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 5 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 4.67   accumulate 6.17   max 4.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.67  coordination 0.17  insufficiency 0.00  implementation 1.33
sample agreement: 90 of 98 section-criterion pairs unanimous (92%)
single-sample totals would have been: 4.50 / 4.00 / 5.00   (all 3 samples: 4.17)
headings: h3 13   <- NOT h2, check the unit list
on threshold: none
splits: motivation[4] 1/0/1  motivation[5] 1/0/1  prior_art[8] 1/0/0  prior_art[10] 1/0/0
        vehicle[12] 0/1/0  coordination[7] 0/0/1  implementation[2] 2/0/2
        implementation[4] 0/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 8 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  1/0/1  -> 0.67
  [5] Intuition                                    1/0/1  -> 0.67
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/1/1  -> 1.00
  [9] std::isintegralv<BitInt(N)> is already tr... 1/1/1  -> 1.00
  [10] Most code handles the change fine            1/1/1  -> 1.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/1/1  -> 1.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 2 (found by 3 of 42 passes): users likely expect `int`, `unsigned long`, etc. instead
candidate 3 (found by 3 of 42 passes): if LLVM is fine with shipping this behavior, why are we not?
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

## prior_art - grade 1.00 (fired in 6 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/0/0  -> 0.33
  [9] std::isintegralv<BitInt(N)> is already tr... 0/0/0  -> 0.00
  [10] Most code handles the change fine            1/0/0  -> 0.33
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    1/1/1  -> 1.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 42 passes): P3666R4 mostly matches C2y taxonomy
candidate 3 (found by 3 of 42 passes): implementation can add `_ExtInt(N)` as extended integer type with same properties as `_BitInt(N)`
candidate 4 (found by 2 of 42 passes): integral type: `int`, `unsigned long`, […] <ins>`_BitInt(N)`</ins>

## vehicle - grade 0.67 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
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
  [12] std::isintegralv<BitInt(N)> is eternal       0/1/0  -> 0.33
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
candidate 2 (found by 1 of 42 passes): This is our *only* chance to make it true.

## coordination - grade 0.17 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/0/0  -> 0.00
  [5] Intuition                                    0/0/0  -> 0.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    0/0/1  -> 0.33
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

## implementation - grade 1.33  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 2/0/2  -> 1.33
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  0/1/0  -> 0.33
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
candidate 1 (found by 2 of 42 passes): implemented by GCC and Clang; max: `_BitInt(8'388'608)`
candidate 2 (found by 1 of 42 passes): other poll outcomes are implemented, *but not this one*

-->
