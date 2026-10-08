Verdict: Adequate (6/14)

The paper offers real support in a couple of narrow places, chiefly by pointing to an existing implementation and by showing that naive user-written code can have undefined behavior, but much of its case rests on repeated assertions rather than demonstrated need or analysis. The thinnest areas are the claims about who is affected, why the standard is the right venue, and why a library solution is insufficient, since those are asserted without evidence or comparison.

- The strongest support is the existence of a full implementation in the `eisenwave/integer-division` repository, which shows the functionality is implementable and gives some implementation experience.
- The paper also clearly establishes one motivating hazard by identifying a function with unintended undefined behavior.
- A notable omission is any real substantiation of the claim that users need this all the time and try to implement it, since no usage data, survey, or representative examples are provided.
- The most glaring gap is the absence of a developed argument for why a library will not do, beyond the unsupported statement that pulling in a third-party library for one function is silly.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 7 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 7.33   accumulate 7.50   max 8.33

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.00  vehicle 0.50  coordination 0.33  insufficiency 0.33  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 5.50 / 6.50   (all 3 samples: 6.17)
headings: h3 8   <- NOT h2, check the unit list
on threshold: motivation, implementation
splits: motivation[2] 1/1/0  prior_art[7] 1/1/0  coordination[3] 1/0/1  insufficiency[3] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/0  -> 0.67
  [3] Why does this need to be in the standard?    2/2/2  -> 2.00
  [4] Computing remainders is hard                 1/1/1  -> 1.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): users need it all the time, and try to implement it - they fail miserably: almost all attempts on StackOverflow/blogs wrong
candidate 2 (found by 3 of 27 passes): The following function has unintended UB
candidate 3 (found by 2 of 27 passes): many other rounding modes are useful

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    1/1/1  -> 1.00
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): users need it all the time, and try to implement it

## prior_art - grade 1.00 (fired in 6 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Why does this need to be in the standard?    1/1/1  -> 1.00
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              1/1/1  -> 1.00
  [6] Library interface                            1/1/1  -> 1.00
  [7] Other design considerations                  1/1/0  -> 0.67
  [8] Implementation experience                    1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): as in − 2 mod 5 = 3 , and as in `mod` in Haskell, Ada, CSS, etc.
candidate 2 (found by 3 of 27 passes): `eisenwave/integer-division` [[GitHub]](https://github%2ecom/Eisenwave/integer-division) repo has full implementation
candidate 3 (found by 2 of 27 passes): software division in other langs. sometimes supports other modes
candidate 4 (found by 2 of 27 passes): pulling in third-party library for one division function is silly

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    1/1/1  -> 1.00
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): pulling in third-party library for one division function is silly

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    1/0/1  -> 0.67
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): users need it all the time, and try to implement it - they fail miserably: almost all attempts on StackOverflow/blogs wrong

## insufficiency - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    1/0/1  -> 0.67
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): they fail miserably: almost all attempts on StackOverflow/blogs wrong
candidate 2 (found by 1 of 27 passes): pulling in third-party library for one division function is silly

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    0/0/0  -> 0.00
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    2/2/2  -> 2.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `eisenwave/integer-division` [[GitHub]](https://github%2ecom/Eisenwave/integer-division) repo has full implementation

-->
