Verdict: Adequate (6/14)

The paper’s support for standardization is uneven: it can point to concrete implementation experience and a direct connection to prior committee discussion, but it does not convincingly establish who is affected or why the library-level obstacles cannot be sidestepped. Much of the argument rests on assertions about consistency and expectation rather than demonstrated need.

- The strongest support is the existence of working implementations, including prototypes for both the bitset and skipfield approaches.
- The paper also establishes a clear prior-art trail through the national body comment and the original author’s published performance work.
- The case for why this belongs in the standard is thin, relying mainly on the claim that leaving one container non-`constexpr` “doesn’t make sense.”
- The most glaring omission is any account of who is affected, leaving the motivating user population and practical impact unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.33   accumulate 6.33   max 8.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.50  vehicle 0.83  coordination 0.33  insufficiency 0.33  implementation 2.00
sample agreement: 29 of 35 section-criterion pairs unanimous (83%)
single-sample totals would have been: 6.50 / 6.50 / 6.00   (all 3 samples: 6.33)
headings: h2 4
on threshold: motivation, prior_art, implementation
splits: motivation[2] 1/2/2  vehicle[1] 0/1/1  coordination[2] 1/1/0  insufficiency[4] 2/0/0
        implementation[2] 0/0/1  implementation[3] 0/2/2
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/2/2  -> 1.67
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper makes `std::hive` usable during constant evaluation, consistently with every other container type in the C++ standard library.
candidate 2 (found by 3 of 15 passes): C++ users are often surprised by missing functionality available during constant evaluation, sometimes there is no real reason in the language, it's just no one wrote a paper making the thing `constexpr`.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): It also resolves NB comment [`CZ 1-231 23.3.8 [hive] make std::hive constexpr`](https://github.com/cplusplus/nbballot/issues/802) which was raised against C++26, but LEWG decided against making hive `constexpr` in C++26 timeframe.
candidate 2 (found by 3 of 15 passes): Original hive's author wrote a publication and implementation of performance improvement over proposed skiplist with a fast bitset.

## vehicle - grade 0.83 (fired in 2 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] Motivation                                   1/1/1  -> 1.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): We believe it's imperative `std::hive` to be `constexpr` as that's what is expected from the container part of the standard library.
candidate 2 (found by 1 of 15 passes): it doesn't make sense to leave this one container non-`constexpr`.
candidate 3 (found by 1 of 15 passes): As before there is existing implementation, and it doesn't make sense to leave this one container non-`constexpr`.

## coordination - grade 0.33 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   1/1/0  -> 0.67
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): All implementations are aware of this intention, and hopefully didn't choose implementation strategy which would force them to break ABI to implement this paper.

## insufficiency - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               2/0/0  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): During constant evaluation there is no global ordering of pointers (even in runtime it's just implementation defined behaviour).

## implementation - grade 2.00  [binary: max] (fired in 4 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   0/0/1  -> 0.33
  [3] History of std::hive and constexpr           0/2/2  -> 1.33
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): As before there is existing implementation, and it doesn't make sense to leave this one container non-`constexpr`.
candidate 2 (found by 3 of 15 passes): [NylteJ](https://github.com/NylteJ) provided implementation of `constexpr std::hive` in his [fork of MS STL](https://github.com/NylteJ/STL/tree/hive)
candidate 3 (found by 2 of 15 passes): [updated STL prototype](https://github.com/NylteJ/STL) was published implementing both bitset and skipfield approaches independently based on the standard draft specification.
candidate 4 (found by 1 of 15 passes): All implementations are aware of this intention, and hopefully didn't choose implementation strategy which would force them to break ABI to implement this paper.

-->
