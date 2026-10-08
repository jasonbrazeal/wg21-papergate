Verdict: Weak to Adequate (3/14)

The paper offers only a thin, mostly asserted case for standardization: its central motivation is tied to a stated goal about `std::inplace_vector` and compile-time usability, but the affected audience, implementation experience, and coordination concerns are left unaddressed. The strongest material appears in the discussion of prior art and wording complexity, yet even those points are presented as claims rather than demonstrated necessity.

- The paper’s clearest support comes from its explanation of how a previous proposal attempted to solve the lifetime problem and why that approach was abandoned.
- The discussion of syntax pattern-matching in the wording gives some sense of why a standard mechanism might be preferable, though it remains an assertion about drafting difficulty.
- The most glaring omission is any account of who is affected by the current rules or what real-world code is blocked.
- The paper also provides no implementation experience, no interoperability analysis, and no argument that a library solution cannot suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.00   accumulate 3.33   max 6.00

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.33  vehicle 1.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 3.00 / 3.00 / 4.00   (all 3 samples: 3.33)
headings: h2 6
on threshold: motivation, prior_art, vehicle
splits: prior_art[4] 0/0/2
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This is also a problem because the original goal of the paper was to make types like `std::inplace_vector` completely usable at compile-time, and this rule (even separate from [[P3074R7]](https://wg21.link/p3074r7)) makes that impossible:

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.33 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   0/0/2  -> 0.67
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): That paper solved this problem by: 1. Making `union`s have trivial default constructors and trivial destructors, by default, and 2. Implicitly starting the lifetime of the first `union` member, if that member has implicit-lifetime type.
candidate 2 (found by 1 of 21 passes): The previous version of this paper [[P3726R0]](https://wg21.link/p3726r0) proposed allowing placement new on an aggregate element to start the lifetime of the aggregate.

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   2/2/2  -> 2.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): Having to pattern match on syntax makes this wording approach increasingly complicated, if not outright weird given the call to a standard library function in there.
candidate 2 (found by 1 of 21 passes): As a production implementation wouldn’t write `new (&storage[n]) T`, it’d write `::new ((void*)std::addressof(storage[n]) T`. Having to pattern match on syntax makes this wording approach increasingly complicated, if not outright weird given the call to a standard library function in there.

## coordination - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
