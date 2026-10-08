Verdict: Strong (9/14)

The paper offers solid support for its core technical motivation and for the existence of implementation experience, but its case for standardization is uneven: the strongest evidence concerns why the current model is inadequate and that the proposed structure has been built and tested, while the thinnest support concerns who is actually affected, why the work belongs in the standard, and how it would interoperate with existing practice.

- The paper most convincingly establishes that real-world use of the reference implementation and independent work in Sequoia reveal genuine limitations in the two-abstraction model, including mathematically permissive or awkward patterns for common engineering quantities.
- It also clearly establishes implementation experience, with most features prototyped in mp-units and the same structural split independently implemented in Sequoia.
- The paper claims but does not establish that the affected audience is broad, relying on reported temperature usability complaints and Au library experience without demonstrating how widespread or representative those cases are.
- The most glaring omission is the absence of an established case for why this needs to be in the C++ standard rather than remaining a library capability, since the paper asserts the need but does not show that a non-standard library would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.33/14)

Provisionally addressed: 7 of 7. Provisional points: 9.33 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.33   corroborated 9.33   accumulate 10.00   max 10.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.33  coordination 0.67  insufficiency 1.33  implementation 2.00
sample agreement: 118 of 133 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.00 / 9.00 / 9.50   (all 3 samples: 9.33)
headings: h2 16
on threshold: insufficiency
splits: motivation[13] 2/0/2  motivation[15] 2/2/0  prior_art[8] 0/0/2  prior_art[13] 1/2/2
        prior_art[14] 2/0/0  prior_art[17] 1/1/0  vehicle[11] 0/1/0  vehicle[13] 0/0/1
        coordination[12] 1/0/0  coordination[13] 0/0/1  insufficiency[4] 1/0/0
        insufficiency[5] 2/0/0  insufficiency[11] 2/0/0  implementation[7] 1/2/1
        implementation[17] 1/0/0
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
  [10] 7 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           2/0/2  -> 1.33
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/0  -> 1.33
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient for several common engineering patterns and, in places, mathematically too permissive.
candidate 2 (found by 3 of 57 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 3 (found by 3 of 57 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.
candidate 4 (found by 3 of 57 passes): many physical quantities — length, mass, duration, thermodynamic temperature, amount of substance, luminous intensity — are inherently non-negative, and a library that cannot express this is forced to scatter manual precondition checks throughout user code

## audience - grade 1.00 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
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
  [14] 11 Integer division safety                   1/1/1  -> 1.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 2 of 57 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 3 (found by 1 of 57 passes): The Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

## prior_art - grade 2.00 (fired in 13 of 19 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/2  -> 0.67
  [9] 6 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [10] 7 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           1/2/2  -> 1.67
  [14] 11 Integer division safety                   2/0/0  -> 0.67
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                1/1/0  -> 0.67
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This paper is the product of a WG21-requested convergence between two independently developed approaches: the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation (Mateusz Pusz) and the Sequoia C++ library [[Sequoia]](https://github.com/ojrosten/sequoia) (Oliver Rosten).
candidate 2 (found by 3 of 57 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 3 (found by 3 of 57 passes): Independent work on convex-space foundations for measurement [[Rosten2025]](https://docs.google.com/presentation/d/1qjw0SURoJtX_DhaFUr62F-BXtQJjdQRqzMUHvQ6h3-E/edit?usp=sharing) reaches the same conclusion: a `quantity<isq::mass[kg]>` is mathematically *not* an element of a vector space, and modelling it as one is a category error, not just an ergonomic one.
candidate 4 (found by 3 of 57 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.

## vehicle - grade 0.33 (fired in 2 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/1/0  -> 0.33
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/1  -> 0.33
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The design handles the two abstractions differently:
candidate 2 (found by 1 of 57 passes): The generic units library provides the underlying quantity point abstraction and enables users to extract and format the displacement from any origin

## coordination - grade 0.67 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  1/0/0  -> 0.33
  [13] 10 Text output for quantity points           0/0/1  -> 0.33
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.
candidate 2 (found by 1 of 57 passes): The motivating use cases (detailed in Limitations of `relative_point_origin`) include: - Location-dependent altitude conversions (MSL ↔︎ HAE with geoid undulation) - Coordinate frame rotations and full affine transformations - Representation types with private members (decimal, rational, arbitrary-precision)
candidate 3 (found by 1 of 57 passes): The generic units library provides the underlying quantity point abstraction and enables users to extract and format the displacement from any origin

## insufficiency - grade 1.33 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               1/0/0  -> 0.33
  [5] 4 Motivation and scope  (part 1 of 2)        2/0/0  -> 0.67
  [6] 4 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            2/0/0  -> 0.67
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 2 (found by 1 of 57 passes): The representation type is unit-unaware. A `BoundedDouble<0, 360>` rep type intended to enforce the bearing range [0°, 360°) works correctly when the quantity is stored in degrees, but becomes meaningless when stored in radians.
candidate 3 (found by 1 of 57 passes): The library’s quantity hierarchy must encode the relationship between `position_vector` and `displacement` somehow, but every option available within [[P3045R7]](https://wg21.link/p3045r7)’s current type system has significant drawbacks
candidate 4 (found by 1 of 57 passes): In the library, the magnitude of a vector quantity is its first scalar ancestor in the tree. Here, `norm(position_vector)` is `radial_distance` and `norm(displacement)` is `distance`.

## implementation - grade 2.00  [binary: max] (fired in 10 of 19 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    1/2/1  -> 1.33
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            1/1/1  -> 1.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                1/0/0  -> 0.33
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): implementation experience from both **[[mp-units]](https://mpusz.github.io/mp-units)** and [[Sequoia]](https://github.com/ojrosten/sequoia) validates the structural conclusions.
candidate 2 (found by 3 of 57 passes): Most proposed features are already implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.
candidate 3 (found by 3 of 57 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 4 (found by 3 of 57 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library already prototypes a `constraint_violation_handler<Rep>` customization point and a `constrained<T, ErrorPolicy>` wrapper

-->
