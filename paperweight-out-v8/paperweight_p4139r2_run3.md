Verdict: Adequate (4/14)

The paper offers focused support for the naming problem it addresses, but little else that would justify standardization on its own. Its strongest material concerns why the operation matters and how the proposed name relates to prior discussion, while the case for putting this in the standard, rather than elsewhere, is essentially absent.

- The paper clearly establishes that the proposed operation fills a real semantic gap and that the name should signal a potentially failing, variable-time lookup.
- It also establishes meaningful prior art and alternatives, showing how earlier names were considered and why the current direction emerged from that discussion.
- The most glaring omission is any explanation of who is affected or why this belongs in the standard library specifically.
- The paper also offers no implementation experience, no coordination or interoperability analysis, and no argument that a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 2 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 4.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.50 / 4.00 / 4.00   (all 3 samples: 3.83)
headings: h2 7
on threshold: none
splits: motivation[2] 1/2/2  prior_art[2] 1/2/2  prior_art[7] 1/0/0
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/2  -> 1.67
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            1/1/1  -> 1.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Since that time, even the author of P3091 has reconsidered the implications of the name `get`.
candidate 2 (found by 3 of 24 passes): Conceptually, `myVector[*index*]` is a lookup operation that could fail if `*index*` is out of range, so member functions similar to the those added to associative containers would fit well in sequence containers, adding to the regularity of the library.
candidate 3 (found by 2 of 24 passes): We conclude that a `get` function returning `optional` after an unbounded search would make it unique among uses of `get` in the library, and so would be inconsistent and confusing.
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

## prior_art - grade 2.00 (fired in 5 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/2  -> 1.67
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            2/2/2  -> 2.00
  [6] 5 Alternatives considered                    1/1/1  -> 1.00
  [7] 6 Wording                                    1/0/0  -> 0.33
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): P3091 offered names `get_optional` and `lookup_optional`, which failed to evoke enthusiasm in Sofia; and `lookup`, which had supporters, but failed to reach consensus.
candidate 2 (found by 2 of 24 passes): Since that time, even the author of P3091 has reconsidered the implications of the name `get`.
candidate 3 (found by 2 of 24 passes): The name `lookup_optional` meets the stated criteria, except for its length.
candidate 4 (found by 1 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5), forwarded to LWG for C++29, adds member functions `get` to associative containers in the Standard Library.

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
