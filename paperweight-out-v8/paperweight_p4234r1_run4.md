Verdict: Strong (10/14)

The paper offers solid support in several areas, particularly in explaining why the issue matters, surveying existing implementation practice, and showing that a standard response is preferable to leaving the behavior as a silent extension. The case is thinnest around who is concretely affected, how standardization would coordinate with other specifications and toolchains, and why a library-based solution cannot address the problem.

- The strongest support is the implementation experience section, which documents broad compiler support and includes an actual implementation attempt for the proposed approach.
- The paper also establishes why the standard should act by framing the current situation as a compliance problem rather than merely a portability nuisance.
- The affected-user argument rests mostly on a GitHub search and general claims about popularity, without showing how widespread or representative those uses are.
- The most glaring omission is the absence of any discussion of why a library solution would be insufficient, leaving that required case entirely unaddressed.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.67/14)

Provisionally addressed: 6 of 7. Provisional points: 9.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.67   corroborated 9.00   accumulate 9.83   max 11.33

## SUMMARY
grades: motivation 2.00  audience 1.17  prior_art 2.00  vehicle 1.50  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 65 of 70 section-criterion pairs unanimous (93%)
single-sample totals would have been: 10.00 / 10.00 / 9.00   (all 3 samples: 9.67)
headings: h2 9
on threshold: vehicle, coordination
splits: audience[6] 2/2/0  prior_art[5] 0/2/0  vehicle[7] 1/0/0  implementation[5] 2/0/0
        implementation[6] 2/0/0
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
candidate 1 (found by 3 of 30 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 2 (found by 3 of 30 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 3 (found by 3 of 30 passes): Unlike the other options, this gets us consistent preprocessing behavior independent of the target's capabilities rather than a silent change in meaning or a hard error.
candidate 4 (found by 2 of 30 passes): In C++ however, the situation is different. The C++ standard does not acknowledge `$` in identifiers at all. As a result, the use of `$` in identifiers pedantically renders your code ill-formed.

## audience - grade 1.17 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/0  -> 1.33
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 2 (found by 2 of 30 passes): [GitHub search](https://github.com/search?q=%22%23define+%24%22+language%3AC%2B%2B&type=code) finds more than 5600 uses in code recognized as C++.
candidate 3 (found by 1 of 30 passes): due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           0/2/0  -> 0.67
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In C++ however, the situation is different. The C++ standard does not acknowledge `$` in identifiers at all.
candidate 2 (found by 3 of 30 passes): The authors prefer option 3 as it is the least user-hostile option. Unlike the other options, this gets us consistent preprocessing behavior independent of the target's capabilities rather than a silent change in meaning or a hard error.
candidate 3 (found by 2 of 30 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code
candidate 4 (found by 1 of 30 passes): [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) mentions that during discussion it was noted that allowing `$` in identifiers is a massive syntactic land-grab.

## vehicle - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Preprocessing                             1/0/0  -> 0.33
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 2 (found by 2 of 30 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 1 of 30 passes): To align with C and implementation reality, this paper proposes making the use of `$` in identifiers conditionally-supported.
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

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     0/0/0  -> 0.00
  [7] 4. Preprocessing                             0/0/0  -> 0.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/2/2  -> 2.00
  [5] 2. Proposed change                           2/0/0  -> 0.67
  [6] 3. Additional Motivation                     2/0/0  -> 0.67
  [7] 4. Preprocessing                             2/2/2  -> 2.00
  [8] 5. Wording                                   0/0/0  -> 0.00
  [9] 6. Acknowledgements                          0/0/0  -> 0.00
  [10] 7. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Amongst many other compilers this is supported by MSVC, GCC (going back to at least GCC 1.27), Clang, EDG (might need opt-in), icx and nvc++ (see Compiler Explorer).
candidate 2 (found by 3 of 30 passes): An implementation attempt for option 3 can be found at [Clang PR #200614](https://github.com/llvm/llvm-project/pull/200614).
candidate 3 (found by 1 of 30 passes): GCC notes in its [documentation](https://gcc.gnu.org/onlinedocs/gcc/Dollar-Signs.html):
candidate 4 (found by 1 of 30 passes): [For example](https://github.com/lvgl/lv_port_raspberry_pi_pico_mdk/blob/cfa86618e87b9d62afc56db8aabdaa5d192aa67d/project/mdk/wrapper/pico/platform.h#L406), RP2040 MDK headers define the following wrapper macros:

-->
