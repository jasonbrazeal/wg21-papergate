Verdict: Strong (10/14)

The paper offers solid, concrete support in the areas where it has real implementation experience and a clear account of the design gaps it addresses, but it is much thinner when it comes to showing who is affected, why the standard library is the right home, and why a library solution cannot suffice. The strongest material is grounded in the convergence of two independent implementations and the specific failures of the current two-abstraction model, while the weakest parts rely on general assertions about user demand and the necessity of standardization without much evidence.

- The paper most convincingly establishes why the current model matters and where it fails, backed by concrete implementation experience from mp-units and Sequoia and by specific examples of incorrect or awkward arithmetic.
- The prior art and alternatives section is well supported, showing an independent convergence on the same three-way split and a clear lineage from committee-requested collaboration.
- The paper claims but does not establish who is affected, offering only broad statements about user requests and usability reports without documented breadth or representative cases.
- The most glaring omission is the case for why a library will not do, where the paper describes internal design costs and limitations but does not show that these cannot be addressed by a non-standard library or that standardization is required to overcome them.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 9.67   accumulate 9.83   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.33  coordination 0.33  insufficiency 1.17  implementation 2.00
sample agreement: 118 of 126 section-criterion pairs unanimous (94%)
single-sample totals would have been: 10.00 / 9.50 / 10.00   (all 3 samples: 9.83)
headings: h2 15
on threshold: vehicle, insufficiency
splits: prior_art[5] 0/2/0  prior_art[7] 2/0/2  prior_art[12] 1/1/2  vehicle[3] 1/1/0
        coordination[2] 1/0/1  insufficiency[10] 0/0/1  implementation[5] 0/1/2
        implementation[9] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 13 of 18 sections, strong in 13)
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
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient for several common engineering patterns and, in places, mathematically too permissive.
candidate 2 (found by 3 of 54 passes): The following gaps — identified through implementation experience in **[[mp-units]](https://mpusz.github.io/mp-units)** and committee feedback — stand between the current model and that goal.
candidate 3 (found by 3 of 54 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 4 (found by 3 of 54 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.

## audience - grade 1.00 (fired in 2 of 18 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
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
  [13] 10 Integer division safety                   1/1/1  -> 1.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 2 (found by 2 of 54 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 3 (found by 1 of 54 passes): Users have consistently requested this feature — the need is real.

## prior_art - grade 2.00 (fired in 13 of 18 sections, strong in 9)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/2/0  -> 0.67
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         2/0/2  -> 1.33
  [8] 5 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [9] 6 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [10] 7 Range-validated quantity points            2/2/2  -> 2.00
  [11] 8 Runtime frame projections                  2/2/2  -> 2.00
  [12] 9 Text output for quantity points            1/1/2  -> 1.33
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   2/2/2  -> 2.00
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                1/1/1  -> 1.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): This paper is the product of a WG21-requested convergence between two independently developed approaches: the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation (Mateusz Pusz) and the Sequoia C++ library [[Sequoia]](https://github.com/ojrosten/sequoia) (Oliver Rosten).
candidate 2 (found by 3 of 54 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 3 (found by 3 of 54 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 4 (found by 3 of 54 passes): The `point_for<>` proposal targets Option 4 (siblings), which preserves the correct ISQ structure but still yields wrong arithmetic without additional annotations.

## vehicle - grade 1.33 (fired in 2 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/0  -> 0.67
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            2/2/2  -> 2.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.
candidate 2 (found by 2 of 54 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.

## coordination - grade 0.33 (fired in 1 of 18 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/0/1  -> 0.67
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
candidate 1 (found by 2 of 54 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.

## insufficiency - grade 1.17 (fired in 2 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        2/2/2  -> 2.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/1  -> 0.33
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 54 passes): The `0 * unit` syntax works, but it has a subtle cost: if the quantity’s stored unit differs from the spelled unit, the right-hand side must be rescaled before the numerical comparison.
candidate 2 (found by 1 of 54 passes): The library’s quantity hierarchy must encode the relationship between `position_vector` and `displacement` somehow, but every option available within [[P3045R7]](https://wg21.link/p3045r7)’s current type system has significant drawbacks:
candidate 3 (found by 1 of 54 passes): With the standard tree-walking rules alone, sibling quantities have no direct arithmetic relationship.
candidate 4 (found by 1 of 54 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.

## implementation - grade 2.00  [binary: max] (fired in 11 of 18 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/1/2  -> 1.00
  [6] 4 Non-negative quantities                    2/2/2  -> 2.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [9] 6 Affine spaces within quantity hierarchies  1/0/0  -> 0.33
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
candidate 3 (found by 3 of 54 passes): The compile-time tag is already implemented as an experimental feature in [[mp-units]](https://mpusz.github.io/mp-units) and it drives an existing **runtime** enforcement on quantity point.
candidate 4 (found by 3 of 54 passes): The [[mp-units]](https://mpusz.github.io/mp-units) library already prototypes a `constraint_violation_handler<Rep>` customization point and a `constrained<T, ErrorPolicy>` wrapper

-->
