Verdict: Strong (11/14)

The paper gives substantial evidence that a null-terminated string view type is widely used, independently implemented, and relevant to common C and C++ interoperability needs. Its weakest support concerns the necessity of standardization itself and why existing library implementations cannot suffice, where the argument remains more asserted than demonstrated.

- The strongest support comes from implementation experience, with multiple independent implementations from major organizations and measurable growth in public usage.
- The paper also clearly establishes the affected audience and the practical need through frequent interaction with C APIs and existing null-terminated string requirements.
- Prior art and alternatives are well documented, including an earlier standardization attempt and an independent NVIDIA implementation with nearly identical features.
- The most glaring omission is a concrete case for why a library solution is inadequate, since the paper leans on the existence of third-party implementations without explaining what standardization uniquely enables.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.67   accumulate 11.33   max 11.67

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 0.83  coordination 1.50  insufficiency 0.33  implementation 2.00
sample agreement: 55 of 63 section-criterion pairs unanimous (87%)
single-sample totals would have been: 11.00 / 11.00 / 11.00   (all 3 samples: 10.67)
headings: h2 8
on threshold: coordination
splits: motivation[2] 0/1/1  motivation[6] 2/2/0  audience[5] 1/0/1  vehicle[5] 0/1/1
        vehicle[6] 1/0/1  coordination[7] 2/0/0  insufficiency[3] 0/1/1  implementation[6] 1/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/1  -> 0.67
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     2/2/0  -> 1.33
  [7] 6 Design rationale                           2/2/2  -> 2.00
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
  [5] 4 Previous Papers                            1/0/1  -> 0.67
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Github code search shows similar popularity between https://github.com/search?q=%2F%5Cbcstring_view%5Cb%2F%20language%3Ac%2B%2B%20-is%3Afork&type=code (1.2k results as of the time of writing) and https://github.com/search?q=%2F%5Cbzstring_view%5Cb%2F+language%3Ac%2B%2B+-is%3Afork&type=code (680 results as of the time of writing).
candidate 3 (found by 2 of 27 passes): Since the first draft of this paper the use of cstring_view and cstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 4 (found by 1 of 27 passes): It was specifically requested by several reviewers of this work.

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
candidate 2 (found by 3 of 27 passes): There is an adjoint paper (P3862) that proposes to fix this in the existing-but-unpublished C++26 standard to avoid future deviation in having std::string::subview return string_view for subview(n).
candidate 3 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.
candidate 4 (found by 2 of 27 passes): An attempt was made in Feb 2019 to concretely propose the type (renamed to cstring_view) with http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1402r0.pdf, but it failed to gain consensus in LEWGI at https://wiki.edg.com/bin/view/Wg21kona2019/P1402.

## vehicle - grade 0.83 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/1/1  -> 0.67
  [6] 5 Discussion on the type                     1/0/1  -> 0.67
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As it's a lingua franca type, it should be part of the standard C++ library.
candidate 2 (found by 2 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 1 of 27 passes): Without them we retain the question we had before - const char*, const std::string& or string_view?
candidate 4 (found by 1 of 27 passes): The type effectively fills out the design space that exists around strings within C++.

## coordination - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           2/0/0  -> 0.67
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Many functions right now whether C++ standard library calls, operating system calls, or third-party library calls require null-terminated C-style strings.
candidate 3 (found by 1 of 27 passes): The use case of having a null-terminated string is much more common, in particular in interaction with C APIs (such as OS APIs, things like the Yubico libfido2 library, libsqlite and others).

## insufficiency - grade 0.33 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               0/1/1  -> 0.67
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     0/0/0  -> 0.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     1/1/2  -> 1.33
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and cstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 3 of 27 passes): A reference implementation is at https://github.com/bemanproject/cstring_view.
candidate 4 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features. This is described in https://wg21.link/p3710, now merged into this paper.

-->
