Verdict: Strong to Excellent (11/14)

The paper offers substantial support for standardizing a null-terminated string view, drawing on widespread existing implementations, active use, and clear interoperability needs. The case is thinnest where it must show why a library solution is insufficient, since the evidence mostly restates the popularity of third-party types rather than demonstrating a barrier those libraries cannot overcome.

- The strongest support comes from implementation experience, with independent implementations from Microsoft, Google, NVIDIA, and the Beman Project showing the design is viable and already in production use.
- The paper clearly establishes why the feature matters and who is affected by documenting active growth in GitHub usage and common demand from C API interactions.
- Prior art and alternatives are well covered through references to P1402, P2495, and the adjoint P3862, situating the proposal within an ongoing standardization conversation.
- The most glaring omission is the failure to establish why a library will not do, as the paper points to the existence of many third-party implementations without explaining what prevents them from serving users adequately outside the standard.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (11.00/14, close to Excellent)

Provisionally addressed: 7 of 7. Provisional points: 11.00 of 14. Unsupported quotes rejected: 9. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 11.00   corroborated 10.00   accumulate 12.00   max 13.00

## SUMMARY
grades: motivation 2.00  audience 1.50  prior_art 2.00  vehicle 1.50  coordination 1.50  insufficiency 0.50  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 11.00 / 11.00 / 11.50   (all 3 samples: 11.00)
headings: h2 8
on threshold: audience, vehicle, coordination
splits: motivation[3] 2/2/0  audience[5] 1/0/0  audience[8] 0/0/2
## END SUMMARY

## motivation - grade 2.00 (fired in 5 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   1/1/1  -> 1.00
  [3] 2 Introduction                               2/2/0  -> 1.33
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            2/2/2  -> 2.00
  [6] 5 Discussion on the type                     0/0/0  -> 0.00
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): We propose a standard string view type that guarantees null-termination.
candidate 2 (found by 3 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 3 of 27 passes): The use case of having a null-terminated string is much more common, in particular in interaction with C APIs (such as OS APIs, things like the Yubico libfido2 library, libsqlite and others).
candidate 4 (found by 3 of 27 passes): What we observed is that, in some case, this might not only make the code safer, but also enable new optimizations.

## audience - grade 1.50 (fired in 4 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/0/0  -> 0.33
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/2  -> 0.67
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 2 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 1 of 27 passes): This is one of the commonly-requested features from the GSL library that does not yet have a std:: equivalent.
candidate 4 (found by 1 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use

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
candidate 2 (found by 3 of 27 passes): An attempt was made in Feb 2019 to concretely propose the type (renamed to cstring_view) with P1402, but it failed to gain consensus in LEWGI at Kona.
candidate 3 (found by 3 of 27 passes): [P2495](https://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2495r0.pdf) attempts to directly patch this specific example. The solution bypasses that the problem is that we're missing an unbroken type-safe chain of knowledge that the value being passed is or is not null-terminated.
candidate 4 (found by 3 of 27 passes): There is an adjoint paper (P3862) that proposes to fix this in the existing-but-unpublished C++26 standard to avoid future deviation in having std::string::subview return string_view for subview(n).

## vehicle - grade 1.50 (fired in 3 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            1/1/1  -> 1.00
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           0/0/0  -> 0.00
  [8] 7 Historically relevant information          0/0/0  -> 0.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): As it's a lingua franca type, it should be part of the standard C++ library.
candidate 2 (found by 3 of 27 passes): As such, we do believe that there is both space for such a type, and a desire from multiple angles to have it defined in the standard library.
candidate 3 (found by 2 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 4 (found by 1 of 27 passes): The type effectively fills out the design space that exists around strings within C++.

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
candidate 2 (found by 2 of 27 passes): Many functions right now whether C++ standard library calls, operating system calls, or third-party library calls require null-terminated C-style strings.
candidate 3 (found by 1 of 27 passes): These problems are visible enough that we have targeted patches for specific instances of this problem in the standard - P2495 attempts to directly patch this specific example.

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)  (SHARED PASSAGE)
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
candidate 1 (found by 2 of 27 passes): For this reason, many C++ developers use custom zstring_view or cstring_view types which are guaranteed to be null-terminated.
candidate 2 (found by 1 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Abstract                                   0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Revision History                           0/0/0  -> 0.00
  [5] 4 Previous Papers                            0/0/0  -> 0.00
  [6] 5 Discussion on the type                     2/2/2  -> 2.00
  [7] 6 Design rationale                           2/2/2  -> 2.00
  [8] 7 Historically relevant information          2/2/2  -> 2.00
  [9] 8 Wording                                    0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Its wide presence on Github with implementations from among others Microsoft, Google, and many smaller projects, indicates a wide support for the type.
candidate 2 (found by 3 of 27 passes): Since the first draft of this paper the use of cstring_view and zstring_view on Github has grown from 1.9k to 2.1k, indicating active use, and in many cases people adding new implementations of the type.
candidate 3 (found by 3 of 27 passes): A reference implementation is at [Beman Project on Github](https://github.com/bemanproject/cstring_view).
candidate 4 (found by 3 of 27 passes): NVIDIA implemented cstring_view independently, with almost identical features.

-->
