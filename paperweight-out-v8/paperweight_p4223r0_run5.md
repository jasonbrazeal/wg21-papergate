Verdict: Adequate (7/14)

The paper makes a reasonably persuasive case that type-erased senders address a real gap in separately compiled asynchronous interfaces, and it grounds that argument in concrete limitations of the status quo and a comparison of design alternatives. The support is thinnest where the paper needs to show that this belongs in the standard rather than in a library, and it offers almost nothing on who is affected or whether the design has been tried in practice.

- The strongest support is the explanation of why existing sender types cannot serve as return types for separately compiled functions, including virtual member functions.
- The paper also establishes that prior art and alternatives exist, and that a function-style type-erasing sender is preferable to construction-time allocation approaches.
- The case for standardization itself is asserted rather than demonstrated, since the paper does not show why a library implementation would be insufficient.
- The most glaring omission is the absence of any implementation experience or evidence about the affected user population.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 12. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.00   accumulate 7.00   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.83  coordination 1.33  insufficiency 0.67  implementation 0.00
sample agreement: 77 of 84 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.50 / 6.50 / 7.00   (all 3 samples: 6.50)
headings: h2 11
on threshold: prior_art, coordination
splits: motivation[5] 1/2/2  motivation[8] 1/2/2  prior_art[7] 1/1/2  vehicle[2] 1/1/0
        vehicle[6] 0/0/1  coordination[2] 2/2/1  insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 12 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Requirements                                 1/2/2  -> 1.67
  [6] Designs Considered                           2/2/2  -> 2.00
  [7] Conclusion                                   1/1/1  -> 1.00
  [8] Interface Discussion                         1/2/2  -> 1.67
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): These characteristics make the majority of standard senders unusable as the return values of separately-compiled functions, preventing their use on interface boundaries.
candidate 2 (found by 3 of 36 passes): The problem with the existing senders is that their types reflect the fully composed computation they represent so it is impossible to achieve this separation with the status quo.
candidate 3 (found by 3 of 36 passes): The need for dynamic allocation of a type-erased operation state is thus a direct consequence of the abstract machine forcing us to use dynamic storage for asynchronous activation frames.
candidate 4 (found by 3 of 36 passes): The abovementioned trade-offs suggest that, of the two designs considered, function is a better match for a broadly-applicable, ergonomic, type-erasing sender for use in asynchronous interface declarations.

## audience - grade 0.00 (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Requirements                                 0/0/0  -> 0.00
  [6] Designs Considered                           0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Interface Discussion                         0/0/0  -> 0.00
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 4 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Requirements                                 1/1/1  -> 1.00
  [6] Designs Considered                           2/2/2  -> 2.00
  [7] Conclusion                                   1/1/2  -> 1.33
  [8] Interface Discussion                         1/1/1  -> 1.00
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The problem with the existing senders is that their types reflect the fully composed computation they represent so it is impossible to achieve this separation with the status quo.
candidate 2 (found by 3 of 36 passes): As Vinnie Falco et al. explore in P4003R2, P4172R0, and P4127R0, construction-time allocation is difficult to customize with an ergonomic interface.
candidate 3 (found by 3 of 36 passes): the existing <ins>completion_signatures</ins> class template will serve.
candidate 4 (found by 2 of 36 passes): The abovementioned trade-offs suggest that, of the two designs considered, <ins>function</ins> is a better match for a broadly-applicable, ergonomic, type-erasing sender for use in asynchronous interface declarations.

## vehicle - grade 0.83 (fired in 3 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] Requirements                                 0/0/0  -> 0.00
  [6] Designs Considered                           0/0/1  -> 0.33
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Interface Discussion                         0/0/0  -> 0.00
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): The standard library ought to fill this gap by providing a sender that can serve as the return type of a function with separate declaration and definition, including virtual member functions.
candidate 2 (found by 2 of 36 passes): These characteristics make the majority of standard senders unusable as the return values of separately-compiled functions, preventing their use on interface boundaries.
candidate 3 (found by 1 of 36 passes): The need for dynamic allocation of a type-erased operation state is thus a direct consequence of the abstract machine forcing us to use dynamic storage for asynchronous activation frames.

## coordination - grade 1.33 (fired in 2 of 12 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/1  -> 1.67
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   1/1/1  -> 1.00
  [5] Requirements                                 0/0/0  -> 0.00
  [6] Designs Considered                           0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Interface Discussion                         0/0/0  -> 0.00
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): These characteristics make the majority of standard senders unusable as the return values of separately-compiled functions, preventing their use on interface boundaries.
candidate 2 (found by 3 of 36 passes): The standard library ought to fill this gap by providing a sender that can serve as the return type of a function with separate declaration and definition, including virtual member functions.

## insufficiency - grade 0.67 (fired in 2 of 12 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Requirements                                 0/0/1  -> 0.33
  [6] Designs Considered                           0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Interface Discussion                         0/0/0  -> 0.00
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 36 passes): These characteristics make the majority of standard senders unusable as the return values of separately-compiled functions, preventing their use on interface boundaries.
candidate 2 (found by 1 of 36 passes): The problem with the existing senders is that their types reflect the fully composed computation they represent so it is impossible to achieve this separation with the status quo.

## implementation - grade 0.00  [binary: max] (fired in 0 of 12 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] Background                                   0/0/0  -> 0.00
  [5] Requirements                                 0/0/0  -> 0.00
  [6] Designs Considered                           0/0/0  -> 0.00
  [7] Conclusion                                   0/0/0  -> 0.00
  [8] Interface Discussion                         0/0/0  -> 0.00
  [9] Summary                                      0/0/0  -> 0.00
  [10] Proposed                                     0/0/0  -> 0.00
  [11] Acknowledgements                             0/0/0  -> 0.00
  [12] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
