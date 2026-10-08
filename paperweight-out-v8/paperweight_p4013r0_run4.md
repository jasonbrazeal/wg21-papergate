Verdict: Adequate (6/14)

The paper gives a partial account of why the feature could matter and shows that a workable implementation exists, but it leaves several essential parts of the standardization case unaddressed. The thinnest areas are the absence of any identified user population, the lack of discussion about coordination with other proposals or library facilities, and the failure to explain why this cannot be delivered as an ordinary library extension.

- The strongest support is the concrete implementation experience, with a visible change and a compiler explorer link demonstrating the approach.
- The paper also establishes prior art and alternatives by comparing template and inheritance-based designs and referencing pointer tagging from P3125.
- The claim that the change can be implemented trivially with `if consteval` is asserted but not backed by enough explanation to establish why standardization is necessary.
- Most glaringly, the paper never establishes who is affected or why a library solution would not suffice, leaving the core need for a standard change unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 4 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.33   max 7.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 34 of 35 section-criterion pairs unanimous (97%)
single-sample totals would have been: 6.00 / 6.00 / 6.00   (all 3 samples: 6.00)
headings: h2 4
on threshold: motivation, implementation
splits: motivation[3] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   2/2/2  -> 2.00
  [3] Changes                                      1/1/0  -> 0.67
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper is making `std::any` usable during constant evaluation.
candidate 2 (found by 3 of 15 passes): Each of this option has ups and downs: templates has instantiation and huge cost of AST copying (and in growing executable size), inheritance has virtual tables.
candidate 3 (found by 2 of 15 passes): This paper can be implemented trivially by prepending this sequence with a `if consteval` statement which will pick the allocating behavior for every type.

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
  [3] Changes                                      1/1/1  -> 1.00
  [4] Implementations                              2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Each of this option has ups and downs: templates has instantiation and huge cost of AST copying (and in growing executable size), inheritance has virtual tables.
candidate 2 (found by 3 of 15 passes): Every standard library implementation sets a metadata type (a custom vtable) which contains methods how to destroy / copy / move specific type in `std::any`.
candidate 3 (found by 3 of 15 passes): To avoid usage of these I used prototype of `pointer_tagging` from [P3125](https://wg21.link/P3125) which does same functionality but it works also during constant evaluation.

## vehicle - grade 0.50 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      1/1/1  -> 1.00
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper can be implemented trivially by prepending this sequence with a `if consteval` statement which will pick the allocating behavior for every type.

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

## implementation - grade 2.00  [binary: max] (fired in 1 of 5 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] Changes                                      0/0/0  -> 0.00
  [4] Implementations                              2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Change is visible on my [github](https://github.com/hanickadot/llvm-project/commit/2fd234e55e24ab7265e5c0b050be5af5b86ccc79) and available on compiler explorer under hana's clang.

-->
