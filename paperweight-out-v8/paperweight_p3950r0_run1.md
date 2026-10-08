Verdict: Adequate (7/14)

The paper gives a partial account of why the restriction should be lifted, but it leaves several essential parts of the standardization case largely unargued. The strongest material concerns the arbitrariness of the current rule and the existence of prior work, while the discussion of affected users, coordination, and implementation experience is thin or absent.

- The paper clearly establishes that the existing ban on combining `return_void` and `return_value` is arbitrary and creates a special case for `void`.
- It also shows awareness of prior art and explains why library workarounds are weaker than language support.
- The claim that only the compiler can implement the change is asserted rather than demonstrated, since the paper does not rule out other standardization or library strategies.
- The paper never identifies who is affected or how the change would coordinate with existing coroutine and sender/receiver specifications, leaving the practical need for standardization largely unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.00   accumulate 7.17   max 9.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.17  implementation 1.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.50 / 6.50 / 7.00   (all 3 samples: 6.67)
headings: h2 7
on threshold: motivation, vehicle, insufficiency
splits: insufficiency[5] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Disallowing `return_void` alongside `return_value` is fundamentally arbitrary, unnecessarily making `void` a special case.
candidate 2 (found by 2 of 24 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): *“If searches for the names `return_void` and `return_value` in the scope of the promise type each find any declarations, the program is ill-formed.”*
candidate 3 (found by 2 of 24 passes): Trying to accept `std::execution::set_value_t()` (i.e. successful completion with no values) alongside any other `std::execution::set_value_t(...)` form, on the other hand, does not work.
candidate 4 (found by 1 of 24 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): “If searches for the names return_void and return_value in the scope of the promise type each find any declarations, the program is ill-formed.”

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): There has previously been a paper by a different author with the same goal as this paper [4]. It had no consensus in Cologne in 2019, however the author of this paper feels there is new information [5][6].
candidate 2 (found by 3 of 24 passes): The library implementation of a function provided by `std::execution`’s senders and receivers is breathtakingly more powerful than C++’s language-level functions
candidate 3 (found by 3 of 24 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).

## vehicle - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This restriction can only be implemented by the compiler. Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.17 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/1  -> 0.33
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.
candidate 2 (found by 1 of 24 passes): This restriction can only be implemented by the compiler. Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.
candidate 3 (found by 1 of 24 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).

## implementation - grade 1.00  [binary: max] (fired in 1 of 8 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The above works. The author has implemented it.

-->
