Verdict: Adequate (6/14)

The paper offers a solid foundation for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several essential questions unanswered, particularly around who is affected and how the change fits with existing practice outside the standard library. The thinnest support is in the sections that should connect the proposal to real-world users and to the broader ecosystem.

- The paper clearly establishes why the current preconditions are problematic and why the proposed change matters for correctness and optimization.
- It demonstrates credible prior art and existing implementation practice, including the use of `memmove` in current standard libraries.
- The paper does not establish who is affected by the change, leaving the practical impact on users unclear.
- It fails to address coordination and interoperability, or why a library-level solution would be insufficient.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.17  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 100 of 105 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.00 / 6.50 / 6.00   (all 3 samples: 6.17)
headings: h2 10 + bold numbered 4
on threshold: implementation
splits: motivation[12] 0/1/1  prior_art[4] 1/2/1  prior_art[7] 1/2/1  prior_art[10] 0/2/2
        vehicle[7] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Proposal                                  1/1/1  -> 1.00
  [6] 1. Option A: "just remove" the preconditi... 1/1/1  -> 1.00
  [7] 2. Option B: remove the preconditions, bu... 2/2/2  -> 2.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          1/1/1  -> 1.00
  [11] 5. Impact on the Standard                    1/1/1  -> 1.00
  [12] 6. Future work                               0/1/1  -> 0.67
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): they are incomplete, and they do not enable any useful optimization.
candidate 2 (found by 3 of 45 passes): In summary: the preconditions are both too strict (they forbid valid patterns that could work correctly, such as overlapping contiguous iterators) and too permissive (they allow patterns that produce garbled results).
candidate 3 (found by 3 of 45 passes): As argued above, the current preconditions offer no optimization benefit and cannot even guarantee a correct result.
candidate 4 (found by 3 of 45 passes): outcomes such as garbled output due to overlap, or reading from already-moved-from objects, etc., are simply the observable consequence of following the assignment order.

## audience - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 0/0/0  -> 0.00
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 15 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                1/2/1  -> 1.33
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 1/2/1  -> 1.33
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          0/2/2  -> 1.33
  [11] 5. Impact on the Standard                    1/1/1  -> 1.00
  [12] 6. Future work                               2/2/2  -> 2.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Amended by [P3179R8] for C++26 to only take into account the elements that are actually copied.
candidate 2 (found by 3 of 45 passes): As mentioned above, right now Standard Library implementations employ `memmove` (or similar) when copying/moving trivially copyable types, and `memmove` already yields the correct result; this means that these implementations will *not* have to change their "runtime" version of these algorithms.
candidate 3 (found by 3 of 45 passes): For `copy_n`, it establishes new preconditions, matching existing practice and resolving [LWG3089].
candidate 4 (found by 2 of 45 passes): Existing implementations ([Godbolt](https://godbolt.org/z/ab6Y1fK3e)) in fact use `memmove` for contiguous ranges of trivially copyable types, which silently produces the *correct* result

## vehicle - grade 0.17 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/1/0  -> 0.33
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 0/0/0  -> 0.00
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): We are concerned that *there may be existing code that is accidentally relying on this runtime behavior*; with the proposed change we would be introducing a regression in it.

## coordination - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 0/0/0  -> 0.00
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 15 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 0/0/0  -> 0.00
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 15 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 2/2/2  -> 2.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 1/1/1  -> 1.00
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Existing implementations ([Godbolt](https://godbolt.org/z/ab6Y1fK3e)) in fact use `memmove` for contiguous ranges of trivially copyable types, which silently produces the *correct* result:
candidate 2 (found by 3 of 45 passes): As mentioned above, right now Standard Library implementations employ `memmove` (or similar) when copying/moving trivially copyable types, and `memmove` already yields the correct result;

-->
