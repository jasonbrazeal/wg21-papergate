Verdict: Weak to Adequate (3/14)

The paper offers a narrow but genuine rationale for ordering `meta::info`, grounded in existing work on `type_order` and the convenience of using standard algorithms over reflection values. Its support is thinnest, however, in connecting that rationale to the standardization process itself: it does not show who is affected, why a library solution would be insufficient, or that the feature has been tried in practice.

- The strongest support is the explicit consistency with P2830R10’s `type_order`, which gives the proposal a clear anchor in prior art and an agreed design constraint.
- The paper also establishes why the feature matters by pointing to concrete metaprogramming needs such as sorting types and functions into a canonical order.
- The most glaring omission is the absence of any argument for why this cannot be provided as a library facility rather than a core language or standard library change.
- Equally unaddressed are the affected audience and implementation experience, leaving the proposal without evidence of demand or feasibility.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.00   accumulate 3.50   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.50 / 3.50 / 3.00   (all 3 samples: 3.33)
headings: h2 6
on threshold: motivation
splits: prior_art[4] 2/2/1
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  0/0/0  -> 0.00
  [3] 2. Background                                1/1/1  -> 1.00
  [4] 3. Motivation                                2/2/2  -> 2.00
  [5] 4. Implementation                            0/0/0  -> 0.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Being able to compare `meta::info` directly makes metaprogramming that needs to sort types, functions, etc... into some canonical order with standard algorithms more convenient.
candidate 2 (found by 2 of 21 passes): Therefore arbitrary reflection values are subject to ordering through indirection to class template specializations:
candidate 3 (found by 1 of 21 passes): This means that class template specializations can have constant template arguments of `meta::info` type. Therefore arbitrary reflection values are subject to ordering through indirection to class template specializations:

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Implementation                            0/0/0  -> 0.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.83 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  1/1/1  -> 1.00
  [3] 2. Background                                1/1/1  -> 1.00
  [4] 3. Motivation                                2/2/1  -> 1.67
  [5] 4. Implementation                            2/2/2  -> 2.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): I propose `meta::info` to be three way comparable with an implementation-defined strong order, consistent with `std::type_order` for reflections that represent types.
candidate 2 (found by 3 of 21 passes): [P2830R10] introduced `type_order`, which exposes an implementation-defined `consteval` strong order on types.
candidate 3 (found by 3 of 21 passes): [P2830R10] argues that any `operator<=>(meta::info, meta::info)` should be consistent with `type_order`. I agree.
candidate 4 (found by 2 of 21 passes): Consider `type_set`, one of the motivating examples of [P2830R10]:

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Implementation                            0/0/0  -> 0.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Implementation                            0/0/0  -> 0.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Implementation                            0/0/0  -> 0.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Proposal                                  0/0/0  -> 0.00
  [3] 2. Background                                0/0/0  -> 0.00
  [4] 3. Motivation                                0/0/0  -> 0.00
  [5] 4. Implementation                            0/0/0  -> 0.00
  [6] 5. Wording                                   0/0/0  -> 0.00
  [7] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
