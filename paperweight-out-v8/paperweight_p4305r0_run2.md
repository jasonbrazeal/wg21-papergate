Verdict: Weak to Adequate (3/14)

The paper offers some support for its own standardization by identifying a real design problem in an existing proposal and by engaging with that proposal’s examples and implications, but it leaves most of the case for standardization unaddressed. The thinnest areas are the absence of any demonstrated affected audience, any argument for why the standard rather than a library is the right venue, and any evidence of implementation experience or coordination.

- The strongest support is the paper’s engagement with P2964R5, including its motivational example and the claim that user-defined types in `std::simd::basic_vec` will inevitably require math function support.
- The paper also establishes that there is a relevant prior proposal and that the current trajectory appears to compound an incoherent collection of mathematical functions.
- The most glaring omission is that the paper never establishes who is affected by the problem or why the standard, as opposed to a library, is needed to address it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 2.00   accumulate 3.83   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.17)
headings: h2 6
on threshold: motivation, prior_art
splits: motivation[4] 0/2/0  prior_art[5] 2/0/2  prior_art[6] 0/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Opt-in vs. opt-out                        0/2/0  -> 0.67
  [5] 3. Operation customization                   2/2/2  -> 2.00
  [6] 4. Call for action                           0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): there are some crucial design problems that are either addressed the wrong way or not discussed whatsoever.
candidate 2 (found by 3 of 21 passes): We appear to have an ever-growing and incoherent collection of mathematical functions, and [[P2964R5]](https://isocpp%2eorg/files/papers/P2964R5%2ehtml) compounds this issue.
candidate 3 (found by 1 of 21 passes): The key issue is that for some types, the better layout for SIMD is structure-of-arrays.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Opt-in vs. opt-out                        0/0/0  -> 0.00
  [5] 3. Operation customization                   0/0/0  -> 0.00
  [6] 4. Call for action                           0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 5 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Opt-in vs. opt-out                        2/2/2  -> 2.00
  [5] 3. Operation customization                   2/0/2  -> 1.33
  [6] 4. Call for action                           0/1/1  -> 0.67
  [7] 5. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper discusses some design problems in [[P2964R5]](https://isocpp%2eorg/files/papers/P2964R5%2ehtml).
candidate 2 (found by 3 of 21 passes): [[P2964R5]](https://isocpp%2eorg/files/papers/P2964R5%2ehtml) enables the use of user-defined types in `std::simd::basic_vec`.
candidate 3 (found by 3 of 21 passes): [[P2964R5]](https://isocpp%2eorg/files/papers/P2964R5%2ehtml) has a motivational example in [§3.5 Compound Types](https://isocpp.org/files/papers/P2964R5.html#compound)
candidate 4 (found by 2 of 21 passes): It seems inevitable that any `vec<custom_float>` would need math function support, so simply ignoring this problem is not viable.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Opt-in vs. opt-out                        0/0/0  -> 0.00
  [5] 3. Operation customization                   0/0/0  -> 0.00
  [6] 4. Call for action                           0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Opt-in vs. opt-out                        0/0/0  -> 0.00
  [5] 3. Operation customization                   0/0/0  -> 0.00
  [6] 4. Call for action                           0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Opt-in vs. opt-out                        0/0/0  -> 0.00
  [5] 3. Operation customization                   0/0/0  -> 0.00
  [6] 4. Call for action                           0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Opt-in vs. opt-out                        0/0/0  -> 0.00
  [5] 3. Operation customization                   0/0/0  -> 0.00
  [6] 4. Call for action                           0/0/0  -> 0.00
  [7] 5. References                                0/0/0  -> 0.00
candidates: (none validated)

-->
