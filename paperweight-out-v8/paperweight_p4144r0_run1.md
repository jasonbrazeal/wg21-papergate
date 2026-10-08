Verdict: Adequate (6/14)

The paper gives a partial account of why the change is worth considering, with concrete evidence about a real compatibility break and a working implementation, but it leaves several essential parts of the standardization case largely unaddressed. The thinnest support concerns the need for a standard change at all, how it would fit with existing specifications, and why a library-level solution would not suffice.

- The strongest support is the demonstrated implementation experience, including a working demo and a partial implementation of the proposed fix.
- The paper also establishes the prior-art and alternatives discussion by identifying the breakage from P2447 and showing how a conforming extension could avoid it.
- The claim about who is affected is asserted but not backed up with evidence, particularly the assertion that `span<const bool>` is likely more common in generic code.
- The most glaring omission is the absence of any established case for why this needs standardization rather than remaining a compiler extension or being handled outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 8
on threshold: motivation
splits: prior_art[5] 1/1/0  prior_art[6] 0/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [5] 4 It’s not “silent,” but implementa... 1/1/1  -> 1.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               1/1/1  -> 1.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): In C++23, constructor `span(element_type*, size_t)` is called. Adoption of P2447R6 for C++26 means that constructor `span(initializer_list<value_type>)` is selected instead.
candidate 2 (found by 2 of 27 passes): GCC trunk compiles this but emits narrowing warnings. Clang stops with an error.
candidate 3 (found by 2 of 27 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span<const bool>` is affected.
candidate 4 (found by 1 of 27 passes): This is actually ill-formed code; it’s a narrowing conversion from pointer to `bool`.

## audience - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 1/1/1  -> 1.00
  [5] 4 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               0/0/0  -> 0.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Creating a `span<const bool>` is likely more common, especially in generic code.
candidate 2 (found by 1 of 27 passes): However, `span<const any>` is a less common use case. Creating a `span<const bool>` is likely more common, especially in generic code.

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [5] 4 It’s not “silent,” but implementa... 1/1/0  -> 0.67
  [6] 5 P2447 introduced wording bugs, later fixed 0/1/1  -> 0.67
  [7] 6 Proposed fix                               2/2/2  -> 2.00
  [8] 7 Alternatives                               2/2/2  -> 2.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).
candidate 2 (found by 3 of 27 passes): Option (2) is higher risk because `span` has many constructors.
candidate 3 (found by 2 of 27 passes): Adoption of P2447 led to bugs in the Standard wording that later had to be fixed.
candidate 4 (found by 1 of 27 passes): GCC implements a conforming “extension” per [[intro.compliance.general] 11](https://eel.is/c++draft/intro#compliance.general-11.sentence-2), in that it attempts to give meaning (by compiling) to invalid code.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [5] 4 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               0/0/0  -> 0.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [5] 4 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               0/0/0  -> 0.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [5] 4 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               0/0/0  -> 0.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 2/2/2  -> 2.00
  [5] 4 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               2/2/2  -> 2.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): We’ve written a demo (also with partial implementation of proposed fix) [here](https://godbolt.org/z/7T9Eof9ba).
candidate 2 (found by 3 of 27 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).

-->
