Verdict: Strong (9/14)

The paper offers solid support in a few areas, particularly in explaining why the current state is a usability problem and in showing that a workable implementation exists, but it leaves several essential parts of the standardization case asserted rather than demonstrated. The thinnest support is around who would actually be affected and why the feature must be standardized rather than supplied through a library.

- The strongest support is the concrete implementation experience, with a working example provided against a current implementation.
- The paper clearly establishes why the status quo is inadequate and why alternatives that discard static extent information are unsatisfactory.
- The case for why this belongs in the standard, rather than in a library, rests on a single unelaborated claim about portability and preventing dependence on the wrong representation.
- The paper does not establish who is affected by the problem or the scale of the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.33/14)

Provisionally addressed: 6 of 7. Provisional points: 9.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.33   corroborated 9.00   accumulate 9.33   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 1.33  implementation 2.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 9.50 / 9.50 / 9.00   (all 3 samples: 9.33)
headings: h2 9
on threshold: vehicle, coordination, insufficiency, implementation
splits: motivation[4] 2/0/0  insufficiency[7] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       2/2/2  -> 2.00
  [4] 3 Impact On the Standard                     2/0/0  -> 0.67
  [5] 4 Design Decisions                           1/1/1  -> 1.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 2/2/2  -> 2.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Comparing before and after, the usability gain with structured bindings alone is marginal, but it allows us to use descriptive names for the extents to improve readability.
candidate 2 (found by 3 of 30 passes): Demoting static extents to runtime values would be lossy, with no way for user code to recover the compile-time nature afterwards.
candidate 3 (found by 3 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.
candidate 4 (found by 1 of 30 passes): Destructuring `std::extents` in the current specification [[N4944]](https://wg21.link/n4944) is ill-formed, because `std::extents` stores its runtime extents in a private non-static data member, which is inaccessible to structured bindings.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       2/2/2  -> 2.00
  [4] 3 Impact On the Standard                     2/2/2  -> 2.00
  [5] 4 Design Decisions                           2/2/2  -> 2.00
  [6] 5 Proposed implementation                    1/1/1  -> 1.00
  [7] 6 Alternative considered: demote static e... 2/2/2  -> 2.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [[P0009R18]](https://wg21.link/p0009r18) proposed `std::mdspan` , which was approved for C++23.
candidate 2 (found by 3 of 30 passes): The proposed implementation uses the tuple interface and queries the extents type whether a specific extent is static or dynamic.
candidate 3 (found by 3 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.
candidate 4 (found by 2 of 30 passes): Such bindings decompose the object representation, not the logical extents.

## vehicle - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     2/2/2  -> 2.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Providing a tuple interface gives users one portable decomposition over the logical extents and prevents code from depending on the wrong representation.

## coordination - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     2/2/2  -> 2.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Providing a tuple interface gives users one portable decomposition over the logical extents and prevents code from depending on the wrong representation.

## insufficiency - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     2/2/2  -> 2.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 1/1/0  -> 0.67
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Providing a tuple interface gives users one portable decomposition over the logical extents and prevents code from depending on the wrong representation.
candidate 2 (found by 2 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/0  -> 0.00
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    2/2/2  -> 2.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): An example of such an implementation using GCC trunk’s implementation of `<mdspan>` with `-std=c++26` on Godbolt is provided here: [https://godbolt.org/z/sfMa5zEd5](https://godbolt.org/z/sfMa5zEd5).

-->
