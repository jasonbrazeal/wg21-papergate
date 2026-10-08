Verdict: Adequate to Strong (8/14)

The paper offers a solid foundation for why lossless path formatting matters and shows meaningful prior art, but it leans heavily on the same few references for several distinct parts of its case. The thinnest support is around why this must be standardized rather than left to libraries, and around concrete implementation experience beyond a single formatting library.

- The clearest support is for the problem itself: the paper establishes that current behavior is inconsistent across platforms and prevents reliable round-tripping of paths.
- The prior art and alternatives section is also well supported, with POSIX behavior, Rust, Node.js, Python, and the {fmt} implementation all cited.
- The case for who is affected rests mostly on claims about Rust and Node.js usage, without showing how C++ users encounter the same need.
- The most glaring omission is a demonstration that a library solution cannot adequately address the problem, since the paper’s own {fmt} implementation suggests otherwise.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 7 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.33   accumulate 7.83   max 9.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 1.17  insufficiency 0.17  implementation 1.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 7.00 / 8.50   (all 3 samples: 7.83)
headings: h2 8
on threshold: audience
splits: motivation[2] 1/2/1  audience[6] 2/1/2  audience[8] 1/0/0  prior_art[2] 2/0/2
        coordination[5] 1/1/2  insufficiency[6] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/2/1  -> 1.33
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposal                                  2/2/2  -> 2.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 2 (found by 3 of 27 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 3 (found by 3 of 27 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## audience - grade 1.00 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  2/1/2  -> 1.67
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 1/0/0  -> 0.33
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 1 of 27 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/0/2  -> 1.33
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposal                                  2/2/2  -> 2.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless
candidate 2 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 3 (found by 3 of 27 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.
candidate 4 (found by 2 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  1/1/1  -> 1.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 1 of 27 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## coordination - grade 1.17 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                1/1/2  -> 1.33
  [6] 5. Proposal                                  1/1/1  -> 1.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  0/0/1  -> 0.33
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

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
