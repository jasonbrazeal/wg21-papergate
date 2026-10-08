Verdict: Strong (8/14)

The paper offers a reasonably grounded case in some areas, particularly around the existing inconsistency and the use of WTF-8 in comparable systems, but it leaves significant gaps in the argument for why this work belongs in the standard rather than in a library. The thinnest parts are the absence of a clear standardization rationale and the lack of evidence that a library solution would be insufficient.

- The strongest support comes from the established prior art, including the adopted C++26 formatting support for `std::filesystem::path` and the demonstrated lossless implementation in {fmt}.
- The paper also credibly establishes coordination and interoperability concerns by pointing to WTF-8’s use in Rust and Node.js and the current impossibility of reliable round-tripping on Windows.
- The claim about who is affected rests mainly on references to other ecosystems rather than a direct account of C++ users or codebases facing the problem.
- The most glaring omission is the failure to establish why the standard is the right venue, since no argument is made that a library cannot adequately address the issue.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.33   accumulate 7.67   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.00  coordination 1.67  insufficiency 0.00  implementation 1.33
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 8.00 / 7.50   (all 3 samples: 7.67)
headings: h2 6
on threshold: coordination
splits: audience[5] 1/2/1  coordination[4] 2/2/0  implementation[5] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              2/2/2  -> 2.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): [P2845], adopted in C++26, added formatting support for `std::filesystem::path`, addressing encoding issues and making formatting lossless except for one case, unpaired surrogates on Windows.
candidate 2 (found by 3 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.
candidate 3 (found by 3 of 21 passes): This will enable round trip of paths from `char` strings which is currently not possible.

## audience - grade 0.67 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Proposal                                  1/2/1  -> 1.33
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
candidate 4 (found by 2 of 21 passes): For comparison, on POSIX formatting of arbitrary paths including the ones that are not valid Unicode works as expected and is lossless

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
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

## coordination - grade 1.67 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Introduction                              0/0/0  -> 0.00
  [3] 2. Changes since R0                          0/0/0  -> 0.00
  [4] 3. Motivation                                2/2/0  -> 1.33
  [5] 4. Proposal                                  2/2/2  -> 2.00
  [6] 5. Implementation experience                 0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): WTF-8 is used to handle invalid UTF-16 in paths and other system APIs in Rust ([RUST-OSSTRING]) and Node.js libuv ([LIBUV]).
candidate 2 (found by 2 of 21 passes): Apart from being inconsistent between platforms, this makes it impossible to reliably round trip paths.

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
