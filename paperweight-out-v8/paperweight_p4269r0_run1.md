Verdict: Adequate to Strong (6/14)

The paper offers a narrow but genuine basis for its standardization case: it clearly explains a real behavioral oddity in `when_all` and shows that the problem has been recognized and worked around in practice. The support is thinnest where the paper needs to show that the change belongs in the standard itself rather than in a library or implementation, and that the proposed behavior is coordinated with the broader senders/receivers design.

- The strongest support is the established account of why the current `when_all` behavior matters, including the observation that an internal stop source creates observable side effects and an unused completion signature.
- The paper also establishes prior art and alternatives by citing an in-the-wild workaround and discussion with Lewis Baker about when a stop source is unnecessary.
- The case for who is affected and for coordination with existing practice is only claimed, resting on a single implementation’s workaround rather than broader evidence.
- The most glaring omission is the absence of any established argument for why the standard must address this, or why a library-level solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.00/14)

Provisionally addressed: 5 of 7. Provisional points: 6.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.00   corroborated 6.00   accumulate 6.33   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.67  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 1.33
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 7.50 / 5.00   (all 3 samples: 6.00)
headings: h2 10
on threshold: prior_art
splits: audience[4] 1/2/1  prior_art[7] 2/1/1  prior_art[9] 1/0/1  coordination[4] 0/2/0
        implementation[4] 2/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 11 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Background                                   1/1/1  -> 1.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Uncertainty of Sender Response               2/2/2  -> 2.00
  [7] Synchronous Senders                          2/2/2  -> 2.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): such a stop source would never be used
candidate 2 (found by 3 of 33 passes): In the unhappy case, wherein any child operation ends with `std::execution::set_error` or `::set_stopped`, `std::execution::when_all` requests that all other children stop, waits for them to end, and then passes on an appropriate unhappy completion.
candidate 3 (found by 3 of 33 passes): Creating a `std::inplace_stop_source` and passing its stop tokens into child operations is an observable side effect (since child operations observe this through their receiver’s environment).
candidate 4 (found by 3 of 33 passes): A bizarre outcome since the second completion signature will never be used.

## audience - grade 0.67 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   1/2/1  -> 1.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

## prior_art - grade 1.67 (fired in 4 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               1/1/1  -> 1.00
  [7] Synchronous Senders                          2/1/1  -> 1.33
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    1/0/1  -> 0.67
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:
candidate 2 (found by 3 of 33 passes): As pointed out to me by Lewis Baker the above is relevant vis-à-vis `std::execution::when_all`.
candidate 3 (found by 3 of 33 passes): Lewis Baker points out that given a fallible sender `s``0` which completes synchronously, and any other sender `s``1`, it is not necessary for `std::execution::when_all(s``0``, s``1``)` to use a stop source.
candidate 4 (found by 2 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [6].

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

## coordination - grade 0.33 (fired in 1 of 11 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   0/2/0  -> 0.67
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`

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

## implementation - grade 1.33  [binary: max] (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/0  -> 1.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    1/1/1  -> 1.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [6].
candidate 2 (found by 2 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

-->
