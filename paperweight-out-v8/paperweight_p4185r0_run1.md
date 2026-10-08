Verdict: Strong to Excellent (12/14)

The paper offers substantial support for its standardization case across most of the required dimensions, with particularly strong evidence from implementation experience, prior art, and committee coordination. The support is thinnest where the paper must show that a library alone cannot solve the problem, since that argument is asserted rather than demonstrated with the same depth as the other claims.

- The strongest support comes from the convergence of two independent implementations and the documented real-world feedback that motivated the three-way abstraction split.
- The paper also clearly establishes who is affected and why the standard is the right venue, especially through the temperature and integer-division examples.
- The most glaring omission is the underdeveloped argument for why a library cannot adequately address the gaps, which remains claimed but not established.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (11.50/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 11.50 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.50   corroborated 10.00   accumulate 12.17   max 13.33

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.67  insufficiency 0.83  implementation 2.00
sample agreement: 115 of 126 section-criterion pairs unanimous (91%)
single-sample totals would have been: 11.50 / 12.50 / 10.50   (all 3 samples: 11.50)
headings: h2 15
on threshold: audience, vehicle, coordination
splits: prior_art[6] 0/0/2  prior_art[12] 1/2/1  vehicle[3] 1/1/0  vehicle[10] 0/1/0
        vehicle[14] 1/0/0  coordination[2] 1/2/1  coordination[10] 0/0/1  insufficiency[5] 2/2/0
        insufficiency[11] 0/1/0  implementation[5] 2/0/2  implementation[14] 1/1/2
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

## audience - grade 1.50 (fired in 2 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
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
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 1 of 54 passes): After years of iteration, the Au team found that silently allowing same-kind different-unit integer division caused enough user confusion that they chose to **block it at compile time** by default
candidate 3 (found by 1 of 54 passes): After years of iteration, the Au team found that silently allowing same-kind different-unit integer division caused enough user confusion that they chose to block it at compile time by default
candidate 4 (found by 1 of 54 passes): The Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

## prior_art - grade 2.00 (fired in 12 of 18 sections, strong in 9)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/2  -> 0.67
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [9] 6 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [10] 7 Range-validated quantity points            2/2/2  -> 2.00
  [11] 8 Runtime frame projections                  2/2/2  -> 2.00
  [12] 9 Text output for quantity points            1/2/1  -> 1.33
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

## vehicle - grade 1.50 (fired in 5 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/0  -> 0.67
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  1/1/1  -> 1.00
  [10] 7 Range-validated quantity points            0/1/0  -> 0.33
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            2/2/2  -> 2.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   1/0/0  -> 0.33
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): The `quantity<point<R>>` unification must be standardized regardless of whether absolute quantities are adopted.
candidate 2 (found by 3 of 54 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.
candidate 3 (found by 2 of 54 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 4 (found by 1 of 54 passes): All of these problems dissolve when bounds and axis conventions are placed on origins.

## coordination - grade 1.67 (fired in 3 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/1  -> 1.33
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/1  -> 0.33
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.
candidate 2 (found by 2 of 54 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming: `quantity`, `double`, and other numeric types should be substitutable in generic algorithms.
candidate 3 (found by 1 of 54 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.
candidate 4 (found by 1 of 54 passes): Since that discussion, the Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

## insufficiency - grade 0.83 (fired in 2 of 18 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        2/2/0  -> 1.33
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/1/0  -> 0.33
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 54 passes): The library’s quantity hierarchy must encode the relationship between `position_vector` and `displacement` somehow, but every option available within [[P3045R7]](https://wg21.link/p3045r7)’s current type system has significant drawbacks
candidate 2 (found by 1 of 54 passes): In the library, the magnitude of a vector quantity is its first scalar ancestor in the tree. Here, `norm(position_vector)` is `radial_distance` and `norm(displacement)` is `distance`.
candidate 3 (found by 1 of 54 passes): The variadic `point_for()` passes the location to the projection functor at the call site

## implementation - grade 2.00  [binary: max] (fired in 10 of 18 sections, strong in 6)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        2/0/2  -> 1.33
  [6] 4 Non-negative quantities                    2/2/2  -> 2.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            1/1/1  -> 1.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   2/2/2  -> 2.00
  [14] 11 Comparison against zero                   1/1/2  -> 1.33
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): implementation experience from both **[[mp-units]](https://mpusz.github.io/mp-units)** and [[Sequoia]](https://github.com/ojrosten/sequoia) validates the structural conclusions.
candidate 2 (found by 3 of 54 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 3 (found by 3 of 54 passes): The compile-time tag is already implemented as an experimental feature in [[mp-units]](https://mpusz.github.io/mp-units) and it drives an existing **runtime** enforcement on quantity point.
candidate 4 (found by 3 of 54 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.

-->
