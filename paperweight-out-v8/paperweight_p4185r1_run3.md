Verdict: Strong to Excellent (11/14)

The paper offers substantial support for its standardization case in the areas that matter most for committee work: it grounds the problem in implementation experience, documents a convergence of independent designs, and explains why the feature belongs in the standard rather than in a library. The support is thinnest where the paper relies on reported user feedback and interoperability concerns without fully demonstrating the breadth or severity of those effects.

- The strongest support comes from the documented convergence of two independent implementations on the same structural taxonomy, backed by concrete implementation experience in both libraries.
- The paper clearly establishes why the standard is the right venue, pointing to domain-specific requirements like calendar arithmetic and the absence of comparable three-type distinctions in other mainstream units libraries.
- The case for who is affected rests on claims about frequently reported usability issues and generic programming concerns, but the paper does not establish the scale or representativeness of that affected population.
- The most glaring omission is the lack of established evidence that a library cannot meet these needs, since the paper acknowledges key parts of the proposal are not yet implemented and leans on assertions about type-system requirements rather than demonstrated library limitations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.17/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.17 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.17   corroborated 10.00   accumulate 12.00   max 12.33

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.50  coordination 1.17  insufficiency 1.33  implementation 2.00
sample agreement: 118 of 133 section-criterion pairs unanimous (89%)
single-sample totals would have been: 12.00 / 11.00 / 12.00   (all 3 samples: 11.17)
headings: h2 16
on threshold: vehicle, coordination
splits: motivation[10] 2/0/2  motivation[15] 2/0/0  audience[14] 1/1/2  prior_art[7] 0/0/2
        vehicle[4] 2/0/1  vehicle[11] 1/0/0  coordination[3] 2/2/1  coordination[4] 0/0/1
        coordination[14] 2/0/0  insufficiency[5] 1/0/0  insufficiency[6] 0/2/2
        insufficiency[10] 1/1/0  insufficiency[11] 0/2/2  implementation[3] 2/1/2
        implementation[15] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 13 of 19 sections, strong in 11)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [7] 5 Non-negative quantities                    2/2/2  -> 2.00
  [8] 6 Absolute quantities  (part 1 of 2)         2/2/2  -> 2.00
  [9] 6 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [10] 7 Affine spaces within quantity hierarchies  2/0/2  -> 1.33
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           2/2/2  -> 2.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/0/0  -> 0.67
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient for several common engineering patterns and, in places, mathematically too permissive.
candidate 2 (found by 3 of 57 passes): The following gaps — identified through implementation experience in **[[mp-units]](https://mpusz.github.io/mp-units)** and committee feedback — stand between the current model and that goal.
candidate 3 (found by 3 of 57 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.
candidate 4 (found by 3 of 57 passes): many physical quantities — length, mass, duration, thermodynamic temperature, amount of substance, luminous intensity — are inherently non-negative, and a library that cannot express this is forced to scatter manual precondition checks throughout user code

## audience - grade 1.17 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Motivation and scope  (part 1 of 2)        1/1/1  -> 1.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   1/1/2  -> 1.33
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 2 of 57 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 3 (found by 1 of 57 passes): After years of iteration, the Au team found that silently allowing same-kind different-unit integer division caused enough user confusion that they chose to **block it at compile time** by default

## prior_art - grade 2.00 (fired in 12 of 19 sections, strong in 10)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/2  -> 0.67
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [10] 7 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           1/1/1  -> 1.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This paper is the product of a WG21-requested convergence between two independently developed approaches: the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation (Mateusz Pusz) and the Sequoia C++ library [[Sequoia]](https://github.com/ojrosten/sequoia) (Oliver Rosten).
candidate 2 (found by 3 of 57 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 3 (found by 3 of 57 passes): The `point_for<>` proposal targets Option 4 (siblings), which preserves the correct ISQ structure but still yields wrong arithmetic without additional annotations.
candidate 4 (found by 3 of 57 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.

## vehicle - grade 1.50 (fired in 3 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/0/1  -> 1.00
  [5] 4 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            1/0/0  -> 0.33
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           2/2/2  -> 2.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.
candidate 2 (found by 1 of 57 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 3 (found by 1 of 57 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.
candidate 4 (found by 1 of 57 passes): This feature is a **pure addition** — it does not affect the existing `quantity` or `quantity_point` interfaces and can be added independently of the absolute quantities proposal.

## coordination - grade 1.17 (fired in 3 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/1  -> 1.67
  [4] 3 Introduction                               0/0/1  -> 0.33
  [5] 4 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   2/0/0  -> 0.67
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.
candidate 2 (found by 1 of 57 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.
candidate 3 (found by 1 of 57 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming: `quantity`, `double`, and other numeric types should be substitutable in generic algorithms.

## insufficiency - grade 1.33 (fired in 4 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Motivation and scope  (part 1 of 2)        1/0/0  -> 0.33
  [6] 4 Motivation and scope  (part 2 of 2)        0/2/2  -> 1.33
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  1/1/0  -> 0.67
  [11] 8 Range-validated quantity points            0/2/2  -> 1.33
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): The `point_for<>` attribute, the associated quantity specification arithmetic, and the `quantity<point<R>>` unification described in this chapter are not yet implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.
candidate 2 (found by 2 of 57 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.
candidate 3 (found by 1 of 57 passes): These requirements cannot be met by a wrapper or a coding convention; they call for non-negativity to be part of the type system.
candidate 4 (found by 1 of 57 passes): The `0 * unit` syntax works, but it has a subtle cost: if the quantity’s stored unit differs from the spelled unit, the right-hand side must be rescaled before the numerical comparison.

## implementation - grade 2.00  [binary: max] (fired in 9 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/1/2  -> 1.67
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    2/2/2  -> 2.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            1/1/1  -> 1.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   1/2/2  -> 1.67
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): implementation experience from both **[[mp-units]](https://mpusz.github.io/mp-units)** and [[Sequoia]](https://github.com/ojrosten/sequoia) validates the structural conclusions.
candidate 2 (found by 3 of 57 passes): Most proposed features are already implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.
candidate 3 (found by 3 of 57 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 4 (found by 3 of 57 passes): The compile-time tag is already implemented as an experimental feature in [[mp-units]](https://mpusz.github.io/mp-units) and it drives an existing **runtime** enforcement on quantity point.

-->
