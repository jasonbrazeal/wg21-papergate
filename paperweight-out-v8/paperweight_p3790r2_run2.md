Verdict: Adequate (5/14)

The paper offers only a thin evidentiary basis for standardization, with its strongest material being the references to prior work and alternatives. Most of the claims that would justify action—about affected users, production use, implementation experience, and the inadequacy of library-only solutions—are asserted rather than demonstrated with concrete examples or data.

- The paper’s clearest support is its citation of prior C and C++ discussions, which shows the problem has been considered before.
- The argument that existing standards do not permit reliable operations on these pointers is stated, but the paper does not show how widespread or critical the affected code is.
- The most glaring omission is the absence of any concrete implementation experience or production evidence beyond a repeated general assertion about decades of use.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 7 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.33   accumulate 5.83   max 6.67

## SUMMARY
grades: motivation 1.17  audience 0.17  prior_art 1.67  vehicle 0.50  coordination 0.33  insufficiency 0.17  implementation 1.00
sample agreement: 63 of 70 section-criterion pairs unanimous (90%)
single-sample totals would have been: 6.00 / 5.00 / 4.50   (all 3 samples: 5.00)
headings: h2 9
on threshold: prior_art
splits: motivation[3] 1/2/1  audience[4] 1/0/0  prior_art[6] 2/1/1  prior_art[7] 2/0/2
        prior_art[10] 2/0/0  coordination[4] 1/1/0  insufficiency[4] 1/0/0
## END SUMMARY

## motivation - grade 1.17 (fired in 3 of 10 sections, strong in 0)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/2/1  -> 1.33
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      1/1/1  -> 1.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.
candidate 2 (found by 3 of 30 passes): In order to support a number of critically important algorithms, this paper proposes a `launder_ptr_bits``()` function and a `ptr_bits&lt;T>` template class to provide a convenience mechanism for encapsulating the pair of `reinterpret_cast&lt;>` operations used to create a prospective pointer value
candidate 3 (found by 3 of 30 passes): This additional provenance information can be problematic for certain types of concurrent algorithms and debugging code, which might need comparison and hashing functions to be consistent with the value representation.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## prior_art - grade 1.67 (fired in 6 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       2/1/1  -> 1.33
  [7] Detailed Proposal                            2/0/2  -> 1.33
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               2/0/0  -> 0.67
candidate 1 (found by 3 of 30 passes): Please note that this paper does not propose adding bag-of-bits pointer semantics to the standard.
candidate 2 (found by 3 of 30 passes): See WG14 [N2369](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2369.pdf) and [N2443](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2443.pdf) for more details on the C language’s handling of pointers to lifetime-ended objects and WG21 [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf) for the corresponding C++ language details.
candidate 3 (found by 3 of 30 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 4 (found by 2 of 30 passes): Those interested in seeing a wider array of historical options are invited to review [P1726R4](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p1726r4.pdf), [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf), and [P2188R1](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p2188r1.html).

## vehicle - grade 0.50 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): We therefore need a solution that not only preserves valuable optimizations and debugging tools, but that also works for existing source code.

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/0  -> 0.67
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## insufficiency - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): the current standards and working drafts for both C and C++ do not permit reliable loading, storing, casting, or comparison of such pointers.

## implementation - grade 1.00  [binary: max] (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

-->
