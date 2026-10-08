Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing `$` in identifiers, particularly through its evidence of widespread implementation practice and the practical portability and compliance problems created by leaving the feature formally undefined. The case is thinnest where it reaches beyond the core language change: the claims about tooling simplification and embedded linker-defined symbols gesture at broader benefits but are not backed by concrete evidence, and the discussion of alternatives to standardization is more asserted than demonstrated.

- The strongest support is the implementation experience, with named compilers, historical depth, and a linked implementation attempt showing that the feature is already broadly and durably available.
- The paper also clearly establishes why the issue matters and who is affected, grounded in the near-universal default support and the real compliance burden in constrained environments.
- The weakest established area is coordination and interoperability, where the paper claims benefits for tooling and embedded toolchains but does not substantiate them with examples or evidence.
- The most glaring omission is the failure to establish why a library-level or source-level workaround will not do, since the only cited alternative is dismissed without a developed argument.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.50/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.50 of 14. Unsupported quotes rejected: 10. Replies missing: 0. Sections: 13. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.50   corroborated 10.33   accumulate 11.00   max 11.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.50  coordination 0.83  insufficiency 0.17  implementation 2.00
sample agreement: 81 of 91 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.50 / 10.50 / 11.50   (all 3 samples: 10.50)
headings: h2 12
on threshold: vehicle
splits: motivation[8] 2/2/1  audience[6] 2/0/0  prior_art[4] 0/0/2  vehicle[7] 1/1/0
        vehicle[8] 1/1/0  coordination[6] 0/2/2  coordination[7] 0/0/1  insufficiency[6] 0/0/1
        implementation[5] 1/0/0  implementation[6] 0/0/2
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
  [8] 5. Other approaches                          2/2/1  -> 1.67
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): In C++, the situation is slightly different. The C++ standard does not acknowledge `$` in identifiers at all. As a result, the use of `$` in identifiers pedantically renders your code ill-formed.
candidate 2 (found by 3 of 39 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 3 of 39 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 4 (found by 3 of 39 passes): Unlike the other options, this gets us consistent preprocessing behavior independent of the target's capabilities rather than a silent change in meaning or a hard error.

## audience - grade 2.00 (fired in 6 of 13 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/0/0  -> 0.67
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Other approaches                          1/1/1  -> 1.00
  [9] 6. Implementation status                     2/2/2  -> 2.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): One of the oldest and most widely supported extensions to C++ is allowing `$` in identifiers.
candidate 2 (found by 3 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.
candidate 3 (found by 3 of 39 passes): A search for `-fno-dollars-in-identifiers` in CMake files yields [only 26 results](https://github.com/search?q=-fno-dollars-in-identifiers+language%3Acmake&type=code) at the time of writing.
candidate 4 (found by 2 of 39 passes): due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.

## prior_art - grade 2.00 (fired in 6 of 13 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/2  -> 0.67
  [5] 2. Proposed change                           2/2/2  -> 2.00
  [6] 3. Additional Motivation                     0/0/0  -> 0.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Other approaches                          2/2/2  -> 2.00
  [9] 6. Implementation status                     1/1/1  -> 1.00
  [10] 7. Opt-out usage                             2/2/2  -> 2.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) mentions that during discussion it was noted that allowing `$` in identifiers is a massive syntactic land-grab.
candidate 2 (found by 3 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.
candidate 3 (found by 3 of 39 passes): With all tested compilers except for NVC++ (which does not seem to have an opt-out), the observed behavior when opting out matches wording option 1.
candidate 4 (found by 3 of 39 passes): The inspected uses therefore provide evidence for preserving assembly-specific preprocessing behavior, but do not demonstrate a need to opt-out of `$`identifiers in C++ mode.

## vehicle - grade 1.50 (fired in 4 of 13 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             1/1/0  -> 0.67
  [8] 5. Other approaches                          1/1/0  -> 0.67
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 3 of 39 passes): Conditionally-supported would not make `$` in identifiers portable, but it would at least make them explicitly recognized by the standard when supported by the implementation.
candidate 2 (found by 3 of 39 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 3 (found by 2 of 39 passes): This also simplifies tooling such as syntax highlighters greatly as they no longer have to be aware of target capabilities in order to tokenize correctly.
candidate 4 (found by 1 of 39 passes): Since almost all compilers support `$` in identifiers in C++ mode by default, this would imply next to no changes to implementations if they wish to remain conforming.

## coordination - grade 0.83 (fired in 2 of 13 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/2/2  -> 1.33
  [7] 4. Preprocessing                             0/0/1  -> 0.33
  [8] 5. Other approaches                          0/0/0  -> 0.00
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 2 of 39 passes): Some embedded toolchains expose identifiers containing `$` through linker-defined symbols and custom linker conventions.
candidate 2 (found by 1 of 39 passes): This also simplifies tooling such as syntax highlighters greatly as they no longer have to be aware of target capabilities in order to tokenize correctly.

## insufficiency - grade 0.17 (fired in 1 of 13 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/0/1  -> 0.33
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Other approaches                          0/0/0  -> 0.00
  [9] 6. Implementation status                     0/0/0  -> 0.00
  [10] 7. Opt-out usage                             0/0/0  -> 0.00
  [11] 8. Wording                                   0/0/0  -> 0.00
  [12] 9. Acknowledgements                          0/0/0  -> 0.00
  [13] 10. References                               0/0/0  -> 0.00
candidate 1 (found by 1 of 39 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code

## implementation - grade 2.00  [binary: max] (fired in 7 of 13 sections, strong in 5)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           1/0/0  -> 0.33
  [6] 3. Additional Motivation                     0/0/2  -> 0.67
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
