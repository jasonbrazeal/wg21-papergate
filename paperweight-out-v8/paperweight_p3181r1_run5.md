Verdict: Adequate (4/14)

The paper gives a partial account of why the current rules are problematic and why the proposed direction is worth considering, but it leaves several essential parts of the standardization case unaddressed. The strongest material concerns the motivating technical problem and the existence of prior reasoning or architectural precedent, while the thinnest areas are the lack of evidence about affected users, implementation experience, and coordination with existing practice.

- The paper clearly establishes that the current object lifetime rules can be too conservative and that the interaction between fences and relaxed atomics creates a surprising loss of guarantee.
- The discussion of prior art and alternatives is grounded in known architectural behavior, mutex implementation history, and earlier committee reasoning.
- The claim that the standard is the necessary place to solve the problem rests mainly on the fence-and-relaxed-store example, but the paper does not develop that into a broader case for standardization.
- The paper offers no established account of who is affected, how implementations have handled the change, or how the proposal would coordinate with existing code and tooling.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 4 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 5.00   accumulate 4.50   max 5.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 0.33  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 48 of 56 section-criterion pairs unanimous (86%)
single-sample totals would have been: 3.50 / 4.50 / 5.00   (all 3 samples: 4.33)
headings: h2 7
on threshold: none
splits: motivation[4] 0/2/0  motivation[6] 1/1/2  motivation[8] 1/1/0  prior_art[4] 1/0/0
        prior_art[5] 0/1/0  prior_art[6] 1/2/2  vehicle[7] 0/1/1  insufficiency[7] 0/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/2/0  -> 0.67
  [5] Detailed example                             2/2/2  -> 2.00
  [6] Stronger semantics are probably still fine   1/1/2  -> 1.33
  [7] Why this matters                             2/2/2  -> 2.00
  [8] Proposed wording                             1/1/0  -> 0.67
candidate 1 (found by 3 of 24 passes): The current object lifetime rules insist that the last update to an object happens-before destruction of the object. This is arguably too conservative in ways that the authors found surprising and undesirable.
candidate 2 (found by 3 of 24 passes): We need a1 happens-before c2, which just doesn't follow.
candidate 3 (found by 3 of 24 passes): If fences aren't strong enough to make this work, "relaxed atomic + fence" suddenly loses the ability to provide this guarantee.
candidate 4 (found by 1 of 24 passes): It is not fine if the store to A is a release fence, followed by a relaxed store, since in that case it is the fence, not the store, that synchronizes with the acquire-load.

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

## prior_art - grade 1.83 (fired in 5 of 8 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Detailed example                             0/1/0  -> 0.33
  [6] Stronger semantics are probably still fine   1/2/2  -> 1.67
  [7] Why this matters                             1/1/1  -> 1.00
  [8] Proposed wording                             2/2/2  -> 2.00
candidate 1 (found by 3 of 24 passes): The only architecture I know of that by design required stronger ordering for relaxed stores was Itanium.
candidate 2 (found by 3 of 24 passes): C++ and posix mutexes work this way, but historically some mutex implementations did not
candidate 3 (found by 3 of 24 passes): We follow the argument made in St. Louis that modifying the happens-before relationship itself is undesirable.
candidate 4 (found by 1 of 24 passes): For something like the standard message passing litmus test the difference between “fence; relaxed-store” is usually stronger than “release-store”, and the difference often doesn’t matter.

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/1/1  -> 0.67
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): If fences aren't strong enough to make this work, "relaxed atomic + fence" suddenly loses the ability to provide this guarantee.

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

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/0/1  -> 0.33
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): If fences aren't strong enough to make this work, "relaxed atomic + fence" suddenly loses the ability to provide this guarantee.

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
