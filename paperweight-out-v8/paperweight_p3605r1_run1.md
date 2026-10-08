Verdict: Adequate (5/14)

The paper gives a partial account of why integer square root deserves standardization, but much of its case rests on assertions rather than demonstrated need. The strongest material concerns the mathematical definition and the awkwardness of forcing signed callers to cast, while the thinnest support appears in implementation experience and the argument that a library solution is insufficient.

- The paper clearly establishes that integer square root is mathematically defined only for nonnegative integers and that excluding signed types would impose avoidable casts on callers who know their values are nonnegative.
- The discussion of prior art in Java, Python, Ruby, Rust, and ISO/IEC 10967-2 is suggestive but does not by itself show why C++ specifically needs a standardized version.
- The claim that the problem cannot be solved by a wider floating-point type is asserted without enough surrounding argument to establish why existing library approaches fall short.
- The paper offers no implementation experience, leaving the practical viability and design consequences of the proposed facility unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 6 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 5.00   accumulate 5.00   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.00  vehicle 1.00  coordination 0.33  insufficiency 0.17  implementation 0.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 4.50 / 4.50   (all 3 samples: 4.50)
headings: h2 10
on threshold: motivation, vehicle
splits: motivation[3] 0/1/0  prior_art[6] 0/2/0  coordination[6] 2/0/0  insufficiency[4] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/1/0  -> 0.33
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     1/1/1  -> 1.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): There are numerous popular questions about integer square root in C++ on StackOverflow.
candidate 2 (found by 2 of 33 passes): However, if the function template could not be instantiated for `signed` integers, it would be necessary to cast the argument to an `unsigned` type, even where it is known (e.g., by construction) that the `signed` integer is non-negative.
candidate 3 (found by 1 of 33 passes): This paper proposes to add an `isqrt` function (template) to calculate the integer square root of a nonnegative integer.
candidate 4 (found by 1 of 33 passes): Mathematically, the integer square root function is defined for only non-negative integers.

## audience - grade 0.50 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     0/0/0  -> 0.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): There are numerous popular questions about integer square root in **C++** on **StackOverflow.**

## prior_art - grade 1.00 (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 2.3. Prior Art                               1/1/1  -> 1.00
  [6] 3. Design Considerations                     0/2/0  -> 0.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The integer square root[[1](https://dl.acm.org/doi/10.5555/2462741)] is a useful number-theoretic primitive.
candidate 2 (found by 2 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method; In **Python,** the `math` module has the `isqrt()` function; In **Ruby,** the `Integer` class has the `sqrt()` method; and In **Rust,** primitive integer types have the `isqrt()` method.
candidate 3 (found by 1 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method[[10](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigInteger.html#sqrt())]; In **Python,** the `math` module has the `isqrt()` function[[11](https://docs.python.org/3/library/math.html#math.isqrt)];
candidate 4 (found by 1 of 33 passes): The **ISO/IEC 10967-2:2001** standard defines an integer square root function named `isqrt`, and we follow this standard's guidance.

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     2/2/2  -> 2.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows WG14 to select possibly a different header and naming convention.
candidate 2 (found by 1 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows **WG14** to select possibly a different header and naming convention.

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     2/0/0  -> 0.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): The **ISO/IEC 10967-2:2001** standard defines an integer square root function named `isqrt`, and we follow this standard's guidance.

## insufficiency - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/1  -> 0.33
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     0/0/0  -> 0.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Therefore, the problem cannot be solved simply by using a wider floating-point type.

## implementation - grade 0.00  [binary: max] (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     0/0/0  -> 0.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidates: (none validated)

-->
