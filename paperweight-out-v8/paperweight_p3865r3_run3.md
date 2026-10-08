Verdict: Adequate (7/14)

The paper offers solid support on the motivating problem, prior art, and the existence of implementation experience, but it leaves several essential parts of the standardization case largely unargued. The thinnest areas are the absence of any identified affected user population and the lack of a clear demonstration that a library-only solution is impossible.

- The strongest support is the explanation of why current deduction rules produce ill-formed or surprising results and why that matters for template template parameters.
- The paper also credibly grounds the proposal in prior discussions and existing implementation behavior, including references to earlier papers and issue reports.
- The case for why a core language change is necessary rests on a single assertion about library wording, without enough surrounding argument to establish that no library workaround is possible.
- The most glaring omission is that the paper never identifies who is affected, so the practical urgency and scope of the problem remain unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 72 of 77 section-criterion pairs unanimous (94%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 10
on threshold: vehicle, coordination
splits: motivation[2] 0/1/0  prior_art[2] 0/1/1  prior_art[4] 0/2/2  prior_art[11] 0/1/1
        implementation[8] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           1/1/1  -> 1.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This means that default template arguments specified on the template template parameters are ignored during deduction and that types can be deduced that can’t otherwise be written using the name of the template template parameter.
candidate 2 (found by 2 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.
candidate 3 (found by 2 of 33 passes): It seems reasonable for the type of `x` to be deduced as `C<int>`.
candidate 4 (found by 2 of 33 passes): Both cases would currently be ill-formed due to the current rules for CTAD for alias templates, i.e., they would both fail the deducible check

## audience - grade 0.00 (fired in 0 of 11 sections, strong in 0)
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

## prior_art - grade 2.00 (fired in 6 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 0/2/2  -> 1.33
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           2/2/2  -> 2.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/1/1  -> 0.67
candidate 1 (found by 3 of 33 passes): But since [P0552R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0522r0.html) "DR: Matching of template template-arguments excludes compatible templates", a template template argument doesn’t have to match a template template parameter exactly; the template template parameter just needs to be more specialized than the template template argument.
candidate 2 (found by 3 of 33 passes): Current implementations accept the above examples (except for the last one) with the "simple substitution" semantics.
candidate 3 (found by 2 of 33 passes): addressing both CWG 3003 and LWG 4381.
candidate 4 (found by 2 of 33 passes): it was pointed out that it was not the design intent of P0091R3 "Template argument deduction for class templates (Rev. 6)" to disallow CTAD for template template parameters.

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

## coordination - grade 1.00 (fired in 1 of 11 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 33 passes): the library makes use of this feature in [[range.utility.conv.to]](https://eel.is/c++draft/range.utility.conv.to) (adopted in C++23)
candidate 2 (found by 1 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.

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
