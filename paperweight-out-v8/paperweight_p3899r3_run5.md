Verdict: Adequate to Strong (8/14)

The paper offers solid support in a few important areas, particularly in showing implementation experience and in arguing that the current divergence between core language and library behavior is undesirable. However, the case is much thinner when it comes to explaining why a standard change is necessary rather than a compiler or library fix, and it does not establish who would actually be affected by the change.

- The strongest support is the concrete implementation experience, with GCC 15 already matching the proposed behavior and the paper clearly identifying that behavior as the target.
- The paper also establishes that the current specification is unclear and that there is little reason for the core language and library to diverge on floating-point overflow.
- The weakest part is the absence of any established argument for why the standard itself must change, as opposed to leaving the behavior to implementations or addressing it through library specifications.
- The paper also fails to establish who is affected, offering only a claimed method for identifying affected code rather than evidence of real-world impact.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.67   accumulate 7.50   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.50 / 7.00 / 7.00   (all 3 samples: 7.50)
headings: h2 8
on threshold: coordination, implementation
splits: motivation[6] 0/1/1  audience[4] 2/0/0  audience[7] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/1/1  -> 0.67
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 6 of 27 passes): The current specification of floating-point overflow is unclear.
candidate 2 (found by 2 of 27 passes): There is little motivation to have the core language and the library diverge in this area. At best, a user's compile-time floating-point computations would overflow and turn into infinity, but is that a useful outcome for constant evaluation? Likely not.
candidate 3 (found by 2 of 27 passes): Existing code that relied on `max() * 2` being a constant expression will fail to compile.
candidate 4 (found by 1 of 27 passes): There is little motivation to have the core language and the library diverge in this area.

## audience - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/0/0  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/0/0  -> 0.33
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): By comparing which initializations of the form `constexpr float f = *expression*;` result in a compiler error, we can identify which expressions implementations believe to be constant.
candidate 2 (found by 1 of 27 passes): GCC 15 implements the proposed behavior exactly.

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): It also seemingly contradicts the design rationale in the note attached to [[expr.pre] paragraph 4](https://eel.is/c++draft/expr.pre#4).
candidate 2 (found by 3 of 27 passes): GCC 15 implements the proposed behavior exactly. Clang and MSVC compilers deviate only slightly.
candidate 3 (found by 2 of 27 passes): This approach is consistent with the design of mathematical functions; for example, `exp(1'000'000)` results in a range error, meaning that infinity is returned and the expression is not constant.
candidate 4 (found by 1 of 27 passes): In short, the GCC 15 behavior is proposed. As can be seen in §2.3. Implementation divergence, GCC 15 considers an expression to be constant if and only if no floating-point exception is raised

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): By comparing which initializations of the form `constexpr float f = *expression*;` result in a compiler error, we can identify which expressions implementations believe to be constant.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    1/1/1  -> 1.00
  [6] 4. Impact on existing code                   0/0/0  -> 0.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Wording                                   0/0/0  -> 0.00
  [9] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The results can be seen in the table below.
candidate 2 (found by 2 of 27 passes): In short, the GCC 15 behavior is proposed.
candidate 3 (found by 2 of 27 passes): GCC 15 implements the proposed behavior exactly.
candidate 4 (found by 1 of 27 passes): As can be seen in §2.3. Implementation divergence, GCC 15 considers an expression to be constant if and only if no floating-point exception is raised

-->
