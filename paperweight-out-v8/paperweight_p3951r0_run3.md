Verdict: Adequate to Strong (7/14)

The paper offers a solid foundation for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several essential arguments underdeveloped or entirely unaddressed. The thinnest support concerns coordination with existing features, why a library solution would be insufficient, and who specifically would be affected by the change.

- The strongest support comes from the demonstrated implementation in Clang, which shows the feature is technically feasible and has been explored in practice.
- The paper clearly establishes why the feature matters by connecting it to real difficulties with `std::format` and debugging needs.
- The discussion of prior art and alternatives is well grounded, showing awareness of related proposals and the design space.
- The most glaring omission is the absence of any argument for why this cannot be done as a library, which is a foundational requirement for a language feature proposal.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 5 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 6.33   accumulate 7.50   max 8.33

## SUMMARY
grades: motivation 1.67  audience 0.17  prior_art 2.00  vehicle 1.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 38 of 42 section-criterion pairs unanimous (90%)
single-sample totals would have been: 7.00 / 7.00 / 7.50   (all 3 samples: 7.17)
headings: h2 4
on threshold: motivation, vehicle, implementation
splits: motivation[5] 1/1/2  audience[2] 0/1/0  prior_art[4] 0/0/1  vehicle[2] 1/0/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      1/1/1  -> 1.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/1/2  -> 1.33
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 3 of 18 passes): The main motivation (and likely the most common use-case) is some version of formatting, for which all we need is `S::fmt()`.
candidate 3 (found by 2 of 18 passes): The ability to support this on the other hand is *very* useful for debugging:
candidate 4 (found by 1 of 18 passes): The important thing is to expose all the relevant information to users to let them do whatever they want with it.

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
  [4] 2 Design  (part 2 of 2)                      0/0/1  -> 0.33
  [5] 3 Alternate Approaches                       2/2/2  -> 2.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different. `interp` is already a `std::string`
candidate 2 (found by 3 of 18 passes): This is a difference in the logic proposed in [[P3412R3]](https://wg21.link/p3412r3), which looks specifically for the *token* (not character) `:`.
candidate 3 (found by 2 of 18 passes): This paper *only* proposes template strings, it does *not* propose a convenient shorthand for creating a `std::string`.
candidate 4 (found by 1 of 18 passes): We could conceivably also just introduce a single token and use braces for everything else.

## vehicle - grade 1.33 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/0/1  -> 0.67
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       2/2/2  -> 2.00
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.
candidate 2 (found by 2 of 18 passes): All this complexity buys us is the ability to create a `std::string` in a single character.

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
