Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why template strings would be useful and how the proposed design relates to earlier work, but it leaves several parts of the standardization case largely unargued. The strongest material concerns motivation, comparison with alternatives, and the existence of an implementation, while the discussion of affected users, library-only solutions, and coordination with existing features is essentially absent.

- The paper establishes the practical motivation well, especially the difficulty of keeping many replacement fields correctly ordered in `std::format` and the value of a simple `S::fmt()` hook for debugging.
- It also establishes meaningful prior art and design context by distinguishing its behavior from P1819 and P3412 and by acknowledging a possible token-sequence macro route.
- The claim that a small dedicated language feature is preferable to waiting for token sequence injection is asserted, but the paper does not really establish why standardization is the right path rather than a compiler extension or a narrower facility.
- The most glaring omissions are the lack of any account of who is affected, how the feature would interoperate with adjacent language and library machinery, and why a library-based approach cannot suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.00 / 6.00 / 6.50   (all 3 samples: 6.17)
headings: h2 4
on threshold: implementation
splits: motivation[5] 1/1/2  vehicle[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/1/2  -> 1.33
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 3 of 18 passes): The ability to support this on the other hand is *very* useful for debugging:
candidate 3 (found by 3 of 18 passes): The main motivation (and likely the most common use-case) is some version of formatting, for which all we need is `S::fmt()`.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [4] 2 Design  (part 2 of 2)                      1/1/1  -> 1.00
  [5] 3 Alternate Approaches                       2/2/2  -> 2.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Note that there is no difference in handling between lines `#1-2` and line `#3` in the example (like the P1819 design and unlike the P3412 one).
candidate 2 (found by 2 of 18 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different. `interp` is already a `std::string`
candidate 3 (found by 2 of 18 passes): We could conceivably also just introduce a single token and use braces for everything else.
candidate 4 (found by 2 of 18 passes): There even is a proposal, [[P3294R2] (Code Injection with Token Sequences)](https://wg21.link/p3294r2), that has walks through how a future macro could solve this problem.

## vehicle - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/1  -> 0.33
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): I implemented this in Clang, on top of the p2996 reflection branch. Code can be found in my fork in the `template-strings` branch [here](https://github.com/brevzin/llvm-project/tree/template-strings)

-->
