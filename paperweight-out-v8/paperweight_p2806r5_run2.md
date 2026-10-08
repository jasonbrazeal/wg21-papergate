Verdict: Strong (9/14)

The paper offers a solid foundation in some areas, particularly in showing that the feature exists in a working implementation and in situating it against familiar alternatives, but it leaves several essential parts of its standardization case asserted rather than demonstrated. The thinnest support concerns who would actually be affected by the change and why the standard, rather than a library or existing language construct, is the necessary vehicle.

- The strongest support is the implementation experience, with a working clang implementation and a compiler explorer link demonstrating the proposed form.
- The paper also establishes prior art and alternatives clearly, comparing the feature to immediately invoked lambdas and discussing alternative spellings and the Rust `?` operator.
- The most glaring omission is any identification of who is affected by the proposal, leaving the audience and impact of the change unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.00   accumulate 9.17   max 11.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 1.33  coordination 0.83  insufficiency 1.00  implementation 2.00
sample agreement: 49 of 56 section-criterion pairs unanimous (88%)
single-sample totals would have been: 9.00 / 9.00 / 9.50   (all 3 samples: 9.00)
headings: h2 6
on threshold: coordination, insufficiency, implementation
splits: motivation[5] 1/2/2  motivation[6] 2/2/1  prior_art[4] 0/2/0  vehicle[4] 2/0/2
        vehicle[6] 0/2/2  coordination[4] 2/2/1  implementation[5] 2/2/0
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/2  -> 2.00
  [5] 4 Proposal Details  (part 1 of 2)            1/2/2  -> 1.67
  [6] 4 Proposal Details  (part 2 of 2)            2/2/1  -> 1.67
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.
candidate 2 (found by 2 of 24 passes): The temporary `std::vector<int>` doesn’t persist through the whole `do` expression, it gets destroyed too soon — so our `__r` would be holding a dangling `span` (in the non-error case).
candidate 3 (found by 1 of 24 passes): There are a lot of interesting rules that we need to discuss about a `do` expression behaves.
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

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   1/1/1  -> 1.00
  [4] 3 Introduction                               0/2/0  -> 0.67
  [5] 4 Proposal Details  (part 1 of 2)            2/2/2  -> 2.00
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.
candidate 2 (found by 3 of 24 passes): Other alternative spellings we’ve considered: - `do return` (in the previous revision of this paper, which has an ambiguity with `do ... while` loops) - `do_yield` (presented to EWG in Issaquah as the initial pre-publication draft of this proposal)
candidate 3 (found by 3 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add
candidate 4 (found by 1 of 24 passes): The most familiar example might be what Rust’s `?` operator (previously its `try!` macro) desugars as:

## vehicle - grade 1.33 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/0/2  -> 1.33
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/2/2  -> 1.33
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature
candidate 2 (found by 1 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:
candidate 3 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add
candidate 4 (found by 1 of 24 passes): The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add.

## coordination - grade 0.83 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               2/2/1  -> 1.67
  [5] 4 Proposal Details  (part 1 of 2)            0/0/0  -> 0.00
  [6] 4 Proposal Details  (part 2 of 2)            0/0/0  -> 0.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:
candidate 2 (found by 1 of 24 passes): This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of: `pattern => expression;`

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

## implementation - grade 2.00  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Abstract                                   0/0/0  -> 0.00
  [4] 3 Introduction                               0/0/0  -> 0.00
  [5] 4 Proposal Details  (part 1 of 2)            2/2/0  -> 1.33
  [6] 4 Proposal Details  (part 2 of 2)            2/2/2  -> 2.00
  [7] 5 Wording                                    0/0/0  -> 0.00
  [8] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This is [implemented in clang](https://github.com/brevzin/llvm-project/commit/ca322b0267ba042db01b111e1380bc7352c2a57d) and can be seen on [compiler explorer](https://compiler-explorer.com/z/vMforYcGP).
candidate 2 (found by 2 of 24 passes): The proposed form [works](https://compiler-explorer.com/z/vMforYcGP).

-->
