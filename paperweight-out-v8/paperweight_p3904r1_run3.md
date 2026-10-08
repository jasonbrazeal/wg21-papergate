Verdict: Adequate to Strong (7/14)

The paper gives a clear and well-supported account of the problem it addresses, particularly the lossless formatting gap left by P2845, and it points to relevant prior art and an existing implementation. The support becomes much thinner when the paper needs to show why this belongs in the C++ standard rather than remaining a library-level solution, and it offers almost nothing on why a library approach would be insufficient.

- The strongest part of the paper is its explanation of why the current behavior matters, with a concrete and acknowledged gap in lossless path formatting.
- The discussion of prior art and alternatives is also well established, including the relationship to P2845 and comparable handling in other ecosystems.
- The case for standardization itself rests mainly on a passing reference to Rust and Node.js, without showing why C++ users need a standard-mandated encoding rather than an implementation detail.
- The most glaring omission is the complete absence of any argument for why a library cannot solve the problem, which leaves the central standardization question unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 8.00   accumulate 7.33   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.50 / 7.50   (all 3 samples: 7.33)
headings: h2 6
on threshold: audience
splits: motivation[2] 0/2/0  audience[5] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/2/0  -> 0.67
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.
candidate 3 (found by 1 of 21 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).

## audience - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  1/2/2  -> 1.67
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 1/1/1  -> 1.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): [P2845], adopted in C++26, added formatting support for `std::filesystem::path`, addressing encoding issues and making formatting lossless except for one case, unpaired surrogates on Windows.
candidate 2 (found by 3 of 21 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless
candidate 3 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 4 (found by 3 of 21 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

## vehicle - grade 0.50 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  1/1/1  -> 1.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## coordination - grade 1.00 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                1/1/1  -> 1.00
  [5] 4. Proposal                                  1/1/1  -> 1.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  0/0/0  -> 0.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  1/1/1  -> 1.00
  [6] 5. Implementation experience                 1/1/1  -> 1.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 3 of 21 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

-->
