Verdict: Weak to Adequate (3/14)

The paper offers only a thin, largely asserted case for standardization, with most of its support resting on a contrast to `cstring_view` rather than on direct evidence about the proposed facility itself. The weakest areas are the absence of any implementation experience and the failure to explain why a library solution would not suffice.

- The clearest, though still indirect, support comes from the paper’s engagement with P3655 and its attempt to distinguish the proposed type from `cstring_view`.
- The discussion of affected users and prior art is suggestive but does not move beyond the author’s limited awareness of relevant C APIs.
- The paper does not establish why the facility belongs in the standard rather than in a library.
- The complete lack of implementation experience leaves the proposal without practical grounding for its design or usefulness.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (3.17/14, close to Weak)

Provisionally addressed: 5 of 7. Provisional points: 3.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 3.17   corroborated 3.67   accumulate 4.83   max 4.33

## SUMMARY
grades: motivation 1.00  audience 0.17  prior_art 1.33  vehicle 0.50  coordination 0.17  insufficiency 0.00  implementation 0.00
sample agreement: 51 of 56 section-criterion pairs unanimous (91%)
single-sample totals would have been: 4.00 / 3.00 / 3.50   (all 3 samples: 3.17)
headings: h2 7
on threshold: prior_art
splits: motivation[4] 0/0/2  motivation[7] 2/0/1  audience[6] 0/0/1  prior_art[7] 2/2/1
        coordination[5] 1/0/0
## END SUMMARY

## motivation - grade 1.00 (fired in 6 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 2.00   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               1/1/1  -> 1.00
  [4] 2 C Strings end at the first NUL byte        0/0/2  -> 0.67
  [5] 3 But string and stringview have all of t... 1/1/1  -> 1.00
  [6] 4 But what if I have a C API that require... 1/1/1  -> 1.00
  [7] REFERENCES                                   2/0/1  -> 1.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): This paper argues why that is not a good design choice for such a type.
candidate 2 (found by 3 of 24 passes): The motivation for `cstring``_``view` is interaction with “operating system calls, C interfaces, third-party library APIs, or even C++ standard library APIs which require null-terminated strings”[P3655].
candidate 3 (found by 3 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.
candidate 4 (found by 3 of 24 passes): P3655 acknowledges that C APIs that allow embedded NUL bytes are rare.

## audience - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 0/0/0  -> 0.00
  [6] 4 But what if I have a C API that require... 0/0/1  -> 0.33
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The author is aware of two types of C APIs that are able to process such strings correctly.

## prior_art - grade 1.33 (fired in 6 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     1/1/1  -> 1.00
  [3] 1 Introduction                               1/1/1  -> 1.00
  [4] 2 C Strings end at the first NUL byte        1/1/1  -> 1.00
  [5] 3 But string and stringview have all of t... 1/1/1  -> 1.00
  [6] 4 But what if I have a C API that require... 1/1/1  -> 1.00
  [7] REFERENCES                                   2/2/1  -> 1.67
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): [P3655] proposes `std::cstring``_``view` as a string-view type for null-terminated strings.
candidate 2 (found by 3 of 24 passes): The paper argues in Section 6.4 that allowing embedded NUL bytes is reasonable, because some C APIs do support embedded NULs in input strings and disallowing them would make `cstring``_``view` unusable for interacting with those APIs.
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

## coordination - grade 0.17 (fired in 1 of 8 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 Introduction                               0/0/0  -> 0.00
  [4] 2 C Strings end at the first NUL byte        0/0/0  -> 0.00
  [5] 3 But string and stringview have all of t... 1/0/0  -> 0.33
  [6] 4 But what if I have a C API that require... 0/0/0  -> 0.00
  [7] REFERENCES                                   0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): But unlike `cstring``_``view`, they were not designed for interop with C functions.

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
