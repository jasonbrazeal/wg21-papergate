Verdict: Weak (1/14)

The paper offers only a thin rationale for standardization, resting almost entirely on a single stated desire by CWG for consistency across a handful of language constructs. Beyond that general aim, it does not identify an affected audience, explain why the standard is the right venue, or show that the problem cannot be addressed outside the standard. The thinnest areas are the complete absence of implementation experience and any discussion of coordination or interoperability.

- The strongest support is the paper’s statement that CWG wants to unify treatment of several constructs to improve language and specification consistency.
- The paper gestures at a proposed unified treatment, but does not compare it against alternatives or prior art in any substantive way.
- The paper never establishes who is affected by the lack of a definition for “immediate context.”
- The most glaring omission is the absence of any implementation experience, leaving the practical consequences of the proposed definition entirely unexamined.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.33/14)

Provisionally addressed: 2 of 7. Provisional points: 1.33 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 5. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.33   corroborated 1.67   accumulate 1.33   max 1.67

## SUMMARY
grades: motivation 1.00  audience 0.00  prior_art 0.33  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 34 of 35 section-criterion pairs unanimous (97%)
single-sample totals would have been: 1.50 / 1.50 / 1.00   (all 3 samples: 1.33)
headings: h2 4
on threshold: none
splits: prior_art[3] 1/1/0
## END SUMMARY

## motivation - grade 1.00 (fired in 2 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 1/1/1  -> 1.00
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidate 1 (found by 3 of 15 passes): This paper aims to provide the definition for the term "immediate context".
candidate 2 (found by 3 of 15 passes): CWG would like to unify the treatment of noexcept-specifiers, function-contract-specifiers, default arguments, and annotations in order to improve the consistency of the language and the specification.

## audience - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 0/0/0  -> 0.00
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.33 (fired in 1 of 5 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 1/1/0  -> 0.67
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidate 1 (found by 1 of 15 passes): CWG would like to unify the treatment of noexcept-specifiers, function-contract-specifiers, default arguments, and annotations in order to improve the consistency of the language and the specification.
candidate 2 (found by 1 of 15 passes): The proposed unified treatment is that the immediate context excludes separately instantiated constructs and includes everything else (other than lambda bodies).

## vehicle - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 0/0/0  -> 0.00
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 0/0/0  -> 0.00
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 0/0/0  -> 0.00
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 5 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. EWG guidance                              0/0/0  -> 0.00
  [3] 2. Further questions for EWG                 0/0/0  -> 0.00
  [4] 3. Wording                                   0/0/0  -> 0.00
  [5] 4. References                                0/0/0  -> 0.00
candidates: (none validated)

-->
