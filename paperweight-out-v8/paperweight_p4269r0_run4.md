Verdict: Adequate (6/14)

The paper offers meaningful support in a few areas, particularly in explaining the problem and showing that the idea has been tried in practice, but it leaves several core standardization questions essentially unaddressed. The thinnest parts concern why this needs to be in the standard, why a library solution would not suffice, and how the proposed facility would coordinate with existing or future sender/receiver machinery.

- The strongest support is the clear motivation for why the current `when_all` behavior creates observable side effects and can produce completion signatures that will never be used.
- The paper also establishes relevant prior art and implementation experience, including a workaround in an existing implementation and an implementation against NVIDIA’s reference library.
- The most glaring omission is the absence of any established case for why the standard should adopt this rather than leaving it to libraries.
- The paper likewise does not establish coordination and interoperability with the broader `std::execution` design or with other sender adaptors.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.67   accumulate 6.33   max 7.00

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 1.67
sample agreement: 74 of 77 section-criterion pairs unanimous (96%)
single-sample totals would have been: 7.00 / 5.00 / 6.50   (all 3 samples: 6.17)
headings: h2 10
on threshold: implementation
splits: audience[4] 2/1/1  prior_art[7] 2/1/2  implementation[4] 2/1/2
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
candidate 1 (found by 3 of 33 passes): In the unhappy case, wherein any child operation ends with `std::execution::set_error` or `::set_stopped`, `std::execution::when_all` requests that all other children stop, waits for them to end, and then passes on an appropriate unhappy completion.
candidate 2 (found by 3 of 33 passes): Creating a `std::inplace_stop_source` and passing its stop tokens into child operations is an observable side effect (since child operations observe this through their receiver’s environment).
candidate 3 (found by 3 of 33 passes): A bizarre outcome since the second completion signature will never be used.
candidate 4 (found by 3 of 33 passes): Unfortunately, due to the above analysis, we cannot determine whether a sender responds to stop requests, because senders do not currently publish generically-consumable information about this property.

## audience - grade 0.67 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/1/1  -> 1.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               0/0/0  -> 0.00
  [7] Synchronous Senders                          0/0/0  -> 0.00
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    0/0/0  -> 0.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

## prior_art - grade 1.83 (fired in 4 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/2/2  -> 2.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Uncertainty of Sender Response               1/1/1  -> 1.00
  [7] Synchronous Senders                          2/1/2  -> 1.67
  [8] Proposal                                     0/0/0  -> 0.00
  [9] Implementation Experience                    1/1/1  -> 1.00
  [10] Acknowledgments                              0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): As pointed out to me by Lewis Baker the above is relevant vis-à-vis `std::execution::when_all`.
candidate 2 (found by 3 of 33 passes): Lewis Baker points out that given a fallible sender `s``0` which completes synchronously, and any other sender `s``1`, it is not necessary for `std::execution::when_all(s``0``, s``1``)` to use a stop source.
candidate 3 (found by 3 of 33 passes): This paper has been implemented against nVidia’s reference implementation of `std::execution` [6].
candidate 4 (found by 2 of 33 passes): At least one senders/receivers implementation in the wild [2] works around/avoids the above by defining `when_all(s)` as being equivalent to `s`:

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

## implementation - grade 1.67  [binary: max] (fired in 2 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Background                                   0/0/0  -> 0.00
  [4] Discussion                                   2/1/2  -> 1.67
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
