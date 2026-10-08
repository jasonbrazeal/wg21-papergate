Verdict: Strong (9/14)

The paper gives a reasonably concrete account of the problem and of why existing library facilities are insufficient, but it leaves the affected audience and the interoperability story almost entirely unaddressed. The thinnest parts are the absence of any clear statement about who needs this and how it would fit with existing practice or adjacent standardization work.

- The strongest support is the demonstration that a library-only solution is not viable, since the operation requires compiler support and cannot be expressed portably with current facilities.
- The paper also establishes meaningful prior art and alternatives by distinguishing the proposed operation from total ordering and from existing range checks.
- The most glaring omission is the lack of any established description of who is affected, which leaves the motivating user base and practical demand unclear.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.50/14)

Provisionally addressed: 5 of 7. Provisional points: 8.50 of 14. Unsupported quotes rejected: 0. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.50   corroborated 8.00   accumulate 9.50   max 8.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 1.00  coordination 0.00  insufficiency 1.50  implementation 2.00
sample agreement: 39 of 42 section-criterion pairs unanimous (93%)
single-sample totals would have been: 9.00 / 8.00 / 8.50   (all 3 samples: 8.50)
headings: h2 5
on threshold: insufficiency, implementation
splits: motivation[1] 2/1/1  insufficiency[4] 2/1/1  insufficiency[5] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 6 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 2/1/1  -> 1.33
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Proposed function                            1/1/1  -> 1.00
  [5] Implementation                               2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Currently there is no way to check in a standard way if a pointer lies within specific memory area without running into implementation specific behaviour.
candidate 2 (found by 3 of 18 passes): Currently you can't express assumption that some memory span doesn't have anything in commont with other memory span.
candidate 3 (found by 3 of 18 passes): Currently there is no way how to safely compare pointers for equality in constant evaluation if one of them points past the end.
candidate 4 (found by 3 of 18 passes): It's not, it's O(n). Any such operation shouldn't be this slow. Also it doesn't allow us to check if subject is in the range as a subject, so the functionality is actually different.

## audience - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed function                            0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 3 of 6 sections, strong in 3)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   2/2/2  -> 2.00
  [4] Proposed function                            2/2/2  -> 2.00
  [5] Implementation                               2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This proposal gives you ability to express a different thing than ordering: *is something related AND belongs inside*? That's in my experience more useful than global total ordering.
candidate 2 (found by 3 of 18 passes): Originally I had it `first, ptr, last`, but was told we have `std::clamp(ptr, first, last)`, so I'm mirroring existing signature.
candidate 3 (found by 3 of 18 passes): It's not, it's O(n). Any such operation shouldn't be this slow. Also it doesn't allow us to check if subject is in the range as a subject, so the functionality is actually different.

## vehicle - grade 1.00 (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Proposed function                            1/1/1  -> 1.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This paper allows you to check if the pointers are related and in a range, it needs compiler magic to do so.
candidate 2 (found by 3 of 18 passes): With this proposal you can do it in portable and defined way.
candidate 3 (found by 3 of 18 passes): Currently there is no way how to safely compare pointers for equality in constant evaluation if one of them points past the end.

## coordination - grade 0.00 (fired in 0 of 6 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed function                            0/0/0  -> 0.00
  [5] Implementation                               0/0/0  -> 0.00
  [6] Wording                                      0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 1.50 (fired in 4 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 2.00   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 1/1/1  -> 1.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   1/1/1  -> 1.00
  [4] Proposed function                            2/1/1  -> 1.33
  [5] Implementation                               2/1/2  -> 1.67
  [6] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): it needs compiler magic to do so.
candidate 2 (found by 3 of 18 passes): Currently you can't express assumption that some memory span doesn't have anything in commont with other memory span.
candidate 3 (found by 3 of 18 passes): Library specified implementation specific strict total ordering for `std::less<T *>`, but this is not a case for constant evaluated code.
candidate 4 (found by 2 of 18 passes): It's not, it's O(n). Any such operation shouldn't be this slow. Also it doesn't allow us to check if subject is in the range as a subject, so the functionality is actually different.

## implementation - grade 2.00  [binary: max] (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Motivation                                   0/0/0  -> 0.00
  [4] Proposed function                            0/0/0  -> 0.00
  [5] Implementation                               2/2/2  -> 2.00
  [6] Wording                                      0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): A prototype in Clang's [ExprConstant.cpp and the new bytecode interpreter](https://github.com/hanickadot/llvm-project/commit/13e0ecf5fbde796ba6f773e55afaefe80ae44def)

-->
