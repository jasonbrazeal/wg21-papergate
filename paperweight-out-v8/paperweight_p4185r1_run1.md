Verdict: Strong (9/14)

The paper offers solid grounding in implementation experience and a clear account of the gaps it addresses, but its case for standardization is uneven: several essential arguments—who is affected, why the standard is the right venue, and why a library cannot suffice—are asserted rather than demonstrated. The thinnest support appears where the paper leans on future work, informal coordination, or the absence of implementation rather than concrete evidence.

- The strongest support comes from real-world experience with mp-units and Au, including specific user-reported gaps and deployed design changes.
- The paper also establishes meaningful prior art and alternatives, particularly through the independent Sequoia library and discussion of the “nature-based constant” idiom.
- The most glaring omission is the lack of established evidence for why standardization is necessary, since the central features are admittedly not yet implemented in the reference library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 19. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.33   accumulate 9.33   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.00  coordination 0.67  insufficiency 0.17  implementation 2.00
sample agreement: 117 of 133 section-criterion pairs unanimous (88%)
single-sample totals would have been: 9.00 / 8.00 / 10.00   (all 3 samples: 9.00)
headings: h2 16
on threshold: none
splits: audience[4] 0/0/1  audience[14] 1/1/2  prior_art[6] 2/0/2  prior_art[13] 0/0/1
        prior_art[14] 0/0/2  vehicle[10] 0/0/2  vehicle[13] 1/1/2  coordination[3] 2/0/1
        coordination[4] 1/0/0  coordination[5] 1/0/0  insufficiency[10] 0/1/0
        implementation[6] 1/0/0  implementation[7] 2/1/2  implementation[11] 0/0/1
        implementation[16] 2/1/2  implementation[17] 1/0/0
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
candidate 2 (found by 3 of 57 passes): The following gaps — identified through implementation experience in **[[mp-units]](https://mpusz.github.io/mp-units)** and committee feedback — stand between the current model and that goal.
candidate 3 (found by 3 of 57 passes): The first seven describe real-world use cases where [[P3045R7]](https://wg21.link/p3045r7)’s two-abstraction model is insufficient or forces users into awkward workarounds.
candidate 4 (found by 3 of 57 passes): None of these options produces correct arithmetic without either manual casts or loss of type safety.

## audience - grade 1.17 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/1  -> 0.33
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
candidate 2 (found by 3 of 57 passes): The Au library evidence is real, but the primary concern with the stricter approach is generic programming
candidate 3 (found by 1 of 57 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.

## prior_art - grade 2.00 (fired in 14 of 19 sections, strong in 10)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        2/0/2  -> 1.33
  [7] 5 Non-negative quantities                    2/2/2  -> 2.00
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         2/2/2  -> 2.00
  [10] 7 Affine spaces within quantity hierarchies  2/2/2  -> 2.00
  [11] 8 Range-validated quantity points            2/2/2  -> 2.00
  [12] 9 Runtime frame projections                  2/2/2  -> 2.00
  [13] 10 Text output for quantity points           0/0/1  -> 0.33
  [14] 11 Integer division safety                   0/0/2  -> 0.67
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/2/2  -> 2.00
  [17] 14 Next steps                                1/1/1  -> 1.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): The closest prior art is Oliver Rosten’s Sequoia C++ library [[Sequoia]], which independently explores the same three-way split from a mathematical perspective.
candidate 2 (found by 3 of 57 passes): An alternative approach — suggested by Chip Hogg as a “nature-based constant” idiom — is to subtract `absolute_zero` directly from the point, obtaining the displacement from the physical zero.
candidate 3 (found by 3 of 57 passes): Oliver Rosten’s Sequoia library [[Sequoia]](https://github.com/ojrosten/sequoia) independently implements the same three-way structural split with a different API surface, confirming that the theoretical taxonomy is sound and implementable in C++.
candidate 4 (found by 3 of 57 passes): The `point_for<>` proposal targets Option 4 (siblings), which preserves the correct ISQ structure but still yields wrong arithmetic without additional annotations.

## vehicle - grade 1.00 (fired in 2 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.33
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
  [10] 7 Affine spaces within quantity hierarchies  0/0/2  -> 0.67
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           1/1/2  -> 1.33
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The `point_for<>` attribute, the associated quantity specification arithmetic, and the `quantity<point<R>>` unification described in this chapter are not yet implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.
candidate 2 (found by 1 of 57 passes): The generic units library provides the underlying quantity point abstraction and enables users to extract and format the displacement from any origin
candidate 3 (found by 1 of 57 passes): For points with non-trivial origins, **text output may be better left to domain-specific libraries and user customization**
candidate 4 (found by 1 of 57 passes): Formatting a timestamp as a calendar date requires knowledge of leap seconds, time zones, and calendar arithmetic — domain-specific logic that belongs in `std::chrono`, not in a units library.

## coordination - grade 0.67 (fired in 3 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/0/1  -> 1.00
  [4] 3 Introduction                               1/0/0  -> 0.33
  [5] 4 Motivation and scope  (part 1 of 2)        1/0/0  -> 0.33
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
candidate 1 (found by 2 of 57 passes): SG6 asked both authors to work together toward a unified design rather than advance separate proposals.
candidate 2 (found by 1 of 57 passes): The convergence of two independent implementations on the same structural conclusions strengthens the case that this taxonomy reflects genuine mathematical structure rather than an arbitrary design choice.
candidate 3 (found by 1 of 57 passes): Users have independently requested the same ergonomic improvements for such cases (see [mp-units discussion #606](https://github.com/mpusz/mp-units/discussions/606)).

## insufficiency - grade 0.17 (fired in 1 of 19 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
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
  [10] 7 Affine spaces within quantity hierarchies  0/1/0  -> 0.33
  [11] 8 Range-validated quantity points            0/0/0  -> 0.00
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   0/0/0  -> 0.00
  [15] 12 Comparison against zero                   0/0/0  -> 0.00
  [16] 13 Summary                                   0/0/0  -> 0.00
  [17] 14 Next steps                                0/0/0  -> 0.00
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 57 passes): The `point_for<>` attribute, the associated quantity specification arithmetic, and the `quantity<point<R>>` unification described in this chapter are not yet implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.

## implementation - grade 2.00  [binary: max] (fired in 11 of 19 sections, strong in 7)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Abstract                                   2/2/2  -> 2.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Motivation and scope  (part 1 of 2)        2/2/2  -> 2.00
  [6] 4 Motivation and scope  (part 2 of 2)        1/0/0  -> 0.33
  [7] 5 Non-negative quantities                    2/1/2  -> 1.67
  [8] 6 Absolute quantities  (part 1 of 2)         0/0/0  -> 0.00
  [9] 6 Absolute quantities  (part 2 of 2)         1/1/1  -> 1.00
  [10] 7 Affine spaces within quantity hierarchies  0/0/0  -> 0.00
  [11] 8 Range-validated quantity points            0/0/1  -> 0.33
  [12] 9 Runtime frame projections                  0/0/0  -> 0.00
  [13] 10 Text output for quantity points           0/0/0  -> 0.00
  [14] 11 Integer division safety                   2/2/2  -> 2.00
  [15] 12 Comparison against zero                   2/2/2  -> 2.00
  [16] 13 Summary                                   2/1/2  -> 1.67
  [17] 14 Next steps                                1/0/0  -> 0.33
  [18] 15 Acknowledgments                           0/0/0  -> 0.00
  [19] 16 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 57 passes): Real-world experience with the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation, together with feedback from SG6, BSI, ANSI, and the broader C++ community, shows that this two-abstraction model is insufficient
candidate 2 (found by 3 of 57 passes): Most proposed features are already implemented in **[[mp-units]](https://mpusz.github.io/mp-units)**.
candidate 3 (found by 3 of 57 passes): Each subsection provides concrete examples from the **[[mp-units]](https://mpusz.github.io/mp-units)** reference implementation and user feedback.
candidate 4 (found by 3 of 57 passes): Since that discussion, the Au library [[Au]](https://aurora-opensource.github.io/au) — which has extensive real-world experience with integer-backed quantities — has developed and deployed a stricter approach that was not presented to SG6 at the time.

-->
