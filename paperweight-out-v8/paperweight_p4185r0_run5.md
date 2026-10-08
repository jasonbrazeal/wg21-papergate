Verdict: Strong (9/14)

The paper offers solid grounding in real-world use cases and implementation experience, but its case for standardization is uneven: several central arguments about affected users, the need for a standard rather than a library, and coordination with other efforts are asserted more than demonstrated. The thinnest support appears where the paper relies on claims about generic programming impact, convergence of independent designs, and the insufficiency of library-only solutions without showing the underlying evidence.

- The strongest support comes from concrete use cases and implementation experience in both mp-units and Sequoia, which establish that the proposed taxonomy is implementable and addresses real limitations in current practice.
- The paper also establishes meaningful prior art and alternatives, particularly through Sequoia’s independent exploration of the same structural split and the identified shortcomings of the `point_for<>` approach.
- The most glaring omission is the lack of established evidence for who is affected and why a library will not do, since the paper asserts broad usability concerns and the absence of comparable libraries without demonstrating the scope or severity of the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 18. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.33   accumulate 9.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 0.67  coordination 0.67  insufficiency 0.50  implementation 2.00
sample agreement: 110 of 126 section-criterion pairs unanimous (87%)
single-sample totals would have been: 9.00 / 9.50 / 9.50   (all 3 samples: 9.00)
headings: h2 15
on threshold: none
splits: motivation[2] 2/2/0  motivation[7] 2/1/2  motivation[14] 2/0/0  audience[13] 1/1/2
        prior_art[7] 0/0/2  prior_art[13] 0/0/2  vehicle[3] 0/1/1  vehicle[9] 0/0/1
        vehicle[10] 2/0/0  vehicle[12] 1/0/0  coordination[2] 1/1/2  insufficiency[3] 0/1/0
        insufficiency[5] 0/2/0  insufficiency[9] 0/1/0  implementation[2] 1/2/2
        implementation[6] 2/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 13 of 18 sections, strong in 11)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/0  -> 1.33
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [6] 4 Non-negative quantities                    2/2/2  -> 2.00
  [7] 5 Absolute quantities  (part 1 of 2)         2/1/2  -> 1.67
  [8] 5 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [9] 6 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [10] 7 Range-validated quantity points            2/2/2  -> 2.00
  [11] 8 Runtime frame projections                  2/2/2  -> 2.00
  [12] 9 Text output for quantity points            2/2/2  -> 2.00
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   2/0/0  -> 0.67
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 2 (found by 3 of 54 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.
candidate 3 (found by 3 of 54 passes): many physical quantities — length, mass, duration, thermodynamic temperature, amount of substance, luminous intensity — are inherently non-negative, and a library that cannot express this is forced to scatter manual precondition checks throughout user code
candidate 4 (found by 3 of 54 passes): Today, the library has no way to express these relationships correctly.

## audience - grade 1.17 (fired in 2 of 18 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        1/1/1  -> 1.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   1/1/2  -> 1.33
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 2 of 54 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 3 (found by 1 of 54 passes): The Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

## prior_art - grade 2.00 (fired in 13 of 18 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/2  -> 0.67
  [8] 5 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [9] 6 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [10] 7 Range-validated quantity points            2/2/2  -> 2.00
  [11] 8 Runtime frame projections                  2/2/2  -> 2.00
  [12] 9 Text output for quantity points            2/2/2  -> 2.00
  [13] 10 Integer division safety                   0/0/2  -> 0.67
  [14] 11 Comparison against zero                   2/2/2  -> 2.00
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                1/1/1  -> 1.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 2 (found by 3 of 54 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 3 (found by 3 of 54 passes): The `point_for<>` proposal targets Option 4 (siblings), which preserves the correct ISQ structure but still yields wrong arithmetic without additional annotations.
candidate 4 (found by 3 of 54 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.

## vehicle - grade 0.67 (fired in 4 of 18 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 1.00   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/1  -> 0.67
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/1  -> 0.33
  [10] 7 Range-validated quantity points            2/0/0  -> 0.67
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            1/0/0  -> 0.33
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 54 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.
candidate 2 (found by 1 of 54 passes): The `quantity<point<R>>` unification must be standardized regardless of whether absolute quantities are adopted.
candidate 3 (found by 1 of 54 passes): All of these problems dissolve when bounds and axis conventions are placed on origins.
candidate 4 (found by 1 of 54 passes): The generic units library provides the underlying quantity point abstraction and enables users to extract and format the displacement from any origin

## coordination - grade 0.67 (fired in 1 of 18 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/2  -> 1.33
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.

## insufficiency - grade 0.50 (fired in 3 of 18 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/0  -> 0.33
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/2/0  -> 0.67
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/1/0  -> 0.33
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 54 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 2 (found by 1 of 54 passes): The library’s quantity hierarchy must encode the relationship between `position_vector` and `displacement` somehow, but every option available within [[P3045R7]](https://wg21.link/p3045r7)’s current type system has significant drawbacks:
candidate 3 (found by 1 of 54 passes): The `point_for<>` attribute, the associated quantity specification arithmetic, and the `quantity<point<R>>` unification described in this chapter are not yet implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.

## implementation - grade 2.00  [binary: max] (fired in 9 of 18 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/2  -> 1.67
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    2/2/1  -> 1.67
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            1/1/1  -> 1.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   2/2/2  -> 2.00
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): implementation experience from both **[[mp-units]](https://mpusz.github.io/mp-units)** and [[Sequoia]](https://github.com/ojrosten/sequoia) validates the structural conclusions.
candidate 2 (found by 3 of 54 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 3 (found by 3 of 54 passes): Since that discussion, the Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.
candidate 4 (found by 3 of 54 passes): A simplified sketch of the implementation in **[[mp-units]](https://mpusz.github.io/mp-units)**:

-->
