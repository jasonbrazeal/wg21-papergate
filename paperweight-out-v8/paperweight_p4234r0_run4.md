Verdict: Strong (10/14)

The paper gives a reasonably solid account of why `$` in identifiers is a real-world compatibility issue and why standardization is the appropriate venue, but it leaves a noticeable gap around whether a non-library solution is actually necessary and does not fully substantiate its claims about coordination and interoperability.

- The strongest support is the implementation experience section, which names multiple major compilers and points to concrete embedded toolchain usage.
- The paper also clearly establishes why the issue matters and who is affected, including evidence of widespread existing use.
- The case for why the standard should address this is made mainly through the compliance and C-alignment arguments.
- The most glaring omission is the absence of any argument for why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.83/14)

Provisionally addressed: 6 of 7. Provisional points: 9.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.83   corroborated 8.00   accumulate 10.67   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 1.67  vehicle 1.50  coordination 1.17  insufficiency 0.00  implementation 2.00
sample agreement: 58 of 63 section-criterion pairs unanimous (92%)
single-sample totals would have been: 10.00 / 10.50 / 10.00   (all 3 samples: 9.83)
headings: h2 8
on threshold: audience, prior_art, vehicle, coordination, implementation
splits: prior_art[4] 2/1/1  prior_art[5] 0/2/2  coordination[4] 0/1/0  implementation[5] 1/1/0
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

## audience - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              1/1/1  -> 1.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): One of the oldest and most widely supported extensions to C++ is allowing `$` in identifiers.
candidate 2 (found by 3 of 27 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.
candidate 3 (found by 3 of 27 passes): [GitHub search](https://github.com/search?q=%22%23define+%24%22+language%3AC%2B%2B&type=code) finds more than 5600 uses in code recognized as C++.

## prior_art - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              2/1/1  -> 1.33
  [5] 2. Proposed change                           0/2/2  -> 1.33
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): With GCC and Clang this can also be addressed by explicitly specifying the name used in assembler code
candidate 2 (found by 2 of 27 passes): In recent years, C has made quite a few changes to what they consider an identifier.
candidate 3 (found by 2 of 27 passes): [[WG14 N3145]](https://www%2eopen-std%2eorg/jtc1/sc22/wg14/www/docs/n3145%2epdf) mentions that during discussion it was noted that allowing `$` in identifiers is a massive syntactic land-grab.
candidate 4 (found by 1 of 27 passes): In C++ however, the situation is different. The C++ standard does not acknowledge `$` in identifiers at all.

## vehicle - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/0/0  -> 0.00
  [5] 2. Proposed change                           1/1/1  -> 1.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In such environments, using a compiler extension is not merely an engineering portability concern. It can become a compliance issue.
candidate 2 (found by 2 of 27 passes): To align with C and implementation reality, this paper proposes making the use of `$` in identifiers conditionally-supported.
candidate 3 (found by 1 of 27 passes): However, due to the popularity of this extension, it seems unrealistic that we can ever use `$` for anything that would conflict with `$identifiers`.

## coordination - grade 1.17 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision history                             0/0/0  -> 0.00
  [4] 1. Introduction                              0/1/0  -> 0.33
  [5] 2. Proposed change                           0/0/0  -> 0.00
  [6] 3. Additional Motivation                     2/2/2  -> 2.00
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Some embedded toolchains expose identifiers containing `$` through linker-defined symbols and custom linker conventions.
candidate 2 (found by 1 of 27 passes): In practice, however, almost all implementations support it as a non-standard extension.

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
  [5] 2. Proposed change                           1/1/0  -> 0.67
  [6] 3. Additional Motivation                     2/0/0  -> 0.67
  [7] 4. Wording                                   0/0/0  -> 0.00
  [8] 5. Acknowledgements                          0/0/0  -> 0.00
  [9] 6. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Amongst many other compilers this is supported by MSVC, GCC (going back to at least GCC 1.27), Clang, EDG (might need opt-in), icx and nvc++ (see Compiler Explorer).
candidate 2 (found by 2 of 27 passes): To align with C and implementation reality, this paper proposes making the use of `$` in identifiers conditionally-supported.
candidate 3 (found by 1 of 27 passes): [For example](https://github.com/lvgl/lv_port_raspberry_pi_pico_mdk/blob/cfa86618e87b9d62afc56db8aabdaa5d192aa67d/project/mdk/wrapper/pico/platform.h#L406), RP2040 MDK headers define the following wrapper macros:

-->
