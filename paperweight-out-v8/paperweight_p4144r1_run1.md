Verdict: Adequate (7/14)

The paper offers a solid account of why the change matters and what alternatives exist, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest areas are the absence of a clear affected-user picture and the lack of any argument for why this must be done through the standard rather than through library or implementation-level remedies.

- The strongest support is the concrete demonstration that the C++26 change itself broke previously valid code, with implementation experience and a working demo to back that up.
- The paper also establishes meaningful prior art and alternatives, including the conscious GCC precedent and the LEWG decision to pursue a different fix.
- The most glaring omission is that the paper never establishes who is affected, leaving the actual scope and severity of the breakage unquantified.
- It also fails to explain why the standard is the necessary venue or why a library-level solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.00   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.83  insufficiency 0.00  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 6.50 / 7.00   (all 3 samples: 6.83)
headings: h2 9
on threshold: coordination
splits: motivation[5] 0/1/0  motivation[10] 1/1/0  prior_art[3] 0/2/2  coordination[3] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 0/1/0  -> 0.33
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 1/1/0  -> 0.67
candidate 1 (found by 2 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.
candidate 2 (found by 2 of 30 passes): In general, GCC treats narrowing with constant expressions as an error, but for non-constant expressions only issues a warning, on the basis that the existing, working code doing it is probably correct.
candidate 3 (found by 2 of 30 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span<const bool>` is affected.
candidate 4 (found by 1 of 30 passes): In C++23, constructor `span(element_type*, size_t)` is called. WG21 adopted P2447R6 for C++26 at the March 2024 Tokyo meeting. This added a new `span(initializer_list<value_type>)` constructor. As a result, in the above example, the new constructor is selected instead.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/2/2  -> 1.33
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 1/1/1  -> 1.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               2/2/2  -> 2.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): GCC made this choice consciously, as a way to promote adoption of C++11.
candidate 2 (found by 3 of 30 passes): Adoption of P2447 led to bugs in both Standard Library implementations and the Standard wording that later had to be fixed.
candidate 3 (found by 3 of 30 passes): LEWG reviewed this on 2026-03-25 and polled to select a different fix.
candidate 4 (found by 2 of 30 passes): This paper expresses [LWG4520](https://cplusplus.github.io/LWG/issue4520) and proposes fixing it by reverting adoption of [P2447R6](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2447r6.html).

## vehicle - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.83 (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/1/2  -> 1.67
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 2/2/2  -> 2.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         2/2/2  -> 2.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): We’ve written a demo (also with partial implementation of proposed fix) [here](https://godbolt.org/z/7T9Eof9ba).
candidate 2 (found by 3 of 30 passes): The libstdc++ [Bug 120997](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=120997) led to filing of [LWG 4293](https://cplusplus.github.io/LWG/issue4293).
candidate 3 (found by 3 of 30 passes): [this blog post](https://quuxplusone.github.io/blog/2026/03/19/p2447-success-story/) about successful use of the `span(initializer_list<value_type>)` constructor in Chromium.
candidate 4 (found by 3 of 30 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).

-->
