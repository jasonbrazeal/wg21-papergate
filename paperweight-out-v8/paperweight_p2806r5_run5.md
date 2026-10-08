Verdict: Strong (10/14)

The paper offers solid support for its core motivation, prior art, and implementation experience, but the case thins considerably when it comes to showing who is affected and why existing language or library mechanisms cannot adequately serve those users. The strongest material is concrete and verifiable; the weakest is largely asserted rather than demonstrated.

- The paper clearly establishes why the feature matters by pointing to control-flow limitations that make `break`, `continue`, `return`, and coroutine operations awkward or impossible in expression-like contexts.
- It credibly documents prior art and alternatives, including immediately invoked lambdas and other spellings, and explains why the existing clang extension is not simply being standardized as-is.
- The implementation experience is well supported with links to a working clang implementation and compiler explorer examples.
- The most glaring omission is any evidence about who is affected, leaving the audience and real-world impact of the problem unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.17/14)

Provisionally addressed: 6 of 7. Provisional points: 10.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.17   corroborated 10.00   accumulate 10.17   max 12.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 2.00  coordination 1.00  insufficiency 1.17  implementation 2.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 10.00 / 10.50 / 10.00   (all 3 samples: 10.17)
headings: h2 6
on threshold: coordination, insufficiency
splits: insufficiency[3] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            1/1/1  -> 1.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 3 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add
candidate 3 (found by 2 of 24 passes): There are a lot of interesting rules that we need to discuss about a `do` expression behaves.
candidate 4 (found by 1 of 24 passes): The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator into a `do` expression.

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

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            2/2/2  -> 2.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.
candidate 2 (found by 3 of 24 passes): Other alternative spellings we’ve considered: - `do return` (in the previous revision of this paper, which has an ambiguity with `do ... while` loops) - `do_yield` (presented to EWG in Issaquah as the initial pre-publication draft of this proposal)
candidate 3 (found by 2 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:
candidate 4 (found by 2 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add

## vehicle - grade 2.00 (fired in 2 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature
candidate 2 (found by 2 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:
candidate 3 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add

## coordination - grade 1.00 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of: `pattern => expression;`
candidate 2 (found by 1 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:

## insufficiency - grade 1.17 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/1/0  -> 0.33
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/0  -> 0.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 1 of 24 passes): It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.

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
