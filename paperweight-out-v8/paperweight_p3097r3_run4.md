Verdict: Strong (9/14)

The paper offers a reasonably grounded case in some areas, particularly its discussion of prior art and the coordination problems that arise when contracts meet virtual functions across component boundaries. Its support is thinnest, however, in showing who is concretely affected and in demonstrating that the proposed behavior has been validated through implementation experience rather than merely asserted.

- The strongest support comes from the paper’s engagement with prior C++ contract proposals and other languages, showing both the history of failed attempts and why direct adoption of those models is unsuitable.
- The coordination discussion is also well supported, with concrete examples like `QIODevice` illustrating how inheritance hierarchies cross component boundaries and why callers cannot rely on dynamic type information.
- The weakest part is the absence of any established statement about who is affected by the current limitation or who would benefit from the proposed extension.
- The claims about implementation experience and why a library solution will not suffice remain asserted rather than demonstrated, leaving the practical validation of the design largely unsubstantiated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 6 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 16. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 8.33   accumulate 9.83   max 10.00

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.33  coordination 1.67  insufficiency 0.67  implementation 1.33
sample agreement: 61 of 70 section-criterion pairs unanimous (87%)
single-sample totals would have been: 9.50 / 10.50 / 8.50   (all 3 samples: 9.00)
headings: h2 9
on threshold: coordination
splits: motivation[4] 2/1/2  motivation[6] 2/0/0  vehicle[5] 1/1/2  vehicle[6] 2/2/0
        coordination[6] 2/0/2  coordination[7] 0/2/2  insufficiency[6] 2/2/0
        implementation[3] 1/2/1  implementation[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   2/1/2  -> 1.67
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/0/0  -> 0.67
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 2 (found by 3 of 30 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions.
candidate 3 (found by 3 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 4 (found by 2 of 30 passes): However, there are cases where controlled inheritance of assertions can be useful.

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
  [3] 1 Motivation                                 2/2/2  -> 2.00
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
candidate 4 (found by 2 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found (e.g., [[P0542R5](https://wg21.link/p0542r5)], [[P2521R5](https://wg21.link/p2521r5)], [[P2954R0](https://wg21.link/p2954r0)], [[P2932R3](https://wg21.link/p2932r3)]).

## vehicle - grade 1.33 (fired in 3 of 10 sections, strong in 0)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                1/1/2  -> 1.33
  [6] 4 Discussion                                 2/2/0  -> 1.33
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 2 of 30 passes): By contrast, our proposal evaluates only the assertions associated with the concrete virtual function call, and thus avoids the false positive.
candidate 3 (found by 1 of 30 passes): Extending the C++ facility to virtual functions requires understanding the kinds of correctness expectations that commonly apply to such functions, and ensuring that the proposed extension can express those expectations effectively.
candidate 4 (found by 1 of 30 passes): This proposal removes this limitation.

## coordination - grade 1.67 (fired in 3 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/0/2  -> 1.33
  [7] 5 Possible extensions                        0/2/2  -> 1.33
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): Inheritance hierarchies can span across such component boundaries. A base class may be defined in a library header and derived from another component, or independently in multiple components.
candidate 2 (found by 2 of 30 passes): The function `boo` cannot know the dynamic type of its parameter, nor whether it supports UTF-8 input; all it knows is that it is calling a virtual function whose interface requires an ASCII string.
candidate 3 (found by 2 of 30 passes): As an example, consider `QIODevice`, the base interface class of all I/O devices in the Qt framework.

## insufficiency - grade 0.67 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 2/2/0  -> 1.33
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): In a language where precondition assertions are OR-ed with those of overridden functions, these assertions could not be made to work.

## implementation - grade 1.33  [binary: max] (fired in 2 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.33   accumulate 1.33   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 1/2/1  -> 1.33
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
