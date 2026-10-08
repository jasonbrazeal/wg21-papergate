Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing `$` in identifiers, particularly through its account of widespread implementation experience, practical impact, and the limits of leaving the extension unacknowledged. The case is thinnest where it needs to show that a library solution cannot address the problem and where coordination with embedded toolchains and system libraries is asserted rather than demonstrated.

- The strongest support comes from concrete implementation evidence across major compilers and a working Clang patch for the preferred wording option.
- The paper clearly establishes why the extension matters to affected users and why conditional support in the standard would be preferable to the status quo.
- The discussion of prior art and alternatives is well grounded, including the syntactic land-grab concern and comparison of conditional approaches.
- The most glaring omission is the absence of any argument for why a library-based approach would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 6 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 10.00   accumulate 11.83   max 12.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.50  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 85 of 91 section-criterion pairs unanimous (93%)
single-sample totals would have been: 11.00 / 11.00 / 11.50   (all 3 samples: 10.83)
headings: h2 12
on threshold: vehicle, coordination
splits: prior_art[4] 0/0/2  prior_art[6] 2/0/2  vehicle[8] 1/1/0  coordination[4] 1/1/0
        coordination[7] 1/0/0  coordination[10] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 13 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
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
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Other approaches                          1/1/1  -> 1.00
  [9] 6. Implementation status                     2/2/2  -> 2.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): One of the oldest and most widely supported extensions to C++ is allowing `$` in identifiers.
candidate 2 (found by 3 of 39 passes): due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 3 of 39 passes): [GitHub search](https://github.com/search?q=%22%23define+%24%22+language%3AC%2B%2B&type=code) finds more than 5600 uses in code recognized as C++.
candidate 4 (found by 3 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.

## prior_art - grade 2.00 (fired in 7 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/2  -> 0.67
  [5] 2. Proposed change                           2/2/2  -> 2.00
  [6] 3. Additional Motivation                     2/0/2  -> 1.33
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Other approaches                          2/2/2  -> 2.00
  [9] 6. Implementation status                     1/1/1  -> 1.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) mentions that during discussion it was noted that allowing `$` in identifiers is a massive syntactic land-grab.
candidate 2 (found by 3 of 39 passes): Among the conditional approaches, the authors prefer option 3 over options 1 and 2, as it is the least user-hostile option.
candidate 3 (found by 3 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.
candidate 4 (found by 3 of 39 passes): With all tested compilers except for NVC++ (which does not seem to have an opt-out), the observed behavior when opting out matches wording option 1.

## vehicle - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             1/1/1  -> 1.00
  [8] 5. Other approaches                          1/1/0  -> 0.67
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Conditionally-supported would not make `$` in identifiers portable, but it would at least make them explicitly recognized by the standard when supported by the implementation.
candidate 2 (found by 3 of 39 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 3 (found by 3 of 39 passes): This also simplifies tooling such as syntax highlighters greatly as they no longer have to be aware of target capabilities in order to tokenize correctly.
candidate 4 (found by 2 of 39 passes): acknowledging extensions as conditionally supported is preferable to leaving them as unstandardized implementation extensions.

## coordination - grade 1.33 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/0  -> 0.67
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             1/0/0  -> 0.33
  [8] 5. Other approaches                          0/0/0  -> 0.00
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/2  -> 0.67
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Some embedded toolchains expose identifiers containing `$` through linker-defined symbols and custom linker conventions.
candidate 2 (found by 2 of 39 passes): In practice, however, almost all implementations support it as a non-standard extension, which was a conforming extension until C++26.
candidate 3 (found by 1 of 39 passes): This also simplifies tooling such as syntax highlighters greatly as they no longer have to be aware of target capabilities in order to tokenize correctly.
candidate 4 (found by 1 of 39 passes): Apple patches libstdc++v3 with additional support for dtrace. These dtrace symbols use dollar signs identifiers, and are incompatible with the compile option -fno-dollars-in-identifiers.

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

## implementation - grade 2.00  [binary: max] (fired in 5 of 13 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/0/0  -> 0.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Other approaches                          2/2/2  -> 2.00
  [9] 6. Implementation status                     2/2/2  -> 2.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Amongst many other compilers this is supported by MSVC, GCC (going back to at least GCC 1.27), Clang, EDG (might need opt-in), icx and nvc++ (see Compiler Explorer).
candidate 2 (found by 3 of 39 passes): An implementation attempt for option 3 can be found at [Clang PR #200614](https://github.com/llvm/llvm-project/pull/200614).
candidate 3 (found by 3 of 39 passes): As demonstrated by Clang, some targets excluded by GCC (such as RS/6000) have no fundamental issue with `$` in identifiers (see [Compiler Explorer](https://godbolt.org/z/5eMKWKaEs)).
candidate 4 (found by 3 of 39 passes): An overview can be found on [Compiler Explorer](https://godbolt.org/z/99sbb7hrT).

-->
