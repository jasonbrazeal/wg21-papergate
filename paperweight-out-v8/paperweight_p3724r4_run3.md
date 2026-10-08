Verdict: Strong (8/14)

The paper gives a workable account of why integer division with selectable rounding is a recurring problem and shows that a reference implementation exists, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why this belongs in the standard library rather than in a standalone library, and the paper does not address coordination or interoperability at all.

- The strongest support is the combination of prior standardization history, cited examples of widespread user error, and a public reference implementation.
- The paper establishes that the functionality is simple to implement and that users have repeatedly attempted it themselves, often incorrectly.
- The argument for standardization over a library is mostly an appeal to the same examples of user error, without showing why a library solution would be insufficient.
- The most glaring omission is the complete absence of any discussion of coordination with existing or planned standard library facilities, or of interoperability concerns.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 6 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.33   accumulate 8.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 1.00  implementation 2.00
sample agreement: 86 of 91 section-criterion pairs unanimous (95%)
single-sample totals would have been: 9.00 / 8.00 / 8.00   (all 3 samples: 8.33)
headings: h2 12
on threshold: insufficiency
splits: motivation[7] 1/1/0  audience[4] 2/0/1  audience[5] 2/1/1  prior_art[13] 0/1/0
        vehicle[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 1/1/0  -> 0.67
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): C++ currently only offers truncating integer division in the form of the `/` operator.
candidate 2 (found by 3 of 39 passes): There is an *ocean* of examples where C and C++ users have gotten this wrong.
candidate 3 (found by 2 of 39 passes): As a rule of thumb, the proposed functionality should be a drop-in replacement for the various bad implementations that users have written themselves (§3.1. Is this not trivial for the user to do?)
candidate 4 (found by 2 of 39 passes): Consequently, the implementation effort for all of these functions is close to zero.

## audience - grade 1.17 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/0/1  -> 1.00
  [5] 3. Motivation                                2/1/1  -> 1.33
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): There is an *ocean* of examples where C and C++ users have gotten this wrong.
candidate 2 (found by 1 of 39 passes): Such a feature was previously part of [[P0105R1]](https://wg21%2elink/p0105r1) and the Numerics TS [[P1889R1]](https://wg21%2elink/p1889r1), but was eventually abandoned by the author.
candidate 3 (found by 1 of 39 passes): However, other rounding modes have various use cases too, and implementing these as the user can be surprisingly hard, especially when integer overflow needs to be avoided, and negative inputs are accepted.
candidate 4 (found by 1 of 39 passes): At the time of writing, the *first* Google search result for "c++ ceiling integer division" yields [[StackOverflowCeil]](https://stackoverflow%2ecom/q/2745074/5740428).

## prior_art - grade 2.00 (fired in 5 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design                                    2/2/2  -> 2.00
  [7] 5. Implementation experience                 1/1/1  -> 1.00
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      0/1/0  -> 0.33
candidate 1 (found by 3 of 39 passes): Such a feature was previously part of [[P0105R1]](https://wg21%2elink/p0105r1) and the Numerics TS [[P1889R1]](https://wg21%2elink/p1889r1), but was eventually abandoned by the author.
candidate 2 (found by 3 of 39 passes): There is an *ocean* of examples where C and C++ users have gotten this wrong. A few droplets are listed below.
candidate 3 (found by 3 of 39 passes): The design somewhat leans on [[P0105R1]](https://wg21%2elink/p0105r1) (which first proposed division functions with custom rounding), but heavily deviates from it.
candidate 4 (found by 3 of 39 passes): A reference implementation can be found on [[GitHub]](https://github%2ecom/Eisenwave/integer-division).

## vehicle - grade 0.17 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/1/0  -> 0.33
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): The user can trivially make such an `enum class` and `switch` themselves, if they actually need to.

## coordination - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 1 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                2/2/2  -> 2.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 0/0/0  -> 0.00
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): There is an *ocean* of examples where C and C++ users have gotten this wrong.

## implementation - grade 2.00  [binary: max] (fired in 2 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision history                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Motivation                                0/0/0  -> 0.00
  [6] 4. Design                                    0/0/0  -> 0.00
  [7] 5. Implementation experience                 2/2/2  -> 2.00
  [8] 6. Try it yourself                           0/0/0  -> 0.00
  [9] 7. Wording                                   0/0/0  -> 0.00
  [10] Integer division [numeric.int.div]           0/0/0  -> 0.00
  [11] 8. Acknowledgements                          0/0/0  -> 0.00
  [12] 9. References                                0/0/0  -> 0.00
  [13] Appendix A — Reference implementation      2/2/2  -> 2.00
candidate 1 (found by 3 of 39 passes): A reference implementation can be found on [[GitHub]](https://github%2ecom/Eisenwave/integer-division).
candidate 2 (found by 3 of 39 passes): See [[GitHub]](https://github%2ecom/Eisenwave/integer-division) for the full implementation.

-->
