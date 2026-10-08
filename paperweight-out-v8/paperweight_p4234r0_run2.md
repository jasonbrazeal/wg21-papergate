Verdict: Strong (10/14)

The paper offers solid evidence that `$` in identifiers is a widely implemented, long-standing extension, but it is much thinner when it comes to showing who is concretely affected and why standardization, rather than continued use of the extension, is necessary. The weakest parts concern the absence of any argument that a library solution is impossible and the largely asserted, rather than demonstrated, claims about affected users and compliance pressure.

- The strongest support is the implementation experience, with named major compilers and documented historical support for `$` in identifiers.
- The paper also establishes prior art through WG14 N3145 and existing compiler mechanisms such as explicit assembler names.
- The case for why the standard must act rests mainly on general assertions about compliance and popularity rather than demonstrated need.
- The most glaring omission is the complete lack of discussion of why a library or other non-core-language approach would not address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.50/14)

Provisionally addressed: 6 of 7. Provisional points: 9.50 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.50   corroborated 9.00   accumulate 10.00   max 11.33

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.33  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 10.00 / 9.50 / 9.50   (all 3 samples: 9.50)
headings: h2 8
on threshold: vehicle, coordination, implementation
splits: audience[6] 2/2/0  prior_art[6] 2/0/2  vehicle[5] 1/0/1  implementation[5] 2/0/2
        implementation[6] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           2/2/2  -> 2.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In C++ however, the situation is different. The C++ standard does not acknowledge `$` in identifiers at all. As a result, the use of `$` in identifiers pedantically renders your code ill-formed.
candidate 2 (found by 3 of 27 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 3 of 27 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.

## audience - grade 1.17 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/0  -> 1.33
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): One of the oldest and most widely supported extensions to C++ is allowing `$` in identifiers.
candidate 2 (found by 2 of 27 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 2 of 27 passes): [GitHub search](https://github.com/search?q=%22%23define+%24%22+language%3AC%2B%2B&type=code) finds more than 5600 uses in code recognized as C++.
candidate 4 (found by 1 of 27 passes): due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.

## prior_art - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           2/2/2  -> 2.00
  [6] 3. Additional Motivation                     2/0/2  -> 1.33
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): To address this, [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) introduced a carve-out to allow `$` anywhere in identifiers as an implementation extension.
candidate 2 (found by 3 of 27 passes): [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) mentions that during discussion it was noted that allowing `$` in identifiers is a massive syntactic land-grab.
candidate 3 (found by 2 of 27 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code ([Compiler Explorer](https://compiler-explorer.com/z/WE8TzTsav))

## vehicle - grade 1.33 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/0/1  -> 0.67
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 2 (found by 2 of 27 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.

## coordination - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Some embedded toolchains expose identifiers containing `$` through linker-defined symbols and custom linker conventions.

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/0/0  -> 0.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           2/0/2  -> 1.33
  [6] 3. Additional Motivation                     2/0/0  -> 0.67
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Amongst many other compilers this is supported by MSVC, GCC (going back to at least GCC 1.27), Clang, EDG (might need opt-in), icx and nvc++ (see Compiler Explorer).
candidate 2 (found by 1 of 27 passes): GCC notes in its [documentation](https://gcc.gnu.org/onlinedocs/gcc/Dollar-Signs.html):
candidate 3 (found by 1 of 27 passes): GCC notes in its [documentation](https://gcc.gnu.org/onlinedocs/gcc/Dollar-Signs.html): > However, dollar signs in identifiers are not supported on a few target machines, typically because the target assembler does not allow them.
candidate 4 (found by 1 of 27 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code ([Compiler Explorer](https://compiler-explorer.com/z/WE8TzTsav))

-->
