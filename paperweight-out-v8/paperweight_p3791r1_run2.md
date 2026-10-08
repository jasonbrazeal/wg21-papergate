Verdict: Adequate (5/14)

The paper offers some useful grounding in implementation experience and prior art, but it leaves the core case for standardization largely unstated. The thinnest areas are the absence of any discussion of who is affected, why a library solution would not suffice, and why the standard itself is the right vehicle.

- The strongest support is the concrete implementation experience, with a linked compiler and library change demonstrating the direction is feasible.
- The paper also establishes some prior art and alternatives by showing existing deterministic behavior and excluding not-yet-constexpr iostream compatibility pieces.
- The rationale for why this matters is only claimed, resting on a general appeal to reducing duplication without showing the problem’s scope or significance.
- The most glaring omissions are the lack of any established audience, standardization rationale, coordination considerations, or argument for why a library cannot address the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 3 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 4.00   accumulate 5.33   max 6.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 69 of 70 section-criterion pairs unanimous (99%)
single-sample totals would have been: 5.00 / 5.00 / 4.50   (all 3 samples: 4.83)
headings: h2 6
on threshold: motivation, prior_art, implementation
splits: motivation[1] 1/1/0
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
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
candidate 2 (found by 2 of 30 passes): This paper proposes making all **deterministic** algorithms and types associated with *random number generators* constant evaluatable.

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

## prior_art - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Implementation experience                    2/2/2  -> 2.00
  [5] Wording                                      1/1/1  -> 1.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Algorithms `shuffle`, `sample` are useful even in compile time, same applies to random distribution types which are fully deterministic.
candidate 2 (found by 3 of 30 passes): Jonathan [sent me a code snippet](https://godbolt.org/z/vPcvvrzvj) and said he will be less concerned if the code he sent passes constant evaluation.
candidate 3 (found by 3 of 30 passes): This proposal also excludes iostream compatibility functions `operator<<` and `operator>>` as `iostream` types are not `constexpr` compatible yet (they will be in future proposal [P3758](https://wg21.link/P3758)).

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Implementation experience                    2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
  [6] 26.4 Header <algorithm> synopsis [algorit... 0/0/0  -> 0.00
  [7] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [8] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [9] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
  [10] 29.5 Random number generation [rand]  (pa... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): [The change](https://github.com/hanickadot/llvm-project/commit/9a3c3b135ca12d08df62f5f2646d53fc926bd654) containing only `<cmath>` and compiler evaluator changes is available on my github.

-->
