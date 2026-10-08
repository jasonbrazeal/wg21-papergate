Verdict: Adequate (6/14)

The paper’s strongest backing comes from concrete implementation experience and a direct tie to prior committee discussion, but much of its case for urgency and user impact rests on assertion rather than demonstrated need. The thinnest areas are the absence of any argument for why a library solution would be insufficient and the lack of evidence connecting the proposed change to real user or implementer demand.

- The paper establishes implementation experience through a working `constexpr std::hive` fork of MS STL and connects the proposal to a prior NB comment and the original hive author’s published performance work.
- The paper claims consistency with other standard containers and user expectations as reasons for standardization, but does not substantiate those claims with evidence beyond anecdote.
- The paper offers no support for why a library-level solution would not address the stated need.
- The paper’s assertions about affected users and implementer coordination are stated as intentions or beliefs rather than established facts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 7.00   accumulate 6.17   max 7.33

## SUMMARY
grades: motivation 0.67  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 0.17  insufficiency 0.00  implementation 2.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.00 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 4
on threshold: implementation
splits: motivation[2] 2/1/1  audience[2] 0/1/1  coordination[2] 0/0/1
## END SUMMARY

## motivation - grade 0.67 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   2/1/1  -> 1.33
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): C++ users are often surprised by missing functionality available during constant evaluation, sometimes there is no real reason in the language, it's just no one wrote a paper making the thing `constexpr`.

## audience - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/1/1  -> 0.67
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): Anecdotally this is often surprise to Jason Turner's students when they start experimenting with `constexpr` code.

## prior_art - grade 2.00 (fired in 3 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           2/2/2  -> 2.00
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): It also resolves NB comment [`CZ 1-231 23.3.8 [hive] make std::hive constexpr`](https://github.com/cplusplus/nbballot/issues/802) which was raised against C++26, but LEWG decided against making hive `constexpr` in C++26 timeframe.
candidate 2 (found by 3 of 15 passes): In the same response paper author states [I never built a constexpr version of hive. I believed I had at the time](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3945r0.html#:~:text=I%20never%20built%20a%20constexpr%20version%20of%20hive.%20I%20believed%20I%20had%20at%20the%20time).
candidate 3 (found by 3 of 15 passes): Original hive's author wrote a publication and implementation of performance improvement over proposed skiplist with a fast bitset.

## vehicle - grade 1.00 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper makes `std::hive` usable during constant evaluation, consistently with every other container type in the C++ standard library.
candidate 2 (found by 3 of 15 passes): We believe it's imperative `std::hive` to be `constexpr` as that's what is expected from the container part of the standard library.

## coordination - grade 0.17 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/1  -> 0.33
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): All implementations are aware of this intention, and hopefully didn't choose implementation strategy which would force them to break ABI to implement this paper.

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): As before there is existing implementation, and it doesn't make sense to leave this one container non-`constexpr`.
candidate 2 (found by 3 of 15 passes): [NylteJ](https://github.com/NylteJ) provided implementation of `constexpr std::hive` in his [fork of MS STL](https://github.com/NylteJ/STL/tree/hive)

-->
