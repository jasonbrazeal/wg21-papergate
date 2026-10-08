Verdict: Strong (9/14)

The paper offers substantial support for standardizing its virtual-function contract assertions, particularly through its engagement with prior art, its account of why the C++ standard is the right venue, and its reported implementation experience. The case is thinnest where the paper asserts breadth of affected users, independence of components, and the impossibility of a library solution without demonstrating those claims in the text.

- The strongest support comes from the paper’s treatment of prior proposals and other languages, showing both what has been tried and why those models do not transfer cleanly to C++.
- The paper also establishes why standardization is necessary by connecting the design to C++26 evaluation semantics and undefined-behaviour concerns that a library cannot address.
- The most glaring omission is the claim that the design covers all known use cases and all of Ada’s functionality, which is asserted rather than shown with evidence.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.00/14)

Provisionally addressed: 7 of 7. Provisional points: 9.00 of 14. Unsupported quotes rejected: 11. Replies missing: 0. Sections: 10. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.00   corroborated 9.67   accumulate 9.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 2.00  coordination 0.83  insufficiency 0.33  implementation 1.67
sample agreement: 60 of 70 section-criterion pairs unanimous (86%)
single-sample totals would have been: 10.00 / 8.00 / 9.00   (all 3 samples: 9.00)
headings: h2 9
on threshold: implementation
splits: motivation[4] 1/2/2  motivation[6] 2/2/0  audience[7] 0/0/1  prior_art[4] 2/0/2
        coordination[4] 0/1/0  coordination[5] 0/1/1  coordination[6] 0/1/0
        coordination[7] 2/1/0  insufficiency[6] 2/0/0  implementation[3] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 10 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/2/2  -> 2.00
  [4] 2 Overview                                   1/2/2  -> 1.67
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/0  -> 1.33
  [7] 5 Possible extensions                        2/2/2  -> 2.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions.
candidate 2 (found by 3 of 30 passes): For virtual functions, the expressible subset is currently very limited: `pre` and `post` cannot be used at all, leaving only `contract_assert`.
candidate 3 (found by 2 of 30 passes): Multiple approaches to precondition and postcondition assertions on virtual functions have been proposed, gained consensus, and lost it again when fundamental issues were found
candidate 4 (found by 2 of 30 passes): Such *widening of preconditions* and *narrowing of postconditions* is a basic application of contracts-based programming, fully compatible with the substitution principle, and supported by Eiffel, D, and Ada.

## audience - grade 0.17 (fired in 1 of 10 sections, strong in 0)
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
candidate 1 (found by 1 of 30 passes): Taken together, the set of extensions described in this section provides *all* of Ada's functionality for precondition and postcondition assertions ... and more broadly *all* currently known use cases for precondition and postcondition assertions on virtual functions

## prior_art - grade 2.00 (fired in 5 of 10 sections, strong in 4)
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
candidate 4 (found by 2 of 30 passes): The design presented in this paper addresses the shortcomings of earlier proposals, supports a broader range of use cases found in real-world code, and aligns naturally with C++26 contract-evaluation semantics and contract-violation handling.

## vehicle - grade 2.00 (fired in 3 of 10 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                2/2/2  -> 2.00
  [6] 4 Discussion                                 2/2/2  -> 2.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): providing a better fit for the C++ language than the more restrictive models in languages like Eiffel and D.
candidate 2 (found by 3 of 30 passes): Extending the C++ facility to virtual functions requires understanding the kinds of correctness expectations that commonly apply to such functions, and ensuring that the proposed extension can express those expectations effectively.
candidate 3 (found by 2 of 30 passes): By contrast, our proposal evaluates only the assertions associated with the concrete virtual function call, and thus avoids the false positive.
candidate 4 (found by 1 of 30 passes): The conclusion is that the "OR-ing preconditions, AND-ing postconditions" approach — originally designed by Bertrand Meyer for a *memory-safe* language with no undefined behaviour — is unsuitable for C++.

## coordination - grade 0.83 (fired in 4 of 10 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/1/0  -> 0.33
  [5] 3 Design goals and principles                0/1/1  -> 0.67
  [6] 4 Discussion                                 0/1/0  -> 0.33
  [7] 5 Possible extensions                        2/1/0  -> 1.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 30 passes): Different components should be able to introduce contract assertions independently, without requiring coordinated changes across the entire inheritance hierarchy or the codebases that participate in it.
candidate 2 (found by 2 of 30 passes): As an example, consider `QIODevice`, the base interface class of all I/O devices in the Qt framework.
candidate 3 (found by 1 of 30 passes): This design deliberately differs from earlier C++ proposals where contract assertions were always inherited by overriding functions.
candidate 4 (found by 1 of 30 passes): We should be able to reason about the correctness of each component individually.

## insufficiency - grade 0.33 (fired in 1 of 10 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 0/0/0  -> 0.00
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 2/0/0  -> 0.67
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 30 passes): In a language where precondition assertions are OR-ed with those of overridden functions, these assertions could not be made to work.

## implementation - grade 1.67  [binary: max] (fired in 1 of 10 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Revision history                             0/0/0  -> 0.00
  [3] 1 Motivation                                 2/1/2  -> 1.67
  [4] 2 Overview                                   0/0/0  -> 0.00
  [5] 3 Design goals and principles                0/0/0  -> 0.00
  [6] 4 Discussion                                 0/0/0  -> 0.00
  [7] 5 Possible extensions                        0/0/0  -> 0.00
  [8] 6 Proposed wording                           0/0/0  -> 0.00
  [9] Acknowledgements                             0/0/0  -> 0.00
  [10] Bibliography                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 30 passes): provided a complete implementation of that wording in GCC

-->
