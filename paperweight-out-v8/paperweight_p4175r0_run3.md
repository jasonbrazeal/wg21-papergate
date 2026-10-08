Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why the restriction is artificial and why users would expect the feature to work, but its broader case rests heavily on assertions about implementation behavior and existing dependence rather than demonstrated evidence. The thinnest parts are the absence of any discussion of a library-level alternative and the repeated but unsubstantiated claim that all implementations already accept the construct.

- The strongest support is the explanation that the original restriction was adopted for simplicity and conservatism, not for a substantive technical reason.
- The paper also establishes that the prior minimal fix was narrowly motivated by a standard library defect rather than the general language issue.
- The claim that users are already depending on the behavior is plausible but not backed by concrete examples or reports.
- The most glaring omission is the failure to address why a library solution would not be sufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.83/14)

Provisionally addressed: 6 of 7. Provisional points: 5.83 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.83   corroborated 5.67   accumulate 5.83   max 6.67

## SUMMARY
grades: motivation 2.00  audience 0.67  prior_art 1.67  vehicle 0.33  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 44 of 49 section-criterion pairs unanimous (90%)
single-sample totals would have been: 5.50 / 6.50 / 5.50   (all 3 samples: 5.83)
headings: h2 6
on threshold: prior_art
splits: audience[3] 1/0/0  prior_art[3] 1/1/2  vehicle[2] 0/1/0  vehicle[4] 0/1/0
        coordination[4] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Deduction guides can only be declared t... 2/2/2  -> 2.00
  [4] 3 Restriction on dependent nested names w... 2/2/2  -> 2.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This paper proposes to relax some Class Template Argument deduction (CTAD) restrictions which were originally put in place for no well motivated reason other than simplicity and being conservative.
candidate 2 (found by 3 of 21 passes): Giving names to certain template specializations is common practice; think of cases like `std::string`, where spelling `std::basic_string<char>` feels unnatural.
candidate 3 (found by 3 of 21 passes): This is not a contrived example, and naturally users would have no reason to believe this is not supposed to work, unless they are language lawyers.

## audience - grade 0.67 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Deduction guides can only be declared t... 1/0/0  -> 0.33
  [4] 3 Restriction on dependent nested names w... 1/1/1  -> 1.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Since all implementations already accept this, it’s highly likely enough time has passed where users could have started depending on this
candidate 2 (found by 1 of 21 passes): Giving names to certain template specializations is common practice; think of cases like `std::string`, where spelling `std::basic_string<char>` feels unnatural.

## prior_art - grade 1.67 (fired in 2 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Deduction guides can only be declared t... 1/1/2  -> 1.33
  [4] 3 Restriction on dependent nested names w... 2/2/2  -> 2.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): According to the author of the paper which added the CTAD feature, this restriction was put in place for simplicity of specification and because a use case was not put forward at the time.
candidate 2 (found by 3 of 21 passes): The fix for [[CWG3003]](https://wg21.link/cwg3003), which was accepted in Croydon 2026, was the minimal fix concerned with the standard library use, and was rushed as so in order to avoid shipping this defect.

## vehicle - grade 0.33 (fired in 2 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/1/0  -> 0.33
  [3] 2 Deduction guides can only be declared t... 0/0/0  -> 0.00
  [4] 3 Restriction on dependent nested names w... 0/1/0  -> 0.33
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): These are already accepted in most implementations, and would be an easy change for the others.
candidate 2 (found by 1 of 21 passes): Since all implementations already accept this, it’s highly likely enough time has passed where users could have started depending on this, similar to the standard library motivating use for CWG3003.

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Deduction guides can only be declared t... 0/0/0  -> 0.00
  [4] 3 Restriction on dependent nested names w... 0/1/0  -> 0.33
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Since all implementations already accept this, it’s highly likely enough time has passed where users could have started depending on this

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Deduction guides can only be declared t... 0/0/0  -> 0.00
  [4] 3 Restriction on dependent nested names w... 0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 3 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Deduction guides can only be declared t... 1/1/1  -> 1.00
  [4] 3 Restriction on dependent nested names w... 1/1/1  -> 1.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): These are already accepted in most implementations, and would be an easy change for the others.
candidate 2 (found by 3 of 21 passes): All implementations currently accept this.
candidate 3 (found by 1 of 21 passes): but in practice only Clang rejects it.
candidate 4 (found by 1 of 21 passes): in practice only Clang rejects it.

-->
