Verdict: Adequate to Strong (7/14)

The paper offers a partial but uneven case for standardization, with its strongest material concentrated in the problem description, prior art, and implementation experience. The argument thins considerably around who is affected and why standardization is necessary, and it is silent on coordination, interoperability, and why a library-level solution would not suffice.

- The paper clearly establishes why the issue matters by showing that `when_all` can introduce observable stop-source side effects and that senders do not currently expose whether they respond to stop requests.
- Prior art and implementation experience are well supported, including a workaround in an existing implementation and an implementation against nVidia’s reference `std::execution`.
- The claim about who is affected rests on a single implementation workaround rather than broader evidence of impact across users or codebases.
- The paper does not establish coordination and interoperability concerns, nor does it explain why the problem cannot be addressed adequately by a library rather than by standardizing a change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 7.33   accumulate 7.00   max 8.00

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 1.83  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.50 / 7.50 / 6.50   (all 3 samples: 6.83)
headings: h2 10
on threshold: audience, implementation
splits: motivation[2] 0/0/1  audience[4] 2/2/1  prior_art[3] 0/1/1  prior_art[7] 1/2/2
        prior_art[9] 1/1/0  vehicle[4] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/1  -> 0.33
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

## audience - grade 0.83 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/1  -> 1.67
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

## prior_art - grade 1.83 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/1/1  -> 0.67
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               1/1/1  -> 1.00
  [7] Synchronous Senders                          1/2/2  -> 1.67
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    1/1/0  -> 0.67
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): As pointed out to me by Lewis Baker the above is relevant vis-à-vis `std::execution::when_all`.
candidate 2 (found by 3 of 33 passes): Lewis Baker points out that given a fallible sender `s``0` which completes synchronously, and any other sender `s``1`, it is not necessary for `std::execution::when_all(s``0``, s``1``)` to use a stop source.
candidate 3 (found by 2 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`
candidate 4 (found by 2 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [6].

## vehicle - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/1/0  -> 0.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): Creating a `std::inplace_stop_source` and passing its stop tokens into child operations is an observable side effect (since child operations observe this through their receiver’s environment).

## coordination - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## implementation - grade 2.00  [binary: max] (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
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
