Verdict: Weak (3/14)

The paper offers some support for its own standardization by showing why the issue matters and by discussing prior art and alternatives, but it leaves most of the necessary case unaddressed. The thinnest areas are the absence of any established need for a standard facility, the lack of implementation experience, and the failure to show why a library solution would not suffice.

- The strongest support is the paper’s account of the controversy and the existence of plausible alternative designs, which establishes that the problem space is real and contested.
- The paper also establishes that some audiences can already achieve the needed configurability without waiting for a standard library facility.
- The most glaring omission is that the paper does not establish who is affected, why the standard is the right venue, or how the proposal would coordinate with existing practice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 2 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.00   accumulate 3.83   max 4.00

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 27 of 28 section-criterion pairs unanimous (96%)
single-sample totals would have been: 3.00 / 3.00 / 3.00   (all 3 samples: 3.00)
headings: h2 3
on threshold: motivation, prior_art
splits: motivation[3] 1/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Syntax and semantics                         1/0/1  -> 0.67
  [4] Why do this now, and what we end up gaini... 2/2/2  -> 2.00
candidate 1 (found by 3 of 12 passes): We've also had some suggestions (e.g. in D3894R0) for a different design for Contracts, but there were some major concerns about it (reliance on lambdas for deferring evaluation for 'ignore', concerns about generic preambles/postambles).
candidate 2 (found by 2 of 12 passes): Audiences who have reported that they need the configurability of something like P3400 can do what they need, today, without having to wait for the standard library facility.
candidate 3 (found by 1 of 12 passes): It may have consensus, but it also has vehement objections, it causes severe heartburn.
candidate 4 (found by 1 of 12 passes): The amount and severity of that heartburn is extraordinary. We have never had this much and this strong opposition to a feature in a DIS.

## audience - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Syntax and semantics                         0/0/0  -> 0.00
  [4] Why do this now, and what we end up gaini... 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Syntax and semantics                         2/2/2  -> 2.00
  [4] Why do this now, and what we end up gaini... 1/1/1  -> 1.00
candidate 1 (found by 3 of 12 passes): We've also had some suggestions (e.g. in D3894R0) for a different design for Contracts, but there were some major concerns about it (reliance on lambdas for deferring evaluation for 'ignore', concerns about generic preambles/postambles).
candidate 2 (found by 3 of 12 passes): There are plausible design alternatives that are palatable to those opposing audiences.
candidate 3 (found by 2 of 12 passes): The P2900 semantics can be used by calling standard library functions that provide those semantics.
candidate 4 (found by 1 of 12 passes): The P2900 semantics can be used by calling standard library functions that provide those semantics. Except for constification.

## vehicle - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Syntax and semantics                         0/0/0  -> 0.00
  [4] Why do this now, and what we end up gaini... 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Syntax and semantics                         0/0/0  -> 0.00
  [4] Why do this now, and what we end up gaini... 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Syntax and semantics                         0/0/0  -> 0.00
  [4] Why do this now, and what we end up gaini... 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Syntax and semantics                         0/0/0  -> 0.00
  [4] Why do this now, and what we end up gaini... 0/0/0  -> 0.00
candidates: (none validated)

-->
