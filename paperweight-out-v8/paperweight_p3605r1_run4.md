Verdict: Adequate (4/14)

The paper gestures toward a real problem and points to relevant prior art, but it does not yet make a persuasive case that this belongs in the C++ standard. Most of its support is asserted rather than demonstrated, and the thinnest parts concern why a library solution is insufficient and whether anyone has actually implemented the proposed facility.

- The strongest support is the citation of existing `isqrt` facilities in other languages and in ISO/IEC 10967-2, which at least shows the function is a recognized primitive elsewhere.
- The paper claims broad relevance through StackOverflow questions and mathematical use, but it does not show who specifically needs this in standard C++ or how widespread the pain is.
- The discussion of header choice and WG14 coordination hints at interoperability concerns, but it does not establish an actual coordination problem or a concrete plan.
- The paper offers no implementation experience and no argument for why a library cannot meet the need, leaving the central standardization question largely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 5 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.67   accumulate 5.17   max 6.67

## SUMMARY
grades: motivation 1.17  audience 0.33  prior_art 1.17  vehicle 1.00  coordination 0.67  insufficiency 0.00  implementation 0.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 5.50 / 5.00   (all 3 samples: 4.33)
headings: h2 10
on threshold: vehicle
splits: motivation[3] 1/1/0  motivation[4] 0/2/2  audience[4] 0/1/1  prior_art[6] 0/2/2
        coordination[6] 1/2/1
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  1/1/0  -> 0.67
  [4] 2. Motivation                                0/2/2  -> 1.33
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     1/1/1  -> 1.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Mathematically, the integer square root function is defined for only non-negative integers.
candidate 2 (found by 2 of 33 passes): This paper proposes to add an `isqrt` function (template) to calculate the integer square root of a nonnegative integer.
candidate 3 (found by 1 of 33 passes): For “large” numbers, these two expressions could give different results, even when the value of `n` is exactly representable in the floating-point type used for `sqrt` calculation.
candidate 4 (found by 1 of 33 passes): There are numerous popular questions about integer square root in C++ on StackOverflow.

## audience - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/1/1  -> 0.67
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     0/0/0  -> 0.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): There are numerous popular questions about integer square root in **C++** on **StackOverflow.**

## prior_art - grade 1.17 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 2.3. Prior Art                               1/1/1  -> 1.00
  [6] 3. Design Considerations                     0/2/2  -> 1.33
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The integer square root[[1](https://dl.acm.org/doi/10.5555/2462741)] is a useful number-theoretic primitive.
candidate 2 (found by 2 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method; In **Python,** the `math` module has the `isqrt()` function; In **Ruby,** the `Integer` class has the `sqrt()` method; and In **Rust,** primitive integer types have the `isqrt()` method.
candidate 3 (found by 2 of 33 passes): The **ISO/IEC 10967-2:2001** standard defines an integer square root function named `isqrt`, and we follow this standard's guidance.
candidate 4 (found by 1 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method[[10](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigInteger.html#sqrt())]; In **Python,** the `math` module has the `isqrt()` function[[11](https://docs.python.org/3/library/math.html#math.isqrt)];

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
candidate 1 (found by 3 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows **WG14** to select possibly a different header and naming convention.

## coordination - grade 0.67 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     1/2/1  -> 1.33
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): The only guaranteed way to evade a potential compatibility issue is to avoid using existing C headers, such as <cmath> corresponding to <math.h> and others.
candidate 2 (found by 1 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows WG14 to select possibly a different header and naming convention.

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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
