Verdict: Weak to Adequate (3/14)

The paper offers some context for its naming choices and connects itself to prior work, but it does not build a substantive case that the proposed facility belongs in the standard. The strongest material concerns alternatives already considered, while the argument for need, affected users, and implementation experience is essentially absent.

- The paper establishes that related naming options were explored and that P3091 is the relevant prior proposal.
- The discussion of why the feature matters gestures at consistency with associative containers, but it is asserted rather than demonstrated.
- The paper does not identify who would be affected by the change or what problem they currently face.
- The most glaring omission is the absence of any implementation experience, standard-library rationale, or explanation of why a library solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.00   accumulate 3.67   max 3.67

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.50 / 3.50 / 3.50   (all 3 samples: 3.33)
headings: h2 7
on threshold: motivation
splits: motivation[2] 1/2/2  motivation[4] 2/0/0  prior_art[2] 1/2/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/2  -> 1.67
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/0/0  -> 0.67
  [5] 4 Proposed Change                            1/1/1  -> 1.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): In hope of making the C++26 cutoff, the naming discussion was curtailed and the name in P3091 was retained when that paper was forwarded in Sofia.
candidate 2 (found by 3 of 24 passes): Conceptually, `myVector[*index*]` is a lookup operation that could fail if `*index*` is out of range, so member functions similar to the those added to associative containers would fit well in sequence containers, adding to the regularity of the library.
candidate 3 (found by 1 of 24 passes): We conclude that a `get` function returning `optional` after an unbounded search would make it unique among uses of `get` in the library, and so would be inconsistent and confusing.

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

## prior_art - grade 2.00 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/1  -> 1.33
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            2/2/2  -> 2.00
  [6] 5 Alternatives considered                    1/1/1  -> 1.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): P3091 offered names `get_optional` and `lookup_optional`, which failed to evoke enthusiasm in Sofia; and `lookup`, which had supporters, but failed to reach consensus.
candidate 2 (found by 3 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5) proposed a new member function for associative containers returning an `optional<mapped_type&>` that identifies an object if the key is found, or otherwise is empty.
candidate 3 (found by 3 of 24 passes): The name `get_optional` mentioned in P3091 is not proposed, for reasons that should be clear.
candidate 4 (found by 2 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5), forwarded to LWG for C++29, adds member functions `get` to associative containers in the Standard Library.

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
