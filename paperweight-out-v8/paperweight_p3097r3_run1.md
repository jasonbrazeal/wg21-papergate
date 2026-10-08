Verdict: Strong (9/14)

The paper offers substantial support for the relevance of its design, the existence of prior art, and the need for a language-level solution, but it leaves the affected audience and practical implementation experience largely unsubstantiated. The thinnest parts concern the claim that a library cannot achieve the same effect and the evidence that the proposed wording has actually been implemented and validated.

- The strongest support is for why the feature matters, with the paper showing that virtual-function contract assertions are currently inexpressible and that earlier inheritance models failed.
- The paper also convincingly establishes prior art and alternatives by comparing Eiffel, D, and Ada and explaining why their models do not fit C++.
- The case for standardization is well supported through arguments about independent component evolution and avoiding false positives in contract evaluation.
- The most glaring omission is the absence of any established description of who is affected by the proposal, leaving the practical user base and impact unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 6 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 12. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 8.67   accumulate 9.50   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.67  coordination 2.00  insufficiency 0.50  implementation 1.00
sample agreement: 62 of 70 section-criterion pairs unanimous (89%)
single-sample totals would have been: 9.00 / 9.50 / 9.00   (all 3 samples: 9.17)
headings: h2 9
on threshold: vehicle
splits: motivation[4] 1/2/2  prior_art[3] 2/2/1  vehicle[1] 0/1/1  vehicle[5] 2/1/1
        coordination[5] 2/2/1  insufficiency[6] 0/2/0  insufficiency[7] 0/0/1
        implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   1/2/2  -> 1.67
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 2 (found by 3 of 30 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions.
candidate 3 (found by 3 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 4 (found by 3 of 30 passes): However, there are cases where controlled inheritance of assertions can be useful.

## audience - grade 0.00 (fired in 0 of 10 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 4 of 10 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/1  -> 1.67
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Each offers valuable lessons, but none provides a model suitable for direct adoption in C++, owing to fundamental differences in language design and philosophy.
candidate 2 (found by 3 of 30 passes): By contrast, in Eiffel, D, and Ada class-wide preconditions and postconditions, B::f implicitly inherits the preconditions and postconditions of C::f, and C::f implicitly inherits those of B::f and N::f.
candidate 3 (found by 3 of 30 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 4 (found by 2 of 30 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.

## vehicle - grade 1.67 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/1/1  -> 0.67
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                2/1/1  -> 1.33
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 2 of 30 passes): For the feature to be deployable at scale, different components should be able to introduce contract assertions independently, without requiring coordinated changes across the entire inheritance hierarchy or the codebases that participate in it.
candidate 3 (found by 2 of 30 passes): By contrast, our proposal evaluates only the assertions associated with the concrete virtual function call, and thus avoids the false positive.
candidate 4 (found by 1 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.

## coordination - grade 2.00 (fired in 3 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                2/2/1  -> 1.67
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The function `boo` cannot know the dynamic type of its parameter, nor whether it supports UTF-8 input; all it knows is that it is calling a virtual function whose interface requires an ASCII string.
candidate 2 (found by 3 of 30 passes): As an example, consider `QIODevice`, the base interface class of all I/O devices in the Qt framework.
candidate 3 (found by 2 of 30 passes): inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 4 (found by 1 of 30 passes): Dependencies are often provided as headers and precompiled binaries.

## insufficiency - grade 0.50 (fired in 2 of 10 sections, strong in 0)
under each rule: top2 0.50   corroborated 0.67   accumulate 0.50   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/2/0  -> 0.67
  [7] 5 Possible extensions                        0/0/1  -> 0.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): In a language where precondition assertions are OR-ed with those of overridden functions, these assertions could not be made to work.
candidate 2 (found by 1 of 30 passes): Note that the desired effect can already be accomplished today without such an add-on by using the non-virtual interface pattern.

## implementation - grade 1.00  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        0/1/0  -> 0.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): provided a complete implementation of that wording in GCC
candidate 2 (found by 1 of 30 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.

-->
