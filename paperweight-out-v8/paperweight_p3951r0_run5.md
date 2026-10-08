Verdict: Adequate (7/14)

The paper offers solid support in a few important areas, particularly in showing why the feature matters, engaging with prior designs, and providing implementation experience. The case is much thinner on the questions that are often decisive for standardization: who exactly is affected, why the standard is the right venue, and why a library solution is insufficient. The absence of any discussion of coordination and interoperability is the most obvious gap.

- The strongest support is the concrete implementation in Clang, which demonstrates that the feature is more than a sketch.
- The paper also does well to compare its approach against earlier proposals and to explain the readability and debugging benefits.
- The weakest part is the lack of any established argument for coordination and interoperability with existing or expected features.
- The claims about affected users and the necessity of a language feature rather than a library facility remain asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 6.67   accumulate 7.00   max 7.67

## SUMMARY
grades: motivation 1.67  audience 0.33  prior_art 2.00  vehicle 0.50  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 36 of 42 section-criterion pairs unanimous (86%)
single-sample totals would have been: 6.50 / 6.50 / 7.00   (all 3 samples: 6.67)
headings: h2 4
on threshold: motivation, implementation
splits: motivation[3] 1/2/1  motivation[5] 1/2/1  audience[2] 0/1/1  vehicle[2] 0/0/1
        vehicle[5] 1/0/1  insufficiency[2] 1/0/0
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      1/2/1  -> 1.33
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/2/1  -> 1.33
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 2 of 18 passes): The ability to support this on the other hand is *very* useful for debugging:
candidate 3 (found by 2 of 18 passes): The reasoning here is that moving from `a` to `b` is a significant gain in readability (as well as other functionality, as illustrated in previous examples), but the gain from `b` to `c` is simply saving a few characters.
candidate 4 (found by 1 of 18 passes): It is also quite easy to implement, since it’s just a matter of checking if the last lexed token of the expression was an `=`.

## audience - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/1/1  -> 0.67
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): String interpolation is a wildly popular language feature due to the ease with which it allows users to express complex ideas.

## prior_art - grade 2.00 (fired in 4 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [4] 2 Design  (part 2 of 2)                      1/1/1  -> 1.00
  [5] 3 Alternate Approaches                       2/2/2  -> 2.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different. `interp` is already a `std::string`
candidate 2 (found by 3 of 18 passes): Note that there is no difference in handling between lines `#1-2` and line `#3` in the example (like the P1819 design and unlike the P3412 one).
candidate 3 (found by 3 of 18 passes): We could conceivably also just introduce a single token and use braces for everything else.
candidate 4 (found by 2 of 18 passes): There even is a proposal, [[P3294R2] (Code Injection with Token Sequences)](https://wg21.link/p3294r2), that has walks through how a future macro could solve this problem.

## vehicle - grade 0.50 (fired in 2 of 6 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/1  -> 0.33
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/0/1  -> 0.67
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.
candidate 2 (found by 1 of 18 passes): All this complexity buys us is the ability to create a `std::string` in a single character.

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
  [2] 1 Introduction                               1/0/0  -> 0.33
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       0/0/0  -> 0.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): The original motivation for the lambda approach was ease of use — get all the expressions in one convenient format. But the language has evolved since 2019.

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
