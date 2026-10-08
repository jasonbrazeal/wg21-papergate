Verdict: Adequate (5/14)

The paper offers some meaningful support for its core semantic motivation and for the choice among provenance models, but it leaves most of the case for standardization unbuilt. The thinnest areas are the absence of any account of who is affected, why a library solution is insufficient, and whether anyone has actually implemented the proposed direction.

- The strongest support is for why the issue matters, with concrete examples of how current rules can be “overly charitable” and how existing nondeterminism already produces undefined behavior in the relevant cases.
- The discussion of prior art and alternatives is also well grounded, particularly in explaining why the PVI model was rejected and how P2318R1’s address-nondeterminism reading was considered but found wanting.
- The paper only claims, without establishing, that the design can coordinate with concurrent lock-free algorithms by allowing pointer values to point into concurrently created allocations.
- The most glaring omission is the complete lack of implementation experience, leaving no evidence that the proposed semantics can be realized in practice or adopted by existing compilers.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 3 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.00   accumulate 5.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.00  coordination 1.00  insufficiency 0.00  implementation 0.00
sample agreement: 49 of 49 section-criterion pairs unanimous (100%)
single-sample totals would have been: 5.00 / 5.00 / 5.00   (all 3 samples: 5.00)
headings: h2 6
on threshold: coordination
splits: none
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 2/2/2  -> 2.00
  [4] Analysis                                     2/2/2  -> 2.00
  [5] Proposal                                     2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): However, in several cases it is overly charitable to the programmer: for example, using an explicit copy loop rather than calling `std::memcpy` “exposes” storage, which can interfere with optimization, even if the byte values obviously do not escape.
candidate 2 (found by 3 of 21 passes): This nondeterminism already implies undefined behavior in many of the circumstances that the provenance models are meant to reject.
candidate 3 (found by 2 of 21 passes): To avoid confusing inconsistencies with comparing their integer representations (on implementations where each address has just one such), restrict [expr.eq] to provide consistent results for any pair of pointer values.
candidate 4 (found by 1 of 21 passes): To implement *udi*, apply the same *angelic nondeterminism* by which implicit object creation selects the objects to create: if any pointer value exists that corresponds to the integer and gives the program defined behavior, one such value is the result.

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

## coordination - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] History                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Analysis                                     0/0/0  -> 0.00
  [5] Proposal                                     2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
  [7] Acknowledgments                              0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): To support lock-free algorithms, allow the pointer values chosen to point into allocations created concurrently.

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
