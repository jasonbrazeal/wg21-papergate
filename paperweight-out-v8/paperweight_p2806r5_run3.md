Verdict: Strong (9/14)

The paper offers a solid foundation for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several essential arguments underdeveloped, particularly around who is affected and why the standard library cannot address the need.

- The strongest support comes from the demonstrated implementation in Clang and the compiler explorer link, which shows the feature is more than speculative.
- The paper also clearly establishes why the feature matters by explaining the control-flow limitations of immediately invoked lambdas and the desire to support macros and pattern matching desugaring.
- The thinnest part of the case is the absence of any discussion of who is affected, leaving the audience and impact of the proposal unclear.
- The arguments for why a library solution will not suffice and why standardization is necessary are asserted rather than demonstrated, relying on brief claims without supporting analysis.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 6 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 8.00   accumulate 9.17   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.33  coordination 1.00  insufficiency 1.00  implementation 2.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 8.50 / 8.50 / 10.00   (all 3 samples: 8.83)
headings: h2 6
on threshold: prior_art, vehicle, coordination, insufficiency
splits: motivation[5] 0/0/2  prior_art[4] 0/0/2  vehicle[6] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/2  -> 0.67
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 2 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:
candidate 3 (found by 1 of 24 passes): The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator
candidate 4 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/0  -> 0.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Introduction                               0/0/2  -> 0.67
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.
candidate 2 (found by 3 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add
candidate 3 (found by 1 of 24 passes): It is idiomatic in languages that have pattern matching to allow control flow out of those expressions.

## vehicle - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/2  -> 0.67
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature
candidate 2 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add

## coordination - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/0  -> 0.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of: `pattern => expression;`

## insufficiency - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/0  -> 0.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Proposal Details  (part 1 of 2)            2/2/2  -> 2.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The proposed form [works](https://compiler-explorer.com/z/vMforYcGP).
candidate 2 (found by 3 of 24 passes): This is [implemented in clang](https://github.com/brevzin/llvm-project/commit/ca322b0267ba042db01b111e1380bc7352c2a57d) and can be seen on [compiler explorer](https://compiler-explorer.com/z/vMforYcGP).

-->
