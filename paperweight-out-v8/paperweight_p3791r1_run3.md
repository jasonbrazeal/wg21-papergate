Verdict: Weak to Adequate (4/14)

The paper offers a narrow but genuine rationale for constexpr deterministic random facilities, centered on avoiding duplicated user code and enabling compile-time use of algorithms like `shuffle` and `sample`. Beyond that motivating claim, however, the case for standardization is largely undeveloped: the affected audience, the need for a standard rather than a library solution, and coordination with existing or future library work are not established. The thinnest areas are the absence of implementation experience beyond a partial compiler patch and the lack of any discussion of why users cannot already achieve the stated goals through existing mechanisms.

- The strongest support is the established motivation that making deterministic random algorithms and distribution types constexpr would reduce duplicated code and `if consteval` workarounds.
- The paper claims some prior art and implementation experience, but neither is substantiated enough to count as established support.
- The proposal does not establish who is affected by the change or why the standard is the right place for it.
- The most glaring omission is the complete lack of discussion of why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 3 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 3.33   accumulate 4.50   max 5.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.33
sample agreement: 67 of 70 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.00 / 5.00 / 5.00   (all 3 samples: 4.17)
headings: h2 6
on threshold: motivation, prior_art
splits: prior_art[3] 1/1/0  prior_art[5] 0/1/1  implementation[4] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Implementation experience                    0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Making these functions `constexpr` limits the need for users to reimplement these and use `if consteval`, limiting number of errors due duplication of code.
candidate 2 (found by 2 of 30 passes): This paper doesn't propose making `random_device` type, `rand()` and `srand()` `constexpr` functions as these are not deterministic.
candidate 3 (found by 1 of 30 passes): This paper proposes making all **deterministic** algorithms and types associated with *random number generators* constant evaluatable.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Implementation experience                    0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   1/1/0  -> 0.67
  [4] Implementation experience                    2/2/2  -> 2.00
  [5] Wording                                      0/1/1  -> 0.67
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Jonathan [sent me a code snippet](https://godbolt.org/z/vPcvvrzvj) and said he will be less concerned if the code he sent passes constant evaluation.
candidate 2 (found by 2 of 30 passes): This proposal also excludes iostream compatibility functions `operator<<` and `operator>>` as `iostream` types are not `constexpr` compatible yet (they will be in future proposal [P3758](https://wg21.link/P3758)).
candidate 3 (found by 1 of 30 passes): They need [random sampling](https://en.wikipedia.org/wiki/Count–min_sketch).
candidate 4 (found by 1 of 30 passes): Algorithms `shuffle`, `sample` are useful even in compile time, same applies to random distribution types which are fully deterministic.

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Implementation experience                    0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Implementation experience                    0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Implementation experience                    0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.33  [binary: max] (fired in 1 of 10 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Implementation experience                    0/2/2  -> 1.33
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): [The change](https://github.com/hanickadot/llvm-project/commit/9a3c3b135ca12d08df62f5f2646d53fc926bd654) containing only `<cmath>` and compiler evaluator changes is available on my github.

-->
