Verdict: Weak (1/14)

The paper offers only a narrow, fragmentary case for its own standardization: it gestures at a real consistency problem in `simd::cat` and at related issue history, but leaves most of the burden of justification unaddressed. The support is thinnest around the basic questions of who is affected, why a library-level fix is insufficient, and whether the proposed direction has any implementation backing.

- The strongest support is the concrete example showing that `simd::cat` can produce unexpectedly inconsistent types, which at least identifies a plausible wording defect.
- The paper also connects its change to several existing LWG issues, suggesting the problem is already recognized in the committee’s own records.
- It does not establish who is affected by the current behavior or how widespread the practical impact is.
- Most glaringly, it offers no implementation experience, no argument that the problem cannot be handled outside the standard, and no discussion of coordination or interoperability.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Weak (1.17/14)

Provisionally addressed: 2 of 7. Provisional points: 1.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 4. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 1.17   corroborated 1.67   accumulate 1.17   max 2.00

## SUMMARY
grades: motivation 0.33  audience 0.00  prior_art 0.83  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 0.00
sample agreement: 25 of 28 section-criterion pairs unanimous (89%)
single-sample totals would have been: 1.00 / 1.00 / 1.50   (all 3 samples: 1.17)
headings: h2 3
on threshold: none
splits: motivation[4] 0/0/2  prior_art[2] 0/1/0  prior_art[4] 2/1/1
## END SUMMARY

## motivation - grade 0.33 (fired in 1 of 4 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             0/0/2  -> 0.67
candidate 1 (found by 1 of 12 passes): The return type of `simd::cat` is defined using `deduce-abi-t` rather than `resize_t`. This can lead to: [example where] `static_assert(is_same_v<decltype(x), decltype(y)>); // can fail`

## audience - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 0.83 (fired in 2 of 4 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/1/0  -> 0.33
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             2/1/1  -> 1.33
candidate 1 (found by 1 of 12 passes): This paper resolves LWG4470. Since the resolution needs to modify wording that LWG4414 and LWG4518 also need to modify, this paper additionally resolves LWG4414 and LWG4518.
candidate 2 (found by 1 of 12 passes): Since the `simd::cat` wording currently uses `integer-from` it makes sense to resolve the two issues together.
candidate 3 (found by 1 of 12 passes): I sketched a potential solution in `https://lists.isocpp.org/lib/2025/04/31251.php`.
candidate 4 (found by 1 of 12 passes): [In the discussion of LWG4238, Tim noted that](https://cplusplus.github.io/LWG/issue4238) `integer-from``<Bytes>` does not work as intended because `Bytes` can be 16 after `complex<double>` became a vectorizable type.

## vehicle - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             0/0/0  -> 0.00
candidates: (none validated)

## coordination - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 0.00  [binary: max] (fired in 0 of 4 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1 CHANGELOG                                  0/0/0  -> 0.00
  [4] 2 THE ISSUE(S) WITH INTEGER-FROM             0/0/0  -> 0.00
candidates: (none validated)

-->
