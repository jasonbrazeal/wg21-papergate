Verdict: Adequate (7/14)

The paper gives a reasonably grounded account of the problem and of the design space, but it leaves several parts of the standardization case more asserted than demonstrated, particularly around who is affected and why the work belongs specifically in the standard rather than in a library.

- The strongest support comes from the concrete implementation experience, with a reference implementation available and derived from existing libstdc++ work.
- The paper also establishes meaningful prior art and alternatives, including the Unicode substitution methodology and the relationship to deprecated `codecvt` facilities.
- The case for who is affected rests on a thin signal such as GitHub stars, which does not by itself show a broad or representative user need.
- The most glaring omissions are the absence of any established discussion of coordination and interoperability, and no argument for why a library would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.67   accumulate 6.83   max 8.00

## SUMMARY
grades: motivation 1.67  audience 0.33  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 100 of 105 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.00 / 6.00   (all 3 samples: 6.67)
headings: h2 14
on threshold: motivation, implementation
splits: motivation[2] 1/0/0  motivation[6] 2/1/1  audience[9] 1/1/0  prior_art[8] 0/1/0
        vehicle[4] 1/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        1/0/0  -> 0.33
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 2/2/2  -> 2.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/0/0  -> 0.00
  [6] 5 Design Overview                            2/1/1  -> 1.33
  [7] 6 Additional Examples                        0/0/0  -> 0.00
  [8] 7 Dependencies                               0/0/0  -> 0.00
  [9] 8 Implementation Experience                  0/0/0  -> 0.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        0/0/0  -> 0.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Because virtually all UTF-8 text processed by C++ is stored in `char` (and similarly for UTF-16 and `wchar_t`), this means that we need a terse way to smooth over the transition for users.
candidate 2 (found by 2 of 45 passes): These functions throw exceptions on encountering invalid UTF. Unicode functions that use exceptions for error handling are a well-known footgun because users consistently invoke them on untrusted user input without handling the exceptions properly, leading to denial-of-service vulnerabilities.
candidate 3 (found by 1 of 45 passes): It handles errors by replacing invalid subsequences with �:
candidate 4 (found by 1 of 45 passes): There are many concerns about these interfaces, particularly with respect to safety.

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

## prior_art - grade 2.00 (fired in 7 of 15 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 2/2/2  -> 2.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 2/2/2  -> 2.00
  [6] 5 Design Overview                            2/2/2  -> 2.00
  [7] 6 Additional Examples                        1/1/1  -> 1.00
  [8] 7 Dependencies                               0/1/0  -> 0.33
  [9] 8 Implementation Experience                  1/1/1  -> 1.00
  [10] 9 Wording                                    0/0/0  -> 0.00
  [11] 10 Design Discussion and Alternatives        2/2/2  -> 2.00
  [12] 11 Changelog                                 0/0/0  -> 0.00
  [13] 12 Relevant Polls/Minutes                    0/0/0  -> 0.00
  [14] 13 Special Thanks                            0/0/0  -> 0.00
  [15] 14 References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Because it doesn’t use exceptions, the functionality proposed by this paper can serve as a safe, modern replacement for the deprecated and removed `codecvt` facets.
candidate 2 (found by 3 of 45 passes): The methodology for doing so is described in §3.9.6 of the Unicode Standard v17.0, Substitution of Maximal Subparts [[Substitution]](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/#G66453).
candidate 3 (found by 3 of 45 passes): An alternative approach to minimize the number of enumerators could merge `truncated_utf8_sequence` with `unpaired_high_surrogate` and merge `unexpected_utf8_continuation_byte` with `unpaired_low_surrogate`, but based on feedback, splitting these up seems to be preferred.
candidate 4 (found by 3 of 45 passes): Note that this depends on P4030R0 “Endian Views” for `std::views::from_big_endian`.

## vehicle - grade 0.67 (fired in 1 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 1/2/1  -> 1.33
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

## implementation - grade 2.00  [binary: max] (fired in 1 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 High-Level Overview                        0/0/0  -> 0.00
  [3] 2 UTF Primer                                 0/0/0  -> 0.00
  [4] 3 Existing Standard UTF Interfaces in C a... 0/0/0  -> 0.00
  [5] 4 Replacing Ill-Formed Subsequences with ... 0/0/0  -> 0.00
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

-->
