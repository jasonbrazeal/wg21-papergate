Verdict: Adequate (7/14)

The paper offers a solid foundation for its core motivation and shows real implementation experience, but it leaves several important parts of the standardization case underdeveloped. The thinnest areas are the failure to show why a library solution cannot suffice and the absence of any discussion of coordination or interoperability with existing features.

- The paper clearly establishes why ordered replacement fields become hard to manage and why a dedicated formatting path is useful, with a working Clang implementation to back that up.
- It also grounds the design in prior proposals and explains how this approach differs from earlier work, which helps situate the idea.
- The claim that string interpolation is widely popular is asserted rather than demonstrated with evidence about affected users or codebases.
- Most notably, the paper never explains why the feature must be a language change rather than a library facility, nor does it address how it would interact with adjacent standardization efforts.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.50/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.50 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.50   corroborated 7.00   accumulate 6.50   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 6.50 / 6.50 / 6.50   (all 3 samples: 6.50)
headings: h2 4
on threshold: implementation
splits: motivation[5] 1/2/2  audience[2] 0/1/1  vehicle[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 6 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               2/2/2  -> 2.00
  [3] 2 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/2/2  -> 1.67
  [6] 4 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 3 of 18 passes): The ability to support this on the other hand is *very* useful for debugging:
candidate 3 (found by 3 of 18 passes): The main motivation (and likely the most common use-case) is some version of formatting, for which all we need is `S::fmt()`.

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
candidate 1 (found by 3 of 18 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different.
candidate 2 (found by 3 of 18 passes): Note that there is no difference in handling between lines `#1-2` and line `#3` in the example (like the P1819 design and unlike the P3412 one).
candidate 3 (found by 2 of 18 passes): It works either way. With delayed concatenation, we rely on phase 5 to concatenate the string literals before parsing anyway.
candidate 4 (found by 2 of 18 passes): This paper *only* proposes template strings, it does *not* propose a convenient shorthand for creating a `std::string`.

## vehicle - grade 0.17 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [4] 2 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [5] 3 Alternate Approaches                       1/0/0  -> 0.33
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
