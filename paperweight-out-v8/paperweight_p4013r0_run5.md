Verdict: Adequate (6/14)

The paper offers a narrow but genuine foundation for its standardization case: it establishes why the change matters to users, identifies prior art and alternatives, and points to a concrete implementation. The support is thinnest around the institutional questions—who is affected, why the standard is the right venue, how the feature coordinates with existing specifications, and why a library solution cannot suffice—none of which are addressed.

- The strongest support is the demonstrated implementation experience, with a visible compiler change and a link for testing.
- The paper also establishes why the change matters by framing `std::any` constexpr support as removing an unnecessary user tradeoff without ABI breakage.
- Prior art and alternatives are credited through discussion of template and inheritance costs and the use of `pointer_tagging` from P3125.
- The most glaring omission is the absence of any argument for why the standard, rather than a library or implementation extension, is necessary.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.50/14)

Provisionally addressed: 3 of 7. Provisional points: 5.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.50   corroborated 5.00   accumulate 5.83   max 6.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 33 of 35 section-criterion pairs unanimous (94%)
single-sample totals would have been: 5.50 / 5.50 / 5.50   (all 3 samples: 5.50)
headings: h2 4
on threshold: motivation, implementation
splits: motivation[3] 1/0/1  prior_art[3] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 5 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   2/2/2  -> 2.00
  [3] Changes                                      1/0/1  -> 0.67
  [4] Implementations                              0/0/0  -> 0.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper is making `std::any` usable during constant evaluation.
candidate 2 (found by 3 of 15 passes): Users shouldn't do such tradeoff, just because `std::any` is not marked `constexpr`.
candidate 3 (found by 1 of 15 passes): This change doesn't break ABI, is fully compatible with existing code.
candidate 4 (found by 1 of 15 passes): Every standard library implementation sets a metadata type (a custom vtable) which contains methods how to destroy / copy / move specific type in `std::any`.

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
  [3] Changes                                      0/0/1  -> 0.33
  [4] Implementations                              2/2/2  -> 2.00
  [5] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): Each of this option has ups and downs: templates has instantiation and huge cost of AST copying (and in growing executable size), inheritance has virtual tables.
candidate 2 (found by 3 of 15 passes): To avoid usage of these I used prototype of `pointer_tagging` from [P3125](https://wg21.link/P3125) which does same functionality but it works also during constant evaluation.
candidate 3 (found by 1 of 15 passes): Every standard library implementation sets a metadata type (a custom vtable) which contains methods how to destroy / copy / move specific type in `std::any`.

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
