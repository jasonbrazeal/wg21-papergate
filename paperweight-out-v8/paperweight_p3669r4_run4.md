Verdict: Adequate to Strong (7/14)

The paper gives a reasonably clear account of the problem it wants to solve and shows some implementation experience, but it leaves several important parts of the standardization case asserted rather than demonstrated. The thinnest support concerns who is affected and why the facility must be standardized rather than provided as a library.

- The strongest support is the explanation of why non-blocking signaling matters for execution environments that cannot tolerate blocking operations.
- The paper also establishes prior art and alternatives by distinguishing its approach from concurrent queues and from an earlier `try_start()` design.
- The most glaring omission is any concrete identification of the users, domains, or workloads that would be affected by the absence of this facility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.83/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 6.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.83   corroborated 8.33   accumulate 7.17   max 8.33

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.83  vehicle 0.50  coordination 0.50  insufficiency 0.17  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 6.50 / 7.50 / 6.50   (all 3 samples: 6.83)
headings: h2 8
on threshold: implementation
splits: motivation[5] 2/2/1  prior_art[5] 1/2/1  prior_art[6] 1/2/2  insufficiency[4] 0/1/0
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 9 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/1  -> 1.67
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `std::execution` as currently specified doesn’t provide support for non-blocking operations.
candidate 2 (found by 3 of 27 passes): Some execution environments want to make sure that specific operations are non-blocking. These can not signal an event using the facilities of `std::execution` as currently specified as it doesn’t provide operations that are guaranteed to be non-blocking.
candidate 3 (found by 2 of 27 passes): If a `start()` on the operation state of a sender returned by `try_schedule()` would block (e.g. for inserting the operation into a work queue protected by a mutex), it immediately calls `set_error(would_block_t())` on the connected receiver.
candidate 4 (found by 1 of 27 passes): In `std::execution` the basic operation to signal an event is to schedule a continuation.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.83 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    1/2/1  -> 1.33
  [6] 4. Naming                                    1/2/2  -> 1.67
  [7] 5. Examples and Implementation               1/1/1  -> 1.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This proposal is completely independent from [C++ Concurrent Queues (P0260)](https://wg21.link/P0260) as the problem of signalling an event in a non-blocking way is not specific to concurrent queues.
candidate 2 (found by 3 of 27 passes): The initial revision of this paper proposed to add a `bool try_start()` operation to the operation states that come from a scheduler and require it to be non-blocking (and to return `false` if it would block).
candidate 3 (found by 3 of 27 passes): `try_schedule` meaning non-blocking (and therefore potentially failing) would be consistent with `try_lock`, `try_push` and `try_pop`, but not with `try_emplace`.
candidate 4 (found by 2 of 27 passes): An implementation of this proposal on top of [execution](https://github.com/bemanproject/execution), [stdexec](https://github.com/NVIDIA/stdexec) and [ustdex](https://github.com/ericniebler/ustdex) is available at

## vehicle - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This proposal is completely independent from [C++ Concurrent Queues (P0260)](https://wg21.link/P0260) as the problem of signalling an event in a non-blocking way is not specific to concurrent queues.

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/1  -> 1.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This became apparent in the proposal for concurrent queues [C++ Concurrent Queues (P0260)](https://wg21.link/P0260), which has support for non-blocking usage, but the problem is far bigger than the concurrent queue issue.

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/1/0  -> 0.33
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): These can not signal an event using the facilities of `std::execution` as currently specified as it doesn’t provide operations that are guaranteed to be non-blocking.

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              0/0/0  -> 0.00
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               2/2/2  -> 2.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): An implementation of this proposal on top of execution, stdexec and ustdex is available at https://gitlab.com/cppzs/std-execution-examples/externals.

-->
