Verdict: Adequate to Strong (7/14)

The paper gives a reasonably solid account of why the core-language change is needed and how it fits with existing deduction behavior, but it leans heavily on implementation acceptance and a related library issue without fully developing those points as evidence for standardization. The thinnest parts are the absence of a library-only alternative and the limited detail on implementation experience and coordination.

- The strongest support is the explanation that current behavior is inconsistent with CTAD for alias templates and that no library wording fix is known without a core change.
- The paper also establishes relevant prior art by connecting the proposal to P0552R0 and to a closely related paper, P3863R0.
- The claims about affected users and implementation experience rest mainly on assertions that implementations accept the examples, without enough supporting detail to establish the breadth or reliability of that experience.
- The most glaring omission is that the paper does not establish why a library-only solution would be insufficient, despite that being a required part of the standardization case.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.17/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.17   corroborated 7.33   accumulate 7.17   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 73 of 77 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.00 / 7.50   (all 3 samples: 7.17)
headings: h2 10
on threshold: vehicle, coordination
splits: motivation[7] 1/0/0  audience[4] 0/0/1  prior_art[2] 0/1/1  prior_art[4] 2/0/0
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
  [7] Proposed Semantics                           1/0/0  -> 0.33
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes to update the core language wording to allow CTAD (class template argument deduction) for type template template parameters and treat it as a DR, addressing both CWG 3003 and LWG 4381.
candidate 2 (found by 3 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.
candidate 3 (found by 3 of 33 passes): This currently crashes most implementations, but as the *defining-type-id* of Alias doesn’t denote a deducible template, it should just be ill-formed.
candidate 4 (found by 2 of 33 passes): This means that default template arguments specified on the template template parameters are ignored during deduction and that types can be deduced that can’t otherwise be written using the name of the template template parameter.

## audience - grade 0.17 (fired in 1 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 0/0/1  -> 0.33
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   0/0/0  -> 0.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 33 passes): and all current implementations actually accept it.

## prior_art - grade 2.00 (fired in 6 of 11 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/1  -> 0.67
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/0/0  -> 0.67
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           2/2/2  -> 2.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             1/1/1  -> 1.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): But since [P0552R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0522r0.html) "DR: Matching of template template-arguments excludes compatible templates", a template template argument doesn’t have to match a template template parameter exactly; the template template parameter just needs to be more specialized than the template template argument.
candidate 2 (found by 3 of 33 passes): Current implementations accept the above examples (except for the last one) with the "simple substitution" semantics.
candidate 3 (found by 3 of 33 passes): This is consistent with how CTAD for alias templates works, and the proposal is to use those semantics instead of directly substituting the template template argument.
candidate 4 (found by 3 of 33 passes): Corentin Jabot has a very similar paper [P3863R0](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3863r0.pdf) "Minimal fix for CWG3003 (CTAD from template template parameters)".

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
candidate 1 (found by 3 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.

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

## implementation - grade 1.00  [binary: max] (fired in 2 of 11 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 1/1/1  -> 1.00
  [5] Examples                                     0/0/0  -> 0.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): and all current implementations actually accept it.
candidate 2 (found by 3 of 33 passes): Current implementations accept the above examples (except for the last one) with the "simple substitution" semantics.

-->
