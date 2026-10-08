Verdict: Strong (11/14)

The paper offers substantial evidence that a null-terminated string view type is widely used, independently implemented, and desired for safer and more convenient interaction with C-style APIs. Its thinnest support concerns the necessity of standardization itself: the arguments that this must be a standard library type rather than a shared vocabulary type, and that a library solution cannot suffice, are asserted more than demonstrated.

- The strongest support is the breadth of prior art and implementation experience, including independent implementations from Microsoft, Google, NVIDIA, and many smaller projects, with measurable growth in GitHub usage.
- The paper clearly establishes who is affected by showing active use across major codebases and repeated requests from reviewers for exactly this type.
- The case for why the standard is needed rests largely on the claim that the type is a “lingua franca” and on the persistence of awkward choices among `const char*`, `std::string`, and `string_view`, without showing that existing non-standard implementations fail to meet that need.
- The most glaring omission is the lack of a convincing argument that a library cannot do the job; the single cited reason about unenforceable contracts is asserted but not developed into a case that standardization is the only viable path.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 8. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.33   accumulate 11.00   max 11.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 1.50  insufficiency 0.17  implementation 2.00
sample agreement: 56 of 63 section-criterion pairs unanimous (89%)
single-sample totals would have been: 10.50 / 10.50 / 11.00   (all 3 samples: 10.67)
headings: h2 8
on threshold: coordination
splits: motivation[2] 0/1/1  motivation[7] 2/1/2  audience[5] 1/1/0  vehicle[5] 0/1/0
        coordination[5] 1/0/0  insufficiency[6] 0/0/1  implementation[6] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/1  -> 0.67
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     0/0/0  -> 0.00
  [7] 6 Design rationale                           2/1/2  -> 1.67
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The use case of having a null-terminated string is much more common, in particular in interaction with C APIs (such as OS APIs, things like the Yubico libfido2 library, libsqlite and others).
candidate 2 (found by 3 of 27 passes): What we observed is that, in some case, this might not only make the code safer, but also enable new optimizations.
candidate 3 (found by 2 of 27 passes): We propose a standard string view type that guarantees null-termination.
candidate 4 (found by 2 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.

## audience - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/1/0  -> 0.67
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Github code search shows similar popularity between https://github.com/search?q=%2F%5Cbcstring_view%5Cb%2F%20language%3Ac%2B%2B%20-is%3Afork&type=code (1.2k results as of the time of writing) and https://github.com/search?q=%2F%5Cbzstring_view%5Cb%2F+language%3Ac%2B%2B+-is%3Afork&type=code (680 results as of the time of writing).
candidate 3 (found by 2 of 27 passes): It was specifically requested by several reviewers of this work.
candidate 4 (found by 2 of 27 passes): Since the first draft of this paper the use of cstring_view and cstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.

## prior_art - grade 2.00 (fired in 5 of 9 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2495r0.pdf attempts to directly patch this specific example. The solution bypasses that the problem is that we're missing an unbroken type-safe chain of knowledge that the value being passed is or is not null-terminated.
candidate 3 (found by 3 of 27 passes): There is an adjoint paper (P3862) that proposes to fix this in the existing-but-unpublished C++26 standard to avoid future deviation in having std::string::subview return string_view for subview(n).
candidate 4 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

## vehicle - grade 1.00 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/1/0  -> 0.33
  [6] 5 Discussion on the type                     1/1/1  -> 1.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As it's a lingua franca type, it should be part of the standard C++ library.
candidate 2 (found by 2 of 27 passes): Since the first draft of this paper the use of cstring_view and cstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 1 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 4 (found by 1 of 27 passes): Without them we retain the question we had before - const char*, const std::string& or string_view?

## coordination - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/0/0  -> 0.33
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Many functions right now whether C++ standard library calls, operating system calls, or third-party library calls require null-terminated C-style strings.
candidate 3 (found by 1 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     0/0/1  -> 0.33
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Such a contract would be unenforceable because pre(sv[sv.size()] == 0) is potentially undefined behavior.

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     1/2/1  -> 1.33
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and cstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 3 of 27 passes): A reference implementation is at https://github.com/bemanproject/cstring_view.
candidate 4 (found by 2 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

-->
