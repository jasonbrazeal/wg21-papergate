Verdict: Strong (9/14)

The paper offers meaningful support in a few areas, particularly by demonstrating implementation experience and by explaining the expressive limitations of immediately invoked lambdas, but it leaves several essential parts of the standardization case asserted rather than shown. The thinnest support concerns who is affected, why a library solution is insufficient, and how the feature would coordinate with existing or forthcoming language facilities.

- The strongest support is the working implementation in Clang, which shows the proposed syntax and semantics are at least concretely realizable.
- The paper also establishes relevant prior art by connecting the idea to immediately invoked lambdas and to the pattern matching proposal’s needs.
- The case for why this belongs in the standard rather than in a library is claimed but not established, since the paper does not fully rule out library-based or alternative language approaches.
- The most glaring omission is any account of who is affected by the problem, leaving the audience and practical motivation largely unspecified.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 6 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 7.67   accumulate 8.83   max 10.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.67  coordination 1.00  insufficiency 1.33  implementation 2.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.50 / 9.00 / 9.50   (all 3 samples: 8.50)
headings: h2 6
on threshold: prior_art, coordination, insufficiency
splits: motivation[5] 1/2/2  prior_art[6] 0/2/0  vehicle[4] 0/2/0  vehicle[6] 0/0/2
        insufficiency[6] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            1/2/2  -> 1.67
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 2 of 24 passes): The temporary `std::vector<int>` doesn’t persist through the whole `do` expression, it gets destroyed too soon — so our `__r` would be holding a dangling `span` (in the non-error case).
candidate 3 (found by 2 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:
candidate 4 (found by 1 of 24 passes): There are a lot of interesting rules that we need to discuss about a `do` expression behaves.

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
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/2/0  -> 0.67
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.
candidate 2 (found by 3 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:
candidate 3 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:

## vehicle - grade 0.67 (fired in 2 of 8 sections, strong in 0)
under each rule: top2 0.67   corroborated 0.67   accumulate 0.67   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/2/0  -> 0.67
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/2  -> 0.67
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature
candidate 2 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add

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
candidate 1 (found by 3 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:

## insufficiency - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:

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
