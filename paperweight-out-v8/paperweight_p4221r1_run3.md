Verdict: Weak (3/14)

The paper offers a narrow but genuine rationale for why the proposed operations would improve clarity in concurrent code, but it leaves most of the standardization case unaddressed. The strongest support is motivational, while the absence of any discussion of affected users, implementation experience, or why a library cannot suffice leaves the proposal largely unsubstantiated.

- The paper clearly establishes that the operations would express intent more directly than a separate atomic load and manual comparison, and that they would avoid fragility under refactoring.
- The paper gestures at prior art by pointing to existing `compare_exchange` semantics, but it does not actually establish that the proposed checks are a recognized alternative in practice.
- The paper does not identify who would be affected by the change or what problem they currently face at a scale that standardization would address.
- The most glaring omission is the complete lack of implementation experience or any argument for why this cannot be provided as a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (2.83/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 2.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 2.83   corroborated 2.67   accumulate 3.17   max 3.67

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 2.50 / 3.00 / 3.00   (all 3 samples: 2.83)
headings: h2 7
on threshold: motivation
splits: motivation[3] 0/0/1  prior_art[7] 1/0/0  vehicle[4] 0/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/1  -> 0.33
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Background                                   0/0/0  -> 0.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     2/2/2  -> 2.00
  [8] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The primary motivation is to provide dedicated operations that express intent more clearly than an atomic `load` followed separately by a manual comparison of non-atomic values.
candidate 2 (found by 3 of 24 passes): While `'if (owner.load() == my_id)'` avoids naming a local variable, it is fragile under refactoring, for instance, when adding debug logging.
candidate 3 (found by 1 of 24 passes): These functions perform an atomic comparison of the atomic object's value with an expected value, following the same bitwise comparison semantics as `compare_exchange_strong`, but without writing a new value to the atomic object.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Background                                   0/0/0  -> 0.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 3 of 8 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   1/1/1  -> 1.00
  [5] Background                                   1/1/1  -> 1.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     1/0/0  -> 0.33
  [8] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Atomic bitwise equality checks offer concurrent programmers an alternative to raw-pointer equality checks (`==`), consistent with compare_exchange equality check semantics.
candidate 2 (found by 3 of 24 passes): The existing `compare_exchange` operations, `compare_exchange_weak` and `compare_exchange_strong`, are defined in **[[atomics.types.operations]](https://eel.is/c++draft/atomics#types.operations)** p21–28.
candidate 3 (found by 1 of 24 passes): Concurrent code on the right avoids raw-pointer equality checks (==).

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/1/1  -> 0.67
  [5] Background                                   0/0/0  -> 0.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): By providing dedicated member functions, the API allows the programmer to specify equality checks directly, supporting both pure predicates and integrated updates of the expected argument.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Background                                   0/0/0  -> 0.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Background                                   0/0/0  -> 0.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Introduction 2                               0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Motivation                                   0/0/0  -> 0.00
  [5] Background                                   0/0/0  -> 0.00
  [6] Proposed Functions                           0/0/0  -> 0.00
  [7] Overview                                     0/0/0  -> 0.00
  [8] Proposed Wording                             0/0/0  -> 0.00
candidates: (none validated)

-->
