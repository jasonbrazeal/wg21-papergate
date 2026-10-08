Verdict: Weak to Adequate (3/14)

The paper offers a narrow but genuine foundation for its standardization case, centered on naming and continuity with prior work, but it leaves most of the practical and procedural justification unaddressed. The strongest support concerns why the operation matters and how the proposed direction relates to earlier alternatives, while the thinnest areas are the absence of any account of affected users, implementation experience, or why standardization—rather than a library solution—is necessary.

- The paper establishes that the proposed operation fills a conceptual gap in sequence containers and that the name should reflect possible failure, distinguishing it from existing `get` semantics.
- It also establishes continuity with P3091 and explains why earlier names were not carried forward, grounding the proposal in recent committee history.
- It does not establish who is affected by the change or what implementation experience exists to support the design.
- Most glaringly, it does not establish why the standard is the right venue or why a library-based approach would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 2 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 2.00   accumulate 4.00   max 4.00

## SUMMARY
grades: motivation 1.67  audience 0.00  prior_art 1.67  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.00 / 4.00 / 3.00   (all 3 samples: 3.33)
headings: h2 7
on threshold: motivation, prior_art
splits: motivation[2] 1/2/1  prior_art[5] 1/2/1
## END SUMMARY

## motivation - grade 1.67 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/2/1  -> 1.33
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            1/1/1  -> 1.00
  [6] 5 Alternatives considered                    0/0/0  -> 0.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Since that time, even the author of P3091 has reconsidered the implications of the name `get`.
candidate 2 (found by 3 of 24 passes): The name of the desired operation should reflect that the lookup may take variable time and could return without finding the value being sought; existing instances of `get` in the Library forbid both.
candidate 3 (found by 3 of 24 passes): Conceptually, `myVector[*index*]` is a lookup operation that could fail if `*index*` is out of range, so member functions similar to the those added to associative containers would fit well in sequence containers, adding to the regularity of the library.

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

## prior_art - grade 1.67 (fired in 4 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Change Log                                 0/0/0  -> 0.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Proposed Change                            1/2/1  -> 1.33
  [6] 5 Alternatives considered                    1/1/1  -> 1.00
  [7] 6 Wording                                    0/0/0  -> 0.00
  [8] 7 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5), forwarded to LWG for C++29, adds member functions `get` to associative containers in the Standard Library.
candidate 2 (found by 3 of 24 passes): P3091 offered names `get_optional` and `lookup_optional`, which failed to evoke enthusiasm in Sofia; and `lookup`, which had supporters, but failed to reach consensus.
candidate 3 (found by 3 of 24 passes): The name `get_optional` mentioned in P3091 is not proposed, for reasons that should be clear.
candidate 4 (found by 2 of 24 passes): [[P3091R5]](https://wg21.link/p3091r5) proposed a new member function for associative containers returning an `optional<mapped_type&>` that identifies an object if the key is found, or otherwise is empty.

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
