Verdict: Adequate (4/14)

The paper offers only a narrow slice of the case for standardization: it can point to real implementation experience in GCC and Clang, but most of the surrounding argument is asserted rather than demonstrated. The thinnest areas are the absence of any explanation for why the standard must change rather than relying on existing mechanisms, and the lack of a library-based alternative.

- The strongest support is the implementation experience, with both a longstanding GCC extension and a Clang prototype showing the feature is technically feasible.
- The paper claims real-world breakage during a C++20 upgrade, but does not provide enough detail to establish who is affected or how widespread the problem is.
- The discussion of prior art and alternatives is only gestured at, leaving the design space and tradeoffs largely unexplored.
- Most glaringly, the paper never establishes why a standard change is necessary or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.33/14)

Provisionally addressed: 5 of 7. Provisional points: 4.33 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.33   corroborated 5.67   accumulate 4.33   max 6.67

## SUMMARY
grades: motivation 1.00  audience 0.50  prior_art 0.50  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 48 of 49 section-criterion pairs unanimous (98%)
single-sample totals would have been: 5.00 / 4.00 / 4.00   (all 3 samples: 4.33)
headings: h2 6
on threshold: motivation
splits: coordination[3] 2/0/0
## END SUMMARY

## motivation - grade 1.00 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): But there is currently no way to designate the base class here.
candidate 2 (found by 1 of 21 passes): However, the two do not mix: a designated initializer can currently only refer to a direct non-static data members.
candidate 3 (found by 1 of 21 passes): While I can initialize an `A` like `A{.a=1}`, I cannot designated-initialize `B`.

## audience - grade 0.50 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## prior_art - grade 0.50 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   1/1/1  -> 1.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The original revisions of this paper dealt with how to name the `A` base class of `B`, and what this means for more complicated base classes (such at those with template parameters).

## vehicle - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/0/0  -> 0.67
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): gcc in `-std=c++17` mode — still to this day on trunk — supports `B{{.a=1}, .b=2}`. We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Proposal                                   0/0/0  -> 0.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Proposal                                   2/2/2  -> 2.00
  [5] 4 Wording                                    0/0/0  -> 0.00
  [6] 5 Acknowledgements                           0/0/0  -> 0.00
  [7] 6 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): gcc in `-std=c++17` mode — still to this day on trunk — supports `B{{.a=1}, .b=2}`.
candidate 2 (found by 3 of 21 passes): I implemented this [in clang](https://github.com/llvm/llvm-project/compare/main...brevzin:llvm-project:p2287?expand=1) in a very literal way

-->
