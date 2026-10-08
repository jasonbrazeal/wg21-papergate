Verdict: Adequate to Strong (7/14)

The paper offers meaningful support for its standardization case in a few areas, particularly its relationship to the SI Brochure, its companion proposal, and the practical need for concise unit syntax, but the support is uneven and leaves several core questions about affected users, interoperability, and implementation experience largely asserted rather than demonstrated. The thinnest part of the case is the absence of any established description of who is affected, alongside only claimed support for why the standard library is the right venue and why a library solution would not suffice.

- The strongest support is for prior art and alternatives, where the paper clearly ties its design to the SI Brochure and to companion proposals such as P3045R8 and P4185R0.
- The paper also establishes why the feature matters by connecting the proposed units to recognized non-SI units and to common needs like human-friendly prefix selection.
- The weakest established area is implementation experience, which rests on derivation from the mp-units library but does not establish independent or standardized implementation evidence.
- The most glaring omission is the complete lack of an established account of who is affected by the proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 14. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.67   accumulate 7.50   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.83  coordination 1.17  insufficiency 0.33  implementation 1.00
sample agreement: 87 of 98 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.50 / 6.50 / 8.00   (all 3 samples: 7.33)
headings: h2 13
on threshold: none
splits: motivation[3] 1/1/0  motivation[4] 0/1/1  motivation[6] 1/2/1  motivation[9] 1/0/2
        prior_art[3] 1/1/0  prior_art[6] 1/2/1  prior_art[7] 1/0/0  vehicle[7] 1/0/1
        vehicle[9] 1/0/0  coordination[8] 2/0/2  insufficiency[6] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 14 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 The International System of Quantities ... 1/1/0  -> 0.67
  [4] 3 Core SI Definitions ( <sicore> )           0/1/1  -> 0.67
  [5] 4 Optional: Non-SI Units Accepted for Use... 1/1/1  -> 1.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/2/1  -> 1.33
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 2/2/2  -> 2.00
  [8] 7 Optional: std::chrono Interoperability ... 1/1/1  -> 1.00
  [9] 8 Optional: Mathematical Functions for SI... 1/0/2  -> 1.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 2/2/2  -> 2.00
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

## prior_art - grade 2.00 (fired in 8 of 14 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 The International System of Quantities ... 1/1/0  -> 0.67
  [4] 3 Core SI Definitions ( <sicore> )           2/2/2  -> 2.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 1/1/1  -> 1.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/2/1  -> 1.33
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 1/0/0  -> 0.33
  [8] 7 Optional: std::chrono Interoperability ... 0/0/0  -> 0.00
  [9] 8 Optional: Mathematical Functions for SI... 1/1/1  -> 1.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): This paper is a companion to [[P3045R8]](https://wg21.link/p3045r8) (Quantities and Units Library).
candidate 2 (found by 3 of 42 passes): The synopses assume that two features proposed in [[P4185R0]](https://wg21.link/p4185r0) are accepted: Non-negativity: if not accepted, all `non_negative` tags in `quantity_spec` definitions can simply be dropped.
candidate 3 (found by 3 of 42 passes): In the pre-P4185 design ([[P3045R8]](https://wg21.link/p3045r8)), `kelvin` had to declare `absolute_zero` as an `absolute_point_origin` , which prevented the multiply syntax from being used and forced users to write `absolute_zero + 28 * K` instead.
candidate 4 (found by 3 of 42 passes): The SI Brochure [[SI]](https://www.bipm.org/en/publications/si-brochure) §5.4.3 states that the unit symbols °, ′, and ″ are not preceded by a space

## vehicle - grade 0.83 (fired in 3 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 1/0/1  -> 0.67
  [8] 7 Optional: std::chrono Interoperability ... 0/0/0  -> 0.00
  [9] 8 Optional: Mathematical Functions for SI... 1/0/0  -> 0.33
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.
candidate 2 (found by 1 of 42 passes): These names must exist for code such as `5 * MHz` or `300 * pm` to compile without resorting to verbose qualified expressions like `5 * si::mega<si::hertz>`.
candidate 3 (found by 1 of 42 passes): Making this feature opt-in (via a dedicated header and an explicit `using namespace std::si::unit_symbols;`) respects the longstanding C++ principle of not polluting namespaces by default.
candidate 4 (found by 1 of 42 passes): When using a quantities library, it is desirable to have overloads that: Accept `quantity<isq::angular_measure, R>` for any angular unit `R`, performing automatic conversion to radians before calling the underlying `std::sin`.

## coordination - grade 1.17 (fired in 2 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 1/1/1  -> 1.00
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 2/0/2  -> 1.33
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): A function returning `quantity<si::speed_of_light_in_vacuum * si::second>` has a type that is only compatible with other code that names the same constant.
candidate 2 (found by 2 of 42 passes): provides bidirectional interoperability between SI time quantities and the `std::chrono` duration and time point types.
candidate 3 (found by 1 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.

## insufficiency - grade 0.33 (fired in 1 of 14 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 The International System of Quantities ... 0/0/0  -> 0.00
  [4] 3 Core SI Definitions ( <sicore> )           0/0/0  -> 0.00
  [5] 4 Optional: Non-SI Units Accepted for Use... 0/0/0  -> 0.00
  [6] 5 Optional: SI-Defining Constants ( <sico... 0/1/1  -> 0.67
  [7] 6 Optional: Unit Symbols ( <siunitsymbols> ) 0/0/0  -> 0.00
  [8] 7 Optional: std::chrono Interoperability ... 0/0/0  -> 0.00
  [9] 8 Optional: Mathematical Functions for SI... 0/0/0  -> 0.00
  [10] 9 Optional: Prefix Utilities ( <siprefixu... 0/0/0  -> 0.00
  [11] 10 Summary                                   0/0/0  -> 0.00
  [12] 11 Consolidated Straw Polls                  0/0/0  -> 0.00
  [13] 12 Acknowledgements                          0/0/0  -> 0.00
  [14] 13 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 42 passes): Standardizing these definitions therefore matters for library interoperability, not only for scientific computing.

## implementation - grade 1.00  [binary: max] (fired in 2 of 14 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
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
candidate 1 (found by 2 of 42 passes): All synopses in this paper are derived from the open-source mp-units library, adapted to use `std::` namespaces.
candidate 2 (found by 2 of 42 passes): constants that proved useful in practice.
candidate 3 (found by 1 of 42 passes): All synopses in this paper are derived from the open-source [mp-units](https://github.com/mpusz/mp-units) library, adapted to use `std::` namespaces.
candidate 4 (found by 1 of 42 passes): The three additional constants listed above are a small, arbitrary selection drawn from the [mp-units](https://github.com/mpusz/mp-units) library — constants that proved useful in practice.

-->
