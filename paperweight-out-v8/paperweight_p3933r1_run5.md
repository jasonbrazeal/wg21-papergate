Verdict: Adequate (7/14)

The paper offers some concrete grounding in implementation experience and prior discussion, but much of its case for standardization rests on assertion rather than demonstrated need. The thinnest support is around who would actually be affected and why existing library-level approaches cannot suffice.

- The strongest support is the existence of a published prototype implementing `constexpr std::hive` in a fork of MS STL.
- The paper also benefits from prior art, including the original hive author’s acknowledgment that a `constexpr` version was never actually built.
- The paper asserts that users expect all standard containers to be `constexpr`, but it does not establish who is affected by the current omission.
- The most glaring omission is the absence of any demonstrated reason that a library-level solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.33   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 0.33  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 6.00 / 7.00   (all 3 samples: 6.67)
headings: h2 4
on threshold: none
splits: coordination[2] 1/0/1  insufficiency[4] 1/0/1
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] History of std::hive and constexpr           0/0/0  -> 0.00
  [4] Implementation                               0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): it doesn't make sense to leave this one container non-`constexpr`.
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

## prior_art - grade 2.00 (fired in 2 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] History of std::hive and constexpr           2/2/2  -> 2.00
  [4] Implementation                               2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Original hive's author wrote a publication and implementation of performance improvement over proposed skiplist with a fast bitset.
candidate 2 (found by 2 of 15 passes): In the same response paper author states [I never built a constexpr version of hive. I believed I had at the time](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3945r0.html#:~:text=I%20never%20built%20a%20constexpr%20version%20of%20hive.%20I%20believed%20I%20had%20at%20the%20time).
candidate 3 (found by 1 of 15 passes): In the same response paper author states [I never built a constexpr version of hive. I believed I had at the time]

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

## coordination - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   1/0/1  -> 0.67
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
  [4] Implementation                               1/0/1  -> 0.67
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): To implement this this paper depends on proposal of mine P3852 or Herb's similar proposal P3952 which provides required functionality.

## implementation - grade 2.00  [binary: max] (fired in 3 of 5 sections, strong in 2)
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
