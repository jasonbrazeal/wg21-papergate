Verdict: Weak to Adequate (3/14)

The paper offers only a narrow slice of the case for standardization: it articulates a real hazard and gestures at the need for rules, but leaves most of the surrounding justification unstated. The thinnest areas are the absence of any identified affected audience, any argument for why this belongs in the standard rather than in guidance or tooling, and any evidence from implementation or practice.

- The strongest support is the concrete scenario showing how linking updated libraries can expose users to vulnerabilities despite both authors’ intentions.
- The paper claims there have been prior attempts and that built-in operations will increase the need, but it does not establish those alternatives or pressures in any detail.
- The paper never establishes who is affected, why the standard is the right venue, or why a library-level solution would be insufficient.
- There is no implementation experience or interoperability evidence offered at all.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 3 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 4.00   accumulate 3.50   max 4.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 0.83  vehicle 0.00  coordination 0.67  insufficiency 0.00  implementation 0.00
sample agreement: 32 of 35 section-criterion pairs unanimous (91%)
single-sample totals would have been: 2.50 / 4.00 / 4.00   (all 3 samples: 3.50)
headings: h2 4
on threshold: none
splits: motivation[5] 2/1/1  prior_art[5] 0/1/1  coordination[4] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 5 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 2/2/2  -> 2.00
  [5] 2 Using Statements to Produce Behavior       2/1/1  -> 1.33
candidate 1 (found by 3 of 15 passes): there is clearly an unmet need for function authors to specify that contract conditions will be enforced.
candidate 2 (found by 3 of 15 passes): The denouement comes when users link B’s program to F’s updated library, and are exposed to a buffer overflow vulnerability — exactly the sort of problem that both F and B took pains to avoid.
candidate 3 (found by 3 of 15 passes): To avoid the problems above, we need to be clear about establishing rules, and avoid turning those rules into offers.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.83 (fired in 2 of 5 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/1/1  -> 0.67
candidate 1 (found by 3 of 15 passes): Various last-minute proposals have attempted to meet that need, but have foundered when they have attempted to specify concrete behaviors within a function declaration.
candidate 2 (found by 1 of 15 passes): The introduction of implicit preconditions for built-in operations will further increase this need.
candidate 3 (found by 1 of 15 passes): Should we adopt implicit conditions on built-in operations, enforcement will also be applied to each nominated built-in operation.

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/0/0  -> 0.00
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.67 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] This is purely an informational paper. Wh... 0/0/0  -> 0.00
  [4] 1 The difference between a rule and an offer 0/2/2  -> 1.33
  [5] 2 Using Statements to Produce Behavior       0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): The denouement comes when users link B’s program to F’s updated library, and are exposed to a buffer overflow vulnerability
candidate 2 (found by 1 of 15 passes): The denouement comes when users link B’s program to F’s updated library, and are exposed to a buffer overflow vulnerability — exactly the sort of problem that both F and B took pains to avoid.

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
