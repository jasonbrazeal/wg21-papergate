Verdict: Weak (3/14)

The paper offers some support for the relevance of its topic by pointing to ongoing design disputes and audience needs, but it does little to establish who is affected, why standardization is necessary, or how the proposed facility would coordinate with existing or future work. The thinnest parts of the case concern the absence of implementation experience and any demonstration that a library solution would be insufficient.

- The strongest support is the recognition that existing contract designs face serious objections and that alternative approaches have been considered, which shows the problem space is live and contested.
- The paper also notes that some audiences can already achieve their goals today, though this cuts against the urgency of standardization rather than supporting it.
- The most glaring omission is the lack of any established evidence about who is affected by the problem or why a standard facility, rather than a library, is required.


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
splits: motivation[3] 0/1/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 4 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Syntax and semantics                         0/1/1  -> 0.67
  [4] Why do this now, and what we end up gaini... 2/2/2  -> 2.00
candidate 1 (found by 2 of 12 passes): We've also had some suggestions (e.g. in D3894R0) for a different design for Contracts, but there were some major concerns about it (reliance on lambdas for deferring evaluation for 'ignore', concerns about generic preambles/postambles).
candidate 2 (found by 2 of 12 passes): Audiences who have reported that they need the configurability of something like P3400 can do what they need, today, without having to wait for the standard library facility.
candidate 3 (found by 2 of 12 passes): It may have consensus, but it also has vehement objections, it causes severe heartburn.
candidate 4 (found by 1 of 12 passes): We have had a couple of attempts to resolve the Romanian NB comment about the lack of guaranteed-enforced contracts.

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
candidate 3 (found by 1 of 12 passes): In this approach, those are to be spelled ... If you spell them in the current status quo (P2900) form, what you get is the 'enforce' semantic
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
