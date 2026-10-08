Verdict: Adequate to Strong (7/14)

The paper offers a narrow but real foundation for its case, centered on the arbitrariness of the current restriction and the existence of prior work and a shipping library context. Its support is thinnest where the argument moves from “this is a problem” to “this needs a standard change now”: the affected audience, coordination with related features, and implementation experience are largely asserted rather than shown.

- The strongest support is the identification of a specific, standard-mandated restriction that cannot be worked around in ordinary library code.
- The paper also establishes that the issue has been raised before and that `std::execution` gives the question renewed practical relevance.
- The case for why a library solution is insufficient is asserted mainly through a claim about what regular C++ can and cannot check, without demonstrating that the available workarounds are inadequate in practice.
- The most glaring omission is the absence of any established affected audience or coordination picture, leaving the actual need for standardization largely unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.17   max 9.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.17  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.00 / 7.50   (all 3 samples: 7.00)
headings: h2 9
on threshold: vehicle, insufficiency
splits: motivation[3] 2/1/2  motivation[5] 1/2/2  vehicle[5] 0/0/1
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 10 sections, strong in 3)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/1/2  -> 1.67
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   1/2/2  -> 1.67
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): *“If searches for the names* `return_void` *and* `return_value` *in the scope of the promise type* *each find any declarations, the program is ill-formed.”*
candidate 2 (found by 3 of 30 passes): Disallowing `return_void` alongside `return_value` is fundamentally arbitrary, unnecessarily making `void` a special case.
candidate 3 (found by 2 of 30 passes): Trying to accept `std::execution::set_value_t()` (i.e. successful completion with no values) alongside any other `std::execution::set_value_t(...)` form, on the other hand, does not work.
candidate 4 (found by 1 of 30 passes): Trying to accept `std::execution::set_value_t()` (i.e. successful completion with no values) alongside any other `std::execution::set_value_t(...)` form, on the other hand, does not work. Not for any conceptual reason, but simply because the standard bans it by fiat.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): There has previously been a paper by a different author with the same goal as this paper [4]. It had no consensus in Cologne in 2019, however the author of this paper feels there is new information [5][6].
candidate 2 (found by 3 of 30 passes): `std::execution`, which will ship in C++26, provides “the [library] implementation of an `async-function`” ([8] at §6).
candidate 3 (found by 3 of 30 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).

## vehicle - grade 1.17 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/1  -> 0.33
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This restriction can only be implemented by the compiler. Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.
candidate 2 (found by 1 of 30 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.

## implementation - grade 1.00  [binary: max] (fired in 1 of 10 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The above works. The author has implemented it.

-->
