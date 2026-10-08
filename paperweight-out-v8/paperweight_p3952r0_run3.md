Verdict: Adequate to Strong (7/14)

The paper offers some concrete grounding for standardization, chiefly through its implementation experience and its acknowledgment of prior art, but it leaves several essential parts of its own case asserted rather than demonstrated. The thinnest support is around why a library-only solution is insufficient, which is not addressed at all, and around the motivating claims that the problem is widespread and that standardization is the right remedy.

- The strongest support is implementation experience, with a Clang intrinsic implementation and existing use in libc++ cited directly.
- Prior art and alternatives are established through the merged parallel proposal and named functions in Boost, Qt, and LLVM.
- The paper claims, but does not establish, that the problem matters and that many projects are affected, relying on general statements rather than demonstrated impact.
- The most glaring omission is the absence of any case for why a library facility will not do, leaving the need for standardization itself unargued.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.33/14, close to Adequate)

Provisionally addressed: 6 of 7. Provisional points: 7.33 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.33   corroborated 7.67   accumulate 7.33   max 10.67

## SUMMARY
grades: motivation 0.33  audience 1.00  prior_art 2.00  vehicle 1.00  coordination 1.00  insufficiency 0.00  implementation 2.00
sample agreement: 40 of 42 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 7.00 / 8.00   (all 3 samples: 7.33)
headings: h2 5
on threshold: audience, vehicle, coordination
splits: motivation[3] 0/0/2  implementation[1] 1/1/0
## END SUMMARY

## motivation - grade 0.33 (fired in 1 of 6 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Overview                                   0/0/0  -> 0.00
  [3] 2 Discussion                                 0/0/2  -> 0.67
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): because a series of parameters of the same type is known to invite call sites to get the argument order wrong without a warning

## audience - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Overview                                   2/2/2  -> 2.00
  [3] 2 Discussion                                 0/0/0  -> 0.00
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: libc++: `__is_pointer_in_range` [[LLVM 2025]], Qt: `q_points_into_range` [[Qt 2020]], Boost: `pointer_in_range`, `ptr_in_range` [[Boost 2014]].
candidate 2 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: libc++: `__is_pointer_in_range`, Qt: `q_points_into_range`, Boost: `pointer_in_range`, `ptr_in_range`
candidate 3 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: libc++, Qt, Boost.

## prior_art - grade 2.00 (fired in 3 of 6 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] 1 Overview                                   2/2/2  -> 2.00
  [3] 2 Discussion                                 2/2/2  -> 2.00
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): The parallel proposal [[P3234R1](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2024/p3234r1.html)] by Glen Fernandes is merged into this paper.
candidate 2 (found by 3 of 18 passes): This paper proposes the “is-pointer” name **“is_pointer_in_range”** which follows existing practice in Boost and LLVM.
candidate 3 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: * libc++: `__is_pointer_in_range` [[LLVM 2025]] * Qt: `q_points_into_range` [[Qt 2020]] * Boost: `pointer_in_range`, `ptr_in_range` [[Boost 2014]]
candidate 4 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: libc++: `__is_pointer_in_range` [[LLVM 2025]], Qt: `q_points_into_range` [[Qt 2020]], Boost: `pointer_in_range`, `ptr_in_range` [[Boost 2014]].

## vehicle - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Overview                                   2/2/2  -> 2.00
  [3] 2 Discussion                                 0/0/0  -> 0.00
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): it is already widely implemented in standard library implementations (e.g., for efficient `string` `insert`/`append` ) but by relying on unspecified behavior or tolerating false positives

## coordination - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Overview                                   2/2/2  -> 2.00
  [3] 2 Discussion                                 0/0/0  -> 0.00
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): it is already widely implemented in standard library implementations (e.g., for efficient `string` `insert`/`append` ) but by relying on unspecified behavior or tolerating false positives
candidate 2 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: libc++, Qt, Boost.

## insufficiency - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Overview                                   0/0/0  -> 0.00
  [3] 2 Discussion                                 0/0/0  -> 0.00
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/0  -> 0.67
  [2] 1 Overview                                   2/2/2  -> 2.00
  [3] 2 Discussion                                 2/2/2  -> 2.00
  [4] 3 Wording                                    0/0/0  -> 0.00
  [5] 4 Acknowledgments                            0/0/0  -> 0.00
  [6] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Hana Dusíková has implemented this proposal with a Clang compiler intrinsic, as described in her parallel proposal [[P3852R0](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3852r0.html)].
candidate 2 (found by 2 of 18 passes): The parallel proposal [[P3852R0](https://open-std.org/jtc1/sc22/wg21/docs/papers/2025/p3852r0.html)] by Hana Dusíková provides an implementation
candidate 3 (found by 2 of 18 passes): libc++: `__is_pointer_in_range` [[LLVM 2025](https://github.com/llvm/llvm-project/blob/main/libcxx/include/__utility/is_pointer_in_range.h)]
candidate 4 (found by 1 of 18 passes): Many projects make this a named function in some form, including large library collections such as: * libc++: `__is_pointer_in_range` [[LLVM 2025](https://github.com/llvm/llvm-project/blob/main/libcxx/include/__utility/is_pointer_in_range.h)]

-->
