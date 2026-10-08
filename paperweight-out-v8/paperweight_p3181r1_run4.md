Verdict: Adequate (5/14)

The paper gives a partial account of why the current object lifetime rules are too restrictive, but it leaves several essential parts of the standardization case largely unargued. The strongest material concerns the technical motivation and the discussion of prior art, while the thinnest areas are the affected audience, coordination with existing practice, and evidence that a library solution or implementation experience would not suffice.

- The paper establishes that the current lifetime rules produce surprising and undesirable outcomes, particularly where release fences followed by relaxed stores fail to provide the intended ordering guarantee.
- The discussion of prior art and alternatives is credited as established, including the treatment of distributed shared-memory intuition, Itanium’s stronger relaxed-store ordering, and the decision not to modify happens-before itself.
- The paper only claims, without establishing, that the standard is the right venue and that a library cannot address the problem, resting both on the same underdeveloped point about fences and relaxed atomics.
- The most glaring omission is the absence of any established account of who is affected or how the change would coordinate and interoperate with existing code, implementations, or tooling.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 5 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.33   accumulate 4.83   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.17  implementation 0.33
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 4.50 / 6.00 / 4.00   (all 3 samples: 4.83)
headings: h2 7
on threshold: none
splits: motivation[6] 1/1/2  prior_art[4] 1/0/0  vehicle[7] 1/1/0  insufficiency[7] 0/1/0
        implementation[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 8 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Detailed example                             2/2/2  -> 2.00
  [6] Stronger semantics are probably still fine   1/1/2  -> 1.33
  [7] Why this matters                             2/2/2  -> 2.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The current object lifetime rules insist that the last update to an object happens-before destruction of the object. This is arguably too conservative in ways that the authors found surprising and undesirable.
candidate 2 (found by 3 of 24 passes): It is not fine if the store to A is a release fence, followed by a relaxed store, since in that case it is the fence, not the store, that synchronizes with the acquire-load.
candidate 3 (found by 3 of 24 passes): We need a1 happens-before c2, which just doesn't follow.
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

## prior_art - grade 2.00 (fired in 5 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 1/0/0  -> 0.33
  [5] Detailed example                             1/1/1  -> 1.00
  [6] Stronger semantics are probably still fine   2/2/2  -> 2.00
  [7] Why this matters                             1/1/1  -> 1.00
  [8] Proposed wording                             2/2/2  -> 2.00
candidate 1 (found by 3 of 24 passes): The current rules are backed by some possible intuition: [ Warning: This is a bit of a stretch. ] Consider a distributed shared-memory implementation that may nondeterministically send asynchronous updates, and has release operations send visible changes to acquire operations.
candidate 2 (found by 3 of 24 passes): The only architecture I know of that by design required stronger ordering for relaxed stores was Itanium.
candidate 3 (found by 3 of 24 passes): C++ and posix mutexes work this way, but historically some mutex implementations did not
candidate 4 (found by 3 of 24 passes): We follow the argument made in St. Louis that modifying the happens-before relationship itself is undesirable.

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             1/1/0  -> 0.67
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
  [7] Why this matters                             0/1/0  -> 0.33
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): If fences aren't strong enough to make this work, "relaxed atomic + fence" suddenly loses the ability to provide this guarantee.

## implementation - grade 0.33  [binary: max] (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/1/0  -> 0.33
  [7] Why this matters                             0/0/0  -> 0.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The only architecture I know of that by design required stronger ordering for relaxed stores was Itanium.

-->
