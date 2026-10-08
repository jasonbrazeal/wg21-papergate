Verdict: Weak to Adequate (4/14)

The paper offers only a thin, largely asserted case for standardization: most of its supporting material is mentioned rather than developed, and the central questions of implementation experience and why a library would not suffice are left entirely unaddressed. The strongest material concerns prior art and interoperability, but even those points are stated as claims rather than demonstrated with concrete analysis.

- The paper’s most substantive support is its citation of existing `isqrt` functionality in Java, Python, Ruby, Rust, and ISO/IEC 10967-2, though it does not explore how these examples inform the C++ design.
- The discussion of header placement and WG14 coordination at least gestures toward a standardization-specific rationale, but it remains a compatibility consideration rather than an established need.
- The paper repeatedly invokes StackOverflow popularity as evidence of user demand, yet never quantifies or characterizes that demand beyond the bare assertion.
- The most glaring omission is the absence of any implementation experience or argument for why a standard library facility is necessary when a user-side library could provide the same functionality.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 5 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 4.33   accumulate 4.83   max 6.67

## SUMMARY
grades: motivation 1.33  audience 0.17  prior_art 1.17  vehicle 0.83  coordination 0.67  insufficiency 0.00  implementation 0.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.00 / 3.00 / 5.00   (all 3 samples: 4.17)
headings: h2 10
on threshold: motivation, vehicle
splits: motivation[3] 0/0/1  motivation[6] 1/0/1  audience[4] 0/0/1  prior_art[6] 2/0/2
        vehicle[6] 2/2/1  coordination[6] 2/0/2
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/1  -> 0.33
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     1/0/1  -> 0.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): There are numerous popular questions about integer square root in **C++** on **StackOverflow.**
candidate 2 (found by 2 of 33 passes): Mathematically, the integer square root function is defined for only non-negative integers.
candidate 3 (found by 1 of 33 passes): This paper proposes to add an `isqrt` function (template) to calculate the integer square root of a nonnegative integer.
candidate 4 (found by 1 of 33 passes): There are numerous popular questions about integer square root in C++ on StackOverflow.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 1 of 33 passes): There are numerous popular questions about integer square root in C++ on StackOverflow.

## prior_art - grade 1.17 (fired in 3 of 11 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 2.3. Prior Art                               1/1/1  -> 1.00
  [6] 3. Design Considerations                     2/0/2  -> 1.33
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): The integer square root[[1](https://dl.acm.org/doi/10.5555/2462741)] is a useful number-theoretic primitive.
candidate 2 (found by 2 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method[[10](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/math/BigInteger.html#sqrt())]; In **Python,** the `math` module has the `isqrt()` function[[11](https://docs.python.org/3/library/math.html#math.isqrt)];
candidate 3 (found by 2 of 33 passes): The **ISO/IEC 10967-2:2001** standard defines an integer square root function named `isqrt`, and we follow this standard's guidance.
candidate 4 (found by 1 of 33 passes): In **Java,** the `BigInteger` class has the `sqrt()` method; In **Python,** the `math` module has the `isqrt()` function; In **Ruby,** the `Integer` class has the `sqrt()` method; and In **Rust,** primitive integer types have the `isqrt()` method.

## vehicle - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     2/2/1  -> 1.67
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): Additionally, selecting this header avoids potential compatibility issue, as it allows **WG14** to select possibly a different header and naming convention.

## coordination - grade 0.67 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 0. Revision history                          0/0/0  -> 0.00
  [3] 1. Abstract                                  0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 2.3. Prior Art                               0/0/0  -> 0.00
  [6] 3. Design Considerations                     2/0/2  -> 1.33
  [7] 4. Implementation Experience                 0/0/0  -> 0.00
  [8] 5. Proposed Wording                          0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
  [11] Prior Art:                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Thus, a decision to place the `isqrt` function into one of the **C** headers will force **WG14** to use specific prefixes/suffixes for this function, and possibly even the data types for which it is defined.
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
