Verdict: Weak to Adequate (3/14)

The paper offers a narrow but real foundation for its standardization case, centered on the demonstrated need for caller-facing enforcement and the risks of leaving enforcement unspecified. Beyond that motivation, however, the supporting argument is largely asserted rather than shown, with no established evidence about affected users, implementation experience, or why a library solution would be inadequate.

- The strongest support is the concrete scenario showing how absent caller-facing enforcement can reintroduce a buffer overflow despite both parties’ intentions.
- The paper also credibly ties the need to future contract support for indirect calls, where caller-facing conditions become more complex.
- The thinnest areas are the complete absence of implementation experience and any established account of who is affected.
- The most glaring omission is the failure to establish why a library cannot address the problem, leaving the standardization rationale incomplete.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.33/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.33 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.33   corroborated 3.67   accumulate 3.33   max 3.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 34 of 35 section-criterion pairs unanimous (97%)
single-sample totals would have been: 3.50 / 3.50 / 3.00   (all 3 samples: 3.33)
headings: h2 4
on threshold: none
splits: vehicle[2] 1/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 5 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 2/2/2  -> 2.00
  [5] 2 Using Statements to Produce Behavior       1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): there is clearly an unmet need for function authors to specify that contract conditions will be enforced.
candidate 2 (found by 3 of 15 passes): The denouement comes when users link B’s program to F’s updated library, and are exposed to a buffer overflow vulnerability — exactly the sort of problem that both F and B took pains to avoid.
candidate 3 (found by 2 of 15 passes): To avoid the problems above, we need to be clear about establishing rules, and avoid turning those rules into offers.
candidate 4 (found by 1 of 15 passes): The need for caller-facing enforcement will increase as we improve contract support for indirect calls, creating situations where the caller-facing conditions are both nontrivial and differ from the callee-facing conditions.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.00 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       1/1/1  -> 1.00
candidate 1 (found by 3 of 15 passes): Various last-minute proposals have attempted to meet that need, but have foundered when they have attempted to specify concrete behaviors within a function declaration.
candidate 2 (found by 3 of 15 passes): Should we adopt implicit conditions on built-in operations, enforcement will also be applied to each nominated built-in operation.

## vehicle - grade 0.33 (fired in 1 of 5 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/0  -> 0.67
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidate 1 (found by 2 of 15 passes): C++ is at its best when program behavior comes from statements, and declarations merely specify points of agreement between components.

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidates: (none validated)

-->
