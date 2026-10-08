Verdict: Adequate to Strong (7/14)

The paper gives a solid account of why the current coroutine restriction is arbitrary and how it conflicts with the direction of `std::execution`, but it leaves several essential parts of the standardization case asserted rather than demonstrated. The strongest material concerns motivation and prior art, while the thinnest areas are the absence of any identified user population and the lack of substantiated evidence for implementation experience or interoperability.

- The paper clearly establishes that the existing prohibition on combining `return_void` and `return_value` is an arbitrary special case that creates real friction with C++26 `std::execution`.
- It also establishes that a previous attempt with the same goal failed for lack of consensus, and that library-level workarounds are awkward enough to motivate a language change.
- The claim that only the compiler can implement the restriction is plausible but not backed by enough explanation to count as established.
- The paper offers no evidence about who is affected by the restriction, leaving the practical urgency of the proposal largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.00   accumulate 7.67   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.83  coordination 1.00  insufficiency 1.00  implementation 1.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.50 / 7.00 / 8.00   (all 3 samples: 7.33)
headings: h2 9
on threshold: prior_art, vehicle, coordination, insufficiency
splits: prior_art[4] 0/0/2  vehicle[4] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 30 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): “If searches for the names return_void and return_value in the scope of the promise type each find any declarations, the program is ill-formed.”
candidate 2 (found by 3 of 30 passes): Trying to accept `std::execution::set_value_t()` (i.e. successful completion with no values) alongside any other `std::execution::set_value_t(...)` form, on the other hand, does not work.
candidate 3 (found by 3 of 30 passes): Disallowing `return_void` alongside `return_value` is fundamentally arbitrary, unnecessarily making `void` a special case.

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

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   0/0/2  -> 0.67
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): There has previously been a paper by a different author with the same goal as this paper [4]. It had no consensus in Cologne in 2019, however the author of this paper feels there is new information [5][6].
candidate 2 (found by 3 of 30 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).
candidate 3 (found by 1 of 30 passes): `std::execution`, which will ship in C++26, provides “the [library] implementation of an `async-function`” ([8] at §6).

## vehicle - grade 0.83 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/1/2  -> 1.67
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): This restriction can only be implemented by the compiler. Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.
candidate 2 (found by 1 of 30 passes): This restriction can only be implemented by the compiler.

## coordination - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 30 passes): Trying to accept `std::execution::set_value_t()` (i.e. successful completion with no values) alongside any other `std::execution::set_value_t(...)` form, on the other hand, does not work.

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
