Verdict: Adequate (5/14)

The paper offers some support for its standardization, chiefly through a concrete motivating failure and implementation experience in three major standard libraries, but it leaves several parts of the case asserted rather than demonstrated. The thinnest areas are the absence of any identified affected audience and the lack of established reasoning for why the standard, rather than library practice or documentation, must change.

- The strongest support is the implementation experience, with partial implementations reported in libc++, microsoft/STL, and libstdc++.
- The paper establishes why the change matters by showing a realistic SFINAE use case that currently produces a hard error.
- The arguments for prior art, why the standard is necessary, and why a library solution will not suffice are only claimed, not backed by sufficient explanation or evidence.
- The most glaring omission is that the paper never establishes who is affected by the current behavior.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (5.17/14)

Provisionally addressed: 5 of 7. Provisional points: 5.17 of 14. Unsupported quotes rejected: 2. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 5.17   corroborated 5.00   accumulate 5.17   max 6.33

## SUMMARY
grades: motivation 1.50  audience 0.00  prior_art 1.17  vehicle 0.33  coordination 0.00  insufficiency 0.17  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 5.00 / 5.00 / 5.50   (all 3 samples: 5.17)
headings: h2 8
on threshold: motivation, implementation
splits: prior_art[4] 2/1/1  vehicle[4] 0/0/2  insufficiency[4] 0/1/0
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Motivation                                 2/2/2  -> 2.00
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): This paper introduce constraints for `std::make_from_tuple` to make it SFINAE friendly.
candidate 2 (found by 3 of 27 passes): When someone write SFINAE code like the following to check whether `T` can constructed from a tuple, they may hit hard errors like “no matching function for call to `make-from-tuple-impl` ”

## audience - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.17 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.17   corroborated 1.00   accumulate 1.17   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation                                 2/1/1  -> 1.33
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  1/1/1  -> 1.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): I’ve partial implemented this improvement in [`libc++`](https://github.com/llvm/llvm-project/pull/85263), [`microsoft/STL`](https://github.com/microsoft/STL/pull/4528), [`libstdc++`](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=73edc003c0a8f0badc7027e6deefd3a573300b03).
candidate 2 (found by 2 of 27 passes): [[LWG3528]](https://wg21.link/lwg3528) introduce constraints:
candidate 3 (found by 1 of 27 passes): This proposal also suggests changing the *Mandates* “If `tuple_size_v<remove_reference_t<Tuple>>` is 1, then `reference_constructs_from_temporary_v<T, decltype(get<0>(declval<Tuple>()))>` is `false` ” to a *Constraints*; this would yield similar benefits

## vehicle - grade 0.33 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/2  -> 0.67
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): This is somehow unclear when the constraints are not literally specified with *Constraints* in the standard wording (16.3.2.4 [[structure.specifications]]).

## coordination - grade 0.00 (fired in 0 of 9 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.17 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation                                 0/1/0  -> 0.33
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  0/0/0  -> 0.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 27 passes): Even If the effects are *Equivalent to* calling a constrained function, the constraints has not apply to `std::make_from_tuple` .

## implementation - grade 2.00  [binary: max] (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Changelog                                  0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Motivation                                 0/0/0  -> 0.00
  [5] 4 Impact on the Standard                     0/0/0  -> 0.00
  [6] 5 Implementation Experience                  2/2/2  -> 2.00
  [7] 6 Proposed Wording                           0/0/0  -> 0.00
  [8] 7 Acknowledgements                           0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): I’ve partial implemented this improvement in [`libc++`](https://github.com/llvm/llvm-project/pull/85263), [`microsoft/STL`](https://github.com/microsoft/STL/pull/4528), [`libstdc++`](https://gcc.gnu.org/git/?p=gcc.git;a=commit;h=73edc003c0a8f0badc7027e6deefd3a573300b03).

-->
