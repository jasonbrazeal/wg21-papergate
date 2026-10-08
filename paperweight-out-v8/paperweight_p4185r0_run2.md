Verdict: Strong to Excellent (11/14)

The paper offers solid grounding in implementation experience and prior art, with a clear account of why the current model falls short and how the proposed direction emerged from real collaboration. The support is thinnest when it comes to showing who is affected at scale, why the work belongs in the standard rather than a library, and why the specific standardization path is necessary.

- The strongest support comes from the convergence of two independent implementations and the documented real-world gaps in the current two-abstraction model.
- The paper also establishes credible prior art through the Sequoia library and the WG21-requested collaboration with mp-units.
- The weakest area is the case for standardization itself, since the paper does not yet establish that a library solution would be insufficient for the proposed design.
- The most glaring omission is the lack of established evidence about the breadth of users affected, beyond anecdotal reports and a single discussion thread.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.67   accumulate 11.50   max 11.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.00  coordination 1.83  insufficiency 0.67  implementation 2.00
sample agreement: 110 of 126 section-criterion pairs unanimous (87%)
single-sample totals would have been: 11.00 / 11.50 / 10.50   (all 3 samples: 10.67)
headings: h2 15
on threshold: none
splits: motivation[15] 0/1/0  audience[4] 2/1/1  prior_art[12] 1/2/2  prior_art[13] 2/2/0
        prior_art[16] 1/0/1  vehicle[3] 0/1/0  vehicle[10] 0/1/1  vehicle[12] 0/2/1
        coordination[2] 1/2/2  coordination[13] 2/0/0  insufficiency[3] 0/0/1
        insufficiency[5] 0/2/0  insufficiency[10] 2/0/0  implementation[2] 2/1/2
        implementation[8] 0/1/1  implementation[14] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 14 of 18 sections, strong in 13)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [6] 4 Non-negative quantities                    2/2/2  -> 2.00
  [7] 5 Absolute quantities  (part 1 of 2)         2/2/2  -> 2.00
  [8] 5 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [9] 6 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [10] 7 Range-validated quantity points            2/2/2  -> 2.00
  [11] 8 Runtime frame projections                  2/2/2  -> 2.00
  [12] 9 Text output for quantity points            2/2/2  -> 2.00
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   2/2/2  -> 2.00
  [15] 12 Summary                                   0/1/0  -> 0.33
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient for several common engineering patterns and, in places, mathematically too permissive.
candidate 2 (found by 3 of 54 passes): The following gaps — identified through implementation experience in **[[mp-units]](https://mpusz.github.io/mp-units)** and committee feedback — stand between the current model and that goal.
candidate 3 (found by 3 of 54 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 4 (found by 3 of 54 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.

## audience - grade 1.17 (fired in 2 of 18 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/1/1  -> 1.33
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   1/1/1  -> 1.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 2 (found by 2 of 54 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 3 (found by 1 of 54 passes): Users have independently requested the same ergonomic improvements for such cases (see [mp-units discussion #606](https://github.com/mpusz/mp-units/discussions/606)).

## prior_art - grade 2.00 (fired in 12 of 18 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [9] 6 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [10] 7 Range-validated quantity points            2/2/2  -> 2.00
  [11] 8 Runtime frame projections                  2/2/2  -> 2.00
  [12] 9 Text output for quantity points            1/2/2  -> 1.67
  [13] 10 Integer division safety                   2/2/0  -> 1.33
  [14] 11 Comparison against zero                   2/2/2  -> 2.00
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                1/0/1  -> 0.67
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): This paper is the product of a WG21-requested convergence between two independently developed approaches: the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation (Mateusz Pusz) and the Sequoia C++ library [[Sequoia]](https://github.com/ojrosten/sequoia) (Oliver Rosten).
candidate 2 (found by 3 of 54 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 3 (found by 3 of 54 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 4 (found by 3 of 54 passes): The `point_for<>` proposal targets Option 4 (siblings), which preserves the correct ISQ structure but still yields wrong arithmetic without additional annotations.

## vehicle - grade 1.00 (fired in 4 of 18 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/0  -> 0.33
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  1/1/1  -> 1.00
  [10] 7 Range-validated quantity points            0/1/1  -> 0.67
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/2/1  -> 1.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 54 passes): The `quantity<point<R>>` unification must be standardized regardless of whether absolute quantities are adopted.
candidate 2 (found by 2 of 54 passes): The design handles the two abstractions differently:
candidate 3 (found by 1 of 54 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 4 (found by 1 of 54 passes): The `point_for<>` attribute, the associated quantity specification arithmetic, and the `quantity<point<R>>` unification described in this chapter are not yet implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.

## coordination - grade 1.83 (fired in 3 of 18 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/2  -> 1.67
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   2/0/0  -> 0.67
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.
candidate 2 (found by 3 of 54 passes): Users have independently requested the same ergonomic improvements for such cases (see [mp-units discussion #606](https://github.com/mpusz/mp-units/discussions/606)).
candidate 3 (found by 1 of 54 passes): Since that discussion, the Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

## insufficiency - grade 0.67 (fired in 3 of 18 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.83   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/1  -> 0.33
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/2/0  -> 0.67
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            2/0/0  -> 0.67
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 54 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 2 (found by 1 of 54 passes): With the standard tree-walking rules alone, sibling quantities have no direct arithmetic relationship.
candidate 3 (found by 1 of 54 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.

## implementation - grade 2.00  [binary: max] (fired in 9 of 18 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/1/2  -> 1.67
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    2/2/2  -> 2.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/1/1  -> 0.67
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            1/1/1  -> 1.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   1/2/1  -> 1.33
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): implementation experience from both **[[mp-units]](https://mpusz.github.io/mp-units)** and [[Sequoia]](https://github.com/ojrosten/sequoia) validates the structural conclusions.
candidate 2 (found by 3 of 54 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 3 (found by 3 of 54 passes): A simplified sketch of the implementation in **[[mp-units]](https://mpusz.github.io/mp-units)**:
candidate 4 (found by 3 of 54 passes): Implemented in [[mp-units]](https://mpusz.github.io/mp-units)

-->
