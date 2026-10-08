Verdict: Strong (10/14)

The paper offers a solid foundation for why `$` in identifiers deserves standardization attention, particularly through its discussion of implementation reality and the limits of treating this as a mere compiler extension. The support is thinnest when it comes to demonstrating who is concretely affected and why existing mechanisms cannot address the problem.

- The strongest support comes from the implementation experience section, which names multiple major compilers and even points to a concrete Clang implementation attempt.
- The paper clearly establishes why the standard should engage with this issue, noting that the extension's popularity makes future conflicting uses of `$` unrealistic.
- The discussion of prior art and alternatives is well grounded, especially in its reference to WG14 N3145 and the recognition that allowing `$` is a significant syntactic commitment.
- The most glaring omission is the lack of established evidence about who is affected, since the GitHub search and general popularity claims do not by themselves demonstrate a standardization need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 7 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 9.33   accumulate 10.50   max 11.67

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.50  coordination 1.00  insufficiency 0.17  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 9.50 / 10.00 / 10.50   (all 3 samples: 9.83)
headings: h2 9
on threshold: vehicle, coordination
splits: audience[6] 0/2/2  prior_art[5] 2/0/2  vehicle[7] 0/1/0  insufficiency[6] 0/0/1
        implementation[5] 0/0/1  implementation[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           2/2/2  -> 2.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In C++ however, the situation is different. The C++ standard does not acknowledge `$` in identifiers at all. As a result, the use of `$` in identifiers pedantically renders your code ill-formed.
candidate 2 (found by 3 of 30 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 3 of 30 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 4 (found by 2 of 30 passes): Unlike the other options, this gets us consistent preprocessing behavior independent of the target's capabilities rather than a silent change in meaning or a hard error.

## audience - grade 1.17 (fired in 3 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     0/2/2  -> 1.33
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): One of the oldest and most widely supported extensions to C++ is allowing `$` in identifiers.
candidate 2 (found by 3 of 30 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 2 of 30 passes): [GitHub search](https://github.com/search?q=%22%23define+%24%22+language%3AC%2B%2B&type=code) finds more than 5600 uses in code recognized as C++.

## prior_art - grade 2.00 (fired in 3 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           2/0/2  -> 1.33
  [6] 3. Additional Motivation                     0/0/0  -> 0.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In C++ however, the situation is different. The C++ standard does not acknowledge `$` in identifiers at all.
candidate 2 (found by 3 of 30 passes): The authors prefer option 3 as it is the least user-hostile option. Unlike the other options, this gets us consistent preprocessing behavior independent of the target's capabilities rather than a silent change in meaning or a hard error.
candidate 3 (found by 2 of 30 passes): [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) mentions that during discussion it was noted that allowing `$` in identifiers is a massive syntactic land-grab.

## vehicle - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             0/1/0  -> 0.33
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 2 (found by 2 of 30 passes): However, it would change the status of the construct from an unstandardized implementation extension into a construct explicitly recognized by the C++ Standard, when supported by the implementation.
candidate 3 (found by 1 of 30 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 4 (found by 1 of 30 passes): The authors prefer option 3 as it is the least user-hostile option.

## coordination - grade 1.00 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Some embedded toolchains expose identifiers containing `$` through linker-defined symbols and custom linker conventions.

## insufficiency - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/0/1  -> 0.33
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): However, it would change the status of the construct from an unstandardized implementation extension into a construct explicitly recognized by the C++ Standard, when supported by the implementation.

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           0/0/1  -> 0.33
  [6] 3. Additional Motivation                     2/0/0  -> 0.67
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Amongst many other compilers this is supported by MSVC, GCC (going back to at least GCC 1.27), Clang, EDG (might need opt-in), icx and nvc++ (see Compiler Explorer).
candidate 2 (found by 3 of 30 passes): An implementation attempt for option 3 can be found at [Clang PR #200614](https://github.com/llvm/llvm-project/pull/200614).
candidate 3 (found by 1 of 30 passes): To align with C and implementation reality, this paper proposes making the use of `$` in identifiers conditionally-supported.
candidate 4 (found by 1 of 30 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code ([Compiler Explorer](https://compiler-explorer.com/z/WE8TzTsav))

-->
