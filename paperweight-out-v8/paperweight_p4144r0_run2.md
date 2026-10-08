Verdict: Adequate (6/14)

The paper offers meaningful support in a few areas, particularly around implementation experience and the existence of prior art, but it leaves several core standardization questions essentially unaddressed. The thinnest parts concern why a standard change is necessary at all, how it would interoperate with existing specifications, and why a library solution cannot suffice.

- The strongest support is the concrete implementation work, including a demo and a partial implementation of the proposed fix.
- The paper also establishes relevant prior art by showing divergent compiler behavior and noting that earlier adoption of P2447 introduced wording bugs.
- The most glaring omission is the absence of any established case for why the standard itself must change, rather than relying on existing or library-level mechanisms.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.67/14)

Provisionally addressed: 4 of 7. Provisional points: 5.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.67   corroborated 5.67   accumulate 6.33   max 6.67

## SUMMARY
grades: motivation 1.50  audience 0.33  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 5.50 / 5.50 / 6.00   (all 3 samples: 5.67)
headings: h2 8
on threshold: motivation
splits: audience[4] 1/0/1  prior_art[7] 1/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 27 passes): That would have the advantage that everything else works fine still, but we can avoid the breakage of valid user code, so only `span<const bool>` is affected.
candidate 2 (found by 2 of 27 passes): Creating a `span<const bool>` is likely more common, especially in generic code.
candidate 3 (found by 2 of 27 passes): This is actually ill-formed code; it’s a narrowing conversion from pointer to `bool`.
candidate 4 (found by 1 of 27 passes): Creating a `span<const bool>` is likely more common, especially in generic code. That means LEWG might not have realized the significance of the change.

## audience - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 1/0/1  -> 0.67
  [5] 4 It’s not “silent,” but implementa... 0/0/0  -> 0.00
  [6] 5 P2447 introduced wording bugs, later fixed 0/0/0  -> 0.00
  [7] 6 Proposed fix                               0/0/0  -> 0.00
  [8] 7 Alternatives                               0/0/0  -> 0.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Creating a `span<const bool>` is likely more common, especially in generic code.

## prior_art - grade 1.83 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Author                                     0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Problem: “Silent” change in span’... 0/0/0  -> 0.00
  [5] 4 It’s not “silent,” but implementa... 1/1/1  -> 1.00
  [6] 5 P2447 introduced wording bugs, later fixed 1/1/1  -> 1.00
  [7] 6 Proposed fix                               1/2/2  -> 1.67
  [8] 7 Alternatives                               2/2/2  -> 2.00
  [9] 8 Wording change                             0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): GCC trunk compiles this but emits narrowing warnings. Clang stops with an error.
candidate 2 (found by 3 of 27 passes): Adoption of P2447 led to bugs in the Standard wording that later had to be fixed.
candidate 3 (found by 3 of 27 passes): Regarding Option (1), Mattermost discussion during the meeting suggests that GCC is unlikely to change its current behavior.
candidate 4 (found by 2 of 27 passes): Here is an [implementation](https://gcc.godbolt.org/z/Esa1nc1jY) (thanks to Giuseppe D’Angelo! who suggests that this constructor could be a C++29 feature, since it’s an extension, as code would move from breaking to non-breaking).

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
