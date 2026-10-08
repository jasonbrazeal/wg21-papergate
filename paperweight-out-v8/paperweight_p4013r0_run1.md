Verdict: Adequate (5/14)

The paper offers some useful groundwork by showing an implementation and pointing to existing practice, but it leaves the central case for standardization largely unargued. The thinnest areas are the absence of any identified audience, the lack of discussion about why a library solution would not suffice, and the missing account of how the change would interact with the wider standard.

- The strongest support is the concrete implementation experience, including a linked compiler change and availability on Compiler Explorer.
- The paper also establishes some prior art by referencing an existing proposal and describing how current standard library implementations handle `std::any` metadata.
- The most glaring omission is that the paper never establishes who is affected by the proposed change or why the standard, rather than a library, is the right place for it.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 3 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.00   accumulate 5.17   max 5.00

## SUMMARY
grades: motivation 0.83  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 5.00 / 5.00 / 5.50   (all 3 samples: 4.83)
headings: h2 4
on threshold: implementation
splits: motivation[1] 1/1/0  motivation[2] 0/0/2  prior_art[3] 1/1/0
## END SUMMARY

## motivation - grade 0.83 (fired in 3 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Motivation                                   0/0/2  -> 0.67
  [3] Changes                                      1/1/1  -> 1.00
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper can be implemented trivially by prepending this sequence with a `if consteval` statement which will pick the allocating behavior for every type.
candidate 2 (found by 2 of 15 passes): This paper is making `std::any` usable during constant evaluation.
candidate 3 (found by 1 of 15 passes): Each of this option has ups and downs: templates has instantiation and huge cost of AST copying (and in growing executable size), inheritance has virtual tables.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      0/0/0  -> 0.00
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   2/2/2  -> 2.00
  [3] Changes                                      1/1/0  -> 0.67
  [4] Implementations                              2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): To avoid usage of these I used prototype of `pointer_tagging` from [P3125](https://wg21.link/P3125) which does same functionality but it works also during constant evaluation.
candidate 2 (found by 2 of 15 passes): Each of this option has ups and downs: templates has instantiation and huge cost of AST copying (and in growing executable size), inheritance has virtual tables.
candidate 3 (found by 2 of 15 passes): Every standard library implementation sets a metadata type (a custom vtable) which contains methods how to destroy / copy / move specific type in `std::any`.
candidate 4 (found by 1 of 15 passes): Standard already provides a facility to pass value based anything `std::any`, and in constant evaluator an allocation costs approx. same as normal values

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      0/0/0  -> 0.00
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      0/0/0  -> 0.00
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      0/0/0  -> 0.00
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      1/1/1  -> 1.00
  [4] Implementations                              2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper can be implemented trivially by prepending this sequence with a `if consteval` statement which will pick the allocating behavior for every type.
candidate 2 (found by 3 of 15 passes): Change is visible on my [github](https://github.com/hanickadot/llvm-project/commit/2fd234e55e24ab7265e5c0b050be5af5b86ccc79) and available on compiler explorer under hana's clang.

-->
