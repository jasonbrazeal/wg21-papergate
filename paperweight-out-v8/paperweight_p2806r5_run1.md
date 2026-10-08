Verdict: Strong (9/14)

The paper gives a reasonably concrete account of why the feature is useful and shows working implementation experience, but it leaves several parts of the standardization case asserted rather than demonstrated, particularly around affected users, interoperability, and why a library approach cannot suffice.

- The strongest support is the implementation experience, with links to a working compiler implementation and a live example.
- The paper also clearly establishes why the feature matters by showing concrete failure modes with existing constructs such as immediately invoked lambdas and temporary lifetime problems.
- Prior art and alternatives are adequately grounded through comparison with immediately invoked lambdas and the pattern matching proposal.
- The thinnest part is the absence of any established audience or affected-user evidence, leaving it unclear who is asking for this or how widespread the need is.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 6 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 8.00   accumulate 9.17   max 11.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 1.33  coordination 0.83  insufficiency 1.00  implementation 2.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 9.00 / 8.50 / 9.50   (all 3 samples: 8.83)
headings: h2 6
on threshold: prior_art, vehicle, coordination, insufficiency
splits: prior_art[6] 2/0/2  vehicle[6] 1/0/1  coordination[4] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            2/2/2  -> 2.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 3 of 24 passes): The temporary `std::vector<int>` doesn’t persist through the whole `do` expression, it gets destroyed too soon — so our `__r` would be holding a dangling `span` (in the non-error case).
candidate 3 (found by 3 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:

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

## prior_art - grade 1.67 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            2/0/2  -> 1.33
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.
candidate 2 (found by 3 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:
candidate 3 (found by 2 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:

## vehicle - grade 1.33 (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            1/0/1  -> 0.67
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature
candidate 2 (found by 2 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add

## coordination - grade 0.83 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               1/2/2  -> 1.67
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/0  -> 0.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:

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
