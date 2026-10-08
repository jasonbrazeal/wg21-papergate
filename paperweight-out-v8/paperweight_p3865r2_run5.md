Verdict: Adequate (7/14)

The paper offers solid grounding for why the problem matters and for the existence of prior art and alternative approaches, but it leaves several essential parts of the standardization case largely unargued. The thinnest support concerns who is affected, why a library-only solution is impossible, and whether there is meaningful implementation experience behind the proposed direction.

- The strongest support is the clear connection to existing core and library issues, including a statement that the library wording has no known fix without core language changes.
- The paper also establishes prior art by citing earlier proposals and noting that current implementations accept many of the examples under simple substitution semantics.
- The case for coordination and interoperability is only asserted through the LWG 4381 reference, without showing how the proposed change interacts with related standardization efforts.
- The most glaring omission is the absence of any identified user community or concrete impact, leaving the affected constituency entirely unestablished.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 75 of 77 section-criterion pairs unanimous (97%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 10
on threshold: vehicle, coordination
splits: prior_art[2] 1/0/0  prior_art[11] 1/0/0
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
  [7] Proposed Semantics                           1/1/1  -> 1.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             0/0/0  -> 0.00
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): addressing both CWG 3003 and LWG 4381.
candidate 2 (found by 3 of 33 passes): This currently crashes most implementations, but as the *defining-type-id* of Alias doesn’t denote a deducible template, it should just be ill-formed.
candidate 3 (found by 3 of 33 passes): Both cases would currently be ill-formed due to the current rules for CTAD for alias templates, i.e., they would both fail the deducible check
candidate 4 (found by 2 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381.

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

## prior_art - grade 2.00 (fired in 7 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/0/0  -> 0.33
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           2/2/2  -> 2.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             1/1/1  -> 1.00
  [11] References                                   1/0/0  -> 0.33
candidate 1 (found by 3 of 33 passes): But since [P0552R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0522r0.html) "DR: Matching of template template-arguments excludes compatible templates", a template template argument doesn’t have to match a template template parameter exactly; the template template parameter just needs to be more specialized than the template template argument.
candidate 2 (found by 3 of 33 passes): Current implementations accept the above examples (except for the last one) with the "simple substitution" semantics.
candidate 3 (found by 3 of 33 passes): Corentin Jabot has a very similar paper [P3863R0](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3863r0.pdf) "Minimal fix for CWG3003 (CTAD from template template parameters)".
candidate 4 (found by 2 of 33 passes): But this looks like something that should be addressed by a future revision of [P3579R0](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3579r0.html) "Fix matching of non-type template parameters when matching template template parameters"

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
candidate 1 (found by 2 of 33 passes): There is no known fix for the library wording without changes to the core language, see LWG 4381 "std::ranges::to specification using CTAD not supported by core language".
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
