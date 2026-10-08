Verdict: Adequate (4/14)

The paper offers some useful framing for why these abstractions matter and points to recognizable prior art, but it leaves most of the standardization case unargued. The thinnest areas are the ones that usually decide whether a facility belongs in the standard: who is affected, why the standard rather than a library, how implementations would coordinate, and what experience exists.

- The strongest support is the explanation of the problem, which connects gates and counting scopes to real needs in structured asynchronous code without falling back on threads or manual signaling.
- The paper also establishes that similar facilities already exist in practice and sketches how they relate to familiar primitives like semaphores and latches.
- It does not establish who is affected by the proposal, leaving the audience and the scope of impact unclear.
- The most glaring omission is the absence of any case for why this cannot be delivered as a library, along with no implementation experience or interoperability discussion to support standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 2 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 4.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 61 of 63 section-criterion pairs unanimous (97%)
single-sample totals would have been: 4.00 / 4.00 / 4.00   (all 3 samples: 4.00)
headings: h2 7
on threshold: none
splits: motivation[4] 1/1/0  prior_art[2] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 Old synchronization primitives             1/1/0  -> 0.67
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            1/1/1  -> 1.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Programs still need to serialize unrelated operations, bound concurrency across independently submitted work, wait for readiness, and coordinate completion or phase boundaries.
candidate 2 (found by 3 of 27 passes): The question is how to express them without falling back to blocking threads, manual signaling protocols, or unstructured lifetime management.
candidate 3 (found by 3 of 27 passes): The sender model gives C++ a vocabulary for structured asynchronous work, but it does not by itself provide replacements for these non-local constraints.
candidate 4 (found by 3 of 27 passes): A gate controls *when* work may execute; a `counting_scope` controls *how long* spawned work remains associated with an enclosing lifetime.

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 7 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 Old synchronization primitives             1/1/1  -> 1.00
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 1/1/1  -> 1.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            1/1/1  -> 1.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Some of these abstractions have a long history in practice. Task queues, strands, serializers, asynchronous semaphores, rate limiters, and similar facilities are widely used in asynchronous systems.
candidate 2 (found by 3 of 27 passes): A `counting_semaphore` behaves like a `mutex` , but allows more than one concurrent access to the same resource.
candidate 3 (found by 3 of 27 passes): Based on the ideas from [[P3955R0]](https://wg21.link/p3955r0), an API might look like:
candidate 4 (found by 3 of 27 passes): Similar to a `latch` , but for structured concurrency, a `completion_gate` delays dependent work until a fixed number of submitted operations have completed.

## vehicle - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
