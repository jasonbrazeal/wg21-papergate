Verdict: Strong (8/14)

The paper gives a partial account of why lossless path formatting would be useful, but it leaves several essential parts of the standardization case largely unsupported, particularly the need for a standard facility rather than a library solution. The strongest material concerns the problem itself and the existence of prior approaches, while the weakest concerns implementation experience and the argument that standardization is necessary.

- The paper clearly establishes that current formatting is not lossless and that this prevents reliable round-tripping of paths.
- It identifies relevant prior art in Rust, Node.js, and Python, and notes an existing implementation in {fmt}.
- It does not establish why a library cannot adequately address the problem, leaving a central justification for standardization unstated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 7.83   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 1.00  insufficiency 0.00  implementation 1.33
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 8.50   (all 3 samples: 7.83)
headings: h2 6
on threshold: audience
splits: prior_art[2] 2/2/0  prior_art[6] 0/0/1  implementation[5] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 2 (found by 3 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 3 (found by 3 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## audience - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/0  -> 1.33
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/0/1  -> 0.33
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless
candidate 2 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 3 (found by 2 of 21 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 4 (found by 1 of 21 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

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
candidate 1 (found by 2 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 1 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  1/1/2  -> 1.33
  [6] 5. Implementation experience                 1/1/1  -> 1.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 3 of 21 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

-->
