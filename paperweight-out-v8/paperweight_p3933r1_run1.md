Verdict: Adequate (7/14)

The paper offers some concrete grounding in implementation work and prior discussion, but its central rationale rests on assertions about user expectations and consistency rather than demonstrated need. The thinnest parts are the absence of any identified affected audience and the lack of a case for why the standard, rather than a library solution, is required.

- The strongest support is the existence of a prototype implementation and the prior art, including the NB comment and the original author’s response paper.
- The paper claims consistency with other containers as a reason to standardize, but does not establish why that consistency matters in practice or who is harmed by its absence.
- The most glaring omission is the complete lack of discussion about who is affected by `std::hive` not being `constexpr` today.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 6.00   accumulate 6.83   max 8.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.67  vehicle 1.00  coordination 0.50  insufficiency 0.00  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 6.50 / 6.50   (all 3 samples: 6.50)
headings: h2 4
on threshold: motivation, prior_art
splits: motivation[1] 1/1/0  prior_art[3] 2/0/2
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Motivation                                   2/2/2  -> 2.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): C++ users are often surprised by missing functionality available during constant evaluation, sometimes there is no real reason in the language, it's just no one wrote a paper making the thing `constexpr`.
candidate 2 (found by 2 of 15 passes): This paper makes `std::hive` usable during constant evaluation, consistently with every other container type in the C++ standard library.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.67 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           2/0/2  -> 1.33
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Original hive's author wrote a publication and implementation of performance improvement over proposed skiplist with a fast bitset.
candidate 2 (found by 2 of 15 passes): It also resolves NB comment [`CZ 1-231 23.3.8 [hive] make std::hive constexpr`](https://github.com/cplusplus/nbballot/issues/802) which was raised against C++26, but LEWG decided against making hive `constexpr` in C++26 timeframe.
candidate 3 (found by 2 of 15 passes): In the same mailing a response paper [P3945](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3945r0.html) was published by the author of the original proposal.
candidate 4 (found by 1 of 15 passes): It also resolves NB comment [`CZ 1-231 23.3.8 [hive] make std::hive constexpr`](https://github.com/cplusplus/nbballot/issues/802) which was raised against C++26

## vehicle - grade 1.00 (fired in 2 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): We believe it's imperative `std::hive` to be `constexpr` as that's what is expected from the container part of the standard library.
candidate 2 (found by 1 of 15 passes): it doesn't make sense to leave this one container non-`constexpr`.
candidate 3 (found by 1 of 15 passes): This is almost identical paper as before, but it's aiming C++29. As before there is existing implementation, and it doesn't make sense to leave this one container non-`constexpr`.
candidate 4 (found by 1 of 15 passes): As before there is existing implementation, and it doesn't make sense to leave this one container non-`constexpr`.

## coordination - grade 0.50 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): All implementations are aware of this intention, and hopefully didn't choose implementation strategy which would force them to break ABI to implement this paper.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           2/2/2  -> 2.00
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): As before there is existing implementation, and it doesn't make sense to leave this one container non-`constexpr`.
candidate 2 (found by 3 of 15 passes): [updated STL prototype](https://github.com/NylteJ/STL) was published implementing both bitset and skipfield approaches independently based on the standard draft specification.
candidate 3 (found by 3 of 15 passes): [NylteJ](https://github.com/NylteJ) provided implementation of `constexpr std::hive` in his [fork of MS STL](https://github.com/NylteJ/STL/tree/hive)

-->
