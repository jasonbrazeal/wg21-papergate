Verdict: Adequate to Strong (7/14)

The paper gives a partial account of why non-blocking signaling needs a place in `std::execution`, and it is strongest when describing the gap in the current model and the availability of an implementation. The case becomes much thinner around the affected audience, the necessity of standardization as opposed to a library solution, and how the proposed interface would coordinate with related or future facilities.

- The paper clearly establishes that `std::execution` currently lacks operations guaranteed to be non-blocking, and that some execution environments require such a guarantee.
- The discussion of prior work and alternatives is concrete, including the earlier `try_start` design and the availability of an implementation on top of execution, stdexec, and ustdex.
- The paper does not establish who is affected by the problem, leaving the motivating user base largely unspecified.
- The most glaring omission is the absence of a developed argument for why this must be standardized rather than provided as a library, since the paper itself notes the interface could be fixed once a signal-safe notification mechanism exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 6 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.67   accumulate 7.33   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.67  vehicle 0.33  coordination 0.50  insufficiency 0.50  implementation 2.00
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.50 / 7.50 / 6.50   (all 3 samples: 7.00)
headings: h2 8
on threshold: prior_art, implementation
splits: prior_art[2] 1/0/1  prior_art[5] 2/2/0  prior_art[6] 1/2/1  vehicle[4] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/2  -> 2.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `std::execution` as currently specified doesn’t provide support for non-blocking operations.
candidate 2 (found by 3 of 27 passes): Some execution environments want to make sure that specific operations are non-blocking. These can not signal an event using the facilities of `std::execution` as currently specified as it doesn’t provide operations that are guaranteed to be non-blocking.
candidate 3 (found by 2 of 27 passes): If a `start()` on the operation state of a sender returned by `try_schedule()` would block (e.g. for inserting the operation into a work queue protected by a mutex), it immediately calls `set_error(would_block_t())` on the connected receiver.
candidate 4 (found by 1 of 27 passes): In practice this generally means that a `start` operation is called on an operation state that comes from a sender provided by a scheduler.

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

## prior_art - grade 1.67 (fired in 5 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/1  -> 0.67
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              2/2/2  -> 2.00
  [5] 3. Design                                    2/2/0  -> 1.33
  [6] 4. Naming                                    1/2/1  -> 1.33
  [7] 5. Examples and Implementation               1/1/1  -> 1.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This proposal is completely independent from [C++ Concurrent Queues (P0260)](https://wg21.link/P0260) as the problem of signalling an event in a non-blocking way is not specific to concurrent queues.
candidate 2 (found by 2 of 27 passes): `std::execution` as currently specified doesn’t provide support for non-blocking operations.
candidate 3 (found by 2 of 27 passes): The initial revision of this paper proposed to add a `bool try_start()` operation to the operation states that come from a scheduler and require it to be non-blocking (and to return `false` if it would block).
candidate 4 (found by 2 of 27 passes): Originally, this paper proposed a `try_start` function as member of a special operation state and the related concept was called `concurrent-op-state`.

## vehicle - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Revision History                          0/0/0  -> 0.00
  [4] 2. Introduction                              1/1/0  -> 0.67
  [5] 3. Design                                    0/0/0  -> 0.00
  [6] 4. Naming                                    0/0/0  -> 0.00
  [7] 5. Examples and Implementation               0/0/0  -> 0.00
  [8] 6. Proposed Wording                          0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): This interface can be fixed as soon as there exist a signal-safe mechanism to notify S/R.

## coordination - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): This interface can be fixed as soon as there exist a signal-safe mechanism to notify S/R.
candidate 2 (found by 1 of 27 passes): This proposal is completely independent from [C++ Concurrent Queues (P0260)](https://wg21.link/P0260) as the problem of signalling an event in a non-blocking way is not specific to concurrent queues.

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): These can not signal an event using the facilities of `std::execution` as currently specified as it doesn’t provide operations that are guaranteed to be non-blocking.
candidate 2 (found by 1 of 27 passes): This interface can be fixed as soon as there exist a signal-safe mechanism to notify S/R.

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
