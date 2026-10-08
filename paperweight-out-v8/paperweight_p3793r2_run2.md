Verdict: Adequate (6/14)

The paper offers solid support for the motivation behind the proposed shift functions and for the existence of prior art and implementation experience, but it leaves several essential parts of the standardization case unaddressed. The thinnest areas are the lack of any identified affected audience, the absence of a rationale for why a standard facility is needed rather than a library, and the missing discussion of coordination or interoperability.

- The paper most clearly establishes why the current shift behavior is problematic and why a standardized alternative would be valuable.
- It also demonstrates prior art and implementation experience through references to existing practice, compiler behavior, and benchmark or reference code.
- The paper does not establish who is affected by the current behavior or who would benefit from the proposed facility.
- Most glaringly, it never explains why a library solution would not suffice or why this needs to be part of the C++ standard itself.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 3 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.00   accumulate 6.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 62 of 63 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.00 / 6.00 / 5.50   (all 3 samples: 5.67)
headings: h2 8
on threshold: prior_art
splits: prior_art[6] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation — Why are overlong shifts... 2/2/2  -> 2.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Possible implementation                   0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): They always produce a mathematically correct result when possible.
candidate 2 (found by 3 of 27 passes): The precedence of these operators is less than the precedence of the additive operators, which is counterintuitive because shift operations behave as multiplication and division by a power of 2.
candidate 3 (found by 3 of 27 passes): We believe that the "wrapping" behavior (most famously exhibited by the x86 family of processors) in which the shift amount is reduced modulo the bit width of the other operand is not useful, other than when implementing bit rotations.
candidate 4 (found by 2 of 27 passes): We consider the undefined behavior of overlong shifts to be gratuitous.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation — Why are overlong shifts... 0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Possible implementation                   0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation — Why are overlong shifts... 1/1/1  -> 1.00
  [6] 4. Design considerations                     2/2/0  -> 1.33
  [7] 5. Possible implementation                   1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Reflector discussion revealed that GCC relies on the second property when vectorizing multiple shift operations on adjacent memory locations, and changing it might therefore not be "free".
candidate 2 (found by 3 of 27 passes): This behavior is inherited from C, in which the arithmetic operators were originally designed to do whatever the corresponding hardware instructions would do; processor families differ as to how overlong shifts are handled.
candidate 3 (found by 3 of 27 passes): See also [[Cxx26BitPermutations]](https://github%2ecom/Eisenwave/cxx26-bit-permutations) for a reference implementation and test code.
candidate 4 (found by 2 of 27 passes): We follow the design of `std::rotl` and `std::rotr` in proposing that the shift functions do not perform integer promotion.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation — Why are overlong shifts... 0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Possible implementation                   0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation — Why are overlong shifts... 0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Possible implementation                   0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation — Why are overlong shifts... 0/0/0  -> 0.00
  [6] 4. Design considerations                     0/0/0  -> 0.00
  [7] 5. Possible implementation                   0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation — Why are overlong shifts... 0/0/0  -> 0.00
  [6] 4. Design considerations                     2/2/2  -> 2.00
  [7] 5. Possible implementation                   2/2/2  -> 2.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): See also [[Cxx26BitPermutations]](https://github%2ecom/Eisenwave/cxx26-bit-permutations) for a reference implementation and test code.
candidate 2 (found by 2 of 27 passes): To make an educated choice about which behavior would be appropriate for negative shifts in `std::shl`, find a comparison of the following functions below ([[QuickBench]](https://quick-bench%2ecom/q/HcAUoOoGFHnm5nx1G_rJs52oLaY), [[CompilerExplorer]](https://godbolt%2eorg/z/1Won5qjo9)):
candidate 3 (found by 1 of 27 passes): find a comparison of the following functions below ([[QuickBench]](https://quick-bench%2ecom/q/HcAUoOoGFHnm5nx1G_rJs52oLaY), [[CompilerExplorer]](https://godbolt%2eorg/z/1Won5qjo9))

-->
