Verdict: Strong to Excellent (10/14)

The paper offers solid support for its standardization case in the areas that matter most for technical credibility: it establishes why the problem is real, shows meaningful prior art and implementation experience, and explains why the standard library is the right home for the work. The support is thinnest around the human and process dimensions—who specifically is affected, how the work coordinates with existing efforts, and why a library outside the standard cannot suffice are asserted more than demonstrated.

- The strongest support is the combination of concrete real-world use cases, independent implementation experience in two libraries, and a clear account of why the current model is insufficient.
- The paper also establishes credible prior art and alternatives, including the WG21-requested convergence between mp-units and Sequoia.
- The case for standardization itself is well grounded in examples where domain logic, such as calendar arithmetic or quantity-point unification, belongs in the standard rather than in user code.
- The most glaring omission is the thin evidence for who is affected and why a non-standard library cannot address the need, since those claims rely on reported feedback and design drawbacks rather than demonstrated community impact or insurmountable library limitations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 7 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 18. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 9.67   accumulate 10.67   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 1.50  coordination 1.33  insufficiency 0.33  implementation 2.00
sample agreement: 117 of 126 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.50 / 10.00 / 11.50   (all 3 samples: 10.17)
headings: h2 15
on threshold: vehicle, coordination
splits: audience[3] 1/0/0  audience[4] 1/1/2  audience[13] 0/1/1  prior_art[12] 2/1/2
        prior_art[13] 2/0/2  vehicle[9] 0/2/0  vehicle[10] 0/2/1  coordination[4] 2/1/2
        insufficiency[5] 0/0/2
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
candidate 2 (found by 3 of 54 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 3 (found by 3 of 54 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.
candidate 4 (found by 3 of 54 passes): many physical quantities — length, mass, duration, thermodynamic temperature, amount of substance, luminous intensity — are inherently non-negative, and a library that cannot express this is forced to scatter manual precondition checks throughout user code

## audience - grade 1.00 (fired in 3 of 18 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/0  -> 0.33
  [4] 3 Motivation and scope  (part 1 of 2)        1/1/2  -> 1.33
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [10] 7 Range-validated quantity points            0/0/0  -> 0.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            0/0/0  -> 0.00
  [13] 10 Integer division safety                   0/1/1  -> 0.67
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 54 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 2 of 54 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 3 (found by 1 of 54 passes): The following gaps — identified through implementation experience in **[[mp-units]](https://mpusz.github.io/mp-units)** and committee feedback — stand between the current model and that goal.
candidate 4 (found by 1 of 54 passes): Users have independently requested the same ergonomic improvements for such cases (see [mp-units discussion #606](https://github.com/mpusz/mp-units/discussions/606)).

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
  [12] 9 Text output for quantity points            2/1/2  -> 1.67
  [13] 10 Integer division safety                   2/0/2  -> 1.33
  [14] 11 Comparison against zero                   2/2/2  -> 2.00
  [15] 12 Summary                                   2/2/2  -> 2.00
  [16] 13 Next steps                                1/1/1  -> 1.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): This paper is the product of a WG21-requested convergence between two independently developed approaches: the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation (Mateusz Pusz) and the Sequoia C++ library [[Sequoia]](https://github.com/ojrosten/sequoia) (Oliver Rosten).
candidate 2 (found by 3 of 54 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 3 (found by 3 of 54 passes): An alternative approach — suggested by Chip Hogg as a “nature-based constant” idiom — is to subtract `absolute_zero` directly from the point, obtaining the displacement from the physical zero
candidate 4 (found by 3 of 54 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.

## vehicle - grade 1.50 (fired in 3 of 18 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    0/0/0  -> 0.00
  [7] 5 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [8] 5 Absolute quantities  (part 2 of 2)         0/0/0  -> 0.00
  [9] 6 Affine spaces within quantity hierarchies  0/2/0  -> 0.67
  [10] 7 Range-validated quantity points            0/2/1  -> 1.00
  [11] 8 Runtime frame projections                  0/0/0  -> 0.00
  [12] 9 Text output for quantity points            2/2/2  -> 2.00
  [13] 10 Integer division safety                   0/0/0  -> 0.00
  [14] 11 Comparison against zero                   0/0/0  -> 0.00
  [15] 12 Summary                                   0/0/0  -> 0.00
  [16] 13 Next steps                                0/0/0  -> 0.00
  [17] 14 Acknowledgments                           0/0/0  -> 0.00
  [18] 15 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 54 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.
candidate 2 (found by 1 of 54 passes): The `quantity<point<R>>` unification must be standardized regardless of whether absolute quantities are adopted.
candidate 3 (found by 1 of 54 passes): The quantity type system has no mechanism to express “add 100 m when converting.”
candidate 4 (found by 1 of 54 passes): The design handles the two abstractions differently:

## coordination - grade 1.33 (fired in 2 of 18 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/1/2  -> 1.67
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
candidate 2 (found by 3 of 54 passes): Users have independently requested the same ergonomic improvements for such cases (see [mp-units discussion #606](https://github.com/mpusz/mp-units/discussions/606)).

## insufficiency - grade 0.33 (fired in 1 of 18 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation and scope  (part 1 of 2)        0/0/0  -> 0.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/2  -> 0.67
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
candidate 1 (found by 1 of 54 passes): The library’s quantity hierarchy must encode the relationship between `position_vector` and `displacement` somehow, but every option available within [[P3045R7]](https://wg21.link/p3045r7)’s current type system has significant drawbacks:

## implementation - grade 2.00  [binary: max] (fired in 9 of 18 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [5] 3 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [6] 4 Non-negative quantities                    2/2/2  -> 2.00
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
candidate 2 (found by 3 of 54 passes): Most proposed features are already implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.
candidate 3 (found by 3 of 54 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 4 (found by 3 of 54 passes): The compile-time tag is already implemented as an experimental feature in [[mp-units]](https://mpusz.github.io/mp-units) and it drives an existing **runtime** enforcement on quantity point.

-->
