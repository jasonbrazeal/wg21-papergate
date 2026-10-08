Verdict: Strong (8/14)

The paper offers substantial support for its standardization case in the areas of motivation, prior art, and the need for a language-level solution, but leaves important parts of the argument unaddressed. The thinnest support concerns who is affected by the problem and why a library-based approach cannot suffice, neither of which is established.

- The strongest support is the clear demonstration that virtual-function contracts are currently inexpressible and that earlier C++ designs failed on a known technical point.
- The paper also credibly establishes that existing languages and prior C++ proposals do not provide a directly adoptable model.
- The case for standardization is further supported by concrete interoperability concerns across component and library boundaries.
- The most glaring omission is the absence of any established account of who is affected by the limitation or why a library solution would be inadequate.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.33/14)

Provisionally addressed: 5 of 7. Provisional points: 8.33 of 14. Unsupported quotes rejected: 13. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.33   corroborated 8.00   accumulate 8.67   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.83  coordination 1.50  insufficiency 0.00  implementation 1.00
sample agreement: 62 of 70 section-criterion pairs unanimous (89%)
single-sample totals would have been: 8.00 / 8.50 / 9.00   (all 3 samples: 8.33)
headings: h2 9
on threshold: coordination
splits: motivation[4] 2/1/2  prior_art[4] 2/0/2  vehicle[1] 1/1/0  vehicle[5] 1/2/2
        coordination[5] 2/1/2  coordination[6] 0/2/2  coordination[7] 1/0/0
        implementation[7] 1/0/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 5)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   2/1/2  -> 1.67
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 2 (found by 3 of 30 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions.
candidate 3 (found by 3 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 4 (found by 3 of 30 passes): Such *widening of preconditions* and *narrowing of postconditions* is a basic application of contracts-based programming, fully compatible with the substitution principle, and supported by Eiffel, D, and Ada.

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

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   2/0/2  -> 1.33
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Each offers valuable lessons, but none provides a model suitable for direct adoption in C++, owing to fundamental differences in language design and philosophy.
candidate 2 (found by 3 of 30 passes): By contrast, in Eiffel, D, and Ada class-wide preconditions and postconditions, B::f implicitly inherits the preconditions and postconditions of C::f, and C::f implicitly inherits those of B::f and N::f.
candidate 3 (found by 3 of 30 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.
candidate 4 (found by 2 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found (e.g., [[P0542R5](https://wg21.link/p0542r5)], [[P2521R5](https://wg21.link/p2521r5)], [[P2954R0](https://wg21.link/p2954r0)], [[P2932R3](https://wg21.link/p2932r3)]).

## vehicle - grade 1.83 (fired in 3 of 10 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                1/2/2  -> 1.67
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): By contrast, our proposal evaluates only the assertions associated with the concrete virtual function call, and thus avoids the false positive.
candidate 2 (found by 2 of 30 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 3 (found by 2 of 30 passes): Extending the C++ facility to virtual functions requires understanding the kinds of correctness expectations that commonly apply to such functions, and ensuring that the proposed extension can express those expectations effectively.
candidate 4 (found by 1 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.

## coordination - grade 1.50 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                2/1/2  -> 1.67
  [6] 4 Discussion                                 0/2/2  -> 1.33
  [7] 5 Possible extensions                        1/0/0  -> 0.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 2 (found by 2 of 30 passes): The function `boo` cannot know the dynamic type of its parameter, nor whether it supports UTF-8 input; all it knows is that it is calling a virtual function whose interface requires an ASCII string.
candidate 3 (found by 1 of 30 passes): A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 4 (found by 1 of 30 passes): As an example, consider `QIODevice`, the base interface class of all I/O devices in the Qt framework.

## insufficiency - grade 0.00 (fired in 0 of 10 sections, strong in 0)
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

## implementation - grade 1.00  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/1/1  -> 1.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        1/0/0  -> 0.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): provided a complete implementation of that wording in GCC
candidate 2 (found by 1 of 30 passes): Notably, all previous C++ proposals that featured assertion inheritance — including C++20 Contracts [[P0542R5](https://wg21.link/p0542r5)] and their implementation in GCC — failed to do this correctly.

-->
