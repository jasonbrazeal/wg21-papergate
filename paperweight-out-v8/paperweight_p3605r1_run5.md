Verdict: Adequate (4/14)

The paper offers only a preliminary sketch of motivation and precedent, but it does not substantiate most of the claims that would justify standardization. The thinnest areas are the absence of any implementation experience and the failure to explain why a library solution would be inadequate.

- The strongest support is the reference to existing integer square root facilities in other languages and an ISO standard, though even this is asserted rather than analyzed.
- The paper gestures at a broad user base and common algorithmic applications, but provides no evidence connecting those needs to a defect in the current C++ standard library.
- The discussion of header selection and WG14 coordination is speculative and does not establish an actual interoperability problem or a shared direction.
- The paper offers no implementation experience and no argument for why a library cannot already serve the need, leaving the core standardization rationale unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 5 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 4.33   accumulate 4.50   max 6.33

## SUMMARY
grades: motivation 1.33  audience 0.17  prior_art 1.00  vehicle 1.00  coordination 0.50  insufficiency 0.00  implementation 0.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 4.00 / 3.50 / 5.00   (all 3 samples: 4.00)
headings: h2 10
on threshold: motivation, vehicle
splits: motivation[3] 0/0/1  motivation[6] 0/1/1  audience[4] 0/0/1  prior_art[6] 0/0/2
        coordination[6] 2/0/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/1  -> 0.33
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     0/1/1  -> 0.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): There are numerous popular questions about integer square root in C++ on StackOverflow.
candidate 2 (found by 2 of 33 passes): Mathematically, the integer square root function is defined for only non-negative integers.
candidate 3 (found by 1 of 33 passes): This paper proposes to add an `isqrt` function (template) to calculate the integer square root of a nonnegative integer.
candidate 4 (found by 1 of 33 passes): For example, it is commonly applied in: **Primality test** and **Integer factorization** algorithms, such as **Trial division** and **Fermat's** method; **Cryptography** algorithms, such as block entanglement (non-linear transformation); **Sqrt-decomposition** method; and **Block Merge Sort** algorithm.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)
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
candidate 1 (found by 1 of 33 passes): There are numerous popular questions about integer square root in **C++** on **StackOverflow.**

## prior_art - grade 1.00 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 2.3. Prior Art                               1/1/1  -> 1.00
  [6] 3. Design Considerations                     0/0/2  -> 0.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The integer square root[[1](https://dl.acm.org/doi/10.5555/2462741)] is a useful number-theoretic primitive.
candidate 2 (found by 2 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method[[10](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigInteger.html#sqrt())]; In **Python,** the `math` module has the `isqrt()` function[[11](https://docs.python.org/3/library/math.html#math.isqrt)];
candidate 3 (found by 1 of 33 passes): Several programming languages have a function (or class method) for calculating the integer square root:
candidate 4 (found by 1 of 33 passes): The **ISO/IEC 10967-2:2001** standard defines an integer square root function named `isqrt`, and we follow this standard's guidance.

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
candidate 1 (found by 2 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows **WG14** to select possibly a different header and naming convention.
candidate 2 (found by 1 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows WG14 to select possibly a different header and naming convention.

## coordination - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     2/0/1  -> 1.00
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows **WG14** to select possibly a different header and naming convention.
candidate 2 (found by 1 of 33 passes): The only guaranteed way to evade a potential compatibility issue is to avoid using existing C headers, such as <cmath> corresponding to <math.h> and others.

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
