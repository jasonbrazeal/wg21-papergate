Verdict: Adequate (4/14)

The paper offers only a partial case for its own standardization, with most of its supporting points asserted rather than demonstrated. The thinnest areas are the absence of any identified affected users, coordination concerns, or explanation of why a library solution would be insufficient, which leaves the standardization need largely unproven.

- The strongest support comes from implementation experience, though even that is only claimed rather than established, with GCC and Clang cited as having implemented the feature.
- The paper asserts that two radically different taxonomies are harder to learn and that this is the only chance to align them, but it does not establish why the standard is the necessary mechanism.
- Prior art in C23’s `_BitInt` is mentioned, but the paper does not establish how thoroughly alternatives were considered or why they fall short.
- Most glaringly, the paper never establishes who is affected, how coordination and interoperability would work, or why a library cannot address the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 4.00   accumulate 5.67   max 4.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 91 of 98 section-criterion pairs unanimous (93%)
single-sample totals would have been: 3.50 / 3.50 / 4.00   (all 3 samples: 3.67)
headings: h3 13   <- NOT h2, check the unit list
on threshold: none
splits: motivation[2] 0/1/1  motivation[9] 0/1/1  prior_art[6] 0/0/1  prior_art[9] 1/1/0
        prior_art[10] 0/1/0  prior_art[13] 1/0/1  vehicle[12] 0/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 9 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/1/1  -> 0.67
  [3] P3666R3 LEWG in Croydon 2026                 0/0/0  -> 0.00
  [4] std::isintegralv<BitInt(N)>                  1/1/1  -> 1.00
  [5] Intuition                                    1/1/1  -> 1.00
  [6] Procedural issues                            0/0/0  -> 0.00
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         1/1/1  -> 1.00
  [9] std::isintegralv<BitInt(N)> is already tr... 0/1/1  -> 0.67
  [10] Most code handles the change fine            1/1/1  -> 1.00
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       1/1/1  -> 1.00
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): LEWG voted with incomplete information
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
  [6] Procedural issues                            0/0/1  -> 0.33
  [7] P3666R4 type taxonomy — C compatibility    1/1/1  -> 1.00
  [8] std::isintegral is underconstraining         0/0/0  -> 0.00
  [9] std::isintegralv<BitInt(N)> is already tr... 1/1/0  -> 0.67
  [10] Most code handles the change fine            0/1/0  -> 0.33
  [11] Extended integer types                       1/1/1  -> 1.00
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/0  -> 0.00
  [13] Extending categories of fundamental types    1/0/1  -> 0.67
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): C23 now has `_BitInt` type for N-bit integers (WG14 N2763, N2775)
candidate 2 (found by 3 of 42 passes): P3666R4 mostly matches C2y taxonomy
candidate 3 (found by 3 of 42 passes): implementation can add `_ExtInt(N)` as extended integer type with same properties as `_BitInt(N)`
candidate 4 (found by 2 of 42 passes): this was *not* mentioned in LEWG

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
  [12] std::isintegralv<BitInt(N)> is eternal       0/0/1  -> 0.33
  [13] Extending categories of fundamental types    0/0/0  -> 0.00
  [14] The end                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): two *radically* different taxonomies are harder to learn
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

## implementation - grade 1.00  [binary: max] (fired in 1 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
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
