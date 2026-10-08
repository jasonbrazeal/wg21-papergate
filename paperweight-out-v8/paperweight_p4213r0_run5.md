Verdict: Adequate to Strong (7/14)

The paper offers solid evidence that the proposed definitions have been drawn from real implementation experience and that the work fits into an existing standardization context, but it does not convincingly establish who is affected or why standardization, rather than a library, is necessary. The thinnest parts of the case are the repeated assertions about interoperability and freestanding use, which are stated as conclusions without supporting detail.

- The strongest support comes from the direct derivation of the synopses from the mp-units library and the note that the selected constants proved useful in practice.
- The paper also grounds itself well in prior art by tying the proposal to P3045R8, the SI Brochure, and the absolute quantities model.
- The case for why this belongs in the standard rather than a library rests almost entirely on a single sentence about interoperability, with no elaboration.
- The most glaring omission is any identification of the affected users or communities, leaving the audience for the proposal unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.67   accumulate 7.83   max 8.67

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.50  vehicle 0.67  coordination 0.83  insufficiency 0.50  implementation 1.67
sample agreement: 89 of 98 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.00 / 7.50 / 8.50   (all 3 samples: 7.00)
headings: h2 13
on threshold: prior_art, implementation
splits: motivation[6] 1/2/2  motivation[7] 0/2/2  motivation[9] 2/1/2  motivation[10] 1/2/2
        prior_art[8] 1/0/0  vehicle[2] 0/0/1  vehicle[8] 0/1/0  coordination[8] 0/0/2
        implementation[2] 1/2/2
## END SUMMARY

## motivation - grade 1.83 (fired in 7 of 14 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 1/1/1  -> 1.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/2/2  -> 1.67
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/2/2  -> 1.33
  [8] 7 Optional: std::chrono Interoperability ... 1/1/1  -> 1.00
  [9] 8 Optional: Mathematical Functions for SI... 2/1/2  -> 1.67
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 1/2/2  -> 1.67
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): These units form a natural boundary with SI proper: they are recognized by the SI Brochure as units accepted for use with SI, but they are not SI units.
candidate 2 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.
candidate 3 (found by 3 of 42 passes): Separating it into its own chapter lets LEWG vote on this integration independently and allows the mandatory core to remain usable in freestanding environments.
candidate 4 (found by 3 of 42 passes): A common need is to express a quantity using the prefix that keeps the numerical value in a human-friendly range — whether for display, logging, or passing to another function.

## audience - grade 0.00 (fired in 0 of 14 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 0/0/0  -> 0.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 0/0/0  -> 0.00
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 6 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           2/2/2  -> 2.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 1/1/1  -> 1.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 1/1/1  -> 1.00
  [8] 7 Optional: std::chrono Interoperability ... 1/0/0  -> 0.33
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper is a companion to [[P3045R8]](https://wg21.link/p3045r8) (Quantities and Units Library).
candidate 2 (found by 3 of 42 passes): Under the absolute quantities model from [[P4185R0]](https://wg21.link/p4185r0), `kelvin` requires no explicit point origin.
candidate 3 (found by 3 of 42 passes): The SI Brochure [[SI]](https://www.bipm.org/en/publications/si-brochure) §5.4.3 states that the unit symbols °, ′, and ″ are not preceded by a space
candidate 4 (found by 3 of 42 passes): The three additional constants listed above are a small, arbitrary selection drawn from the [mp-units](https://github.com/mpusz/mp-units) library — constants that proved useful in practice.

## vehicle - grade 0.67 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/1  -> 0.33
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 0/1/0  -> 0.33
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.
candidate 2 (found by 1 of 42 passes): Shipping the framework without SI content would be like shipping `<algorithm>` without `<vector>` — or the coroutine framework without `std::task`.
candidate 3 (found by 1 of 42 passes): Separating it into its own chapter lets LEWG vote on this integration independently and allows the mandatory core to remain usable in freestanding environments.

## coordination - grade 0.83 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 0/0/2  -> 0.67
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.
candidate 2 (found by 1 of 42 passes): provides bidirectional interoperability between SI time quantities and the `std::chrono` duration and time point types.

## insufficiency - grade 0.50 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 0/0/0  -> 0.00
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.

## implementation - grade 1.67  [binary: max] (fired in 2 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/2/2  -> 1.67
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 0/0/0  -> 0.00
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): All synopses in this paper are derived from the open-source [mp-units](https://github.com/mpusz/mp-units) library, adapted to use `std::` namespaces.
candidate 2 (found by 2 of 42 passes): constants that proved useful in practice.
candidate 3 (found by 1 of 42 passes): The three additional constants listed above are a small, arbitrary selection drawn from the mp-units library — constants that proved useful in practice.

-->
