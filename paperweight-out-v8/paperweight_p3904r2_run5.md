Verdict: Adequate to Strong (7/14)

The paper offers solid support for the core motivation and the existence of a workable alternative, but much of its broader case rests on assertions that are not yet backed up with evidence or detail. The thinnest areas are the arguments that standardization is necessary, that a library solution would be insufficient, and that the approach has meaningful implementation experience beyond a single formatter.

- The strongest support is for the problem itself and the proposed WTF-8 approach, including prior art in Rust, Node.js, and Python, and an existing {fmt} implementation.
- The paper establishes that current Windows path formatting is inconsistent and lossy, and that the proposed change would make it lossless and more consistent with POSIX.
- The claim that a library solution will not suffice is asserted mainly through the round-trip benefit, but the paper does not show why that benefit cannot be achieved outside the standard.
- The most glaring omission is the lack of established evidence for who is affected and why standardization, rather than a library or existing practice, is required.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 7 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 8.00   accumulate 7.17   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 0.50  coordination 0.33  insufficiency 0.17  implementation 1.33
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 7.50 / 7.00 / 7.00   (all 3 samples: 7.17)
headings: h2 8
on threshold: audience
splits: motivation[2] 2/2/1  audience[6] 1/2/2  vehicle[2] 0/0/1  vehicle[6] 0/1/1
        coordination[6] 2/0/0  insufficiency[6] 0/1/0  implementation[6] 2/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/1  -> 1.67
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                2/2/2  -> 2.00
  [6] 5. Proposal                                  2/2/2  -> 2.00
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 27 passes): This will enable round trip of paths from `char` strings which is currently not possible.
candidate 3 (found by 2 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 4 (found by 1 of 27 passes): This will improve consistency in path handling between Windows and POSIX platforms and align with the design of `std::format` where the default formatting is normally lossless.

## audience - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  1/2/2  -> 1.67
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
  [8] 7. Implementation experience                 1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 2 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 3 (found by 3 of 27 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.
candidate 4 (found by 2 of 27 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless

## vehicle - grade 0.50 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/1  -> 0.33
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  0/1/1  -> 0.67
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 1 of 27 passes): This will improve consistency in path handling between Windows and POSIX platforms and align with the design of `std::format` where the default formatting is normally lossless.

## coordination - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  2/0/0  -> 0.67
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  0/1/0  -> 0.33
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## implementation - grade 1.33  [binary: max] (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R1                          0/0/0  -> 0.00
  [4] 3. Changes since R0                          0/0/0  -> 0.00
  [5] 4. Motivation                                0/0/0  -> 0.00
  [6] 5. Proposal                                  2/1/1  -> 1.33
  [7] 6. Wording                                   0/0/0  -> 0.00
  [8] 7. Implementation experience                 1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 3 of 27 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

-->
