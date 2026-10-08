Verdict: Adequate to Strong (8/14)

The paper offers a solid foundation for its core motivation and for the existence of a viable implementation path, but it leaves several essential parts of the standardization case asserted rather than demonstrated. The thinnest support concerns why this must be done in the standard rather than in a library, and there is no material at all on coordination or interoperability with existing features and implementations.

- The paper most convincingly establishes why the problem matters and that a proof-of-concept implementation exists for major ABIs.
- It also credibly surveys prior art and alternatives by mapping the valid uses of `reinterpret_cast` to replacement operations.
- The case for affected users and for standardization specifically rests mainly on repeated claims about `std::function`, `std::any`, and polymorphic types, without showing those users or their needs in detail.
- The most glaring omission is the complete absence of discussion about coordination and interoperability with existing standard facilities, implementations, or related proposals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.67/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.67   corroborated 8.33   accumulate 8.00   max 9.67

## SUMMARY
grades: motivation 1.83  audience 0.33  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 0.83  implementation 1.67
sample agreement: 48 of 56 section-criterion pairs unanimous (86%)
single-sample totals would have been: 7.50 / 9.00 / 7.00   (all 3 samples: 7.67)
headings: h2 7
on threshold: vehicle, insufficiency, implementation
splits: motivation[3] 2/2/1  audience[2] 0/1/1  vehicle[2] 0/1/0  vehicle[3] 1/0/0
        vehicle[6] 2/2/1  insufficiency[6] 2/2/1  implementation[6] 1/2/2
        implementation[7] 1/0/0
## END SUMMARY

## motivation - grade 1.83 (fired in 3 of 8 sections, strong in 2)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] It's not just about compile-time programming 2/2/1  -> 1.67
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/2  -> 2.00
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Over many years of the constexprification of C++, the committee have identified various blocking problems.
candidate 2 (found by 2 of 24 passes): As `reinterpret_cast` is defined to do various transformations, it's really easy to get confused what is supposed to be done just by looking at the code
candidate 3 (found by 1 of 24 passes): As `reinterpret_cast` is defined to do various transformations, it's really easy to get confused what is supposed to be done just by looking at the code, like here in this snippet: `auto x = reinterpret_cast<T>(val);`.
candidate 4 (found by 1 of 24 passes): Even when defined, when done explicitly, such manipulation is problematic when combined with pointer authentication. It also can't work on architectures without numeric addresses (like the C++ constant evaluator).

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/1/1  -> 0.67
  [3] It's not just about compile-time programming 0/0/0  -> 0.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  0/0/0  -> 0.00
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): This will allow easy constexprification of at least `std::function`, `std::any`, and other polymorphic types in the standard library.

## prior_art - grade 2.00 (fired in 5 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] It's not just about compile-time programming 1/1/1  -> 1.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/2  -> 2.00
  [7] Implementation                               2/2/2  -> 2.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): First, it explores all valid use-cases of `reinterpret_cast`, and identifies a replacement API for each.
candidate 2 (found by 3 of 24 passes): This paper doesn't aim to remove `reinterpret_cast`; it aims to provide bounded functionality which happens to work also during constant evaluation, in the same manner as `static_cast`, `const_cast` and `dynamic_cast` have done with c-style casts.
candidate 3 (found by 2 of 24 passes): One can even say `reinterpret_cast` is *"a swiss-army knife with multiple footguns and a minimal manual"*.
candidate 4 (found by 2 of 24 passes): The validity of these operations was explored by Jeff Snyder in [P0149R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0149r0.pdf), but they were removed from the paper due to implementation complexity concerns.

## vehicle - grade 1.00 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/1/0  -> 0.33
  [3] It's not just about compile-time programming 1/0/0  -> 0.33
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/1  -> 1.67
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The only portable way is asking the standard library to provide an implementation compatible with the target architecture.
candidate 2 (found by 1 of 24 passes): This will allow easy constexprification of at least `std::function`, `std::any`, and other polymorphic types in the standard library.
candidate 3 (found by 1 of 24 passes): A huge side-effect of this proposal is improving the safety of C++ by making explicitly visible the programmer's intent, where previously she needed to use `reinterpret_cast` for multiple wildly different purposes.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/0/0  -> 0.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  0/0/0  -> 0.00
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.83 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/0/0  -> 0.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/1  -> 1.67
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): It also can't work on architectures without numeric addresses (like the C++ constant evaluator). The only portable way is asking the standard library to provide an implementation compatible with the target architecture.
candidate 2 (found by 1 of 24 passes): The only portable way is asking the standard library to provide an implementation compatible with the target architecture.

## implementation - grade 1.67  [binary: max] (fired in 2 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.67   corroborated 1.67   accumulate 1.67   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/0/0  -> 0.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  1/2/2  -> 1.67
  [7] Implementation                               1/0/0  -> 0.33
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): A proof-of-concept implementation was successful for the itanium and microsoft ABIs in a fork of clang by Hana.
candidate 2 (found by 1 of 24 passes): Working on it, did some prototypes for individual use-cases.

-->
