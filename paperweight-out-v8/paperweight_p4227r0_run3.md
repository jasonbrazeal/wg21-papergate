Verdict: Adequate (4/14)

The paper offers only partial support for its own standardization, with the strongest material concentrated in its discussion of prior art and alternatives. The case is thinnest where it matters most: the paper does not establish who is concretely affected, why the standard is the right venue, how the feature would coordinate with existing practice, why a library solution is insufficient, or that there is implementation experience to draw on.

- The paper’s prior-art discussion is its most solid contribution, clearly situating the proposal against P3655 and the existing `cstring_view` design.
- The motivation is asserted rather than demonstrated, since the paper itself concedes that C APIs allowing embedded NUL bytes are rare.
- The paper does not establish why standardization is necessary as opposed to a library type, nor does it show coordination with existing string-view or C-interop facilities.
- The most glaring omission is the complete absence of implementation experience, leaving the proposal without evidence that the design has been tried and found workable.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.50/14, close to Weak)

Provisionally addressed: 4 of 7. Provisional points: 3.50 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.50   corroborated 3.67   accumulate 4.83   max 5.00

## SUMMARY
grades: motivation 1.17  audience 0.33  prior_art 1.50  vehicle 0.50  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 54 of 56 section-criterion pairs unanimous (96%)
single-sample totals would have been: 4.00 / 3.50 / 3.50   (all 3 samples: 3.50)
headings: h2 7
on threshold: prior_art
splits: motivation[4] 2/2/0  audience[6] 1/0/1
## END SUMMARY

## motivation - grade 1.17 (fired in 6 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               1/1/1  -> 1.00
  [4] 2 C Strings end at the first NUL byte        2/2/0  -> 1.33
  [5] 3 But string and stringview have all of t... 1/1/1  -> 1.00
  [6] 4 But what if I have a C API that require... 1/1/1  -> 1.00
  [7] REFERENCES                                   1/1/1  -> 1.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper argues why that is not a good design choice for such a type.
candidate 2 (found by 3 of 24 passes): The motivation for `cstring``_``view` is interaction with “operating system calls, C interfaces, third-party library APIs, or even C++ standard library APIs which require null-terminated strings”[P3655].
candidate 3 (found by 3 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.
candidate 4 (found by 3 of 24 passes): P3655 acknowledges that C APIs that allow embedded NUL bytes are rare.

## audience - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 0/0/0  -> 0.00
  [6] 4 But what if I have a C API that require... 1/0/1  -> 0.67
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): P3655 acknowledges that C APIs that allow embedded NUL bytes are rare.

## prior_art - grade 1.50 (fired in 6 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               1/1/1  -> 1.00
  [4] 2 C Strings end at the first NUL byte        1/1/1  -> 1.00
  [5] 3 But string and stringview have all of t... 1/1/1  -> 1.00
  [6] 4 But what if I have a C API that require... 1/1/1  -> 1.00
  [7] REFERENCES                                   2/2/2  -> 2.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): [P3655] proposes `std::cstring``_``view` as a string-view type for null-terminated strings.
candidate 2 (found by 3 of 24 passes): A function which, according to P3655, is one of the key motivations for introducing this type in the first place.
candidate 3 (found by 3 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.
candidate 4 (found by 3 of 24 passes): P3655 acknowledges that C APIs that allow embedded NUL bytes are rare.

## vehicle - grade 0.50 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 1/1/1  -> 1.00
  [6] 4 But what if I have a C API that require... 0/0/0  -> 0.00
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 0/0/0  -> 0.00
  [6] 4 But what if I have a C API that require... 0/0/0  -> 0.00
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 0/0/0  -> 0.00
  [6] 4 But what if I have a C API that require... 0/0/0  -> 0.00
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 0/0/0  -> 0.00
  [6] 4 But what if I have a C API that require... 0/0/0  -> 0.00
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

-->
