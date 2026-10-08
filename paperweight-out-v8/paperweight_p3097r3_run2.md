Verdict: Strong (9/14)

The paper offers substantial support for standardizing its approach to virtual function contract assertions, particularly in explaining why the feature matters, how it differs from prior art, and why it belongs in the standard rather than in a library. The support is thinnest around the breadth of the affected audience and around concrete implementation experience, where the paper asserts more than it demonstrates.

- The strongest support is the paper’s account of prior C++ contract proposals and their failures, which grounds the need for a new design in documented history.
- The paper also makes a clear case that the standard is the right venue, since the proposed semantics avoid false positives that arise in other languages’ inheritance models.
- The discussion of cross-component hierarchies and real interfaces like `QIODevice` credibly establishes that coordination and interoperability concerns are not hypothetical.
- The most glaring omission is the lack of established evidence about who is affected and whether the proposed wording has been meaningfully implemented and exercised, leaving the practical reach and readiness of the proposal largely asserted.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.67/14)

Provisionally addressed: 7 of 7. Provisional points: 8.67 of 14. Unsupported quotes rejected: 14. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.67   corroborated 8.00   accumulate 9.00   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 0.17  implementation 1.33
sample agreement: 61 of 70 section-criterion pairs unanimous (87%)
single-sample totals would have been: 8.00 / 8.00 / 10.00   (all 3 samples: 8.67)
headings: h2 9
on threshold: vehicle, coordination
splits: motivation[4] 1/2/1  motivation[6] 2/2/0  audience[5] 0/0/1  prior_art[4] 0/2/0
        prior_art[8] 0/1/0  coordination[7] 1/1/0  insufficiency[7] 0/0/1
        implementation[3] 1/1/2  implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   1/2/1  -> 1.33
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/0  -> 1.33
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 2 (found by 3 of 30 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions.
candidate 3 (found by 3 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 4 (found by 2 of 30 passes): Such misuse of a polymorphic interface should be caught early.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/1  -> 0.33
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): C++ is a mature and widely used language with billions of lines of existing code deployed across many diverse domains

## prior_art - grade 2.00 (fired in 6 of 10 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   0/2/0  -> 0.67
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/1/0  -> 0.33
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.
candidate 2 (found by 3 of 30 passes): We are aware of three languages that provide built-in precondition and postcondition assertions fully integrated with runtime polymorphism: Eiffel, D, and Ada.
candidate 3 (found by 3 of 30 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 4 (found by 2 of 30 passes): By contrast, in Eiffel, D, and Ada class-wide preconditions and postconditions, B::f implicitly inherits the preconditions and postconditions of C::f, and C::f implicitly inherits those of B::f and N::f.

## vehicle - grade 1.50 (fired in 2 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 2 of 30 passes): By contrast, our proposal evaluates only the assertions associated with the concrete virtual function call, and thus avoids the false positive.
candidate 3 (found by 1 of 30 passes): The conclusion is that the "OR-ing preconditions, AND-ing postconditions" approach — originally designed by Bertrand Meyer for a *memory-safe* language with no undefined behaviour — is unsuitable for C++.

## coordination - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                1/1/1  -> 1.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        1/1/0  -> 0.67
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): The function `boo` cannot know the dynamic type of its parameter, nor whether it supports UTF-8 input; all it knows is that it is calling a virtual function whose interface requires an ASCII string.
candidate 2 (found by 2 of 30 passes): A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 3 (found by 1 of 30 passes): inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 4 (found by 1 of 30 passes): As an example, consider `QIODevice`, the base interface class of all I/O devices in the Qt framework.

## insufficiency - grade 0.17 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        0/0/1  -> 0.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): However, this approach requires refactoring the base class function definition, which may not always be possible or practical.

## implementation - grade 1.33  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/2  -> 1.33
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        0/1/0  -> 0.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): provided a complete implementation of that wording in GCC
candidate 2 (found by 1 of 30 passes): provided a complete implementation of that wording in GCC, and re-proposed it.
candidate 3 (found by 1 of 30 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.

-->
