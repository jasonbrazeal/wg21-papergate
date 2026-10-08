Verdict: Adequate to Strong (7/14)

The paper offers a solid account of the problem’s history and some useful evidence of implementation experience, but it leaves several core parts of the standardization case largely unargued. The thinnest support concerns why this change belongs in the standard itself rather than being handled by libraries or implementations, and the paper does not establish that existing practice or coordination would make standardization the natural next step.

- The strongest support is the concrete implementation experience, including a demo, a partial implementation, and links to real-world bug reports and usage discussions.
- The paper also establishes that alternatives and prior art were considered, including a constrained-constructor suggestion and the history of GCC’s deliberate choice around C++11 narrowing.
- The claim about who is affected rests mainly on an assertion that `span<const bool>` is likely common in generic code, without evidence about actual prevalence or impact.
- The most glaring omission is the absence of any established reason why this needs to be a standard change rather than something addressable through library design or implementation choices.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.50/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.50   corroborated 7.33   accumulate 7.50   max 8.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 1.33  insufficiency 0.00  implementation 2.00
sample agreement: 66 of 70 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.00 / 8.00   (all 3 samples: 7.50)
headings: h2 9
on threshold: coordination
splits: motivation[5] 0/1/0  audience[3] 1/0/0  prior_art[3] 2/0/2  coordination[4] 0/0/2
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
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 1/1/1  -> 1.00
candidate 1 (found by 3 of 30 passes): The libcu++ authors found that they had correctly implemented the specification and that the specification change itself caused the issue.
candidate 2 (found by 3 of 30 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span<const bool>` is affected.
candidate 3 (found by 1 of 30 passes): Rejecting code like this because of the C++11 narrowing rules would have hindered adoption of C++11 enormously.
candidate 4 (found by 1 of 30 passes): GCC made this choice consciously, as a way to promote adoption of C++11.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 1/0/0  -> 0.33
  [4] 3 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [5] 4 P2447 introduced Standard Library and w... 0/0/0  -> 0.00
  [6] 5 Proposed fix: Remove initializerlist co... 0/0/0  -> 0.00
  [7] 6 Alternatives                               0/0/0  -> 0.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): Creating a `span<const bool>` is likely more common, especially in generic code.

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Problem: “Silent” change in span’... 2/0/2  -> 1.33
  [4] 3 It’s not “silent,” but implementa... 2/2/2  -> 2.00
  [5] 4 P2447 introduced Standard Library and w... 1/1/1  -> 1.00
  [6] 5 Proposed fix: Remove initializerlist co... 1/1/1  -> 1.00
  [7] 6 Alternatives                               2/2/2  -> 2.00
  [8] 7 Dissenting opinion                         0/0/0  -> 0.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): GCC made this choice consciously, as a way to promote adoption of C++11.
candidate 2 (found by 3 of 30 passes): Adoption of P2447 led to bugs in both Standard Library implementations and the Standard wording that later had to be fixed.
candidate 3 (found by 3 of 30 passes): LEWG asked this paper to be revised to include that solution.
candidate 4 (found by 3 of 30 passes): One suggestion is to constrain the constructor as follows.

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
  [4] 3 It’s not “silent,” but implementa... 0/0/2  -> 0.67
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
  [8] 7 Dissenting opinion                         1/1/1  -> 1.00
  [9] 8 Proposed wording                           0/0/0  -> 0.00
  [10] 9 Appendix A: Original (pre-LEWG-review) ... 2/2/2  -> 2.00
candidate 1 (found by 3 of 30 passes): We’ve written a demo (also with partial implementation of proposed fix) [here](https://godbolt.org/z/7T9Eof9ba).
candidate 2 (found by 3 of 30 passes): The libstdc++ [Bug 120997](https://gcc.gnu.org/bugzilla/show_bug.cgi?id=120997) led to filing of [LWG 4293](https://cplusplus.github.io/LWG/issue4293).
candidate 3 (found by 3 of 30 passes): Arthur O’Dwyer, contacted Tomasz Kamiński and myself to ask us to link to this blog post about successful use of the `span(initializer_list<value_type>)` constructor in Chromium.
candidate 4 (found by 3 of 30 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo!

-->
