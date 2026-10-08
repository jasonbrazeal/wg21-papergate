Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing `$` in identifiers, with its strongest evidence coming from implementation experience, demonstrated compiler behavior, and clear documentation of real-world usage and affected users. The case is thinnest where it needs to show why standardization—rather than continued reliance on the existing extension—is necessary, and it offers no argument at all for why a library solution would be inadequate.

- The paper most convincingly establishes implementation experience through a Clang implementation attempt, compiler explorer demonstrations across targets, and evidence that opt-out flags are rarely used in practice.
- It clearly establishes who is affected and why the issue matters, citing thousands of GitHub matches and the practical impossibility of repurposing `$` without breaking existing code.
- The paper documents prior art and alternatives well, including assembler-name workarounds and a comparison of conditional wording options against observed compiler behavior.
- The most glaring omission is the absence of any discussion of why a library-based approach cannot address the need, leaving that requirement entirely unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 6 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 10.00   accumulate 11.83   max 12.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.33  coordination 1.67  insufficiency 0.00  implementation 2.00
sample agreement: 79 of 91 section-criterion pairs unanimous (87%)
single-sample totals would have been: 11.50 / 11.00 / 11.50   (all 3 samples: 11.00)
headings: h2 12
on threshold: vehicle, coordination
splits: motivation[5] 1/2/1  audience[4] 0/1/0  audience[8] 0/1/1  prior_art[4] 2/2/0
        prior_art[5] 0/0/2  vehicle[5] 0/1/1  vehicle[7] 1/0/1  vehicle[8] 0/1/0
        coordination[4] 2/1/1  coordination[7] 0/0/2  implementation[5] 0/1/0
        implementation[6] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           1/2/1  -> 1.33
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Other approaches                          2/2/2  -> 2.00
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 2 (found by 3 of 39 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 3 (found by 3 of 39 passes): Unlike the other options, this gets us consistent preprocessing behavior independent of the target's capabilities rather than a silent change in meaning or a hard error.
candidate 4 (found by 3 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.

## audience - grade 2.00 (fired in 6 of 13 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/1/0  -> 0.33
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Other approaches                          0/1/1  -> 0.67
  [9] 6. Implementation status                     2/2/2  -> 2.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 2 (found by 3 of 39 passes): [GitHub search](https://github.com/search?q=%22%23define+%24%22+language%3AC%2B%2B&type=code) finds more than 5600 uses in code recognized as C++.
candidate 3 (found by 3 of 39 passes): With all tested compilers except for NVC++ (which does not seem to have an opt-out), the observed behavior when opting out matches wording option 1.
candidate 4 (found by 3 of 39 passes): A search for `-fno-dollars-in-identifiers` in CMake files yields [only 26 results](https://github.com/search?q=-fno-dollars-in-identifiers+language%3Acmake&type=code) at the time of writing.

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/0  -> 1.33
  [5] 2. Proposed change                           0/0/2  -> 0.67
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Other approaches                          2/2/2  -> 2.00
  [9] 6. Implementation status                     1/1/1  -> 1.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code
candidate 2 (found by 3 of 39 passes): Among the conditional approaches, the authors prefer option 3 over options 1 and 2, as it is the least user-hostile option.
candidate 3 (found by 3 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.
candidate 4 (found by 3 of 39 passes): With all tested compilers except for NVC++ (which does not seem to have an opt-out), the observed behavior when opting out matches wording option 1.

## vehicle - grade 1.33 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/1/1  -> 0.67
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             1/0/1  -> 0.67
  [8] 5. Other approaches                          0/1/0  -> 0.33
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 2 (found by 2 of 39 passes): This also simplifies tooling such as syntax highlighters greatly as they no longer have to be aware of target capabilities in order to tokenize correctly.
candidate 3 (found by 1 of 39 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 4 (found by 1 of 39 passes): To align with C and implementation reality, this paper proposes making the use of `$` in identifiers conditionally-supported or supported.

## coordination - grade 1.67 (fired in 3 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/1/1  -> 1.33
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             0/0/2  -> 0.67
  [8] 5. Other approaches                          0/0/0  -> 0.00
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In practice, however, almost all implementations support it as a non-standard extension, which was a conforming extension until C++26.
candidate 2 (found by 3 of 39 passes): Some embedded toolchains expose identifiers containing `$` through linker-defined symbols and custom linker conventions.
candidate 3 (found by 1 of 39 passes): This also simplifies tooling such as syntax highlighters greatly as they no longer have to be aware of target capabilities in order to tokenize correctly.

## insufficiency - grade 0.00 (fired in 0 of 13 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/0/0  -> 0.00
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Other approaches                          0/0/0  -> 0.00
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 7 of 13 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           0/1/0  -> 0.33
  [6] 3. Additional Motivation                     0/0/2  -> 0.67
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Other approaches                          2/2/2  -> 2.00
  [9] 6. Implementation status                     2/2/2  -> 2.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): An implementation attempt for option 3 can be found at [Clang PR #200614](https://github.com/llvm/llvm-project/pull/200614).
candidate 2 (found by 3 of 39 passes): As demonstrated by Clang, some targets excluded by GCC (such as RS/6000) have no fundamental issue with `$` in identifiers (see [Compiler Explorer](https://godbolt.org/z/5eMKWKaEs)).
candidate 3 (found by 3 of 39 passes): An overview can be found on [Compiler Explorer](https://godbolt.org/z/99sbb7hrT).
candidate 4 (found by 3 of 39 passes): A search for `-fno-dollars-in-identifiers` in CMake files yields [only 26 results](https://github.com/search?q=-fno-dollars-in-identifiers+language%3Acmake&type=code) at the time of writing.

-->
