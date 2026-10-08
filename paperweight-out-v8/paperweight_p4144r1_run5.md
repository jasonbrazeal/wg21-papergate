Verdict: Adequate (6/14)

The paper offers meaningful support in a few areas, particularly in showing real implementation experience and in identifying prior discussion of alternatives, but it leaves the central standardization rationale largely unargued. The thinnest parts are the absence of a case for why this must be handled in the standard, why a library solution would not suffice, and how the change would coordinate with existing implementations and specifications.

- The strongest support is the implementation experience, including a demo, a reported libstdc++ bug, an LWG issue, and a concrete implementation of the proposed fix.
- The paper also establishes that alternatives were considered, including a different fix selected by LEWG and a suggested constrained constructor.
- The most glaring omission is the lack of any established argument for why the standard is the right place to address the problem rather than a library-level or implementation-level remedy.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.67   accumulate 6.33   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 64 of 70 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.00 / 6.50 / 6.50   (all 3 samples: 6.33)
headings: h2 9
on threshold: none
splits: motivation[5] 0/1/1  audience[3] 0/1/1  prior_art[5] 0/0/1  prior_art[6] 1/1/0
        prior_art[8] 1/1/0  implementation[8] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 0/1/1  -> 0.67
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 1/1/1  -> 1.00
candidate 1 (found by 3 of 30 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span<const bool>` is affected.
candidate 2 (found by 2 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.
candidate 3 (found by 2 of 30 passes): GCC made this choice consciously, as a way to promote adoption of C++11.
candidate 4 (found by 2 of 30 passes): Adoption of P2447 led to bugs in both Standard Library implementations and the Standard wording that later had to be fixed.

## audience - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/1/1  -> 0.67
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Creating a `span<const bool>` is likely more common, especially in generic code.

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/1  -> 0.33
  [6] 5 Proposed fix: Remove initializerlist co... 1/1/0  -> 0.67
  [7] 6 Alternatives                               2/2/2  -> 2.00
  [8] 7 Dissenting opinion                         1/1/0  -> 0.67
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

## coordination - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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
  [8] 7 Dissenting opinion                         1/1/0  -> 0.67
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): We’ve written a demo (also with partial implementation of proposed fix) [here](https://godbolt.org/z/7T9Eof9ba).
candidate 2 (found by 3 of 30 passes): The libstdc++ [Bug 120997](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=120997) led to filing of [LWG 4293](https://cplusplus.github.io/LWG/issue4293).
candidate 3 (found by 2 of 30 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).
candidate 4 (found by 1 of 30 passes): One of P2447’s authors, Arthur O’Dwyer, contacted Tomasz Kamiński and myself to ask us to link to this blog post about successful use of the `span(initializer_list<value_type>)` constructor in Chromium.

-->
