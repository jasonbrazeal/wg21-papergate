Verdict: Adequate (6/14)

The paper offers a mixed case for its own standardization, with solid grounding in implementation experience and prior art but much thinner support for the broader need, affected audience, and role of the standard. The most persistent weakness is that several distinct requirements lean on the same brief claim about replacing `codecvt`, without developing the argument for why standardization, rather than a library, is necessary.

- The strongest support is implementation experience, with a reference implementation and a fork of an existing implementation credited as evidence.
- Prior art and alternatives are also established, including the Unicode substitution methodology and discussion of enumerator design choices.
- The case for why the problem matters, who is affected, why the standard is the right venue, and why a library will not suffice is only asserted, often through a single repeated rationale.
- Coordination and interoperability with related standardization work is not established at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 7.00   accumulate 6.50   max 8.00

## SUMMARY
grades: motivation 0.83  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 99 of 105 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 6.50 / 6.00   (all 3 samples: 6.33)
headings: h2 14
on threshold: vehicle, implementation
splits: motivation[5] 0/1/0  motivation[11] 1/1/0  audience[9] 1/1/0  prior_art[12] 1/0/0
        insufficiency[4] 0/0/1  implementation[5] 1/0/0
## END SUMMARY

## motivation - grade 0.83 (fired in 3 of 15 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/0  -> 0.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/1/0  -> 0.33
  [6] 5 Design Overview                            1/1/1  -> 1.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        1/1/0  -> 0.67
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Because virtually all UTF-8 text processed by C++ is stored in `char` (and similarly for UTF-16 and `wchar_t`), this means that we need a terse way to smooth over the transition for users.
candidate 2 (found by 2 of 45 passes): To avoid this situation, the `to_utfN` CPOs reject all inputs that are arrays of `char`, as do the `as_charT` casting CPOs.
candidate 3 (found by 1 of 45 passes): When a transcoder encounters an invalid subsequence, the modern best practice is to replace it in the output with one or more � characters (`U+FFFD`, `REPLACEMENT CHARACTER`).

## audience - grade 0.33 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/0  -> 0.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/0/0  -> 0.00
  [6] 5 Design Overview                            0/0/0  -> 0.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  1/1/0  -> 0.67
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): Boost.Text has hundreds of stars on GitHub.

## prior_art - grade 2.00 (fired in 7 of 15 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 2/2/2  -> 2.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 1/1/1  -> 1.00
  [6] 5 Design Overview                            2/2/2  -> 2.00
  [7] 6 Additional Examples                        1/1/1  -> 1.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        2/2/2  -> 2.00
  [12] 11 Changelog                                 1/0/0  -> 0.33
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Because it doesn’t use exceptions, the functionality proposed by this paper can serve as a safe, modern replacement for the deprecated and removed `codecvt` facets.
candidate 2 (found by 3 of 45 passes): The methodology for doing so is described in §3.9.6 of the Unicode Standard v17.0, Substitution of Maximal Subparts [[Substitution]](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G66453).
candidate 3 (found by 3 of 45 passes): An alternative approach to minimize the number of enumerators could merge `truncated_utf8_sequence` with `unpaired_high_surrogate` and merge `unexpected_utf8_continuation_byte` with `unpaired_low_surrogate`, but based on feedback, splitting these up seems to be preferred.
candidate 4 (found by 3 of 45 passes): Note that this depends on P4030R0 “Endian Views” for `std::views::from_big_endian`.

## vehicle - grade 1.00 (fired in 1 of 15 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 2/2/2  -> 2.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/0/0  -> 0.00
  [6] 5 Design Overview                            0/0/0  -> 0.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Because it doesn’t use exceptions, the functionality proposed by this paper can serve as a safe, modern replacement for the deprecated and removed `codecvt` facets.

## coordination - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/0  -> 0.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/0/0  -> 0.00
  [6] 5 Design Overview                            0/0/0  -> 0.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.17 (fired in 1 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/1  -> 0.33
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/0/0  -> 0.00
  [6] 5 Design Overview                            0/0/0  -> 0.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): Because it doesn’t use exceptions, the functionality proposed by this paper can serve as a safe, modern replacement for the deprecated and removed `codecvt` facets.

## implementation - grade 2.00  [binary: max] (fired in 2 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/0  -> 0.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 1/0/0  -> 0.33
  [6] 5 Design Overview                            0/0/0  -> 0.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  2/2/2  -> 2.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The most recent revision of this paper has a reference implementation called [beman.utf_view](https://github.com/bemanproject/utf_view) available on GitHub, which is a fork of Jonathan Wakely’s implementation of P2728R6 as an implementation detail for libstdc++.
candidate 2 (found by 1 of 45 passes): Each of the proposed `to_utfN_view` views adheres to this specification.

-->
