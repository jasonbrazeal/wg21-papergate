Verdict: Adequate (5/14)

The paper gives a partial account of why integer square root deserves standardization, with its strongest material concentrated in motivation and existing practice, but it leaves several essential parts of the case essentially unargued. The thinnest areas are the absence of any identified audience, the lack of implementation experience, and the failure to explain why a library solution would not suffice.

- The paper establishes that integer square root is a well-known primitive with precedent in other languages and standards.
- The discussion of header choice gestures at WG14 coordination but does not actually demonstrate an interoperability plan.
- The paper does not identify who would be affected by adding this facility to the C++ standard.
- The most glaring omission is the absence of any argument for why an ordinary library implementation would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 4.00   accumulate 5.33   max 7.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 1.00  coordination 0.83  insufficiency 0.00  implementation 0.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 4.50 / 5.00 / 5.00   (all 3 samples: 4.83)
headings: h2 10
on threshold: motivation, prior_art, vehicle, coordination
splits: coordination[6] 1/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     1/1/1  -> 1.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Mathematically, the integer square root function is defined for only non-negative integers.
candidate 2 (found by 2 of 33 passes): There are numerous popular questions about integer square root in C++ on StackOverflow.
candidate 3 (found by 1 of 33 passes): There are numerous popular questions about integer square root in **C++** on **StackOverflow.**

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## prior_art - grade 1.50 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 2.3. Prior Art                               1/1/1  -> 1.00
  [6] 3. Design Considerations                     2/2/2  -> 2.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The integer square root[[1](https://dl.acm.org/doi/10.5555/2462741)] is a useful number-theoretic primitive.
candidate 2 (found by 3 of 33 passes): The **ISO/IEC 10967-2:2001** standard defines an integer square root function named `isqrt`, and we follow this standard's guidance.
candidate 3 (found by 2 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method[[10](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigInteger.html#sqrt())]; In **Python,** the `math` module has the `isqrt()` function[[11](https://docs.python.org/3/library/math.html#math.isqrt)];
candidate 4 (found by 1 of 33 passes): Several programming languages have a function (or class method) for calculating the integer square root:

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## coordination - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     1/2/2  -> 1.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows WG14 to select possibly a different header and naming convention.
candidate 2 (found by 1 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows **WG14** to select possibly a different header and naming convention.

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
