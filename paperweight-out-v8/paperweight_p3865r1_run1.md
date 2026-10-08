Verdict: Adequate (7/14)

The paper gives a reasonably clear account of why the current interaction between CTAD and template template parameters is defective, and it grounds that motivation in existing core and library issues, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest areas are the absence of a concrete affected-user picture, the lack of evidence that a library-only solution is impossible, and the reliance on implementation behavior without a structured implementation-experience report.

- The strongest support is the established motivation, anchored in CWG 3003 and LWG 4381 and in the observation that current rules make otherwise plausible cases ill-formed or crash implementations.
- The paper also establishes relevant prior art by tracing the design intent of P0091R3 and the later effect of P0552R0 on template template argument matching.
- The claim that no library fix is possible without core language changes is only asserted by reference to LWG 4381, not established with analysis or alternatives.
- The most glaring omission is the lack of any established description of who is affected, leaving the practical scope and urgency of the problem largely unsupported.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (7.00/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 7.00 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 11. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.00   corroborated 7.00   accumulate 7.00   max 9.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 1.00
sample agreement: 76 of 77 section-criterion pairs unanimous (99%)
single-sample totals would have been: 7.00 / 7.00 / 7.00   (all 3 samples: 7.00)
headings: h2 10
on threshold: vehicle, coordination
splits: prior_art[10] 1/1/0
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
candidate 1 (found by 3 of 33 passes): This paper proposes to update the core language wording to allow CTAD (class template argument deduction) for type template template parameters and treat it as a DR, addressing both CWG 3003 and LWG 4381.
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

## prior_art - grade 2.00 (fired in 6 of 11 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] Changelog                                    0/0/0  -> 0.00
  [4] Introduction                                 2/2/2  -> 2.00
  [5] Examples                                     2/2/2  -> 2.00
  [6] Status Quo                                   1/1/1  -> 1.00
  [7] Proposed Semantics                           2/2/2  -> 2.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] Wording (relative to N5032)                  0/0/0  -> 0.00
  [10] Acknowledgements                             1/1/0  -> 0.67
  [11] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 33 passes): This paper proposes to update the core language wording to allow CTAD (class template argument deduction) for type template template parameters and treat it as a DR, addressing both CWG 3003 and LWG 4381.
candidate 2 (found by 3 of 33 passes): it was pointed out that it was not the design intent of P0091R3 "Template argument deduction for class templates (Rev. 6)" to disallow CTAD for template template parameters.
candidate 3 (found by 3 of 33 passes): But since [P0552R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0522r0.html) "DR: Matching of template template-arguments excludes compatible templates", a template template argument doesn’t have to match a template template parameter exactly; the template template parameter just needs to be more specialized than the template template argument.
candidate 4 (found by 3 of 33 passes): Current implementations accept the above examples (except for the last one) with the "simple substitution" semantics.

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
