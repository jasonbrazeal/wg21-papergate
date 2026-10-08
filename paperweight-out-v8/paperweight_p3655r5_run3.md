Verdict: Strong to Excellent (11/14)

The paper offers substantial evidence that a null-terminated string view is widely used, independently implemented, and backed by real deployment experience, but it is noticeably thinner when it comes to explaining why that type must enter the standard library rather than remain a shared vocabulary type supplied by libraries. The strongest support is empirical, while the weakest parts are the arguments about standardization itself and interoperability with the existing standard string ecosystem.

- The paper clearly establishes implementation experience through widespread GitHub usage, independent implementations at Microsoft, Google, and NVIDIA, and a reference implementation in the Beman Project.
- The need for the type is well grounded in common interactions with C APIs and the prevalence of hand-rolled cstring_view and zstring_view types across the ecosystem.
- The paper does not adequately establish why the standard library is the necessary home for this type, resting on the assertion that it is a “lingua franca” without showing what breaks when it remains a library type.
- The coordination and interoperability case is largely asserted rather than demonstrated, leaving open how this type would relate to existing standard string facilities and whether its absence from the standard actually blocks the claimed use cases.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.83/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.83 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.83   corroborated 11.00   accumulate 11.50   max 11.33

## SUMMARY
grades: motivation 2.00  audience 2.00  prior_art 2.00  vehicle 1.00  coordination 1.17  insufficiency 0.67  implementation 2.00
sample agreement: 53 of 63 section-criterion pairs unanimous (84%)
single-sample totals would have been: 12.00 / 10.50 / 10.50   (all 3 samples: 10.83)
headings: h2 8
on threshold: none
splits: motivation[3] 2/0/2  motivation[6] 0/0/2  motivation[7] 2/1/1  audience[5] 1/0/0
        vehicle[6] 2/0/0  coordination[6] 2/1/1  coordination[7] 1/0/1  insufficiency[6] 1/0/0
        implementation[6] 1/2/2  implementation[8] 1/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Introduction                               2/0/2  -> 1.33
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     0/0/2  -> 0.67
  [7] 6 Design rationale                           2/1/1  -> 1.33
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): We propose a standard string view type that guarantees null-termination.
candidate 2 (found by 3 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 3 of 27 passes): The use case of having a null-terminated string is much more common, in particular in interaction with C APIs (such as OS APIs, things like the Yubico libfido2 library, libsqlite and others).
candidate 4 (found by 3 of 27 passes): What we observed is that, in some case, this might not only make the code safer, but also enable new optimizations.

## audience - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/0/0  -> 0.33
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 3 of 27 passes): Github code search shows similar popularity between [`cstring_view`](https://github.com/search?q=%2F%5Cbcstring_view%5Cb%2F%20language%3Ac%2B%2B%20-is%3Afork&type=code) (1.2k results as of the time of writing) and [`zstring_view`](https://github.com/search?q=%2F%5Cbzstring_view%5Cb%2F+language%3Ac%2B%2B+-is%3Afork&type=code) (680 results as of the time of writing).
candidate 4 (found by 1 of 27 passes): This is one of the commonly-requested features from the GSL library that does not yet have a std:: equivalent.

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
candidate 1 (found by 3 of 27 passes): An attempt was made in Feb 2019 to concretely propose the type (renamed to cstring_view) with P1402, but it failed to gain consensus in LEWGI at Kona.
candidate 2 (found by 3 of 27 passes): [P2495](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2495r0.pdf) attempts to directly patch this specific example. The solution bypasses that the problem is that we're missing an unbroken type-safe chain of knowledge that the value being passed is or is not null-terminated.
candidate 3 (found by 3 of 27 passes): There is an adjoint paper (P3862) that proposes to fix this in the existing-but-unpublished C++26 standard to avoid future deviation in having std::string::subview return string_view for subview(n).
candidate 4 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

## vehicle - grade 1.00 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/1/1  -> 1.00
  [6] 5 Discussion on the type                     2/0/0  -> 0.67
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As it's a lingua franca type, it should be part of the standard C++ library.
candidate 2 (found by 3 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 1 of 27 passes): Without them we retain the question we had before - const char*, const std::string& or string_view?

## coordination - grade 1.17 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.50   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     2/1/1  -> 1.33
  [7] 6 Design rationale                           1/0/1  -> 0.67
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Many functions right now whether C++ standard library calls, operating system calls, or third-party library calls require null-terminated C-style strings.
candidate 3 (found by 2 of 27 passes): The use case of having a null-terminated string is much more common, in particular in interaction with C APIs (such as OS APIs, things like the Yubico libfido2 library, libsqlite and others).

## insufficiency - grade 0.67 (fired in 2 of 9 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     1/0/0  -> 0.33
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): For this reason, many C++ developers use custom zstring_view or cstring_view types which are guaranteed to be null-terminated.
candidate 2 (found by 1 of 27 passes): The type effectively fills out the design space that exists around strings within C++.

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     1/2/2  -> 1.67
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          1/2/2  -> 1.67
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 3 of 27 passes): A reference implementation is at [Beman Project on Github](https://github.com/bemanproject/cstring_view).
candidate 4 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

-->
