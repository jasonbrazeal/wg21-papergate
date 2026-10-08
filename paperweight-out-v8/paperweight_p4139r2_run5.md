Verdict: Adequate (4/14)

The paper offers a narrow but genuine case for revisiting the naming and consistency questions around a lookup-style member function, but it leaves most of the standardization burden unaddressed. The strongest material concerns prior art and the acknowledged instability of the earlier name, while the thinnest areas are the absence of any demonstrated user impact, implementation experience, or reason the facility must live in the standard rather than in a library.

- The paper’s clearest support comes from its engagement with P3091’s naming history and the author’s own reconsideration of `get`, which grounds the discussion in real committee precedent.
- It also establishes that the proposed operation would fit a broader pattern of fallible lookup in the standard library, supporting the consistency argument.
- The paper does not establish who is concretely affected by the absence of this facility, leaving the motivating need largely abstract.
- Most glaringly, it offers no implementation experience and no argument for why the feature cannot be provided adequately by a library.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.17/14)

Provisionally addressed: 3 of 7. Provisional points: 4.17 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.17   corroborated 4.33   accumulate 4.17   max 4.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.17  insufficiency 0.00  implementation 0.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.50 / 4.00 / 4.00   (all 3 samples: 4.17)
headings: h2 7
on threshold: none
splits: prior_art[2] 1/2/2  coordination[4] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            1/1/1  -> 1.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): We conclude that a `get` function returning `optional` after an unbounded search would make it unique among uses of `get` in the library, and so would be inconsistent and confusing.
candidate 2 (found by 3 of 24 passes): Conceptually, `myVector[*index*]` is a lookup operation that could fail if `*index*` is out of range, so member functions similar to the those added to associative containers would fit well in sequence containers, adding to the regularity of the library.
candidate 3 (found by 2 of 24 passes): Since that time, even the author of P3091 has reconsidered the implications of the name `get`.
candidate 4 (found by 1 of 24 passes): In hope of making the C++26 cutoff, the naming discussion was curtailed and the name in P3091 was retained when that paper was forwarded in Sofia.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Change                            0/0/0  -> 0.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/2  -> 1.67
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            2/2/2  -> 2.00
  [6] 5 Alternatives considered                    1/1/1  -> 1.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): P3091 offered names `get_optional` and `lookup_optional`, which failed to evoke enthusiasm in Sofia; and `lookup`, which had supporters, but failed to reach consensus.
candidate 2 (found by 3 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5) proposed a new member function for associative containers returning an `optional<mapped_type&>` that identifies an object if the key is found, or otherwise is empty.
candidate 3 (found by 2 of 24 passes): Since that time, even the author of P3091 has reconsidered the implications of the name `get`.
candidate 4 (found by 2 of 24 passes): The name `get_optional` mentioned in P3091 is not proposed, for reasons that should be clear.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Change                            0/0/0  -> 0.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 1/0/0  -> 0.33
  [5] 4 Proposed Change                            0/0/0  -> 0.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The library has accumulated an assortment of `try_*xxxxx*` members that share the feature of returning in the case of failure, but yield a variety of result types

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Change                            0/0/0  -> 0.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Proposed Change                            0/0/0  -> 0.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
