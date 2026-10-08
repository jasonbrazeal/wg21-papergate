Verdict: Adequate (6/14)

The paper offers some useful context by connecting its concerns to prior work on pointer provenance in C and C++, but it does not adequately establish the need for standardization on its own terms. The strongest material is the discussion of related efforts, while the case for who is affected, why the standard is necessary, and whether the approach has been implemented remains largely asserted rather than demonstrated.

- The paper’s clearest support comes from its references to prior work on pointer provenance and related C and C++ discussions, which grounds the problem in existing standardization conversations.
- The claims about production use and affected concurrent algorithms are repeated but not substantiated with concrete examples, code, or evidence of scale.
- The argument for why a library solution would be insufficient is absent, leaving a key part of the standardization rationale unaddressed.
- The paper provides no implementation experience beyond the same general assertion of longstanding production use, making it hard to evaluate the proposed design in practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 6 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 7.00   accumulate 5.83   max 7.00

## SUMMARY
grades: motivation 1.00  audience 0.50  prior_art 2.00  vehicle 0.50  coordination 0.50  insufficiency 0.00  implementation 1.00
sample agreement: 68 of 70 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 9
on threshold: none
splits: motivation[6] 1/1/0  prior_art[6] 1/2/2
## END SUMMARY

## motivation - grade 1.00 (fired in 3 of 10 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/1/0  -> 0.67
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      1/1/1  -> 1.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.
candidate 2 (found by 3 of 30 passes): This additional provenance information can be problematic for certain types of concurrent algorithms and debugging code, which might need comparison and hashing functions to be consistent with the value representation.
candidate 3 (found by 2 of 30 passes): In order to support a number of critically important algorithms, this paper proposes a `launder_ptr_bits``()` function and a `ptr_bits&lt;T>` template class

## audience - grade 0.50 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       1/2/2  -> 1.67
  [7] Detailed Proposal                            2/2/2  -> 2.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): Similar issues result from object-lifetime aspects of C *pointer* *provenance.*
candidate 2 (found by 3 of 30 passes): See WG14 [N2369](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2369.pdf) and [N2443](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2443.pdf) for more details on the C language’s handling of pointers to lifetime-ended objects and WG21 [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf) for the corresponding C++ language details.
candidate 3 (found by 3 of 30 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 4 (found by 3 of 30 passes): This function can be based on a `reinterpret_cast` pair as suggested in P2434R4 (see the “Consequences for pointer zap” section), for example, by using an `uintptr_t` data member private to `ptr_bits<T>`.

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

## coordination - grade 0.50 (fired in 1 of 10 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidates: (none validated)

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
