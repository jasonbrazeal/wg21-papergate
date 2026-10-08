Verdict: Adequate to Strong (7/14)

The paper offers solid grounding for the core technical motivation and the prior design history, but it leaves several practical and procedural points asserted rather than demonstrated. The thinnest support concerns the absence of implementation experience with the exact semantics being proposed and the lack of any argument for why a library-only solution is impossible.

- The paper clearly establishes why the issue matters by tying it to existing core and library defect reports and to current implementation crashes or ill-formed behavior.
- It also establishes credible prior art and alternatives by connecting the proposal to earlier evolution papers and explaining the intended deduction semantics.
- The claim that all current implementations accept the relevant cases is asserted but not substantiated with concrete evidence or version details.
- The most glaring omission is the failure to establish why a library-only fix will not do, despite the paper’s own framing that the library wording depends on core language changes.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.67   accumulate 7.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 71 of 77 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.00 / 7.50 / 7.50   (all 3 samples: 7.33)
headings: h2 10
on threshold: vehicle, coordination
splits: motivation[7] 0/1/1  audience[4] 0/1/1  prior_art[2] 0/1/1  prior_art[4] 0/2/2
        prior_art[6] 1/0/0  implementation[8] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           0/1/1  -> 0.67
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes to update the core language wording to allow CTAD (class template argument deduction) for type template template parameters and treat it as a DR, addressing both CWG 3003 and LWG 4381.
candidate 2 (found by 3 of 33 passes): This currently crashes most implementations, but as the *defining-type-id* of Alias doesn’t denote a deducible template, it should just be ill-formed.
candidate 3 (found by 3 of 33 passes): This means that default template arguments specified on the template template parameters are ignored during deduction and that types can be deduced that can’t otherwise be written using the name of the template template parameter.
candidate 4 (found by 2 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.

## audience - grade 0.33 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 0/1/1  -> 0.67
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   0/0/0  -> 0.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 33 passes): and all current implementations actually accept it.

## prior_art - grade 2.00 (fired in 5 of 11 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 0/2/2  -> 1.33
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/0/0  -> 0.33
  [7] Proposed Semantics                           2/2/2  -> 2.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): But since [P0552R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0522r0.html) "DR: Matching of template template-arguments excludes compatible templates", a template template argument doesn’t have to match a template template parameter exactly; the template template parameter just needs to be more specialized than the template template argument.
candidate 2 (found by 2 of 33 passes): addressing both CWG 3003 and LWG 4381
candidate 3 (found by 2 of 33 passes): it was pointed out that it was not the design intent of P0091R3 "Template argument deduction for class templates (Rev. 6)" to disallow CTAD for template template parameters.
candidate 4 (found by 2 of 33 passes): This is consistent with how CTAD for alias templates works, and the proposal is to use those semantics instead of directly substituting the template template argument.

## vehicle - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   0/0/0  -> 0.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   0/0/0  -> 0.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381 "std::ranges::to specification using CTAD not supported by core language".

## insufficiency - grade 0.00 (fired in 0 of 11 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 0/0/0  -> 0.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   0/0/0  -> 0.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 1.00  [binary: max] (fired in 3 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/1/0  -> 0.33
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): and all current implementations actually accept it.
candidate 2 (found by 3 of 33 passes): Current implementations accept the above examples (except for the last one) with the "simple substitution" semantics.
candidate 3 (found by 1 of 33 passes): None yet for the exact semantics specified in this paper, but all implementations already support the simple case.

-->
