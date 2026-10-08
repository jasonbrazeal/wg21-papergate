Verdict: Adequate (5/14)

The paper offers some grounding for its proposal, chiefly by pointing to existing implementation behavior and the acknowledged conservatism of the original CTAD rules, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why a library solution is impossible and whether the affected audience is more than hypothetical.

- The strongest support is the account of prior art, including the original rationale for the restriction and the narrow, rushed nature of the CWG3003 fix.
- The paper establishes that the change matters by connecting it to common naming practices and showing that the motivating example is not contrived.
- The claim that users are already depending on the behavior is plausible but not backed by evidence beyond the assertion that implementations accept it.
- The most glaring omission is the absence of any argument for why a library-level solution cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.00/14)

Provisionally addressed: 6 of 7. Provisional points: 5.00 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.00   corroborated 5.00   accumulate 5.50   max 6.67

## SUMMARY
grades: motivation 1.50  audience 0.50  prior_art 1.50  vehicle 0.33  coordination 0.17  insufficiency 0.00  implementation 1.00
sample agreement: 42 of 49 section-criterion pairs unanimous (86%)
single-sample totals would have been: 5.00 / 6.00 / 4.50   (all 3 samples: 5.00)
headings: h2 6
on threshold: motivation, prior_art
splits: motivation[4] 0/2/0  prior_art[2] 1/0/0  prior_art[3] 2/2/1  prior_art[4] 2/1/1
        vehicle[2] 0/1/1  coordination[4] 0/1/0  implementation[3] 0/0/1
## END SUMMARY

## motivation - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Deduction guides can only be declared t... 2/2/2  -> 2.00
  [4] 3 Restriction on dependent nested names w... 0/2/0  -> 0.67
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Giving names to certain template specializations is common practice; think of cases like `std::string`, where spelling `std::basic_string<char>` feels unnatural.
candidate 2 (found by 2 of 21 passes): These are already accepted in most implementations, and would be an easy change for the others.
candidate 3 (found by 1 of 21 passes): This paper proposes to relax some Class Template Argument deduction (CTAD) restrictions which were originally put in place for no well motivated reason other than simplicity and being conservative.
candidate 4 (found by 1 of 21 passes): This is not a contrived example, and naturally users would have no reason to believe this is not supposed to work, unless they are language lawyers.

## audience - grade 0.50 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Deduction guides can only be declared t... 1/1/1  -> 1.00
  [4] 3 Restriction on dependent nested names w... 0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): Giving names to certain template specializations is common practice; think of cases like `std::string`, where spelling `std::basic_string<char>` feels unnatural.

## prior_art - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/0/0  -> 0.33
  [3] 2 Deduction guides can only be declared t... 2/2/1  -> 1.67
  [4] 3 Restriction on dependent nested names w... 2/1/1  -> 1.33
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): According to the author of the paper which added the CTAD feature, this restriction was put in place for simplicity of specification and because a use case was not put forward at the time.
candidate 2 (found by 3 of 21 passes): The fix for [[CWG3003]](https://wg21.link/cwg3003), which was accepted in Croydon 2026, was the minimal fix concerned with the standard library use, and was rushed as so in order to avoid shipping this defect.
candidate 3 (found by 1 of 21 passes): These are already accepted in most implementations, and would be an easy change for the others.

## vehicle - grade 0.33 (fired in 1 of 7 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/1/1  -> 0.67
  [3] 2 Deduction guides can only be declared t... 0/0/0  -> 0.00
  [4] 3 Restriction on dependent nested names w... 0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): These are already accepted in most implementations, and would be an easy change for the others.

## coordination - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Deduction guides can only be declared t... 0/0/0  -> 0.00
  [4] 3 Restriction on dependent nested names w... 0/1/0  -> 0.33
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): Since all implementations already accept this, it’s highly likely enough time has passed where users could have started depending on this, similar to the standard library motivating use for CWG3003.

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
  [3] 2 Deduction guides can only be declared t... 0/0/1  -> 0.33
  [4] 3 Restriction on dependent nested names w... 1/1/1  -> 1.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): These are already accepted in most implementations, and would be an easy change for the others.
candidate 2 (found by 3 of 21 passes): All implementations currently accept this.
candidate 3 (found by 1 of 21 passes): but in practice only Clang rejects it.

-->
