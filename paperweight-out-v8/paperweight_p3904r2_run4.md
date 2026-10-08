Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of the problem and the intended lossless formatting behavior, but its support for standardization is uneven: the strongest material concerns the inconsistency and round-trip failure, while the case for why this belongs in the standard rather than in a library is essentially absent.

- The paper establishes the core motivation by showing that current formatting is inconsistent across platforms and cannot reliably round-trip paths.
- It also establishes relevant prior art and alternatives, including POSIX behavior, Rust and Node.js usage, Python’s mechanism, and an {fmt} implementation.
- The claim about who is affected leans on external projects but does not demonstrate the breadth or significance of the affected C++ audience.
- The most glaring omission is the lack of any argument for why a library solution would not suffice, leaving the need for standardization itself unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.67   accumulate 7.50   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.33  coordination 1.50  insufficiency 0.00  implementation 1.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 8.00 / 7.00   (all 3 samples: 7.50)
headings: h2 8
on threshold: coordination
splits: motivation[2] 1/1/2  audience[6] 1/2/1  prior_art[8] 0/1/0  vehicle[6] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/2  -> 1.33
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposal                                  2/2/2  -> 2.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 27 passes): This will enable round trip of paths from `char` strings which is currently not possible.
candidate 3 (found by 1 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 4 (found by 1 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding.

## audience - grade 0.67 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  1/2/1  -> 1.33
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposal                                  2/2/2  -> 2.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/1/0  -> 0.33
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 2 (found by 3 of 27 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless
candidate 3 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 4 (found by 1 of 27 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

## vehicle - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  1/1/0  -> 0.67
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## coordination - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposal                                  1/1/1  -> 1.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  0/0/0  -> 0.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  1/1/1  -> 1.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 3 of 27 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

-->
