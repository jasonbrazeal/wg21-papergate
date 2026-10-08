Verdict: Weak to Adequate (4/14)

The paper offers only preliminary, self-referential support for its standardization case, with most of its arguments resting on general claims about attribute usage and future reflection work rather than demonstrated need or concrete evidence. The thinnest areas are the absence of any case for why the standard is the right venue, why a library solution cannot suffice, or how the feature would coordinate with existing and upcoming language facilities.

- The strongest support is the mention of an experimental implementation available on Compiler Explorer, though even that is only asserted rather than shown through results or usage.
- The paper gestures toward prior art and alternatives by referencing code generation and reflection proposals, but it does not compare its approach against them in any depth.
- The most glaring omission is the complete lack of discussion about why standardization is necessary at all, including why a library-level or existing reflection mechanism would not be adequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.67/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.67   corroborated 3.67   accumulate 4.17   max 4.67

## SUMMARY
grades: motivation 1.33  audience 0.33  prior_art 1.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.00 / 3.00 / 4.00   (all 3 samples: 3.67)
headings: h2 7
on threshold: motivation
splits: motivation[4] 1/0/1  audience[3] 1/0/1
## END SUMMARY

## motivation - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Scope                                      1/0/1  -> 0.67
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We have no way to appertain `[[deprecated]]`, `[[maybe_unused]]`, or any other attributes.
candidate 2 (found by 2 of 24 passes): Ultimately to not force a particular strategy until progress is made on reflection of expressions, the current proposal does not allow `^^[[assume(expr)]]`.

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)
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
candidate 1 (found by 2 of 24 passes): Attributes are used to a great extent, and there is new attributes being added to the language somewhat regularly.

## prior_art - grade 1.00 (fired in 3 of 8 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Scope                                      1/1/1  -> 1.00
  [5] 4 Proposed Features                          1/1/1  -> 1.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We expect a number of applications for attribute introspection to happen in the context of code generation [[P2237R0]](https://wg21.link/p2237r0)
candidate 2 (found by 3 of 24 passes): Here we introduce an alternative terminology to guide the conversation in the context of reflection and attributes
candidate 3 (found by 3 of 24 passes): Passing attributes through the above proposed approach is well in line with the philosophy of leveraging `info` as the opaque vehicle to carry every and all reflections.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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

## implementation - grade 1.00  [binary: max] (fired in 2 of 8 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision history                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Scope                                      1/1/1  -> 1.00
  [5] 4 Proposed Features                          0/0/0  -> 0.00
  [6] 5 Proposed wording                           0/0/0  -> 0.00
  [7] 6 Feedback                                   1/1/1  -> 1.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): In our experimental implementation, we show a possible strategy where we do not transform the expression into a canonical representation before evaluating equality via profiling
candidate 2 (found by 3 of 24 passes): The features presented here are available on compiler explorer<sup>2</sup>.

-->
