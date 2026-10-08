Verdict: Strong (9/14)

The paper gives a reasonably solid account of the problem and the design space, but its support becomes noticeably thinner when it moves from describing the issue to justifying why the work belongs in the standard rather than in a library. The strongest material concerns losslessness, round-tripping, and consistency with existing formatting practice, while the weakest concerns evidence of real-world use and implementation experience.

- The paper clearly establishes that current path formatting is inconsistent and lossy, and that the proposed WTF-8 approach would enable lossless round-tripping.
- It also establishes relevant prior art and alternatives, including Rust, Node.js, Python, and an existing {fmt} implementation.
- The paper only claims, without fully establishing, that the affected audience and the need for standardization are demonstrated by those external uses.
- The most glaring omission is the lack of established implementation experience or a convincing argument that a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 7 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 9.00   accumulate 8.50   max 10.00

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.17  coordination 1.83  insufficiency 0.17  implementation 1.33
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 8.00 / 8.50 / 9.00   (all 3 samples: 8.50)
headings: h2 6
on threshold: audience
splits: motivation[6] 0/1/0  vehicle[5] 0/1/0  coordination[5] 1/2/2  insufficiency[5] 1/0/0
        implementation[5] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/1  -> 1.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/1/0  -> 0.33
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.
candidate 3 (found by 2 of 21 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 4 (found by 1 of 21 passes): This will improve consistency in path handling between Windows and POSIX platforms and align with the design of `std::format` where the default formatting is normally lossless.

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
candidate 1 (found by 3 of 21 passes): This paper proposes addressing this case and making formatting 100% lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 2 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 3 (found by 3 of 21 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.
candidate 4 (found by 2 of 21 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless:

## vehicle - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  0/1/0  -> 0.33
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## coordination - grade 1.83 (fired in 2 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  1/2/2  -> 1.67
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 2 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 3 (found by 1 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## insufficiency - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  1/0/0  -> 0.33
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.

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
