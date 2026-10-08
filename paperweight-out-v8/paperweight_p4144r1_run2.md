Verdict: Adequate to Strong (7/14)

The paper offers solid support in a few narrow areas—particularly implementation experience and prior art—but leaves several core parts of the standardization case unstated, especially why the standard itself must change and why a library-level solution would not suffice. The thinnest support is around the necessity of standardization, with no direct argument for why the standard is the right venue or why a library cannot address the problem.

- The strongest support is the implementation experience, including a demo, a reported libstdc++ bug, and a concrete implementation of the proposed fix.
- The paper also establishes prior art and alternatives, showing that GCC made a deliberate choice and that LEWG reviewed and selected a different fix.
- The case for who is affected is only claimed, resting on assertions about generic code and the aftermath of P2447 without direct evidence of user impact.
- The most glaring omission is the absence of any established argument for why the standard must change or why a library will not do.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.33   accumulate 7.00   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 2.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 63 of 70 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.50 / 7.50 / 6.00   (all 3 samples: 7.00)
headings: h2 9
on threshold: none
splits: motivation[7] 1/0/0  motivation[10] 1/2/1  audience[3] 1/1/0  audience[5] 0/2/0
        prior_art[3] 2/0/0  prior_art[6] 0/0/1  coordination[3] 2/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 1/1/1  -> 1.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               1/0/0  -> 0.33
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 1/2/1  -> 1.33
candidate 1 (found by 3 of 30 passes): In C++23, constructor `span(element_type*, size_t)` is called.
candidate 2 (found by 3 of 30 passes): Rejecting code like this because of the C++11 narrowing rules would have hindered adoption of C++11 enormously.
candidate 3 (found by 3 of 30 passes): Adoption of P2447 led to bugs in both Standard Library implementations and the Standard wording that later had to be fixed.
candidate 4 (found by 2 of 30 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span&lt;const bool>` is affected.

## audience - grade 0.67 (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 1/1/0  -> 0.67
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/2/0  -> 0.67
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Creating a `span<const bool>` is likely more common, especially in generic code.
candidate 2 (found by 1 of 30 passes): Adoption of P2447 led to bugs in both Standard Library implementations and the Standard wording that later had to be fixed.

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/0/0  -> 0.67
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 1/1/1  -> 1.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/1  -> 0.33
  [7] 6 Alternatives                               2/2/2  -> 2.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): GCC made this choice consciously, as a way to promote adoption of C++11.
candidate 2 (found by 3 of 30 passes): Adoption of P2447 led to bugs in both Standard Library implementations and the Standard wording that later had to be fixed.
candidate 3 (found by 3 of 30 passes): LEWG reviewed this on 2026-03-25 and polled to select a different fix.
candidate 4 (found by 2 of 30 passes): One suggestion is to constrain the constructor as follows.

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

## coordination - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/0/0  -> 0.67
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.

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

## implementation - grade 2.00  [binary: max] (fired in 3 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 2/2/2  -> 2.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): We’ve written a demo (also with partial implementation of proposed fix) [here](https://godbolt.org/z/7T9Eof9ba).
candidate 2 (found by 3 of 30 passes): The libstdc++ [Bug 120997](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=120997) led to filing of [LWG 4293](https://cplusplus.github.io/LWG/issue4293).
candidate 3 (found by 3 of 30 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).

-->
