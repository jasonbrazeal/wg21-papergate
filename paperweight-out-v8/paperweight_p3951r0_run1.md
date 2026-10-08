Verdict: Adequate to Strong (7/14)

The paper gives a reasonably grounded account of the problem and shows real implementation experience, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support is around coordination with existing features and the claim that a library solution cannot suffice.

- The strongest support comes from the concrete Clang implementation, which shows the feature is at least buildable and gives the proposal a practical anchor.
- The discussion of prior art and alternatives is well developed, including comparison with earlier designs and acknowledgment of possible macro-based futures.
- The case for why this belongs in the standard leans on a prediction about token sequence injection rather than evidence about the limits of library approaches.
- The paper does not establish how the feature would coordinate or interoperate with related standardization efforts or existing language machinery.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.67   accumulate 7.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.67  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.00 / 7.50 / 6.50   (all 3 samples: 7.00)
headings: h2 4
on threshold: implementation
splits: motivation[3] 2/1/1  audience[2] 0/1/0  vehicle[5] 1/2/1  insufficiency[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      2/1/1  -> 1.33
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       2/2/2  -> 2.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 3 of 18 passes): The main motivation (and likely the most common use-case) is some version of formatting, for which all we need is `S::fmt()`.
candidate 3 (found by 2 of 18 passes): The ability to support this on the other hand is *very* useful for debugging:
candidate 4 (found by 1 of 18 passes): It is at most a minor burden on users as I doubt this approach is in widespread use, and allows for a design that is as simple as possible.

## audience - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/1/0  -> 0.33
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): String interpolation is a wildly popular language feature due to the ease with which it allows users to express complex ideas.

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [4] 2 Design  (part 2 of 2)                      1/1/1  -> 1.00
  [5] 3 Alternate Approaches                       2/2/2  -> 2.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): We could conceivably also just introduce a single token and use braces for everything else.
candidate 2 (found by 3 of 18 passes): There even is a proposal, [[P3294R2] (Code Injection with Token Sequences)](https://wg21.link/p3294r2), that has walks through how a future macro could solve this problem.
candidate 3 (found by 2 of 18 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different.
candidate 4 (found by 2 of 18 passes): Note that there is no difference in handling between lines `#1-2` and line `#3` in the example (like the P1819 design and unlike the P3412 one).

## vehicle - grade 0.67 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/2/1  -> 1.33
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.

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

## insufficiency - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/0/0  -> 0.33
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): Given those pieces, the implementation of something like Rust’s `format_args!` is basically the same as how you would implement it in a compiler.

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
