Verdict: Strong (9/14)

The paper offers substantial support for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several essential arguments underdeveloped, particularly the need for a standard rather than a library and the breadth of the affected user base. The strongest material comes from concrete implementation evidence and independent convergence on the same design, while the thinnest support concerns why existing libraries cannot adequately serve the need.

- The paper convincingly grounds its motivation in real-world implementation experience and documented gaps in the current two-abstraction model.
- It establishes meaningful prior art and implementation experience through both mp-units and the independent Sequoia library, reinforcing the design’s viability.
- The case for who is affected and why standardization is necessary remains asserted rather than demonstrated with concrete user or ecosystem evidence.
- The paper does not establish why a library solution would be insufficient, leaving a central standardization rationale unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 6 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.00   accumulate 9.83   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 0.83  coordination 1.17  insufficiency 0.00  implementation 2.00
sample agreement: 121 of 133 section-criterion pairs unanimous (91%)
single-sample totals would have been: 10.00 / 9.00 / 10.00   (all 3 samples: 9.17)
headings: h2 16
on threshold: coordination
splits: audience[14] 1/2/1  prior_art[13] 1/0/1  prior_art[16] 1/2/2  prior_art[17] 0/0/1
        vehicle[4] 1/1/0  vehicle[13] 0/0/2  coordination[3] 2/1/2  coordination[4] 1/0/1
        coordination[14] 2/0/0  implementation[6] 0/0/2  implementation[9] 1/0/1
        implementation[11] 0/1/0
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
  [8] 6 Absolute quantities  (part 1 of 2)         2/2/2  -> 2.00
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
candidate 2 (found by 3 of 57 passes): The following gaps — identified through implementation experience in mp-units and committee feedback — stand between the current model and that goal.
candidate 3 (found by 3 of 57 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 4 (found by 3 of 57 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.

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
  [14] 11 Integer division safety                   1/2/1  -> 1.33
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): By far the most frequently reported usability issue with the current [[P3045R7]](https://wg21.link/p3045r7) design involves temperature.
candidate 2 (found by 3 of 57 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming

## prior_art - grade 2.00 (fired in 13 of 19 sections, strong in 11)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/0  -> 0.00
  [7] 5 Non-negative quantities                    2/2/2  -> 2.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [10] 7 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           1/0/1  -> 0.67
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   1/2/2  -> 1.67
  [17] 14 Next steps                                0/0/1  -> 0.33
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 2 (found by 3 of 57 passes): This chapter describes what [[mp-units]](https://mpusz.github.io/mp-units) V2 has already implemented (tagging, inheritance, and runtime enforcement on `quantity_point`) and where the design hits genuine limits (propagation through arithmetic and automatic inference for named derived specs).
candidate 3 (found by 3 of 57 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 4 (found by 3 of 57 passes): Oliver Rosten raised in LEWGI discussions that `relative_point_origin` cannot express axis-inverting transformations, and that this gap suggests origins are insufficient — and that quantities should bear more of the modeling burden, as his library does.

## vehicle - grade 0.83 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
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
  [10] 7 Affine spaces within quantity hierarchies  1/1/1  -> 1.00
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/2  -> 0.67
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The `quantity<point<R>>` unification must be standardized regardless of whether absolute quantities are adopted.
candidate 2 (found by 1 of 57 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.
candidate 3 (found by 1 of 57 passes): No mainstream units library in any programming language — including F# Units of Measure, Haskell’s *dimensional* package, or Python’s Pint — distinguishes absolute quantities, deltas, and points as three separate types in the type system.
candidate 4 (found by 1 of 57 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.

## coordination - grade 1.17 (fired in 3 of 19 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/1/2  -> 1.67
  [4] 3 Introduction                               1/0/1  -> 0.67
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
candidate 2 (found by 2 of 57 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.
candidate 3 (found by 1 of 57 passes): The Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

## insufficiency - grade 0.00 (fired in 0 of 19 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
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
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 11 of 19 sections, strong in 7)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        0/0/2  -> 0.67
  [7] 5 Non-negative quantities                    2/2/2  -> 2.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         1/0/1  -> 0.67
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/1/0  -> 0.33
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                1/1/1  -> 1.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient
candidate 2 (found by 3 of 57 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 3 (found by 3 of 57 passes): This chapter describes what [[mp-units]](https://mpusz.github.io/mp-units) V2 has already implemented (tagging, inheritance, and runtime enforcement on `quantity_point`) and where the design hits genuine limits (propagation through arithmetic and automatic inference for named derived specs).
candidate 4 (found by 3 of 57 passes): Since that discussion, the Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

-->
