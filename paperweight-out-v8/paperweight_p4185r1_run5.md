Verdict: Strong to Excellent (10/14)

The paper offers solid support in the areas that matter most for a library-level design discussion: it clearly motivates the problem, shows credible prior art, and demonstrates real implementation experience. The case is much thinner, however, when it comes to explaining who is concretely affected, why this belongs in the standard rather than in a library, and how the work coordinates with existing standardization efforts.

- The strongest support is the combination of concrete real-world use cases, independent implementation experience from two libraries, and clear identification of where the current two-abstraction model breaks down.
- The paper also establishes meaningful prior art by showing that the proposed three-way split has been independently explored and implemented, which lends credibility to the design direction.
- The most glaring omission is the lack of an established argument for why this must be standardized in C++ itself, since the paper does not show that existing or proposed library mechanisms cannot carry the design.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 7 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 10.00   accumulate 11.00   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.00  coordination 0.83  insufficiency 1.50  implementation 2.00
sample agreement: 118 of 133 section-criterion pairs unanimous (89%)
single-sample totals would have been: 11.50 / 9.00 / 10.50   (all 3 samples: 10.17)
headings: h2 16
on threshold: coordination, insufficiency
splits: motivation[8] 2/1/2  audience[14] 1/0/1  prior_art[8] 0/0/2  prior_art[16] 2/1/2
        vehicle[4] 1/1/0  vehicle[10] 0/0/1  vehicle[12] 1/0/0  vehicle[13] 2/0/2
        coordination[3] 2/1/2  insufficiency[5] 2/1/0  insufficiency[10] 0/1/0
        insufficiency[11] 2/0/0  implementation[7] 2/2/1  implementation[15] 2/1/2
        implementation[17] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 13 of 19 sections, strong in 13)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [7] 5 Non-negative quantities                    2/2/2  -> 2.00
  [8] 6 Absolute quantities  (part 1 of 2)         2/1/2  -> 1.67
  [9] 6 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [10] 7 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           2/2/2  -> 2.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient for several common engineering patterns and, in places, mathematically too permissive.
candidate 2 (found by 3 of 57 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 3 (found by 3 of 57 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.
candidate 4 (found by 3 of 57 passes): many physical quantities — length, mass, duration, thermodynamic temperature, amount of substance, luminous intensity — are inherently non-negative, and a library that cannot express this is forced to scatter manual precondition checks throughout user code

## audience - grade 0.83 (fired in 2 of 19 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
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
  [14] 11 Integer division safety                   1/0/1  -> 0.67
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 1 of 57 passes): The Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.
candidate 3 (found by 1 of 57 passes): After years of iteration, the Au team found that silently allowing same-kind different-unit integer division caused enough user confusion that they chose to block it at compile time by default

## prior_art - grade 2.00 (fired in 11 of 19 sections, strong in 9)
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
  [13] 10 Text output for quantity points           1/1/1  -> 1.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/1/2  -> 1.67
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): This paper is the product of a WG21-requested convergence between two independently developed approaches: the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation (Mateusz Pusz) and the Sequoia C++ library [[Sequoia]](https://github.com/ojrosten/sequoia) (Oliver Rosten).
candidate 2 (found by 3 of 57 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 3 (found by 3 of 57 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 4 (found by 3 of 57 passes): The `point_for<>` proposal targets Option 4 (siblings), which preserves the correct ISQ structure but still yields wrong arithmetic without additional annotations.

## vehicle - grade 1.00 (fired in 4 of 19 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               1/1/0  -> 0.67
  [5] 4 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/1  -> 0.33
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  1/0/0  -> 0.33
  [13] 10 Text output for quantity points           2/0/2  -> 1.33
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 57 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 2 (found by 2 of 57 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.
candidate 3 (found by 1 of 57 passes): The `quantity<point<R>>` unification must be standardized regardless of whether absolute quantities are adopted.
candidate 4 (found by 1 of 57 passes): The two mechanisms are complementary.

## coordination - grade 0.83 (fired in 1 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/1/2  -> 1.67
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.

## insufficiency - grade 1.50 (fired in 4 of 19 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/1/0  -> 1.00
  [6] 4 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [7] 5 Non-negative quantities                    0/0/0  -> 0.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [10] 7 Affine spaces within quantity hierarchies  0/1/0  -> 0.33
  [11] 8 Range-validated quantity points            2/0/0  -> 0.67
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The library’s quantity hierarchy must encode the relationship between `position_vector` and `displacement` somehow, but every option available within [[P3045R7]](https://wg21.link/p3045r7)’s current type system has significant drawbacks:
candidate 2 (found by 1 of 57 passes): The representation type has no access to the unit, so it cannot reason about physical bounds.
candidate 3 (found by 1 of 57 passes): These requirements cannot be met by a wrapper or a coding convention; they call for non-negativity to be part of the type system.
candidate 4 (found by 1 of 57 passes): The `point_for<>` attribute, the associated quantity specification arithmetic, and the `quantity<point<R>>` unification described in this chapter are not yet implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.

## implementation - grade 2.00  [binary: max] (fired in 10 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    2/2/1  -> 1.67
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            1/1/1  -> 1.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/1/2  -> 1.67
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                1/0/1  -> 0.67
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): implementation experience from both **[[mp-units]](https://mpusz.github.io/mp-units)** and [[Sequoia]](https://github.com/ojrosten/sequoia) validates the structural conclusions.
candidate 2 (found by 3 of 57 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 3 (found by 3 of 57 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library already prototypes a `constraint_violation_handler<Rep>` customization point and a `constrained<T, ErrorPolicy>` wrapper
candidate 4 (found by 3 of 57 passes): Since that discussion, the Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

-->
