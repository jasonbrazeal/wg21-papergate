Verdict: Adequate (4/14)

The paper offers a solid conceptual case for why sender-native gates and counting scopes matter, and it situates the design against a credible history of prior art, but it leaves the standardization argument largely incomplete. The strongest support is for the problem framing and the lineage of the abstractions; the thinnest support is in the areas that would actually justify a standards-track library addition, such as affected users, implementation experience, and why existing libraries cannot suffice.

- The paper clearly establishes that structured asynchronous programs still need non-local ordering and lifetime constraints that the sender model alone does not provide.
- It credibly connects the proposed primitives to established practice in task queues, serializers, asynchronous semaphores, and similar facilities.
- The claim that these gates must be sender-native rather than wrappers over blocking primitives is asserted but not demonstrated.
- The paper does not establish who is affected, what implementation experience exists, or why a library outside the standard cannot meet the need.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 3 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 4.33   accumulate 4.17   max 4.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.00 / 4.50 / 4.00   (all 3 samples: 4.17)
headings: h2 7
on threshold: none
splits: motivation[8] 0/1/1  prior_art[4] 0/1/0  vehicle[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            0/1/1  -> 0.67
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Programs still need to serialize unrelated operations, bound concurrency across independently submitted work, wait for readiness, and coordinate completion or phase boundaries.
candidate 2 (found by 3 of 27 passes): The question is how to express them without falling back to blocking threads, manual signaling protocols, or unstructured lifetime management.
candidate 3 (found by 3 of 27 passes): The sender model gives C++ a vocabulary for structured asynchronous work, but it does not by itself provide replacements for these non-local constraints.
candidate 4 (found by 2 of 27 passes): A gate controls *when* work may execute; a `counting_scope` controls *how long* spawned work remains associated with an enclosing lifetime.

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
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 Old synchronization primitives             0/1/0  -> 0.33
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 1/1/1  -> 1.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            1/1/1  -> 1.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The design is motivated by the ordering relations expressed by existing synchronization primitives, but aims to preserve sender composition, safety invariants, progress, non-blocking waiting, and compatibility with structured lifetime management.
candidate 2 (found by 3 of 27 passes): Some of these abstractions have a long history in practice. Task queues, strands, serializers, asynchronous semaphores, rate limiters, and similar facilities are widely used in asynchronous systems.
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
  [7] 4 Relation to other facilities               0/1/0  -> 0.33
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Gates are not wrappers around blocking primitives; they are sender-native forms of the same kinds of ordering and admission constraints.

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
