Verdict: Strong (9/14)

The paper offers a solid foundation for its standardization case in the areas where it engages directly with existing practice and alternatives, but it leaves several essential justifications asserted rather than demonstrated. The thinnest support concerns the people affected by the problem and the argument that only a standard library change—rather than some other mechanism—can provide the portability the paper seeks.

- The strongest support comes from the concrete demonstration that current implementations already expose structured bindings through representation details, making the need for a portable logical interface tangible.
- The discussion of alternatives credibly shows why discarding compile-time extents or relying on accidental representation decomposition would be unsatisfactory.
- The paper claims, but does not establish, that a tuple interface is the right standardization vehicle for preventing dependence on the wrong representation.
- The most glaring omission is any account of who is affected by the current state of affairs, leaving the motivating user base unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.00   max 11.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 9.50 / 8.50 / 9.00   (all 3 samples: 9.00)
headings: h2 9
on threshold: vehicle, coordination, insufficiency, implementation
splits: insufficiency[4] 2/1/2  insufficiency[7] 1/0/0  implementation[4] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       2/2/2  -> 2.00
  [4] 3 Impact On the Standard                     2/2/2  -> 2.00
  [5] 4 Design Decisions                           1/1/1  -> 1.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 2/2/2  -> 2.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Comparing before and after, the usability gain with structured bindings alone is marginal, but it allows us to use descriptive names for the extents to improve readability.
candidate 2 (found by 3 of 30 passes): Demoting static extents to runtime values would be lossy, with no way for user code to recover the compile-time nature afterwards.
candidate 3 (found by 3 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.
candidate 4 (found by 1 of 30 passes): Such bindings decompose the object representation, not the logical extents.

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
candidate 1 (found by 3 of 30 passes): Some implementations nevertheless happen to accept structured bindings for `std::extents` due to representation details. Such bindings decompose the object representation, not the logical extents.
candidate 2 (found by 3 of 30 passes): An example of such an implementation using GCC trunk’s implementation of `<mdspan>` with `-std=c++26` on Godbolt is provided here: [https://godbolt.org/z/sfMa5zEd5](https://godbolt.org/z/sfMa5zEd5).
candidate 3 (found by 3 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.
candidate 4 (found by 2 of 30 passes): The proposed feature becomes even more powerful in combination with [[P1061R10]](https://wg21.link/p1061r10) (adopted into C++26), which allows structured bindings to introduce a pack:

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

## insufficiency - grade 1.00 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     2/1/2  -> 1.67
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    0/0/0  -> 0.00
  [7] 6 Alternative considered: demote static e... 1/0/0  -> 0.33
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Providing a tuple interface gives users one portable decomposition over the logical extents and prevents code from depending on the wrong representation.
candidate 2 (found by 1 of 30 passes): This alternative is simpler to specify, but that simplicity is bought by discarding the compile-time information that the user encoded in the static extents, with no way for user code to recover it.

## implementation - grade 2.00  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Motivation and Scope                       0/0/0  -> 0.00
  [4] 3 Impact On the Standard                     0/0/1  -> 0.33
  [5] 4 Design Decisions                           0/0/0  -> 0.00
  [6] 5 Proposed implementation                    2/2/2  -> 2.00
  [7] 6 Alternative considered: demote static e... 0/0/0  -> 0.00
  [8] 7 Wording                                    0/0/0  -> 0.00
  [9] 8 Acknowledgements                           0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): An example of such an implementation using GCC trunk’s implementation of `<mdspan>` with `-std=c++26` on Godbolt is provided here: [https://godbolt.org/z/sfMa5zEd5](https://godbolt.org/z/sfMa5zEd5).
candidate 2 (found by 1 of 30 passes): Some implementations nevertheless happen to accept structured bindings for `std::extents` due to representation details.

-->
