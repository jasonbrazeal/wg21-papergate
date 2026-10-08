Verdict: Adequate (7/14)

The paper offers meaningful support in a few important areas, particularly its motivation around exception-based error handling and its reference implementation, but it leaves several core parts of the standardization case largely unaddressed. The thinnest support concerns who is affected, how the feature coordinates with existing practice, and why a library would be insufficient.

- The strongest support is the concrete implementation experience, including a reference implementation and an experimental branch for a specific API.
- The paper also clearly establishes why the problem matters, especially the denial-of-service risks from exception-based Unicode error handling on untrusted input.
- Prior art and alternatives are reasonably covered, including the relationship to removed `codecvt` facets and the Unicode substitution methodology.
- The most glaring omission is the absence of any established discussion of who is affected, coordination and interoperability, or why a library cannot provide the functionality.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 7.00   max 8.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 101 of 105 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 6.83)
headings: h2 14
on threshold: vehicle
splits: motivation[5] 0/1/1  motivation[6] 2/2/1  motivation[11] 2/1/2  implementation[5] 0/1/0
## END SUMMARY

## motivation - grade 1.83 (fired in 4 of 15 sections, strong in 3)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 2/2/2  -> 2.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/1/1  -> 0.67
  [6] 5 Design Overview                            2/2/1  -> 1.67
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        2/1/2  -> 1.67
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): These functions throw exceptions on encountering invalid UTF. Unicode functions that use exceptions for error handling are a well-known footgun because users consistently invoke them on untrusted user input without handling the exceptions properly, leading to denial-of-service vulnerabilities.
candidate 2 (found by 3 of 45 passes): Because virtually all UTF-8 text processed by C++ is stored in `char` (and similarly for UTF-16 and `wchar_t`), this means that we need a terse way to smooth over the transition for users.
candidate 3 (found by 3 of 45 passes): To avoid this situation, the `to_utfN` CPOs reject all inputs that are arrays of `char`, as do the `as_charT` casting CPOs.
candidate 4 (found by 2 of 45 passes): When a transcoder encounters an invalid subsequence, the modern best practice is to replace it in the output with one or more � characters (`U+FFFD`, `REPLACEMENT CHARACTER`).

## audience - grade 0.00 (fired in 0 of 15 sections, strong in 0)
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

## prior_art - grade 2.00 (fired in 5 of 15 sections, strong in 2)  (SHARED PASSAGE)
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
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
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

## insufficiency - grade 0.00 (fired in 0 of 15 sections, strong in 0)
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

## implementation - grade 2.00  [binary: max] (fired in 3 of 15 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/0  -> 0.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/1/0  -> 0.33
  [6] 5 Design Overview                            0/0/0  -> 0.00
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  2/2/2  -> 2.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        2/2/2  -> 2.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): The most recent revision of this paper has a reference implementation called [beman.utf_view](https://github.com/bemanproject/utf_view) available on GitHub, which is a fork of Jonathan Wakely’s implementation of P2728R6 as an implementation detail for libstdc++.
candidate 2 (found by 3 of 45 passes): An experimental implementation of `.base_code_units()` is available on the `enolan_basecodeunits2` branch of `beman.utf_view`.
candidate 3 (found by 1 of 45 passes): Each of the proposed `to_utfN_view` views adheres to this specification.

-->
