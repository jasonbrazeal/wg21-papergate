Verdict: Adequate (4/14)

The paper offers a partial case for standardization, with its strongest material going to motivation and prior art, but it leaves several essential questions about affected users, implementability, and the limits of a library solution largely unanswered. The support is thinnest where the proposal needs to show that the facility cannot be delivered outside the standard and that there is real implementation experience behind the design.

- The paper establishes why sender-native non-local constraints matter and connects the proposed gates to well-known synchronization and structured-concurrency ideas.
- It claims, but does not establish, that gates require standardization because they add shared state across otherwise independent sender expressions.
- It claims, but does not establish, that the design coordinates cleanly with existing sender composition and interoperability expectations.
- It does not establish who is affected, why a library implementation would be insufficient, or that the design has been validated through implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 4 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.67   accumulate 4.33   max 4.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.17  insufficiency 0.00  implementation 0.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 4.50 / 4.50 / 4.00   (all 3 samples: 4.33)
headings: h2 7
on threshold: none
splits: motivation[4] 0/0/1  vehicle[7] 0/1/0  coordination[3] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               2/2/2  -> 2.00
  [4] 2 Old synchronization primitives             0/0/1  -> 0.33
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            1/1/1  -> 1.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Programs still need to serialize unrelated operations, bound concurrency across independently submitted work, wait for readiness, and coordinate completion or phase boundaries.
candidate 2 (found by 3 of 27 passes): The sender model gives C++ a vocabulary for structured asynchronous work, but it does not by itself provide replacements for these non-local constraints.
candidate 3 (found by 3 of 27 passes): A gate controls *when* work may execute; a `counting_scope` controls *how long* spawned work remains associated with an enclosing lifetime.
candidate 4 (found by 3 of 27 passes): The main question is whether SG1 agrees that C++ needs sender-native primitives for these non-local constraints.

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
  [4] 2 Old synchronization primitives             1/1/1  -> 1.00
  [5] 3 Primitives for non-local concurrency  (... 2/2/2  -> 2.00
  [6] 3 Primitives for non-local concurrency  (... 1/1/1  -> 1.00
  [7] 4 Relation to other facilities               2/2/2  -> 2.00
  [8] 5 The ask for SG1                            1/1/1  -> 1.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The design is motivated by the ordering relations expressed by existing synchronization primitives, but aims to preserve sender composition, safety invariants, progress, non-blocking waiting, and compatibility with structured lifetime management.
candidate 2 (found by 3 of 27 passes): Some of these abstractions have a long history in practice. Task queues, strands, serializers, asynchronous semaphores, rate limiters, and similar facilities are widely used in asynchronous systems.
candidate 3 (found by 3 of 27 passes): Similar to a `latch` , but for structured concurrency, a `completion_gate` delays dependent work until a fixed number of submitted operations have completed.
candidate 4 (found by 3 of 27 passes): The gates proposed in this paper are complementary. A gate controls *when* work may execute; a `counting_scope` controls *how long* spawned work remains associated with an enclosing lifetime.

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
candidate 1 (found by 1 of 27 passes): Gates add shared state that allows different sender expressions to participate in the same non-local constraint.

## coordination - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               1/0/0  -> 0.33
  [4] 2 Old synchronization primitives             0/0/0  -> 0.00
  [5] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [6] 3 Primitives for non-local concurrency  (... 0/0/0  -> 0.00
  [7] 4 Relation to other facilities               0/0/0  -> 0.00
  [8] 5 The ask for SG1                            0/0/0  -> 0.00
  [9] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): A gate is shared by otherwise independent sender expressions, and it imposes a named non-local concurrency constraint on the work associated with it.

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
