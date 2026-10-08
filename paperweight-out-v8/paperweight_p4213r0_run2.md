Verdict: Adequate to Strong (7/14)

The paper offers some useful groundwork by explaining why these units matter and by situating the proposal within existing work and the SI Brochure, but it leaves the central case for standardization largely asserted rather than demonstrated. The thinnest areas are the absence of any identified affected audience and the repeated reliance on a single sentence about interoperability to carry several distinct burdens.

- The strongest support is the clear motivation that these units are recognized by the SI Brochure as accepted for use with SI but are not SI units, making them a natural boundary for standardization.
- The paper also credibly grounds itself in prior art, including the companion quantities and units proposal and the mp-units implementation.
- The most glaring omission is that the paper never establishes who is affected by the lack of these standardized definitions.
- The claims about why a library will not do, why the standard is the right venue, and what implementation experience shows are all asserted but not substantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.33   accumulate 7.33   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.50  coordination 1.00  insufficiency 0.50  implementation 1.33
sample agreement: 92 of 98 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 8.00 / 6.50   (all 3 samples: 7.00)
headings: h2 13
on threshold: prior_art
splits: motivation[9] 0/2/2  motivation[10] 1/2/1  prior_art[6] 1/1/2  prior_art[9] 0/0/1
        coordination[8] 1/2/0  implementation[2] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 7 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 1/1/1  -> 1.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 2/2/2  -> 2.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 2/2/2  -> 2.00
  [8] 7 Optional: std::chrono Interoperability ... 1/1/1  -> 1.00
  [9] 8 Optional: Mathematical Functions for SI... 0/2/2  -> 1.33
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 1/2/1  -> 1.33
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): A user who includes the framework gets `quantity` , `unit` , `quantity_spec` , `prefix` — but no `metre` , no `kilogram` , no `second` .
candidate 2 (found by 3 of 42 passes): These units form a natural boundary with SI proper: they are recognized by the SI Brochure as units accepted for use with SI, but they are not SI units.
candidate 3 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.
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

## prior_art - grade 1.67 (fired in 7 of 14 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           2/2/2  -> 2.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 1/1/1  -> 1.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/2  -> 1.33
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 1/1/1  -> 1.00
  [8] 7 Optional: std::chrono Interoperability ... 1/1/1  -> 1.00
  [9] 8 Optional: Mathematical Functions for SI... 0/0/1  -> 0.33
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper is a companion to [[P3045R8]](https://wg21.link/p3045r8) (Quantities and Units Library).
candidate 2 (found by 3 of 42 passes): Under the absolute quantities model from [[P4185R0]](https://wg21.link/p4185r0), `kelvin` requires no explicit point origin.
candidate 3 (found by 3 of 42 passes): The SI Brochure [[SI]](https://www.bipm.org/en/publications/si-brochure) §5.4.3 states that the unit symbols °, ′, and ″ are not preceded by a space
candidate 4 (found by 3 of 42 passes): Short, unqualified symbols can conflict with existing names in user or library code.

## vehicle - grade 0.50 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
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

## coordination - grade 1.00 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 1/2/0  -> 1.00
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.
candidate 2 (found by 2 of 42 passes): provides bidirectional interoperability between SI time quantities and the `std::chrono` duration and time point types.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/2/1  -> 1.33
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
candidate 2 (found by 2 of 42 passes): The three additional constants listed above are a small, arbitrary selection drawn from the [mp-units](https://github.com/mpusz/mp-units) library — constants that proved useful in practice.
candidate 3 (found by 1 of 42 passes): The three additional constants listed above are a small, arbitrary selection drawn from the mp-units library — constants that proved useful in practice.

-->
