Verdict: Adequate (4/14)

The paper offers only partial support for its own standardization, with its strongest material concentrated in motivating the problem and comparing one alternative model. The case is thin where it matters most for a standards-track proposal: the affected audience, the need for a standard change rather than another solution, and any evidence from implementation are all absent.

- The paper does establish why the current behavior is problematic, particularly through the example of explicit copy loops interfering with optimization despite no real escape of byte values.
- It also credibly engages with prior art by explaining why the PVI model was considered and rejected.
- The discussion of coordination and interoperability gestures at lock-free concerns but does not actually establish how the proposal would coordinate with existing practice.
- Most glaringly, the paper never establishes who is affected, why a library cannot address the problem, or that there is any implementation experience to support standardization.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 3 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.67   accumulate 4.33   max 4.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 0.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 4.00 / 4.00 / 5.00   (all 3 samples: 4.33)
headings: h2 6
on threshold: none
splits: coordination[5] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Analysis                                     2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): However, in several cases it is overly charitable to the programmer: for example, using an explicit copy loop rather than calling `std::memcpy` “exposes” storage, which can interfere with optimization, even if the byte values obviously do not escape.
candidate 2 (found by 3 of 21 passes): This nondeterminism already implies undefined behavior in many of the circumstances that the provenance models are meant to reject.

## audience - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Analysis                                     0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Analysis                                     2/2/2  -> 2.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The main alternative that was considered and rejected is the PVI model, which avoids the notion of storage exposure but imposes further restrictions on integer conversions.
candidate 2 (found by 3 of 21 passes): P2318R1 considers this interpretation but does not deem it conclusive, explaining that the same analysis of many tests can be obtained from address nondeterminism instead of the explicit provenance semantics but lamenting that that approach “requir[es] examination of multiple executions”.

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Analysis                                     0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Analysis                                     0/0/0  -> 0.00
  [5] Proposal                                     0/0/2  -> 0.67
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): To support lock-free algorithms, allow the pointer values chosen to point into allocations created concurrently.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Analysis                                     0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Analysis                                     0/0/0  -> 0.00
  [5] Proposal                                     0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidates: (none validated)

-->
