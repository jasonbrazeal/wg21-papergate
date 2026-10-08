Verdict: Weak to Adequate (3/14)

The paper offers only a narrow foundation for its own standardization, anchored in its discussion of prior art and alternatives, while most of the case for why the standard should act remains asserted rather than demonstrated. The thinnest support lies in the absence of any account of who is affected, how the feature would interoperate with existing practice, why a library solution is insufficient, or what implementation experience exists.

- The strongest support is the paper’s engagement with P3655 and its acknowledgment that C APIs allowing embedded NUL bytes are rare, which grounds the discussion in a concrete prior proposal.
- The paper claims the type matters for interaction with C interfaces but does not establish that need beyond restating P3655’s motivation.
- The paper asserts that existing alternatives were not designed for C interop, but it does not show why that difference requires standardization rather than a library type.
- The most glaring omission is the complete lack of evidence about affected users, interoperability constraints, library feasibility, or implementation experience.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (3.00/14, close to Adequate)

Provisionally addressed: 3 of 7. Provisional points: 3.00 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.00   corroborated 2.67   accumulate 4.33   max 4.00

## SUMMARY
grades: motivation 1.17  audience 0.00  prior_art 1.50  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 3.00 / 3.00 / 3.50   (all 3 samples: 3.00)
headings: h2 7
on threshold: prior_art
splits: motivation[4] 2/0/2  prior_art[5] 1/0/1  vehicle[5] 0/1/1
## END SUMMARY

## motivation - grade 1.17 (fired in 6 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 2.00   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               1/1/1  -> 1.00
  [4] 2 C Strings end at the first NUL byte        2/0/2  -> 1.33
  [5] 3 But string and stringview have all of t... 1/1/1  -> 1.00
  [6] 4 But what if I have a C API that require... 1/1/1  -> 1.00
  [7] REFERENCES                                   1/1/1  -> 1.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper argues why that is not a good design choice for such a type.
candidate 2 (found by 3 of 24 passes): The motivation for `cstring``_``view` is interaction with “operating system calls, C interfaces, third-party library APIs, or even C++ standard library APIs which require null-terminated strings”[P3655].
candidate 3 (found by 3 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.
candidate 4 (found by 3 of 24 passes): P3655 acknowledges that C APIs that allow embedded NUL bytes are rare.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
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

## prior_art - grade 1.50 (fired in 6 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               1/1/1  -> 1.00
  [4] 2 C Strings end at the first NUL byte        1/1/1  -> 1.00
  [5] 3 But string and stringview have all of t... 1/0/1  -> 0.67
  [6] 4 But what if I have a C API that require... 1/1/1  -> 1.00
  [7] REFERENCES                                   2/2/2  -> 2.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): [P3655] proposes `std::cstring``_``view` as a string-view type for null-terminated strings.
candidate 2 (found by 3 of 24 passes): P3655 acknowledges that C APIs that allow embedded NUL bytes are rare.
candidate 3 (found by 2 of 24 passes): The motivation for `cstring``_``view` is interaction with “operating system calls, C interfaces, third-party library APIs, or even C++ standard library APIs which require null-terminated strings”[P3655].
candidate 4 (found by 2 of 24 passes): A function which, according to P3655, is one of the key motivations for introducing this type in the first place.

## vehicle - grade 0.33 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 0/1/1  -> 0.67
  [6] 4 But what if I have a C API that require... 0/0/0  -> 0.00
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.

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
