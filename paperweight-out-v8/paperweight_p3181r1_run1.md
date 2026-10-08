Verdict: Adequate (4/14)

The paper offers a narrow but genuine case that the current rules are too conservative, and it does useful work in locating prior architectural and standards discussion around the problem. Beyond that, however, the support for standardization is thin: the affected audience, the need for a standard change rather than a library solution, coordination concerns, and implementation experience are all essentially unaddressed.

- The strongest support is the explanation of why the current lifetime rules produce a surprising and undesirable ordering requirement.
- The discussion of prior art credibly grounds the issue in existing practice and earlier committee reasoning.
- The most glaring omission is the absence of any account of who is affected by the problem in real code.
- The paper also leaves entirely open why a library-level fix would not suffice and whether any implementation experience exists.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.83/14)

Provisionally addressed: 3 of 7. Provisional points: 3.83 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.83   corroborated 4.33   accumulate 4.17   max 4.33

## SUMMARY
grades: motivation 1.83  audience 0.00  prior_art 1.83  vehicle 0.00  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 4.50 / 3.50 / 3.50   (all 3 samples: 3.83)
headings: h2 7
on threshold: none
splits: motivation[5] 2/1/2  motivation[8] 0/1/1  prior_art[5] 0/1/1  prior_art[6] 2/2/1
        insufficiency[7] 1/0/0
## END SUMMARY

## motivation - grade 1.83 (fired in 5 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             2/1/2  -> 1.67
  [6] Stronger semantics are probably still fine   1/1/1  -> 1.00
  [7] Why this matters                             2/2/2  -> 2.00
  [8] Proposed wording                             0/1/1  -> 0.67
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
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/1/1  -> 0.67
  [6] Stronger semantics are probably still fine   2/2/1  -> 1.67
  [7] Why this matters                             1/1/1  -> 1.00
  [8] Proposed wording                             2/2/2  -> 2.00
candidate 1 (found by 3 of 24 passes): The only architecture I know of that by design required stronger ordering for relaxed stores was Itanium.
candidate 2 (found by 3 of 24 passes): C++ and posix mutexes work this way, but historically some mutex implementations did not
candidate 3 (found by 3 of 24 passes): We follow the argument made in St. Louis that modifying the happens-before relationship itself is undesirable.
candidate 4 (found by 2 of 24 passes): The current rules are backed by some possible intuition: [ Warning: This is a bit of a stretch. ] Consider a distributed shared-memory implementation that may nondeterministically send asynchronous updates, and has release operations send visible changes to acquire operations.

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

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Modification history                         0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Detailed example                             0/0/0  -> 0.00
  [6] Stronger semantics are probably still fine   0/0/0  -> 0.00
  [7] Why this matters                             1/0/0  -> 0.33
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
