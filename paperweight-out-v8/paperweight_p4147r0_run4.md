Verdict: Adequate (4/14)

The paper offers only a narrow foundation for its standardization case: it clearly identifies a missing customization point and why that gap matters, but most of the surrounding argument is asserted rather than demonstrated. The thinnest areas are the absence of any case for why this belongs in the standard rather than in a library, and the lack of implementation experience beyond an early prototype.

- The strongest support is the established need for a way to detect or modify values crossing between constant evaluation and runtime, which the paper identifies as currently impossible.
- The paper claims the feature would be commonly provided by users, but does not show evidence of demand or affected code.
- The discussion of prior art and alternatives gestures at related work and possible wording changes, but does not establish that the proposed approach is the right one.
- The most glaring omission is that the paper never explains why a library solution cannot suffice or why standardization is necessary at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.33   accumulate 4.33   max 4.33

## SUMMARY
grades: motivation 1.50  audience 0.17  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 47 of 49 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.50 / 4.00 / 3.50   (all 3 samples: 3.67)
headings: h2 6
on threshold: motivation
splits: audience[5] 0/1/0  prior_art[7] 1/0/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 1/1/1  -> 1.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    1/1/1  -> 1.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper introduces a customization point which is called when a constant-evaluated value is moving outside of its constant-evaluation
candidate 2 (found by 3 of 21 passes): Currently there is a now way to modify or even detect a value being moved across boundaries of constant-evaluation and runtime-evaluation.
candidate 3 (found by 2 of 21 passes): I think having both would be most friendly to users.
candidate 4 (found by 1 of 21 passes): Member function limits extension of types provided by others, free functions raises question how it will be resolved and where it will be looked for.

## audience - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    0/1/0  -> 0.33
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): I believe such function would be provided by users in their namespace or inside of their types quite commonly.

## prior_art - grade 1.00 (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    1/1/1  -> 1.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      1/0/0  -> 0.33
candidate 1 (found by 3 of 21 passes): I think having both would be most friendly to users.
candidate 2 (found by 2 of 21 passes): This will allow pure library solution for problems like new core wording introduced in [P3771: constexpr mutex, locks, and condition variable](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3771r0.html).
candidate 3 (found by 1 of 21 passes): [P3771: constexpr mutex, locks, and condition variable](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3771r0.html)
candidate 4 (found by 1 of 21 passes): For the first option I will probably change [[dcl.constexpr]](https://eel.is/c++draft/dcl.constexpr#6) by adding a paragraph about the magic function being called for class types objects and same thing would be needed in [[dcl.constinit]](https://eel.is/c++draft/dcl.constinit).

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    0/0/0  -> 0.00
  [6] Implementation                               0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 1 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction                                 0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Design                                       0/0/0  -> 0.00
  [5] Free function or member function or both?    0/0/0  -> 0.00
  [6] Implementation                               1/1/1  -> 1.00
  [7] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): I have started prototyping it after Croydon meeting, but at this moment I'm only interested in EWG's opinion about usefulness of this approach.

-->
