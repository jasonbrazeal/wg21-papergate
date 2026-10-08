Verdict: Adequate (7/14)

The paper offers a narrow but genuine basis for its standardization request: it clearly identifies an arbitrary language restriction and points to existing prior art, but it leaves several essential parts of the case largely unargued. The support is thinnest around who would actually benefit, how the feature would interact with the broader ecosystem, and whether there is meaningful implementation experience beyond the author’s own claim.

- The paper establishes that the current ban on combining `return_void` and `return_value` is arbitrary and creates a real mismatch with `std::execution` completion signatures.
- It also establishes that the problem has been raised before in a prior paper, and that library-level workarounds are comparatively awkward.
- The paper claims, but does not establish, that the restriction requires a compiler change rather than a library solution, since the supporting reasoning is asserted rather than demonstrated against plausible alternatives.
- The most glaring omission is the absence of any established affected-user population, coordination story, or corroborated implementation experience, leaving the practical urgency and readiness for standardization unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.00   accumulate 7.00   max 9.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.00  implementation 1.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 6.50 / 6.50 / 7.00   (all 3 samples: 6.67)
headings: h2 7
on threshold: motivation, vehicle, insufficiency
splits: motivation[3] 1/1/2
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   1/1/2  -> 1.33
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Disallowing `return_void` alongside `return_value` is fundamentally arbitrary, unnecessarily making `void` a special case.
candidate 2 (found by 2 of 24 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): *“If searches for the names* `return_void` *and* `return_value` *in the scope of the promise type* *each find any declarations, the program is ill-formed.”*
candidate 3 (found by 2 of 24 passes): Trying to accept `std::execution::set_value_t()` (i.e. successful completion with no values) alongside any other `std::execution::set_value_t(...)` form, on the other hand, does not work.
candidate 4 (found by 1 of 24 passes): Unfortunately the standard bans this by fiat (§9.6.4 [dcl.fct.def.coroutine]): *“If searches for the names `return_void` and `return_value` in the scope of the promise type each find any declarations, the program is ill-formed.”*

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

## prior_art - grade 2.00 (fired in 3 of 8 sections, strong in 2)
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
candidate 1 (found by 3 of 24 passes): The library implementation of a function provided by `std::execution`’s senders and receivers is breathtakingly more powerful than C++’s language-level functions
candidate 2 (found by 3 of 24 passes): Disallowing it either disadvantages coroutines vis-à-vis `std::execution` or necessitates library workarounds (e.g. the tag type approach discussed in the preceding section).
candidate 3 (found by 2 of 24 passes): There has previously been a paper by a different author with the same goal as this paper [4]. It had no consensus in Cologne in 2019, however the author of this paper feels there is new information [5][6].
candidate 4 (found by 1 of 24 passes): There has previously been a paper by a different author with the same goal as this paper [4].

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

## insufficiency - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 24 passes): Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.
candidate 2 (found by 1 of 24 passes): This restriction can only be implemented by the compiler. Regular C++ code cannot check for “names” or “declarations,” it can only check for well-formed expressions.

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
