Verdict: Adequate (5/14)

The paper offers a solid conceptual foundation for why the current lifetime rules are too conservative and engages seriously with prior art, but it leaves several practical and evidentiary questions open. The thinnest areas are the absence of any implementation experience and the lack of a clear account of who is affected, which makes the case for standardization feel more theoretical than grounded.

- The strongest support is the paper’s explanation of why the current rules are surprising and undesirable, backed by concrete reasoning about happens-before and fence semantics.
- The discussion of prior art and alternatives is substantive, including architectural considerations and historical mutex behavior.
- The claims about why the standard is needed and why a library solution will not suffice are asserted but not fully demonstrated.
- The most glaring omission is the absence of any implementation experience or evidence about who would actually be affected by the change.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 5 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 5.67   accumulate 5.00   max 6.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 0.17  coordination 0.17  insufficiency 0.67  implementation 0.00
sample agreement: 49 of 56 section-criterion pairs unanimous (88%)
single-sample totals would have been: 5.00 / 4.50 / 5.00   (all 3 samples: 4.83)
headings: h2 7
on threshold: none
splits: motivation[4] 2/0/0  motivation[8] 0/0/1  prior_art[4] 0/1/0  prior_art[6] 2/2/1
        vehicle[7] 0/1/0  coordination[7] 0/0/1  insufficiency[5] 2/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 2/0/0  -> 0.67
  [5] Detailed example                             2/2/2  -> 2.00
  [6] Stronger semantics are probably still fine   1/1/1  -> 1.00
  [7] Why this matters                             2/2/2  -> 2.00
  [8] Proposed wording                             0/0/1  -> 0.33
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

## prior_art - grade 1.83 (fired in 5 of 8 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/1/0  -> 0.33
  [5] Detailed example                             1/1/1  -> 1.00
  [6] Stronger semantics are probably still fine   2/2/1  -> 1.67
  [7] Why this matters                             1/1/1  -> 1.00
  [8] Proposed wording                             2/2/2  -> 2.00
candidate 1 (found by 3 of 24 passes): The current rules are backed by some possible intuition: [ Warning: This is a bit of a stretch. ] Consider a distributed shared-memory implementation that may nondeterministically send asynchronous updates, and has release operations send visible changes to acquire operations.
candidate 2 (found by 3 of 24 passes): The only architecture I know of that by design required stronger ordering for relaxed stores was Itanium.
candidate 3 (found by 3 of 24 passes): C++ and posix mutexes work this way, but historically some mutex implementations did not
candidate 4 (found by 3 of 24 passes): We follow the argument made in St. Louis that modifying the happens-before relationship itself is undesirable.

## vehicle - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
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

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)
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
candidate 1 (found by 1 of 24 passes): When you're writing some bit of synchronization you don't necessarily know how your caller will use the synchronization you provide, so you can't assume it *won't* be used to synchronize destruction.

## insufficiency - grade 0.67 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             2/0/2  -> 1.33
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             0/0/0  -> 0.00
  [8] Proposed wording                             0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): The allocator must ensure that b2 happens-before c1. We need a1 happens-before c2, which just doesn't follow.

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
