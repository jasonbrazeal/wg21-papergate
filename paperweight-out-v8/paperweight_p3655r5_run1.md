Verdict: Strong (11/14)

The paper offers substantial support for standardizing a null-terminated string view type, particularly through evidence of widespread existing implementations and active use. Its thinnest support lies in explaining why the type must be in the standard library rather than remaining a widely shared third-party component.

- The strongest support comes from implementation experience, with named adopters like Microsoft, Google, and NVIDIA, plus measurable growth in GitHub usage across multiple independent implementations.
- The paper also clearly establishes who is affected and why the type matters, citing common C API interactions and the safety and optimization benefits of preserving null-termination guarantees.
- Prior art and alternatives are well documented, including the earlier P1402 attempt and the adjoint P3862 proposal addressing related string interface issues.
- The most glaring omission is the lack of a concrete argument for why a library solution is insufficient, since the paper itself notes that many developers already use custom types successfully outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (10.67/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 10.67 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 10.67   corroborated 10.00   accumulate 11.17   max 12.00

## SUMMARY
grades: motivation 2.00  audience 1.67  prior_art 2.00  vehicle 1.00  coordination 1.50  insufficiency 0.50  implementation 2.00
sample agreement: 57 of 63 section-criterion pairs unanimous (90%)
single-sample totals would have been: 11.00 / 10.50 / 11.00   (all 3 samples: 10.67)
headings: h2 8
on threshold: audience, coordination
splits: motivation[2] 0/1/1  motivation[6] 2/0/2  motivation[7] 2/2/1  audience[8] 2/0/2
        prior_art[6] 2/2/0  vehicle[6] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 6 of 9 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/1/1  -> 0.67
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     2/0/2  -> 1.33
  [7] 6 Design rationale                           2/2/1  -> 1.67
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Because of a lack of a desirable option for passing non-owned null-terminated strings, std::string_view parameters are nonetheless sometimes used today in cases where null-terminated strings are needed, calling std::string_view::data to get a const char*.
candidate 2 (found by 3 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 3 of 27 passes): The use case of having a null-terminated string is much more common, in particular in interaction with C APIs (such as OS APIs, things like the Yubico libfido2 library, libsqlite and others).
candidate 4 (found by 3 of 27 passes): What we observed is that, in some case, this might not only make the code safer, but also enable new optimizations.

## audience - grade 1.67 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.67   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          2/0/2  -> 1.33
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 2 of 27 passes): Github code search shows similar popularity between [`cstring_view`](https://github.com/search?q=%2F%5Cbcstring_view%5Cb%2F%20language%3Ac%2B%2B%20-is%3Afork&type=code) (1.2k results as of the time of writing) and [`zstring_view`](https://github.com/search?q=%2F%5Cbzstring_view%5Cb%2F+language%3Ac%2B%2B+-is%3Afork&type=code) (680 results as of the time of writing).

## prior_art - grade 2.00 (fired in 5 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     2/2/0  -> 1.33
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): An attempt was made in Feb 2019 to concretely propose the type (renamed to cstring_view) with P1402, but it failed to gain consensus in LEWGI at Kona.
candidate 2 (found by 3 of 27 passes): There is an adjoint paper (P3862) that proposes to fix this in the existing-but-unpublished C++26 standard to avoid future deviation in having std::string::subview return string_view for subview(n).
candidate 3 (found by 2 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 4 (found by 2 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

## vehicle - grade 1.00 (fired in 3 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.17   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/1/1  -> 1.00
  [6] 5 Discussion on the type                     0/1/0  -> 0.33
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As it's a lingua franca type, it should be part of the standard C++ library.
candidate 2 (found by 3 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 1 of 27 passes): The solution bypasses that the problem is that we're missing an unbroken type-safe chain of knowledge that the value being passed is or is not null-terminated.

## coordination - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Many functions right now whether C++ standard library calls, operating system calls, or third-party library calls require null-terminated C-style strings.

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     0/0/0  -> 0.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): For this reason, many C++ developers use custom zstring_view or cstring_view types which are guaranteed to be null-terminated.

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     1/1/1  -> 1.00
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 3 of 27 passes): A reference implementation is at [Beman Project on Github](https://github.com/bemanproject/cstring_view).
candidate 4 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

-->
