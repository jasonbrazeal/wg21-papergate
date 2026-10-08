Verdict: Adequate (5/14)

The paper gives a reasonably clear account of why the problem matters and shows that related ideas have been considered before, but it leaves several essential parts of the standardization case almost entirely unaddressed. The thinnest areas are the lack of any discussion of affected users, implementation experience, or why a library-level solution would be insufficient.

- The strongest support is the explanation of how *ignore* semantics can undermine library attempts to use preconditions for UB-safety.
- The paper also adequately situates itself among prior proposals and acknowledges that alternative spellings could be considered.
- The claim that this belongs in the standard is asserted mainly through references to the NB comment and the existing contracts design, without a fuller demonstration of the standardization need.
- The most glaring omission is the absence of any implementation experience or evidence about who would be affected by the proposed change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.67/14)

Provisionally addressed: 3 of 7. Provisional points: 4.67 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.67   corroborated 5.00   accumulate 5.50   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.00 / 4.50 / 5.00   (all 3 samples: 4.67)
headings: h3 6   <- NOT h2, check the unit list
on threshold: none
splits: motivation[5] 1/1/2  prior_art[4] 2/1/2  vehicle[2] 0/1/1  vehicle[3] 1/1/0
        vehicle[5] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Proposal                                  1/1/1  -> 1.00
  [5] 3. Analysis                                  1/1/2  -> 1.33
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           1/1/1  -> 1.00
candidate 1 (found by 3 of 21 passes): Because preconditions may be evaluated with *ignore* semantics, a library that relies on contract preconditions to prevent undefined behavior cannot guarantee that those checks will execute.
candidate 2 (found by 3 of 21 passes): However, C++26 contracts do not guarantee that preconditions will be evaluated. A program may configure contract evaluation to use *ignore* semantics. In that case, a library that encodes UB-safety requirements as preconditions cannot rely on those checks being executed.
candidate 3 (found by 3 of 21 passes): Should C++ aim to improve UB-safety?
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

## prior_art - grade 1.83 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1. Introduction                              2/2/2  -> 2.00
  [4] 2. Proposal                                  2/1/2  -> 1.67
  [5] 3. Analysis                                  1/1/1  -> 1.00
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Several proposals attempted to address this limitation ([P3911R2](https://wg21.link/P3911R2), [P3919R0](https://wg21.link/P3919R0), [P4005R0](https://wg21.link/P4005R0), [P4009R0](https://wg21.link/P4009R0)), but none achieved consensus.
candidate 2 (found by 3 of 21 passes): Alternative spellings could be considered if the committee prefers a different notation.
candidate 3 (found by 2 of 21 passes): [P3911R2](https://wg21.link/P3911R2) was rejected by EWG in a telecon.
candidate 4 (found by 2 of 21 passes): While bikeshedding syntax is fun, we will restrain ourselves and just propose the `pre!` syntax, as described in [P3911R2](https://wg21.link/P3911R2) — P3911R2 provides enough motivation in support of `pre!`.

## vehicle - grade 0.83 (fired in 4 of 7 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] 1. Introduction                              1/1/0  -> 0.67
  [4] 2. Proposal                                  1/1/1  -> 1.00
  [5] 3. Analysis                                  0/1/1  -> 0.67
  [6] 4. Wording                                   0/0/0  -> 0.00
  [7] 5. Suggested polls                           0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This proposal merely provides a way for authors to require that already-permitted behavior for specific preconditions.
candidate 2 (found by 2 of 21 passes): This proposal aims to resolve the RO 2-056 NB comment.
candidate 3 (found by 2 of 21 passes): To use contracts to enforce UB-safety, precondition violations must terminate execution.
candidate 4 (found by 1 of 21 passes): The proposal introduces a minimal syntactic mechanism to require behavior that is already permitted by the current contracts design, allowing the C++26 contracts facility to be used to improve program UB-safety.

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
