Verdict: Adequate (4/14)

The paper offers some support for its naming argument, particularly by appealing to established terminology and criticizing the alternative proposal’s names, but it does not build a case that this facility belongs in the C++ standard. The thinnest areas are the complete absence of discussion about why standardization is necessary, why a library solution would be insufficient, or whether there is any implementation experience to draw on.

- The strongest support is the established precedent for calling these operations ceiling and floor division, which the paper uses effectively to argue against the names in P3724R4.
- The paper also establishes that the alternative proposal’s names diverge sharply from common practice in other languages and libraries.
- The most glaring omission is the lack of any argument for why this needs to be in the standard rather than in a user-provided or third-party library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 3 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.33   accumulate 4.33   max 4.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 26 of 28 section-criterion pairs unanimous (93%)
single-sample totals would have been: 4.50 / 4.50 / 4.00   (all 3 samples: 4.33)
headings: h2 3
on threshold: none
splits: audience[2] 1/0/0  audience[3] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 4 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Proposal                                   2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 12 passes): The answer to what `div_floor` does for negative numbers is of course the same as it is for positive numbers: it gives the largest integer less than or equal to the quotient.
candidate 2 (found by 2 of 12 passes): The names `std::div_to_pos_inf` and `std::div_to_neg_inf` proposed by [[P3724R4]](https://wg21.link/p3724r4) are poor names.
candidate 3 (found by 1 of 12 passes): There is broadly established precedent for referring to these operations as ceiling and floor division, respectively. People looking for these operations will look for them *under those names*.

## audience - grade 0.33 (fired in 2 of 4 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/0/0  -> 0.33
  [3] 2 Proposal                                   0/1/0  -> 0.33
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 12 passes): Here is a list of programming languages and the name they give their functions for these operations:
candidate 2 (found by 1 of 12 passes): There is broadly established precedent for referring to these operations as ceiling and floor division, respectively.

## prior_art - grade 2.00 (fired in 2 of 4 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Proposal                                   2/2/2  -> 2.00
  [4] 3 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 12 passes): There is broadly established precedent for referring to these operations as ceiling and floor division, respectively.
candidate 2 (found by 1 of 12 passes): To compare the names of the other functions proposed in [[P3724R4]](https://wg21.link/p3724r4) to the rounding modes provided in Julia and Swift, I think the proposed names are the worst of the three:
candidate 3 (found by 1 of 12 passes): That proposal’s names for the two rounding modes described above are: ... `std::div_to_neg_inf(x, y)` ... `std::div_to_pos_inf(x, y)`. That is extremely different from established practice.
candidate 4 (found by 1 of 12 passes): That proposal’s names for the two rounding modes described above are: ... That is extremely different from established practice.

## vehicle - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Proposal                                   0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Proposal                                   0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Proposal                                   0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Proposal                                   0/0/0  -> 0.00
  [4] 3 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
