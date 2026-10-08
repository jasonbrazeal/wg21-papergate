Verdict: Adequate (5/14)

The paper offers a narrow but genuine case that the current rules are too conservative, and it does useful work in situating the problem against prior architectural and standardization discussions. The support is thinnest, however, on the questions that matter most for a standardization proposal: who is concretely affected, why the standard is the right place to fix it, and whether any implementation experience exists.

- The strongest support is the motivation, where the paper identifies a specific ordering that the current rules fail to provide and explains why that failure is surprising.
- The prior-art discussion is also creditable, particularly the references to Itanium, mutex implementations, and the St. Louis argument against changing happens-before directly.
- The most glaring omission is the absence of any established affected audience, implementation experience, or interoperability analysis, leaving the practical demand and readiness for standardization unshown.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.50/14)

Provisionally addressed: 3 of 7. Provisional points: 4.50 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.50   corroborated 5.00   accumulate 4.67   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.67  implementation 0.00
sample agreement: 52 of 56 section-criterion pairs unanimous (93%)
single-sample totals would have been: 5.00 / 4.50 / 4.00   (all 3 samples: 4.50)
headings: h2 7
on threshold: none
splits: motivation[8] 1/1/0  prior_art[4] 0/1/1  prior_art[8] 2/2/1  insufficiency[5] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             2/2/2  -> 2.00
  [6] Stronger semantics are probably still fine   1/1/1  -> 1.00
  [7] Why this matters                             2/2/2  -> 2.00
  [8] Proposed wording                             1/1/0  -> 0.67
candidate 1 (found by 3 of 24 passes): The current object lifetime rules insist that the last update to an object happens-before destruction of the object. This is arguably too conservative in ways that the authors found surprising and undesirable.
candidate 2 (found by 3 of 24 passes): We need a1 happens-before c2, which just doesn't follow.
candidate 3 (found by 3 of 24 passes): The only small fly in the ointment here is the non-atomic store at c2.
candidate 4 (found by 3 of 24 passes): If fences aren't strong enough to make this work, "relaxed atomic + fence" suddenly loses the ability to provide this guarantee.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/0/0  -> 0.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.83 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/1/1  -> 0.67
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   2/2/2  -> 2.00
  [7] Why this matters                             1/1/1  -> 1.00
  [8] Proposed wording                             2/2/1  -> 1.67
candidate 1 (found by 3 of 24 passes): The only architecture I know of that by design required stronger ordering for relaxed stores was Itanium.
candidate 2 (found by 3 of 24 passes): C++ and posix mutexes work this way, but historically some mutex implementations did not
candidate 3 (found by 3 of 24 passes): We follow the argument made in St. Louis that modifying the happens-before relationship itself is undesirable.
candidate 4 (found by 2 of 24 passes): For something like the standard message passing litmus test the difference between “fence; relaxed-store” is usually stronger than “release-store”, and the difference often doesn’t matter.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/0/0  -> 0.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/0/0  -> 0.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.67 (fired in 2 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             1/0/0  -> 0.33
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             1/1/1  -> 1.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): If fences aren't strong enough to make this work, "relaxed atomic + fence" suddenly loses the ability to provide this guarantee.
candidate 2 (found by 1 of 24 passes): The allocator must ensure that b2 happens-before c1. We need a1 happens-before c2, which just doesn't follow.

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/0/0  -> 0.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidates: (none validated)

-->
