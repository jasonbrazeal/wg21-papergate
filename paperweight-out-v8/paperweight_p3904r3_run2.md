Verdict: Strong (9/14)

The paper gives credible support in a few important areas, particularly implementation experience and the existence of prior art, but it leaves several core arguments asserted rather than demonstrated. The thinnest parts concern why this needs to be in the standard rather than a library, and who specifically is affected by the current behavior.

- The strongest support is implementation experience, since the approach is already used in Rust and Node.js and has been implemented in {fmt}.
- The paper also establishes prior art and alternatives by naming WTF-8, Rust, Node.js, and Python’s different mechanism.
- The weakest area is the claim that a library solution would not suffice, which rests on a single sentence about enabling round trips without showing why standardization is required for that.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 7 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 8.67   accumulate 8.67   max 10.33

## SUMMARY
grades: motivation 2.00  audience 1.00  prior_art 2.00  vehicle 0.50  coordination 1.33  insufficiency 0.17  implementation 1.67
sample agreement: 62 of 70 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.50 / 8.00 / 9.50   (all 3 samples: 8.67)
headings: h2 9
on threshold: audience, coordination, implementation
splits: motivation[2] 1/1/0  audience[7] 2/1/2  audience[9] 1/0/0  vehicle[2] 0/0/1
        vehicle[7] 1/0/1  coordination[7] 1/1/0  insufficiency[7] 0/0/1  implementation[7] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              1/1/0  -> 0.67
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                2/2/2  -> 2.00
  [7] 6. Proposal                                  2/2/2  -> 2.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 3 of 30 passes): This will enable round trip of paths from `char` strings which is currently not possible.
candidate 3 (found by 2 of 30 passes): This will improve consistency in path handling between Windows and POSIX platforms and align with the design of `std::format` where the default formatting is normally lossless.

## audience - grade 1.00 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposal                                  2/1/2  -> 1.67
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 1/0/0  -> 0.33
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 1 of 30 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                2/2/2  -> 2.00
  [7] 6. Proposal                                  2/2/2  -> 2.00
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This paper proposes addressing this case and making such formatting lossless by default via the WTF-8 encoding ([WTF-8]).
candidate 2 (found by 3 of 30 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]). Python also handles this but with a different mechanism ([PEP383]).
candidate 3 (found by 3 of 30 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.
candidate 4 (found by 2 of 30 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless

## vehicle - grade 0.50 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/1  -> 0.33
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposal                                  1/0/1  -> 0.67
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 1 of 30 passes): This will improve consistency in path handling between Windows and POSIX platforms and align with the design of `std::format` where the default formatting is normally lossless.

## coordination - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                2/2/2  -> 2.00
  [7] 6. Proposal                                  1/1/0  -> 0.67
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 2 (found by 2 of 30 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).

## insufficiency - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposal                                  0/0/1  -> 0.33
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 0/0/0  -> 0.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## implementation - grade 1.67  [binary: max] (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R2                          0/0/0  -> 0.00
  [4] 3. Changes since R1                          0/0/0  -> 0.00
  [5] 4. Changes since R0                          0/0/0  -> 0.00
  [6] 5. Motivation                                0/0/0  -> 0.00
  [7] 6. Proposal                                  1/2/2  -> 1.67
  [8] 7. Wording                                   0/0/0  -> 0.00
  [9] 8. Implementation experience                 1/1/1  -> 1.00
  [10] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 3 of 30 passes): The proposal has been implemented in {fmt} where the default `std::filesystem::path` representation is now lossless.

-->
