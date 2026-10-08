Verdict: Adequate (6/14)

The paper offers only partial support for its own standardization, with its strongest grounding in prior art and alternatives but little concrete evidence for the prevalence, portability, or standardization need of the affected code. The thinnest areas are the absence of any argument for why a library solution would not suffice and the reliance on broad, repeated claims about production use without specifics.

- The paper clearly connects its approach to existing C and C++ provenance discussions and prior proposals, establishing that the problem space has recognized precedent.
- The claims about who is affected and why the issue matters rest on general assertions of long-standing production use rather than named codebases, measurements, or concrete examples.
- The case for why a standard language or library facility is required, as opposed to a non-standard library, is not made at all.
- Implementation experience is asserted only through the same vague production-use statements, with no evidence of actual deployment or testing of the proposed facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 6 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 6.67   accumulate 6.50   max 6.67

## SUMMARY
grades: motivation 1.00  audience 0.83  prior_art 1.83  vehicle 0.50  coordination 0.33  insufficiency 0.00  implementation 1.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 5.50 / 5.50 / 6.50   (all 3 samples: 5.50)
headings: h2 9
on threshold: none
splits: motivation[4] 0/0/2  audience[3] 1/0/1  prior_art[4] 2/1/2  prior_art[6] 1/2/1
        prior_art[7] 2/2/0  coordination[4] 0/1/1
## END SUMMARY

## motivation - grade 1.00 (fired in 4 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 0/0/2  -> 0.67
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       1/1/1  -> 1.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      1/1/1  -> 1.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.
candidate 2 (found by 3 of 30 passes): In order to support a number of critically important algorithms, this paper proposes a `launder_ptr_bits``()` function and a `ptr_bits&lt;T>` template class to provide a convenience mechanism for encapsulating the pair of `reinterpret_cast&lt;>` operations used to create a prospective pointer value
candidate 3 (found by 3 of 30 passes): This additional provenance information can be problematic for certain types of concurrent algorithms and debugging code, which might need comparison and hashing functions to be consistent with the value representation.
candidate 4 (found by 1 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

## audience - grade 0.83 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/0/1  -> 0.67
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades
candidate 2 (found by 1 of 30 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms
candidate 3 (found by 1 of 30 passes): it is not consistent with long-standing usage, especially for a range of concurrent and sequential algorithms that rely on loads, stores, equality comparisons, and even dereferencing of such pointers.

## prior_art - grade 1.83 (fired in 6 of 10 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract 2                                   0/0/0  -> 0.00
  [3] Abstract                                     1/1/1  -> 1.00
  [4] Introduction                                 2/1/2  -> 1.67
  [5] Terminology                                  1/1/1  -> 1.00
  [6] What We Are Asking For                       1/2/1  -> 1.33
  [7] Detailed Proposal                            2/2/0  -> 1.33
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): Similar issues result from object-lifetime aspects of C *pointer* *provenance.*
candidate 2 (found by 3 of 30 passes): See WG14 [N2369](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2369.pdf) and [N2443](http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2443.pdf) for more details on the C language’s handling of pointers to lifetime-ended objects and WG21 [P1726R5](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1726r5.pdf) for the corresponding C++ language details.
candidate 3 (found by 3 of 30 passes): For more information, please see [P2434R4](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p2434r3.html).
candidate 4 (found by 3 of 30 passes): TL;DR: `ptr_bits<T>` and `launder_ptr_bits()` were chosen, following Anthony Williams's P2188R1 ("Zap the Zap: Pointers are sometimes just bags of bits").

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
  [4] Introduction                                 0/1/1  -> 0.67
  [5] Terminology                                  0/0/0  -> 0.00
  [6] What We Are Asking For                       0/0/0  -> 0.00
  [7] Detailed Proposal                            0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
  [9] History                                      0/0/0  -> 0.00
  [10] Appendix: Name-Selection Guide               0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): concurrent algorithms that rely on loading, storing, casting, and comparing such pointer values have been used in production in large bodies of code for decades

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
