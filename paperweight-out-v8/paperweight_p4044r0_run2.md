Verdict: Adequate (5/14)

The paper gives a partial account of why a terminating precondition mechanism matters and shows that related ideas have been brought to the committee before, but it leaves several basic parts of the standardization case unaddressed. The thinnest areas concern the affected audience, interaction with the wider standard and ecosystem, feasibility outside the standard, and any practical experience with the proposed approach.

- The strongest support is the explanation of why contract preconditions with ignore semantics cannot by themselves guarantee the checks needed for UB-safety.
- The paper also establishes that prior proposals and a related national-body comment have failed to reach consensus, situating this work within an ongoing committee discussion.
- The case for standardization itself is asserted mainly through the goal of resolving RO 2-056 and requiring already-permitted behavior, but the paper does not develop that into a fuller justification.
- The most glaring omissions are the absence of any identified affected users or codebases, any implementation experience, and any analysis of coordination, interoperability, or why a library-level solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 4.00   accumulate 6.00   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 4.50 / 4.50 / 4.50   (all 3 samples: 4.50)
headings: h3 6   <- NOT h2, check the unit list
on threshold: prior_art
splits: prior_art[5] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Proposal                                  1/1/1  -> 1.00
  [5] 3. Analysis                                  1/1/1  -> 1.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           1/1/1  -> 1.00
candidate 1 (found by 3 of 21 passes): Because preconditions may be evaluated with *ignore* semantics, a library that relies on contract preconditions to prevent undefined behavior cannot guarantee that those checks will execute.
candidate 2 (found by 3 of 21 passes): Should C++ aim to improve UB-safety?
candidate 3 (found by 2 of 21 passes): To use contracts to enforce UB-safety, precondition violations must terminate execution. If contracts cannot guarantee terminating enforcement for such safety preconditions, it is unclear what mechanism library authors should use to express and enforce these interface requirements.
candidate 4 (found by 2 of 21 passes): This paper proposes the following: - Semantics: allow certain precondition contract assertions to always use *terminating semantics*.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Proposal                                  0/0/0  -> 0.00
  [5] 3. Analysis                                  0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 4 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Proposal                                  1/1/1  -> 1.00
  [5] 3. Analysis                                  0/0/1  -> 0.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Several proposals attempted to address this limitation ([P3911R2](https://wg21.link/P3911R2), [P3919R0](https://wg21.link/P3919R0), [P4005R0](https://wg21.link/P4005R0), [P4009R0](https://wg21.link/P4009R0)), but none achieved consensus.
candidate 2 (found by 2 of 21 passes): [P3911R2](https://wg21.link/P3911R2) was rejected by EWG in a telecon.
candidate 3 (found by 2 of 21 passes): Alternative syntax may be considered if the committee prefers a different spelling.
candidate 4 (found by 1 of 21 passes): [P3911R2](https://wg21.link/P3911R2) was rejected by EWG in a telecon. The underlying RO 2-056 NB-comment was left unresolved. Follow-up attempts to resolve this NB still failed ([P4005R0](https://wg21.link/P4005R0), [P4009R0](https://wg21.link/P4009R0)).

## vehicle - grade 1.00 (fired in 4 of 7 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              1/1/1  -> 1.00
  [4] 2. Proposal                                  1/1/1  -> 1.00
  [5] 3. Analysis                                  1/1/1  -> 1.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper proposes a minimal mechanism to address RO 2-056.
candidate 2 (found by 3 of 21 passes): To use contracts to enforce UB-safety, precondition violations must terminate execution.
candidate 3 (found by 3 of 21 passes): This proposal merely provides a way for authors to require that already-permitted behavior for specific preconditions.
candidate 4 (found by 2 of 21 passes): The proposal introduces a minimal syntactic mechanism to require behavior that is already permitted by the current contracts design, allowing the C++26 contracts facility to be used to improve program UB-safety.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Proposal                                  0/0/0  -> 0.00
  [5] 3. Analysis                                  0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Proposal                                  0/0/0  -> 0.00
  [5] 3. Analysis                                  0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Introduction                              0/0/0  -> 0.00
  [4] 2. Proposal                                  0/0/0  -> 0.00
  [5] 3. Analysis                                  0/0/0  -> 0.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidates: (none validated)

-->
