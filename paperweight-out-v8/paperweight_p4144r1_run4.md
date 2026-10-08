Verdict: Adequate to Strong (8/14)

The paper offers solid support in a few narrow areas—particularly prior art, alternatives, and implementation experience—but leaves several core parts of the standardization case unargued. The thinnest support concerns why the standard is the right vehicle and why a library solution would not suffice, with the affected-user claim also resting more on assertion than evidence.

- The strongest material is the concrete implementation experience, including a demo, a libstdc++ bug report, an LWG issue, and a suggested implementation.
- The discussion of prior art and alternatives is well grounded, showing conscious compiler choices and LEWG direction toward a different fix.
- The claim about who is affected is asserted rather than demonstrated, especially the suggestion that `span<const bool>` is likely common in generic code.
- The paper does not establish why standardization is necessary or why a library-only approach cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 7.67   accumulate 7.67   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 8.50 / 7.50 / 7.00   (all 3 samples: 7.67)
headings: h2 9
on threshold: coordination
splits: motivation[10] 0/1/1  audience[3] 1/1/0  prior_art[6] 1/1/0  prior_art[8] 0/1/1
        coordination[4] 2/0/0  implementation[8] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/1/1  -> 0.67
candidate 1 (found by 3 of 30 passes): In general, GCC treats narrowing with constant expressions as an error, but for non-constant expressions only issues a warning, on the basis that the existing, working code doing it is probably correct.
candidate 2 (found by 2 of 30 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span<const bool>` is affected.
candidate 3 (found by 1 of 30 passes): In C++23, constructor `span(element_type*, size_t)` is called.
candidate 4 (found by 1 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.

## audience - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 1/1/0  -> 0.67
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Creating a `span<const bool>` is likely more common, especially in generic code.

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 1/1/0  -> 0.67
  [7] 6 Alternatives                               2/2/2  -> 2.00
  [8] 7 Dissenting opinion                         0/1/1  -> 0.67
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): GCC made this choice consciously, as a way to promote adoption of C++11.
candidate 2 (found by 3 of 30 passes): LEWG reviewed this on 2026-03-25 and polled to select a different fix.
candidate 3 (found by 2 of 30 passes): LEWG asked this paper to be revised to include that solution.
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

## coordination - grade 1.33 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 2/0/0  -> 0.67
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.
candidate 2 (found by 1 of 30 passes): GCC trunk compiles this but emits narrowing warnings. Clang stops with an error.

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

## implementation - grade 2.00  [binary: max] (fired in 4 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 2/2/2  -> 2.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         1/2/1  -> 1.33
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): We’ve written a demo (also with partial implementation of proposed fix) [here](https://godbolt.org/z/7T9Eof9ba).
candidate 2 (found by 3 of 30 passes): The libstdc++ [Bug 120997](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=120997) led to filing of [LWG 4293](https://cplusplus.github.io/LWG/issue4293).
candidate 3 (found by 3 of 30 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).
candidate 4 (found by 2 of 30 passes): This could be relevant for discussion of restoring the removed feature in future C++ versions.

-->
