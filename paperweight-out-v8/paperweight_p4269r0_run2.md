Verdict: Adequate (6/14)

The paper offers a partial case for standardization, with its strongest material concentrated in explaining the problem and showing that the issue has been recognized in prior work and implementation practice. The support becomes noticeably thinner when the paper turns to the standard’s role, interoperability, and whether the proposed facility could be delivered outside the standard.

- The paper clearly establishes why the current behavior of `when_all` creates an observable and avoidable side effect in the unhappy path.
- It also establishes that the problem has prior art and has been discussed with implementers, including a concrete workaround in an existing implementation.
- The weakest part of the case is the absence of an established argument for why this needs to be addressed in the standard itself rather than through a library or implementation-level solution.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 6 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 7.00   accumulate 6.17   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.17  implementation 1.33
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 5.50 / 6.00 / 7.00   (all 3 samples: 6.17)
headings: h2 10
on threshold: none
splits: motivation[2] 1/0/1  prior_art[3] 0/0/1  prior_art[9] 1/0/0  coordination[4] 0/0/1
        insufficiency[7] 0/1/0  implementation[4] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Uncertainty of Sender Response               2/2/2  -> 2.00
  [7] Synchronous Senders                          2/2/2  -> 2.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): In the unhappy case, wherein any child operation ends with `std::execution::set_error` or `::set_stopped`, `std::execution::when_all` requests that all other children stop, waits for them to end, and then passes on an appropriate unhappy completion.
candidate 2 (found by 3 of 33 passes): Creating a `std::inplace_stop_source` and passing its stop tokens into child operations is an observable side effect (since child operations observe this through their receiver’s environment).
candidate 3 (found by 3 of 33 passes): A bizarre outcome since the second completion signature will never be used.
candidate 4 (found by 3 of 33 passes): Unfortunately, due to the above analysis, we cannot determine whether a sender responds to stop requests, because senders do not currently publish generically-consumable information about this property.

## audience - grade 0.50 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/1/1  -> 1.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/1  -> 0.33
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               1/1/1  -> 1.00
  [7] Synchronous Senders                          2/2/2  -> 2.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    1/0/0  -> 0.33
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`
candidate 2 (found by 3 of 33 passes): As pointed out to me by Lewis Baker the above is relevant vis-à-vis `std::execution::when_all`.
candidate 3 (found by 3 of 33 passes): Lewis Baker points out that given a fallible sender `s``0` which completes synchronously, and any other sender `s``1`, it is not necessary for `std::execution::when_all(s``0``, s``1``)` to use a stop source.
candidate 4 (found by 1 of 33 passes): `std::execution::when_all` accepts one (soon to be zero [1]) or more senders and returns a sender

## vehicle - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/1  -> 0.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

## insufficiency - grade 0.17 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/0/0  -> 0.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/1/0  -> 0.33
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): We don’t have the ability to determine whether or not a sender’s associated asynchronous operation is synchronous [5] (beyond running the operation, by which time it’s too late to decide whether to compile the code to use a stop source).

## implementation - grade 1.33  [binary: max] (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/1/2  -> 1.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    1/1/1  -> 1.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:
candidate 2 (found by 3 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [6].

-->
