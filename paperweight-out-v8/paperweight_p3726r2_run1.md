Verdict: Weak to Adequate (4/14)

The paper offers only partial support for its own standardization, with its strongest material concerning prior art and alternatives, while several essential parts of the case are asserted rather than demonstrated. The thinnest areas are the absence of any identified affected users, implementation experience, or coordination considerations, leaving the motivation largely tied to a single stated goal rather than a broader demonstrated need.

- The paper’s treatment of prior art and alternatives is its most solid contribution, clearly connecting earlier proposals and explaining why a previous wording approach was incomplete.
- The argument for why a library solution will not suffice is asserted through the compile-time usability goal and syntactic concerns, but it is not independently established.
- The paper does not identify who is affected by the problem, making the practical stakes of standardization unclear.
- There is no implementation experience or coordination and interoperability discussion, leaving the proposal without evidence of real-world viability or ecosystem fit.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.00/14)

Provisionally addressed: 4 of 7. Provisional points: 4.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.00   corroborated 3.33   accumulate 4.00   max 6.33

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 1.67  vehicle 1.00  coordination 0.00  insufficiency 0.33  implementation 0.00
sample agreement: 46 of 49 section-criterion pairs unanimous (94%)
single-sample totals would have been: 4.50 / 3.00 / 4.50   (all 3 samples: 4.00)
headings: h2 6
on threshold: motivation, prior_art, vehicle
splits: prior_art[4] 2/0/2  insufficiency[3] 0/0/1  insufficiency[4] 1/0/0
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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

## prior_art - grade 1.67 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   2/0/2  -> 1.33
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): That paper solved this problem by: 1. Making `union`s have trivial default constructors and trivial destructors, by default, and 2. Implicitly starting the lifetime of the first `union` member, if that member has implicit-lifetime type.
candidate 2 (found by 1 of 21 passes): The previous version of this paper [[P3726R0]](https://wg21.link/p3726r0) proposed allowing placement new on an aggregate element to start the lifetime of the aggregate.
candidate 3 (found by 1 of 21 passes): The previous version of this paper [[P3726R0]](https://wg21.link/p3726r0) proposed allowing placement new on an aggregate element to start the lifetime of the aggregate. It turns out that the wording to allow this was wholly incomplete

## vehicle - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   2/2/2  -> 2.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): As a production implementation wouldn’t write `new (&storage[n]) T`, it’d write `::new ((void*)std::addressof(storage[n]) T`. Having to pattern match on syntax makes this wording approach increasingly complicated, if not outright weird given the call to a standard library function in there.

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

## insufficiency - grade 0.33 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/1  -> 0.33
  [4] 3 Proposal                                   1/0/0  -> 0.33
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgments                            0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): This is also a problem because the original goal of the paper was to make types like `std::inplace_vector` completely usable at compile-time, and this rule (even separate from [[P3074R7]](https://wg21.link/p3074r7)) makes that impossible:
candidate 2 (found by 1 of 21 passes): As a production implementation wouldn’t write `new (&storage[n]) T`, it’d write `::new ((void*)std::addressof(storage[n]) T`. Having to pattern match on syntax makes this wording approach increasingly complicated, if not outright weird given the call to a standard library function in there.

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
