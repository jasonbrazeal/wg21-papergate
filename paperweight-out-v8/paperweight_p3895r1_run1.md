Verdict: Adequate (6/14)

The paper offers real support in a couple of places, particularly by pointing to a complete implementation and by showing that the problem is both common and easy to get wrong, but much of its case for standardization rests on repeated assertions rather than demonstrated need. The thinnest areas are the arguments that a library solution is insufficient and that the standard itself is the right venue, since those claims are mostly stated without being backed up.

- The strongest support is the existence of a full implementation in the `eisenwave/integer-division` repository, which shows the feature is implementable and has been worked through in practice.
- The paper does establish that the problem matters by noting that users frequently need these operations and that common attempts to implement them are often incorrect.
- The case for why this must be in the standard rather than a library is claimed but not established, relying mainly on the inconvenience of pulling in a third-party dependency.
- The most glaring omission is the lack of established evidence about who is affected and how widespread the need is, beyond the repeated assertion that users need it all the time.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 7 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 7.33   accumulate 7.50   max 8.67

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.00  vehicle 0.67  coordination 0.17  insufficiency 0.50  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 6.50 / 6.00   (all 3 samples: 6.33)
headings: h3 8   <- NOT h2, check the unit list
on threshold: motivation, implementation
splits: motivation[4] 0/1/0  vehicle[3] 1/2/1  coordination[3] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Why does this need to be in the standard?    2/2/2  -> 2.00
  [4] Computing remainders is hard                 0/1/0  -> 0.33
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): users need it all the time, and try to implement it - they fail miserably: almost all attempts on StackOverflow/blogs wrong
candidate 2 (found by 2 of 27 passes): many other rounding modes are useful
candidate 3 (found by 1 of 27 passes): many other rounding modes are useful:
candidate 4 (found by 1 of 27 passes): The following function has unintended UB:

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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

## prior_art - grade 1.00 (fired in 5 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Why does this need to be in the standard?    1/1/1  -> 1.00
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              1/1/1  -> 1.00
  [6] Library interface                            1/1/1  -> 1.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): software division in other langs. sometimes supports other modes
candidate 2 (found by 3 of 27 passes): pulling in third-party library for one division function is silly
candidate 3 (found by 3 of 27 passes): marked functions are must-have, others fill the gaps
candidate 4 (found by 3 of 27 passes): as in − 2 mod 5 = 3 , and as in `mod` in Haskell, Ada, CSS, etc.

## vehicle - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    1/2/1  -> 1.33
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): pulling in third-party library for one division function is silly
candidate 2 (found by 1 of 27 passes): users need it all the time, and try to implement it - they fail miserably: almost all attempts on StackOverflow/blogs wrong

## coordination - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Why does this need to be in the standard?    1/0/0  -> 0.33
  [4] Computing remainders is hard                 0/0/0  -> 0.00
  [5] Which rounding modes to support              0/0/0  -> 0.00
  [6] Library interface                            0/0/0  -> 0.00
  [7] Other design considerations                  0/0/0  -> 0.00
  [8] Implementation experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): users need it all the time, and try to implement it

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): pulling in third-party library for one division function is silly
candidate 2 (found by 1 of 27 passes): they fail miserably: almost all attempts on StackOverflow/blogs wrong

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
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
