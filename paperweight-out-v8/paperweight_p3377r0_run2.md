Verdict: Strong (8/14)

The paper gives a solid account of why the operations it targets are needed during constant evaluation and shows that a plausible implementation exists, but it leaves several parts of the standardization case asserted rather than demonstrated. The thinnest support is around coordination with existing features and the claim that a library solution cannot suffice.

- The strongest support is the explanation of the constexpr blocking problems and the confusion caused by overloading `reinterpret_cast` for unrelated transformations.
- The paper also establishes prior art and alternatives by surveying earlier proposals and mapping replacement APIs onto valid use cases.
- Implementation experience is credibly established through a proof-of-concept clang fork covering both Itanium and Microsoft ABIs.
- The most glaring omission is the absence of any established discussion of coordination and interoperability with other standard features or implementations.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.17/14)

Provisionally addressed: 6 of 7. Provisional points: 8.17 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.17   corroborated 8.33   accumulate 8.33   max 9.67

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.33  coordination 0.00  insufficiency 0.67  implementation 2.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 7.50 / 9.00 / 8.00   (all 3 samples: 8.17)
headings: h2 7
on threshold: vehicle, implementation
splits: audience[3] 0/1/0  prior_art[1] 1/1/0  vehicle[3] 0/1/1  vehicle[7] 0/0/1
        insufficiency[6] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   1/1/1  -> 1.00
  [3] It's not just about compile-time programming 2/2/2  -> 2.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/2  -> 2.00
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Over many years of the constexprification of C++, the committee have identified various blocking problems.
candidate 2 (found by 3 of 24 passes): Currently such code can't be `constexpr`, so library authors opt for two different codepaths, one for runtime and one for constant evaluation.
candidate 3 (found by 2 of 24 passes): As `reinterpret_cast` is defined to do various transformations, it's really easy to get confused what is supposed to be done just by looking at the code, like here in this snippet: `auto x = reinterpret_cast&lt;T>(val);`.
candidate 4 (found by 1 of 24 passes): As `reinterpret_cast` is defined to do various transformations, it's really easy to get confused what is supposed to be done just by looking at the code

## audience - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/1/0  -> 0.33
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  0/0/0  -> 0.00
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): A huge side-effect of this proposal is improving the safety of C++ by making explicitly visible the programmer's intent, where previously she needed to use `reinterpret_cast` for multiple wildly different purposes.

## prior_art - grade 2.00 (fired in 5 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] Motivation                                   1/1/1  -> 1.00
  [3] It's not just about compile-time programming 1/1/1  -> 1.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/2  -> 2.00
  [7] Implementation                               2/2/2  -> 2.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper proposes features previously unavailable during constant evaluation (in "`constexpr`").
candidate 2 (found by 3 of 24 passes): The validity of these operations was explored by Jeff Snyder in [P0149R0](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0149r0.pdf), but they were removed from the paper due to implementation complexity concerns.
candidate 3 (found by 3 of 24 passes): Is not proposed by this paper and the pointer tagging functionality is proposed by [P3125](https://wg21.link/P3125) which does it by providing a value type which can be tracked by compiler, so compiler can also have metadata with the tag.
candidate 4 (found by 2 of 24 passes): First, it explores all valid use-cases of `reinterpret_cast`, and identifies a replacement API for each.

## vehicle - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/1/1  -> 0.67
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/2  -> 2.00
  [7] Implementation                               0/0/1  -> 0.33
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The only portable way is asking the standard library to provide an implementation compatible with the target architecture.
candidate 2 (found by 2 of 24 passes): A huge side-effect of this proposal is improving the safety of C++ by making explicitly visible the programmer's intent, where previously she needed to use `reinterpret_cast` for multiple wildly different purposes.
candidate 3 (found by 1 of 24 passes): Putting this into language would allows us to easily make things like `std::is_pointer_v<a_function_pointer>` to be `true`.

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

## insufficiency - grade 0.67 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/0/0  -> 0.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  1/2/1  -> 1.33
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The only portable way is asking the standard library to provide an implementation compatible with the target architecture.

## implementation - grade 2.00  [binary: max] (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Motivation                                   0/0/0  -> 0.00
  [3] It's not just about compile-time programming 0/0/0  -> 0.00
  [4] Disclaimer                                   0/0/0  -> 0.00
  [5] Summary                                      0/0/0  -> 0.00
  [6] reinterpretcast's use-cases                  2/2/2  -> 2.00
  [7] Implementation                               0/0/0  -> 0.00
  [8] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): A proof-of-concept implementation was successful for the itanium and microsoft ABIs in a fork of clang by Hana.

-->
