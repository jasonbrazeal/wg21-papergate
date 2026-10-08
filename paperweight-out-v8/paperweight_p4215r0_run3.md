Verdict: Adequate (5/14)

The paper offers a partial foundation for its standardization case, with the strongest material going to the relevance of the problem and the existence of familiar prior art, but it leaves several essential questions essentially unaddressed. The thinnest areas are the absence of any identified audience, the lack of evidence that a library solution is insufficient, and the absence of implementation experience beyond a general historical claim.

- The paper does establish that the problem is real and that similar abstractions are widely used in asynchronous systems.
- It also establishes that the proposed gates have recognizable analogues in existing practice, such as mutexes and latches.
- The claim that standardization is necessary rests on a single assertion about preventing manual acquire/release protocols, without showing why a library cannot provide that protection.
- The paper does not identify who would be affected by standardization or provide concrete implementation experience for the proposed facilities.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 4 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.67   accumulate 4.50   max 4.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.33
sample agreement: 59 of 63 section-criterion pairs unanimous (94%)
single-sample totals would have been: 4.50 / 5.00 / 4.00   (all 3 samples: 4.50)
headings: h2 7
on threshold: none
splits: motivation[4] 1/1/0  prior_art[4] 1/1/0  vehicle[7] 1/0/0  implementation[3] 0/1/0
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

## prior_art - grade 2.00 (fired in 7 of 9 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 Old synchronization primitives             1/1/0  -> 0.67
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            1/1/1  -> 1.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Some of these abstractions have a long history in practice. Task queues, strands, serializers, asynchronous semaphores, rate limiters, and similar facilities are widely used in asynchronous systems.
candidate 2 (found by 3 of 27 passes): Similar to a `mutex` but for the structured concurrency world, a `serial_gate` ensures that only one work item is executed at a given time.
candidate 3 (found by 3 of 27 passes): Similar to a `latch` , but for structured concurrency, a `completion_gate` delays dependent work until a fixed number of submitted operations have completed.
candidate 4 (found by 3 of 27 passes): Is the connection to [[P3955R0]](https://wg21.link/p3955r0) the right foundation for these primitives, or should gates be expressed through a different sender vocabulary?

## vehicle - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               1/0/0  -> 0.33
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This is what prevents the gate from degenerating into a manual acquire/release protocol.

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

## implementation - grade 0.33  [binary: max] (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/1/0  -> 0.33
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Some of these abstractions have a long history in practice. Task queues, strands, serializers, asynchronous semaphores, rate limiters, and similar facilities are widely used in asynchronous systems.

-->
