Verdict: Adequate (4/14)

The paper offers a narrow but genuine case for why the naming question matters and why the previously considered alternatives were unsatisfactory, but it leaves most of the standardization rationale unaddressed. The support is thinnest around the questions that would normally justify committee action: who is affected, why a library solution is insufficient, and whether there is any implementation experience.

- The paper establishes that the naming inconsistency around `get` would cause real confusion and that existing library conventions argue against the proposed use.
- It also establishes that the prior naming alternatives from P3091 were considered and found wanting, and that even the original author has reconsidered.
- The paper does not establish who would be affected by the change or what practical problem it solves for them.
- Most glaringly, it offers no argument for why this belongs in the standard rather than in a library, and no implementation experience to support standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.00   accumulate 3.83   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 55 of 56 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h2 7
on threshold: motivation
splits: motivation[5] 1/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            1/1/0  -> 0.67
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): In hope of making the C++26 cutoff, the naming discussion was curtailed and the name in P3091 was retained when that paper was forwarded in Sofia.
candidate 2 (found by 2 of 24 passes): We conclude that a `get` function returning `optional` after an unbounded search would make it unique among uses of `get` in the library, and so would be inconsistent and confusing.
candidate 3 (found by 2 of 24 passes): It is common to downplay the importance of naming, but bad names do real harm.
candidate 4 (found by 1 of 24 passes): The name of the desired operation should reflect that the lookup may take variable time and could return without finding the value being sought; existing instances of `get` in the Library forbid both.

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

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   2/2/2  -> 2.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            2/2/2  -> 2.00
  [6] 5 Alternatives considered                    1/1/1  -> 1.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Since that time, even the author of P3091 has reconsidered the implications of the name `get`.
candidate 2 (found by 3 of 24 passes): P3091 offered names `get_optional` and `lookup_optional`, which failed to evoke enthusiasm in Sofia; and `lookup`, which had supporters, but failed to reach consensus.
candidate 3 (found by 3 of 24 passes): The name `get_optional` mentioned in P3091 is not proposed, for reasons that should be clear.
candidate 4 (found by 1 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5) proposed a new member function for associative containers returning an `optional<mapped_type&>` that identifies an object if the key is found, or otherwise is empty.

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

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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
