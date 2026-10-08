Verdict: Excellent (14/14)

The paper offers substantial support for its own standardization, with every major category of need marked as established and backed by concrete evidence from implementation experience, user impact, and prior art. The support is broad rather than thin, though the case leans heavily on the deficiencies of existing practice and the momentum of P2900 implementations rather than on novel argumentation.

- The strongest support comes from implementation experience, where complete forks of GCC and Clang, upstreaming progress, and real-world adoption through Boost.Build demonstrate that the proposal is already viable in practice.
- The paper also convincingly establishes why a library solution will not do, showing that the semantics require language-level integration and that macro-based alternatives create fragmentation and IFNDR risks.
- The case for coordination and interoperability is well made, particularly through the argument that consistent contract-evaluation semantics across transitive dependencies are infeasible without a standard mechanism.
- The thinnest area is the reliance on prior art and alternatives, where the paper mostly cites concerns and criticisms of P2900 rather than presenting a fully developed comparison of alternative designs that were considered and rejected.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Excellent (14.00/14)

Provisionally addressed: 7 of 7. Provisional points: 14.00 of 14. Unsupported quotes rejected: 32. Replies missing: 0. Sections: 90. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 14.00   corroborated 14.00   accumulate 14.00   max 14.00

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 2.00  coordination 2.00  insufficiency 2.00  implementation 2.00
sample agreement: 569 of 630 section-criterion pairs unanimous (90%)
single-sample totals would have been: 14.00 / 14.00 / 14.00   (all 3 samples: 14.00)
headings: h2 89
on threshold: none
splits: motivation[11] 0/1/2  motivation[24] 2/2/0  motivation[26] 0/0/1  motivation[29] 2/1/1
        motivation[31] 1/0/1  motivation[34] 2/2/1  motivation[39] 0/2/2  motivation[71] 1/1/2
        motivation[74] 0/0/2  motivation[78] 1/0/0  motivation[83] 1/2/2  motivation[87] 0/0/1
        audience[48] 1/1/0  audience[64] 2/2/1  prior_art[5] 0/0/1  prior_art[9] 2/0/2
        prior_art[11] 0/1/1  prior_art[12] 1/1/0  prior_art[27] 1/0/0  prior_art[32] 1/0/0
        prior_art[33] 0/1/1  prior_art[38] 1/1/2  prior_art[46] 2/2/1  prior_art[47] 1/0/0
        prior_art[52] 0/1/0  prior_art[61] 0/1/1  prior_art[68] 1/0/1  prior_art[71] 1/2/1
        prior_art[76] 0/1/0  prior_art[78] 2/1/1  prior_art[89] 0/1/0  vehicle[13] 2/1/2
        vehicle[24] 0/1/1  vehicle[33] 0/1/1  vehicle[54] 1/2/2  vehicle[58] 1/0/0
        vehicle[59] 2/2/1  vehicle[68] 1/0/1  vehicle[69] 1/1/0  vehicle[81] 2/1/1
        vehicle[86] 2/1/2  coordination[11] 0/1/0  coordination[13] 1/1/0
        coordination[14] 0/2/2  coordination[24] 0/2/2  coordination[49] 2/0/2
        coordination[71] 1/0/0  insufficiency[28] 1/1/0  insufficiency[29] 1/1/0
        insufficiency[38] 1/0/0  insufficiency[43] 1/1/0  insufficiency[49] 0/1/0
        insufficiency[59] 0/1/0  implementation[4] 2/1/1  implementation[13] 0/1/0
        implementation[44] 2/1/2  implementation[49] 1/1/0  implementation[64] 1/1/2
        implementation[71] 1/0/1  implementation[73] 0/1/0  implementation[74] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 50 of 90 sections, strong in 16)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] Summary                                      1/1/1  -> 1.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     1/1/1  -> 1.00
  [9] Details                                      2/2/2  -> 2.00
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/1/2  -> 1.00
  [12] Discussion Status                            0/0/0  -> 0.00
  [13] Response                                     2/2/2  -> 2.00
  [14] Details                                      2/2/2  -> 2.00
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      1/1/1  -> 1.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     1/1/1  -> 1.00
  [19] Details                                      2/2/2  -> 2.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      2/2/2  -> 2.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     1/1/1  -> 1.00
  [24] Details                                      2/2/0  -> 1.33
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      0/0/1  -> 0.33
  [27] Discussion Status                            0/0/0  -> 0.00
  [28] Response                                     1/1/1  -> 1.00
  [29] Details                                      2/1/1  -> 1.33
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      1/0/1  -> 0.67
  [32] Discussion Status                            0/0/0  -> 0.00
  [33] Response                                     1/1/1  -> 1.00
  [34] Details                                      2/2/1  -> 1.67
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      1/1/1  -> 1.00
  [37] Discussion Status                            0/0/0  -> 0.00
  [38] Response                                     2/2/2  -> 2.00
  [39] Details                                      0/2/2  -> 1.33
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      1/1/1  -> 1.00
  [42] Discussion Status                            0/0/0  -> 0.00
  [43] Response                                     2/2/2  -> 2.00
  [44] Details                                      2/2/2  -> 2.00
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      1/1/1  -> 1.00
  [47] Discussion Status                            0/0/0  -> 0.00
  [48] Response                                     1/1/1  -> 1.00
  [49] Details                                      0/0/0  -> 0.00
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      1/1/1  -> 1.00
  [52] Discussion Status                            0/0/0  -> 0.00
  [53] Response                                     1/1/1  -> 1.00
  [54] Details                                      2/2/2  -> 2.00
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      1/1/1  -> 1.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     1/1/1  -> 1.00
  [59] Details                                      2/2/2  -> 2.00
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      1/1/1  -> 1.00
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     1/1/1  -> 1.00
  [64] Details                                      2/2/2  -> 2.00
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      1/1/1  -> 1.00
  [67] Discussion Status                            0/0/0  -> 0.00
  [68] Response                                     1/1/1  -> 1.00
  [69] Details                                      2/2/2  -> 2.00
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      1/1/2  -> 1.33
  [72] Discussion Status                            0/0/0  -> 0.00
  [73] Response                                     1/1/1  -> 1.00
  [74] Details                                      0/0/2  -> 0.67
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/0/0  -> 0.00
  [77] Discussion Status                            0/0/0  -> 0.00
  [78] Response                                     1/0/0  -> 0.33
  [79] Details                                      1/1/1  -> 1.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      2/2/2  -> 2.00
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      1/2/2  -> 1.67
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     1/1/1  -> 1.00
  [86] Details                                      1/1/1  -> 1.00
  [87] 3 Conclusion                                 0/0/1  -> 0.33
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/0/0  -> 0.00
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Recent papers and NB comments raise concerns about contract assertions as specified in the C++26 working draft, some even arguing for their removal.
candidate 2 (found by 3 of 270 passes): Without a standard assertion facility other than the limited C `assert`, libraries develop bespoke assertion facilities with incompatible functionality and configuration models.
candidate 3 (found by 3 of 270 passes): A central concern is that P2900 provides no method to guarantee *in* *code* that a particular assertion, or all assertions in a given ‘component of a program’, will always be checked.
candidate 4 (found by 3 of 270 passes): Assertions enable developers to incrementally improve the correctness of their code but are not intended to prove or guarantee the absence of undefined behaviour on their own.

## audience - grade 2.00 (fired in 12 of 90 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               0/0/0  -> 0.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] Summary                                      0/0/0  -> 0.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     0/0/0  -> 0.00
  [9] Details                                      0/0/0  -> 0.00
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/0/0  -> 0.00
  [12] Discussion Status                            0/0/0  -> 0.00
  [13] Response                                     0/0/0  -> 0.00
  [14] Details                                      0/0/0  -> 0.00
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      0/0/0  -> 0.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     0/0/0  -> 0.00
  [19] Details                                      2/2/2  -> 2.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      0/0/0  -> 0.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     0/0/0  -> 0.00
  [24] Details                                      2/2/2  -> 2.00
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      0/0/0  -> 0.00
  [27] Discussion Status                            0/0/0  -> 0.00
  [28] Response                                     0/0/0  -> 0.00
  [29] Details                                      0/0/0  -> 0.00
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      0/0/0  -> 0.00
  [32] Discussion Status                            0/0/0  -> 0.00
  [33] Response                                     0/0/0  -> 0.00
  [34] Details                                      0/0/0  -> 0.00
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      0/0/0  -> 0.00
  [37] Discussion Status                            0/0/0  -> 0.00
  [38] Response                                     0/0/0  -> 0.00
  [39] Details                                      0/0/0  -> 0.00
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      0/0/0  -> 0.00
  [42] Discussion Status                            0/0/0  -> 0.00
  [43] Response                                     1/1/1  -> 1.00
  [44] Details                                      2/2/2  -> 2.00
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      0/0/0  -> 0.00
  [47] Discussion Status                            0/0/0  -> 0.00
  [48] Response                                     1/1/0  -> 0.67
  [49] Details                                      0/0/0  -> 0.00
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      0/0/0  -> 0.00
  [52] Discussion Status                            0/0/0  -> 0.00
  [53] Response                                     0/0/0  -> 0.00
  [54] Details                                      0/0/0  -> 0.00
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      0/0/0  -> 0.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     1/1/1  -> 1.00
  [59] Details                                      1/1/1  -> 1.00
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      0/0/0  -> 0.00
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     1/1/1  -> 1.00
  [64] Details                                      2/2/1  -> 1.67
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      0/0/0  -> 0.00
  [67] Discussion Status                            0/0/0  -> 0.00
  [68] Response                                     1/1/1  -> 1.00
  [69] Details                                      2/2/2  -> 2.00
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      0/0/0  -> 0.00
  [72] Discussion Status                            0/0/0  -> 0.00
  [73] Response                                     0/0/0  -> 0.00
  [74] Details                                      0/0/0  -> 0.00
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/0/0  -> 0.00
  [77] Discussion Status                            0/0/0  -> 0.00
  [78] Response                                     0/0/0  -> 0.00
  [79] Details                                      0/0/0  -> 0.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      2/2/2  -> 2.00
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      0/0/0  -> 0.00
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     0/0/0  -> 0.00
  [86] Details                                      0/0/0  -> 0.00
  [87] 3 Conclusion                                 0/0/0  -> 0.00
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/0/0  -> 0.00
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Boost.Build already added such support on top of the available GCC and Clang implementations of P2900. Adding this support took less than an hour of implementation effort
candidate 2 (found by 3 of 270 passes): Because such optimisations are unsound, both Clang ([LLVMPR26774](http://llvm.org/PR26774)) and GCC ([GCCBug70018](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=70018))) disabled them nearly a decade ago.
candidate 3 (found by 3 of 270 passes): By contrast, when existing implementations of P2900 in GCC and Clang were applied as a replacement for legacy assertion libraries, `const`-ification revealed genuine bugs in existing libraries.
candidate 4 (found by 3 of 270 passes): applying `const`- ification directly to several large codebases ([P3268R0], [P3336R0]) produced no reported cases of breakage and revealed genuine bugs in those codebases.

## prior_art - grade 2.00 (fired in 62 of 90 sections, strong in 20)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Discussion                                 0/0/1  -> 0.33
  [6] Summary                                      1/1/1  -> 1.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     1/1/1  -> 1.00
  [9] Details                                      2/0/2  -> 1.33
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/1/1  -> 0.67
  [12] Discussion Status                            1/1/0  -> 0.67
  [13] Response                                     0/0/0  -> 0.00
  [14] Details                                      2/2/2  -> 2.00
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      1/1/1  -> 1.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     1/1/1  -> 1.00
  [19] Details                                      2/2/2  -> 2.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      2/2/2  -> 2.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     1/1/1  -> 1.00
  [24] Details                                      2/2/2  -> 2.00
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      1/1/1  -> 1.00
  [27] Discussion Status                            1/0/0  -> 0.33
  [28] Response                                     1/1/1  -> 1.00
  [29] Details                                      1/1/1  -> 1.00
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      1/1/1  -> 1.00
  [32] Discussion Status                            1/0/0  -> 0.33
  [33] Response                                     0/1/1  -> 0.67
  [34] Details                                      2/2/2  -> 2.00
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      1/1/1  -> 1.00
  [37] Discussion Status                            1/1/1  -> 1.00
  [38] Response                                     1/1/2  -> 1.33
  [39] Details                                      2/2/2  -> 2.00
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      1/1/1  -> 1.00
  [42] Discussion Status                            1/1/1  -> 1.00
  [43] Response                                     2/2/2  -> 2.00
  [44] Details                                      2/2/2  -> 2.00
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      2/2/1  -> 1.67
  [47] Discussion Status                            1/0/0  -> 0.33
  [48] Response                                     1/1/1  -> 1.00
  [49] Details                                      2/2/2  -> 2.00
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      1/1/1  -> 1.00
  [52] Discussion Status                            0/1/0  -> 0.33
  [53] Response                                     1/1/1  -> 1.00
  [54] Details                                      2/2/2  -> 2.00
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      1/1/1  -> 1.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     1/1/1  -> 1.00
  [59] Details                                      2/2/2  -> 2.00
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      0/1/1  -> 0.67
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     1/1/1  -> 1.00
  [64] Details                                      2/2/2  -> 2.00
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      1/1/1  -> 1.00
  [67] Discussion Status                            1/1/1  -> 1.00
  [68] Response                                     1/0/1  -> 0.67
  [69] Details                                      2/2/2  -> 2.00
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      1/2/1  -> 1.33
  [72] Discussion Status                            1/1/1  -> 1.00
  [73] Response                                     1/1/1  -> 1.00
  [74] Details                                      2/2/2  -> 2.00
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/1/0  -> 0.33
  [77] Discussion Status                            1/1/1  -> 1.00
  [78] Response                                     2/1/1  -> 1.33
  [79] Details                                      2/2/2  -> 2.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      2/2/2  -> 2.00
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      2/2/2  -> 2.00
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     1/1/1  -> 1.00
  [86] Details                                      2/2/2  -> 2.00
  [87] 3 Conclusion                                 0/0/0  -> 0.00
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/1/0  -> 0.33
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Recent papers and NB comments raise concerns about contract assertions as specified in the C++26 working draft, some even arguing for their removal.
candidate 2 (found by 3 of 270 passes): SG21 spent five years gathering use cases ([P1995R1]), exploring the design space, researching alternatives, and refining every aspect of the proposal before forwarding it to EWG
candidate 3 (found by 3 of 270 passes): [P3835R0], [US 25-052], [FI-071], and [RO 2-056] characterise P2900 as being ‘not safe’ and diminishing the overall ‘safety’ of C++.
candidate 4 (found by 3 of 270 passes): Mechanisms for non-ignorable checks exist today (e.g., the `if` statement) and are not weakened by P2900.

## vehicle - grade 2.00 (fired in 22 of 90 sections, strong in 8)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] Summary                                      0/0/0  -> 0.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     0/0/0  -> 0.00
  [9] Details                                      2/2/2  -> 2.00
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/0/0  -> 0.00
  [12] Discussion Status                            0/0/0  -> 0.00
  [13] Response                                     2/1/2  -> 1.67
  [14] Details                                      2/2/2  -> 2.00
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      0/0/0  -> 0.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     1/1/1  -> 1.00
  [19] Details                                      2/2/2  -> 2.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      0/0/0  -> 0.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     0/0/0  -> 0.00
  [24] Details                                      0/1/1  -> 0.67
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      0/0/0  -> 0.00
  [27] Discussion Status                            0/0/0  -> 0.00
  [28] Response                                     0/0/0  -> 0.00
  [29] Details                                      1/1/1  -> 1.00
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      0/0/0  -> 0.00
  [32] Discussion Status                            0/0/0  -> 0.00
  [33] Response                                     0/1/1  -> 0.67
  [34] Details                                      0/0/0  -> 0.00
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      0/0/0  -> 0.00
  [37] Discussion Status                            0/0/0  -> 0.00
  [38] Response                                     0/0/0  -> 0.00
  [39] Details                                      0/0/0  -> 0.00
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      0/0/0  -> 0.00
  [42] Discussion Status                            0/0/0  -> 0.00
  [43] Response                                     0/0/0  -> 0.00
  [44] Details                                      0/0/0  -> 0.00
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      0/0/0  -> 0.00
  [47] Discussion Status                            0/0/0  -> 0.00
  [48] Response                                     1/1/1  -> 1.00
  [49] Details                                      0/0/0  -> 0.00
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      0/0/0  -> 0.00
  [52] Discussion Status                            0/0/0  -> 0.00
  [53] Response                                     0/0/0  -> 0.00
  [54] Details                                      1/2/2  -> 1.67
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      0/0/0  -> 0.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     1/0/0  -> 0.33
  [59] Details                                      2/2/1  -> 1.67
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      0/0/0  -> 0.00
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     1/1/1  -> 1.00
  [64] Details                                      0/0/0  -> 0.00
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      0/0/0  -> 0.00
  [67] Discussion Status                            0/0/0  -> 0.00
  [68] Response                                     1/0/1  -> 0.67
  [69] Details                                      1/1/0  -> 0.67
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      0/0/0  -> 0.00
  [72] Discussion Status                            0/0/0  -> 0.00
  [73] Response                                     1/1/1  -> 1.00
  [74] Details                                      1/1/1  -> 1.00
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/0/0  -> 0.00
  [77] Discussion Status                            0/0/0  -> 0.00
  [78] Response                                     0/0/0  -> 0.00
  [79] Details                                      1/1/1  -> 1.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      2/1/1  -> 1.33
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      0/0/0  -> 0.00
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     1/1/1  -> 1.00
  [86] Details                                      2/1/2  -> 1.67
  [87] 3 Conclusion                                 0/0/0  -> 0.00
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/0/0  -> 0.00
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Standardising contract assertions doesn’t hinder the continued use of this approach.
candidate 2 (found by 3 of 270 passes): This strategy relies on contract assertion semantics being a language feature and does not work with preprocessor macros.
candidate 3 (found by 3 of 270 passes): P2900 introduces no new configuration dimension; rather, it replaces a proliferation of custom flags to control macro-based assertions with a single mechanism.
candidate 4 (found by 3 of 270 passes): P2900 replaces this fragmented landscape with a single mechanism for controlling assertions that does not rely on the preprocessor.

## coordination - grade 2.00 (fired in 13 of 90 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/2/2  -> 2.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] Summary                                      0/0/0  -> 0.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     0/0/0  -> 0.00
  [9] Details                                      0/0/0  -> 0.00
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/1/0  -> 0.33
  [12] Discussion Status                            0/0/0  -> 0.00
  [13] Response                                     1/1/0  -> 0.67
  [14] Details                                      0/2/2  -> 1.33
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      0/0/0  -> 0.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     1/1/1  -> 1.00
  [19] Details                                      2/2/2  -> 2.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      0/0/0  -> 0.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     0/0/0  -> 0.00
  [24] Details                                      0/2/2  -> 1.33
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      0/0/0  -> 0.00
  [27] Discussion Status                            0/0/0  -> 0.00
  [28] Response                                     0/0/0  -> 0.00
  [29] Details                                      0/0/0  -> 0.00
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      0/0/0  -> 0.00
  [32] Discussion Status                            0/0/0  -> 0.00
  [33] Response                                     0/0/0  -> 0.00
  [34] Details                                      0/0/0  -> 0.00
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      0/0/0  -> 0.00
  [37] Discussion Status                            0/0/0  -> 0.00
  [38] Response                                     0/0/0  -> 0.00
  [39] Details                                      0/0/0  -> 0.00
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      0/0/0  -> 0.00
  [42] Discussion Status                            0/0/0  -> 0.00
  [43] Response                                     0/0/0  -> 0.00
  [44] Details                                      0/0/0  -> 0.00
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      0/0/0  -> 0.00
  [47] Discussion Status                            0/0/0  -> 0.00
  [48] Response                                     1/1/1  -> 1.00
  [49] Details                                      2/0/2  -> 1.33
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      0/0/0  -> 0.00
  [52] Discussion Status                            0/0/0  -> 0.00
  [53] Response                                     0/0/0  -> 0.00
  [54] Details                                      0/0/0  -> 0.00
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      0/0/0  -> 0.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     0/0/0  -> 0.00
  [59] Details                                      0/0/0  -> 0.00
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      0/0/0  -> 0.00
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     1/1/1  -> 1.00
  [64] Details                                      2/2/2  -> 2.00
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      0/0/0  -> 0.00
  [67] Discussion Status                            0/0/0  -> 0.00
  [68] Response                                     0/0/0  -> 0.00
  [69] Details                                      0/0/0  -> 0.00
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      1/0/0  -> 0.33
  [72] Discussion Status                            0/0/0  -> 0.00
  [73] Response                                     0/0/0  -> 0.00
  [74] Details                                      0/0/0  -> 0.00
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/0/0  -> 0.00
  [77] Discussion Status                            0/0/0  -> 0.00
  [78] Response                                     0/0/0  -> 0.00
  [79] Details                                      0/0/0  -> 0.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      2/2/2  -> 2.00
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      0/0/0  -> 0.00
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     0/0/0  -> 0.00
  [86] Details                                      0/0/0  -> 0.00
  [87] 3 Conclusion                                 0/0/0  -> 0.00
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/0/0  -> 0.00
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Without a standard assertion facility other than the limited C `assert`, libraries develop bespoke assertion facilities with incompatible functionality and configuration models.
candidate 2 (found by 3 of 270 passes): Ensuring ABI compatibility across all these dependencies is challenging enough; requiring consistent contract-evaluation semantics across all dependencies — including transitive ones unknown to the top-level program owner — is infeasible in most cases.
candidate 3 (found by 3 of 270 passes): It allows the application owner to decide how to report and manage violations when integrating libraries from a wide variety of third-party suppliers, which is not possible with nonstandard solutions.
candidate 4 (found by 3 of 270 passes): P2900 directly addresses the limitations of macro-based assertions that static analysis tools already exploit today, and the vendors of these tools have consistently confirmed that its design will substantially improve their ability to detect bugs.

## insufficiency - grade 2.00 (fired in 12 of 90 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               1/1/1  -> 1.00
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] Summary                                      0/0/0  -> 0.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     0/0/0  -> 0.00
  [9] Details                                      0/0/0  -> 0.00
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/0/0  -> 0.00
  [12] Discussion Status                            0/0/0  -> 0.00
  [13] Response                                     1/1/1  -> 1.00
  [14] Details                                      2/2/2  -> 2.00
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      0/0/0  -> 0.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     0/0/0  -> 0.00
  [19] Details                                      0/0/0  -> 0.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      0/0/0  -> 0.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     0/0/0  -> 0.00
  [24] Details                                      0/0/0  -> 0.00
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      0/0/0  -> 0.00
  [27] Discussion Status                            0/0/0  -> 0.00
  [28] Response                                     1/1/0  -> 0.67
  [29] Details                                      1/1/0  -> 0.67
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      0/0/0  -> 0.00
  [32] Discussion Status                            0/0/0  -> 0.00
  [33] Response                                     0/0/0  -> 0.00
  [34] Details                                      0/0/0  -> 0.00
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      0/0/0  -> 0.00
  [37] Discussion Status                            0/0/0  -> 0.00
  [38] Response                                     1/0/0  -> 0.33
  [39] Details                                      0/0/0  -> 0.00
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      0/0/0  -> 0.00
  [42] Discussion Status                            0/0/0  -> 0.00
  [43] Response                                     1/1/0  -> 0.67
  [44] Details                                      0/0/0  -> 0.00
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      0/0/0  -> 0.00
  [47] Discussion Status                            0/0/0  -> 0.00
  [48] Response                                     1/1/1  -> 1.00
  [49] Details                                      0/1/0  -> 0.33
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      0/0/0  -> 0.00
  [52] Discussion Status                            0/0/0  -> 0.00
  [53] Response                                     0/0/0  -> 0.00
  [54] Details                                      0/0/0  -> 0.00
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      0/0/0  -> 0.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     0/0/0  -> 0.00
  [59] Details                                      0/1/0  -> 0.33
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      0/0/0  -> 0.00
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     0/0/0  -> 0.00
  [64] Details                                      2/2/2  -> 2.00
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      0/0/0  -> 0.00
  [67] Discussion Status                            0/0/0  -> 0.00
  [68] Response                                     0/0/0  -> 0.00
  [69] Details                                      0/0/0  -> 0.00
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      0/0/0  -> 0.00
  [72] Discussion Status                            0/0/0  -> 0.00
  [73] Response                                     0/0/0  -> 0.00
  [74] Details                                      0/0/0  -> 0.00
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/0/0  -> 0.00
  [77] Discussion Status                            0/0/0  -> 0.00
  [78] Response                                     0/0/0  -> 0.00
  [79] Details                                      0/0/0  -> 0.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      0/0/0  -> 0.00
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      0/0/0  -> 0.00
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     0/0/0  -> 0.00
  [86] Details                                      1/1/1  -> 1.00
  [87] 3 Conclusion                                 0/0/0  -> 0.00
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/0/0  -> 0.00
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Standardising an assertion facility is the only way to mitigate this complexity.
candidate 2 (found by 3 of 270 passes): With C `assert`, mixed mode makes programs IFNDR, with limited mitigation options in tooling due to missing information about macro values.
candidate 3 (found by 3 of 270 passes): This strategy relies on contract assertion semantics being a language feature and does not work with preprocessor macros.
candidate 4 (found by 3 of 270 passes): which is not possible with nonstandard solutions.

## implementation - grade 2.00  [binary: max] (fired in 21 of 90 sections, strong in 6)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Revision History                             0/0/0  -> 0.00
  [4] 1 Introduction                               2/1/1  -> 1.33
  [5] 2 Discussion                                 0/0/0  -> 0.00
  [6] Summary                                      0/0/0  -> 0.00
  [7] Discussion Status                            0/0/0  -> 0.00
  [8] Response                                     0/0/0  -> 0.00
  [9] Details                                      1/1/1  -> 1.00
  [10] Concern 2: P2900 does not provide consist... 0/0/0  -> 0.00
  [11] Summary                                      0/0/0  -> 0.00
  [12] Discussion Status                            0/0/0  -> 0.00
  [13] Response                                     0/1/0  -> 0.33
  [14] Details                                      2/2/2  -> 2.00
  [15] Concern 3: The impact of P2900 on depende... 0/0/0  -> 0.00
  [16] Summary                                      0/0/0  -> 0.00
  [17] Discussion Status                            0/0/0  -> 0.00
  [18] Response                                     0/0/0  -> 0.00
  [19] Details                                      2/2/2  -> 2.00
  [20] Concern 4: P2900 violates the spirit of t... 0/0/0  -> 0.00
  [21] Summary                                      0/0/0  -> 0.00
  [22] Discussion Status                            0/0/0  -> 0.00
  [23] Response                                     0/0/0  -> 0.00
  [24] Details                                      2/2/2  -> 2.00
  [25] Concern 5: P2900 does not work well with ... 0/0/0  -> 0.00
  [26] Summary                                      0/0/0  -> 0.00
  [27] Discussion Status                            0/0/0  -> 0.00
  [28] Response                                     0/0/0  -> 0.00
  [29] Details                                      0/0/0  -> 0.00
  [30] Concern 6: Too much in P2900 is implement... 0/0/0  -> 0.00
  [31] Summary                                      0/0/0  -> 0.00
  [32] Discussion Status                            0/0/0  -> 0.00
  [33] Response                                     0/0/0  -> 0.00
  [34] Details                                      2/2/2  -> 2.00
  [35] Concern 7: P2900 relies on guidelines the... 0/0/0  -> 0.00
  [36] Summary                                      0/0/0  -> 0.00
  [37] Discussion Status                            0/0/0  -> 0.00
  [38] Response                                     0/0/0  -> 0.00
  [39] Details                                      1/1/1  -> 1.00
  [40] Concern 8: const-ification is problematic    0/0/0  -> 0.00
  [41] Summary                                      0/0/0  -> 0.00
  [42] Discussion Status                            0/0/0  -> 0.00
  [43] Response                                     1/1/1  -> 1.00
  [44] Details                                      2/1/2  -> 1.67
  [45] Concern 9: Global contract-violation hand... 0/0/0  -> 0.00
  [46] Summary                                      0/0/0  -> 0.00
  [47] Discussion Status                            0/0/0  -> 0.00
  [48] Response                                     0/0/0  -> 0.00
  [49] Details                                      1/1/0  -> 0.67
  [50] Concern 10: Observing consecutive contrac... 0/0/0  -> 0.00
  [51] Summary                                      0/0/0  -> 0.00
  [52] Discussion Status                            0/0/0  -> 0.00
  [53] Response                                     0/0/0  -> 0.00
  [54] Details                                      0/0/0  -> 0.00
  [55] Concern 11: Treating exceptions as contra... 0/0/0  -> 0.00
  [56] Summary                                      0/0/0  -> 0.00
  [57] Discussion Status                            0/0/0  -> 0.00
  [58] Response                                     0/0/0  -> 0.00
  [59] Details                                      1/1/1  -> 1.00
  [60] Concern 12: P2900 does not support static... 0/0/0  -> 0.00
  [61] Summary                                      0/0/0  -> 0.00
  [62] Discussion Status                            0/0/0  -> 0.00
  [63] Response                                     1/1/1  -> 1.00
  [64] Details                                      1/1/2  -> 1.33
  [65] Concern 13: P2900 is too complex             0/0/0  -> 0.00
  [66] Summary                                      0/0/0  -> 0.00
  [67] Discussion Status                            0/0/0  -> 0.00
  [68] Response                                     1/1/1  -> 1.00
  [69] Details                                      0/0/0  -> 0.00
  [70] Concern 14: P2900 lacks important features   0/0/0  -> 0.00
  [71] Summary                                      1/0/1  -> 0.67
  [72] Discussion Status                            0/0/0  -> 0.00
  [73] Response                                     0/1/0  -> 0.33
  [74] Details                                      1/2/1  -> 1.33
  [75] Concern 15: P2900 makes future desirable ... 0/0/0  -> 0.00
  [76] Summary                                      0/0/0  -> 0.00
  [77] Discussion Status                            0/0/0  -> 0.00
  [78] Response                                     0/0/0  -> 0.00
  [79] Details                                      0/0/0  -> 0.00
  [80] Concern 16: P2900 should be composed from... 0/0/0  -> 0.00
  [81] Summary                                      2/2/2  -> 2.00
  [82] Concern 18: Standard-library hardening sh... 0/0/0  -> 0.00
  [83] Summary                                      0/0/0  -> 0.00
  [84] Discussion Status                            0/0/0  -> 0.00
  [85] Response                                     1/1/1  -> 1.00
  [86] Details                                      1/1/1  -> 1.00
  [87] 3 Conclusion                                 0/0/0  -> 0.00
  [88] Acknowledgments                              0/0/0  -> 0.00
  [89] Appendix: NB Comments overview               0/0/0  -> 0.00
  [90] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 270 passes): Complete implementations exist in publicly available forks of GCC and Clang ([P3460R0]), with upstreaming in progress.
candidate 2 (found by 3 of 270 passes): The naive implementation (implemented in GCC and Clang): compile each function with the contract-evaluation semantic specified for that TU; if multiple definitions exist, the compiler will choose one arbitrarily.
candidate 3 (found by 3 of 270 passes): Boost.Build already added such support on top of the available GCC and Clang implementations of P2900.
candidate 4 (found by 3 of 270 passes): During upstreaming of GCC’s P2900 implementation, we filed a complete bug report and reproducer in [GCCBug121936](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=121936).

-->
