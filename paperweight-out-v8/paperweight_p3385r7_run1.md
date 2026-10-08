Verdict: Adequate (5/14)

The paper offers some concrete support for its standardization case, chiefly through an experimental implementation and a clear statement of the core language gap around appertaining attributes. Beyond that, however, the argument rests largely on assertions and expectations rather than demonstrated need, with the thinnest support around who is affected and how the proposed approach coordinates with existing or future reflection facilities.

- The strongest support is the reported implementation experience, including availability on Compiler Explorer and a described strategy for expression equality.
- The paper clearly establishes why the problem matters by pointing to the absence of any way to appertain attributes such as `[[deprecated]]` or `[[maybe_unused]]`.
- The discussion of prior art and alternatives is asserted but not substantiated, relying on expected applications and a claimed unanimous post-Wroclaw position without showing the underlying evidence.
- The most glaring omission is any account of who is affected by the problem, leaving the audience and practical impact of the proposal unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 6 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.00   accumulate 5.67   max 6.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.33  vehicle 0.33  coordination 0.17  insufficiency 0.17  implementation 1.67
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 6.00 / 5.50 / 4.00   (all 3 samples: 5.17)
headings: h2 7
on threshold: motivation, prior_art, implementation
splits: prior_art[3] 2/2/1  vehicle[3] 1/0/1  coordination[3] 1/0/0  insufficiency[3] 0/1/0
        implementation[7] 2/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Scope                                      1/1/1  -> 1.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We have no way to appertain `[[deprecated]]`, `[[maybe_unused]]`, or any other attributes.
candidate 2 (found by 2 of 24 passes): Feedback post Wroclaw was unanimous on treating the argument clause as a salient property
candidate 3 (found by 1 of 24 passes): Ultimately to not force a particular strategy until progress is made on reflection of expressions, the current proposal does not allow `^^[[assume(expr)]]`.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope                                      0/0/0  -> 0.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/1  -> 1.67
  [4] 3 Scope                                      1/1/1  -> 1.00
  [5] 4 Proposed Features                          1/1/1  -> 1.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Passing attributes through the above proposed approach is well in line with the philosophy of leveraging `info` as the opaque vehicle to carry every and all reflections.
candidate 2 (found by 2 of 24 passes): We expect a number of applications for attribute introspection to happen in the context of code generation [[P2237R0]](https://wg21.link/p2237r0), where for example, one may want to skip over `[[deprecated]]` members, explicitly tag python bindings with `@deprecated` decorators, etc.
candidate 3 (found by 2 of 24 passes): Feedback post Wroclaw was unanimous on treating the argument clause as a salient property
candidate 4 (found by 1 of 24 passes): We expect a number of applications for attribute introspection to happen in the context of code generation [[P2237R0]](https://wg21.link/p2237r0)

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Scope                                      0/0/0  -> 0.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): Having a uniform vehicle to solve this design concern is a major motivation for this paper.

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/0  -> 0.33
  [4] 3 Scope                                      0/0/0  -> 0.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): Having a uniform vehicle to solve this design concern is a major motivation for this paper.

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/0  -> 0.33
  [4] 3 Scope                                      0/0/0  -> 0.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): We have no way to appertain `[[deprecated]]`, `[[maybe_unused]]`, or any other attributes.

## implementation - grade 1.67  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope                                      1/1/1  -> 1.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   2/2/1  -> 1.67
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): In our experimental implementation, we show a possible strategy where we do not transform the expression into a canonical representation before evaluating equality via profiling
candidate 2 (found by 3 of 24 passes): The features presented here are available on compiler explorer<sup>2</sup>.

-->
