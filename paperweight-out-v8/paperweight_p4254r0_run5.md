Verdict: Adequate (6/14)

The paper offers some grounding for its position in the interaction between the Lakos Rule and library design, but it does not build a complete case for standardization. The strongest material concerns why the issue matters and what alternatives exist, while the thinnest areas are the absence of affected users, implementation experience, and any argument that a library solution would be insufficient.

- The paper clearly establishes why the Lakos Rule’s effect on `noexcept` and generic interrogation is a problem worth addressing.
- It also establishes prior art and alternatives by pointing to existing standard-library traits and the principle that “Throws: Nothing” should imply `noexcept`.
- The paper claims but does not establish why the standard is the right venue, resting mainly on the existence of `std::invoke_result_t` and `std::is_nothrow_invocable_v`.
- It offers no evidence about who is affected, no implementation experience, and no argument for why a library-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 4 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 6.00   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 5.50 / 5.50 / 6.00   (all 3 samples: 5.50)
headings: h2 7
on threshold: prior_art, vehicle, coordination
splits: motivation[5] 2/2/1  motivation[6] 1/1/0  prior_art[3] 2/1/2  prior_art[4] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   2/2/2  -> 2.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   2/2/1  -> 1.67
  [6] Proposal                                     1/1/0  -> 0.67
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper considers the Lakos Rule [1] and how it negatively interacts with the process of library design.
candidate 2 (found by 3 of 24 passes): This has impeded the adoption of `noexcept` in the library, and has led to arguably-ridiculous consequences (e.g. `std::vector::operator[]` not being marked `noexcept` despite being distinguished from `std::vector::at` only by the fact that it does not throw).
candidate 3 (found by 3 of 24 passes): It renders facially-correct code suspect by introducing throwing paths where the designs of the functions being composed say they oughtn’t exist.
candidate 4 (found by 2 of 24 passes): The Lakos Rule, however, would have `std::is_nothrow_invocable_v` yield `false` for invocables which everyone knows don’t throw, just because they have a precondition (i.e. the template variable would claim an error channel exists when, in practice, it does not).

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Proposal                                     0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 5 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   2/1/2  -> 1.67
  [4] Discussion                                   0/2/2  -> 1.33
  [5] Conclusion                                   1/1/1  -> 1.00
  [6] Proposal                                     1/1/1  -> 1.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper considers the Lakos Rule [1] and how it negatively interacts with the process of library design.
candidate 2 (found by 3 of 24 passes): LEWG should reject the Lakos Rule and write the equivalent in code (`noexcept`) to what is said in prose (“Throws: Nothing”).
candidate 3 (found by 3 of 24 passes): “Throws: Nothing” should mean/imply `noexcept` [16].
candidate 4 (found by 2 of 24 passes): It is now being argued [5] that the above renders the Lakos Rule *fait accompli* (exactly as I articulated in my justification for my vote on P3471 in Hagenberg).

## vehicle - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Proposal                                     0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The standard library supplies `std::invoke_result_t` which allows generic code to determine the type an invocable yields when invoked with a certain cv- and ref-qualification, and with arguments of certain types.

## coordination - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Proposal                                     0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The fact that `std::execution` is not designed in accordance with the Lakos Rule is not the only interesting thing here.
candidate 2 (found by 1 of 24 passes): The standard library supplies `std::invoke_result_t` which allows generic code to determine the type an invocable yields when invoked with a certain cv- and ref-qualification, and with arguments of certain types.
candidate 3 (found by 1 of 24 passes): The standard library also supplies `std::is_nothrow_invocable_v` which allows for the same interrogation, save for the error channel (i.e. exceptions).

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Proposal                                     0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Conclusion                                   0/0/0  -> 0.00
  [6] Proposal                                     0/0/0  -> 0.00
  [7] Acknowledgements                             0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
