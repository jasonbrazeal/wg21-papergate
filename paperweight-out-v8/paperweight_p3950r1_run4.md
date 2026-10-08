Verdict: Adequate (6/14)

The paper offers solid support for the core motivation and for the existence of viable alternatives, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas are the absence of any demonstrated affected audience, the lack of coordination or interoperability discussion, and the very brief treatment of implementation experience.

- The paper clearly establishes that the current restriction is arbitrary and that the proposed direction has prior art and a meaningful alternative in the library model.
- The claim that only the compiler can address this is asserted, but the paper does not develop enough of a case for why standardization is the necessary remedy.
- The paper offers almost no evidence about who is affected or how the change would interact with existing coroutine and execution practices.
- The implementation experience consists of a single sentence, with no detail about compiler, scale, or observed problems.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.00   accumulate 6.67   max 8.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.00 / 7.00 / 6.00   (all 3 samples: 6.33)
headings: h2 9
on threshold: motivation, insufficiency
splits: motivation[3] 1/2/1  prior_art[5] 0/1/1  vehicle[4] 0/2/1  vehicle[5] 1/0/0
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/2/1  -> 1.33
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): *“If searches for the names `return_void` and `return_value` in the scope of the promise type each find any declarations, the program is ill-formed.”*
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

## prior_art - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/1/1  -> 0.67
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): There has previously been a paper by a different author with the same goal as this paper [4]. It had no consensus in Cologne in 2019, however the author of this paper feels there is new information [5][6].
candidate 2 (found by 3 of 30 passes): The library implementation of a function provided by `std::execution`’s senders and receivers is breathtakingly more powerful than C++’s language-level functions
candidate 3 (found by 2 of 30 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).

## vehicle - grade 0.67 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/2/1  -> 1.00
  [5] Conclusion                                   1/0/0  -> 0.33
  [6] Wording                                      0/0/0  -> 0.00
  [7] Review History                               0/0/0  -> 0.00
  [8] Revision History                             0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): This restriction can only be implemented by the compiler. Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.
candidate 2 (found by 1 of 30 passes): This restriction can only be implemented by the compiler.
candidate 3 (found by 1 of 30 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).

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
