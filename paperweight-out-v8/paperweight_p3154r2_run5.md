Verdict: Adequate (5/14)

The paper offers a narrow but genuine foundation for its case, centered on the surprising treatment of `signed char` and `unsigned char` as characters rather than integers, and it points to relevant prior art in `std::format` and the C++20 stream signature change. Beyond that, however, the support thins quickly: the paper does not establish why standardization is necessary, how it would coordinate with existing practice, why a library solution is insufficient, or that there is implementation experience behind the proposal.

- The strongest support is the clear demonstration that current stream insertion and extraction behavior for `signed char` and `unsigned char` is surprising and inconsistent with their status as integer types.
- The paper also credibly cites `std::format` and the C++20 `operator>>` signature change as relevant prior art and precedent.
- The claim about who is affected rests on a very small study of open source code, and the paper itself notes that only four instances of use were found, which leaves the impact largely unestablished.
- The most glaring omission is the absence of any case for why the standard is the right venue, why a library cannot address the problem, or how the change would interoperate with existing code and implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 3 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 5.00   accumulate 4.67   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 5.00 / 4.00 / 5.00   (all 3 samples: 4.67)
headings: h2 6
on threshold: none
splits: audience[5] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Impact                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This behavior is unexpected, especially when using the aliases `int8_t` or `uint8_t`.
candidate 2 (found by 2 of 21 passes): This is surprising.
candidate 3 (found by 2 of 21 passes): It’s easy to find counter-examples, however, where workarounds have to be employed to insert or extract `signed char`s or `unsigned char`s as integers.
candidate 4 (found by 1 of 21 passes): This is surprising. Per [[basic.fundamental](https://eel.is/c++draft/basic.fundamental#1)] p1 and p2: ... Thus, `signed char` and `unsigned char` should be treated as integers, not as characters.

## audience - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Impact                                    2/0/2  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): To gauge the potential impact of this deprecation, the author tried building open source C++ code bases, using a patched version of libc++.
candidate 2 (found by 1 of 21 passes): Only four instances of use were found during this study, which is not a lot.

## prior_art - grade 2.00 (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Impact                                    2/2/2  -> 2.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): `std::format` has already taken a step in the right direction here, by treating `signed char` and `unsigned char` as integers.
candidate 2 (found by 3 of 21 passes): The signature of `operator>>` for `basic_istream` was updated for C++20 in [P0487R1], where these functions were changed to take `T (&)[N]` instead of `T*`, for safety reasons.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Impact                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Impact                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Impact                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Impact                                    0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
