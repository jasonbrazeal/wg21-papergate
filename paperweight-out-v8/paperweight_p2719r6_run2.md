Verdict: Adequate (4/14)

The paper offers a partial case for standardization, with its strongest material going to motivation and the limitations of existing mechanisms, but it leaves several essential questions unanswered. The support is thinnest around who would actually be affected, why the standard is the right venue, and whether the approach has been validated in practice.

- The paper clearly explains why type-aware allocation and deallocation matter and what current C++ mechanisms cannot express.
- It also shows awareness of prior art and alternative designs, including a rejected simpler mechanism and a possible resolution to an existing core issue.
- The most glaring omission is any account of who is affected by the problem or who would use the proposed feature.
- The paper also does not establish why a library solution is insufficient or provide evidence of implementation experience beyond a passing reference.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 4 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 4.33   accumulate 4.67   max 5.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.50  vehicle 0.00  coordination 0.00  insufficiency 0.50  implementation 0.33
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 4.00 / 4.00   (all 3 samples: 4.33)
headings: h2 7
on threshold: prior_art
splits: motivation[2] 1/1/2  prior_art[7] 1/1/0  implementation[3] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/2  -> 1.33
  [3] 2 Revision history                           2/2/2  -> 2.00
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   1/1/1  -> 1.00
  [6] 5 Design choices and notes                   2/2/2  -> 2.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): In addition to providing valuable information to the allocator, this allows the creation of type-specific `operator new` and `operator delete` for types that cannot have intrusive class-scoped operators specified.
candidate 2 (found by 3 of 24 passes): Knowledge of the type being [de]allocated in a *new-expression* is necessary in order to achieve certain levels of flexibility when defining a custom allocation function.
candidate 3 (found by 3 of 24 passes): In the current specification it is not possible for an author to specify a constexpr `operator new` or `operator delete`.
candidate 4 (found by 2 of 24 passes): There are many cases where projects may not want types to be allocated and deallocated via `new` and `delete` operators.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 Design choices and notes                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.50 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               1/1/1  -> 1.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 Design choices and notes                   2/2/2  -> 2.00
  [7] 6 Proposed wording                           1/1/0  -> 0.67
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): C++ currently provides two ways of customizing the creation of objects in new expressions.
candidate 2 (found by 3 of 24 passes): In an earlier draft, this paper was proposing the following (seemingly simpler) mechanism. Instead of using `std::type_identity<T>` as a tag, the compiler would search as per the following expression:
candidate 3 (found by 1 of 24 passes): [ Drafting note: The new wording for the return type of allocation and deallocation functions might resolve CWG1676 “auto return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “auto return type for main”. ]
candidate 4 (found by 1 of 24 passes): The new wording for the return type of allocation and deallocation functions might resolve CWG1676 “auto return type for allocation and deallocation functions”, as it follows the approach in CWG1669 “auto return type for main”.

## vehicle - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 Design choices and notes                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           0/0/0  -> 0.00
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 Design choices and notes                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.50 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           1/1/1  -> 1.00
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 Design choices and notes                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): However, in addition to these intrusive mechanisms being cumbersome and error-prone, they do not make it possible to customize how allocation is performed for types controlled by a third-party, or to customize allocation for an open set of types.

## implementation - grade 0.33  [binary: max] (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Introduction                               0/0/0  -> 0.00
  [3] 2 Revision history                           1/0/0  -> 0.33
  [4] 3 Current behavior recap                     0/0/0  -> 0.00
  [5] 4 Proposal                                   0/0/0  -> 0.00
  [6] 5 Design choices and notes                   0/0/0  -> 0.00
  [7] 6 Proposed wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgments                            0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): Simplified the lookup mechanism by removing the need to perform ADL (based on implementation experience)

-->
