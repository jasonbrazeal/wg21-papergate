Verdict: Adequate to Strong (7/14)

The paper offers a mixed case for its own standardization, with its strongest material concentrated in explaining why the current preconditions are problematic and in showing that implementations already behave in the desired way. The support thins considerably around the affected audience, coordination with existing practice, and the absence of any discussion of why a library-level solution would not suffice.

- The paper clearly establishes that the current preconditions are both too strict and too permissive, and that they provide no optimization or correctness benefit.
- The implementation experience is well supported, since existing standard libraries already use `memmove` for trivially copyable contiguous ranges and thereby produce the correct result.
- The paper only claims, rather than establishes, who is affected and how the change would coordinate with existing implementations, relying on a single poll and a Godbolt link rather than broader evidence.
- The most glaring omission is the complete lack of argument for why the standard is the right place for this change or why a library-level solution would not do.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 5 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 5. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.33   accumulate 6.67   max 7.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.00  coordination 0.33  insufficiency 0.00  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.50 / 6.00 / 6.50   (all 3 samples: 6.67)
headings: h2 10 + bold numbered 4
on threshold: implementation
splits: motivation[2] 2/2/1  motivation[11] 1/0/1  audience[9] 1/0/1  prior_art[4] 2/1/1
        prior_art[10] 2/0/0  prior_art[13] 0/0/1  coordination[7] 2/0/0  implementation[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/1  -> 1.67
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Proposal                                  1/1/1  -> 1.00
  [6] 1. Option A: "just remove" the preconditi... 1/1/1  -> 1.00
  [7] 2. Option B: remove the preconditions, bu... 2/2/2  -> 2.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          1/1/1  -> 1.00
  [11] 5. Impact on the Standard                    1/0/1  -> 0.67
  [12] 6. Future work                               1/1/1  -> 1.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): In summary: the preconditions are both too strict (they forbid valid patterns that could work correctly, such as overlapping contiguous iterators) and too permissive (they allow patterns that produce garbled results).
candidate 2 (found by 3 of 45 passes): As argued above, the current preconditions offer no optimization benefit and cannot even guarantee a correct result.
candidate 3 (found by 3 of 45 passes): outcomes such as garbled output due to overlap, or reading from already-moved-from objects, etc., are simply the observable consequence of following the assignment order.
candidate 4 (found by 3 of 45 passes): We are concerned that *there may be existing code that is accidentally relying on this runtime behavior*; with the proposed change we would be introducing a regression in it.

## audience - grade 0.33 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 1/0/1  -> 0.67
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 45 passes): SG9 polled E3 for trivially copyable types (the exact wording is in the § 1 Changelog); the result was **SF 2 / F 1 / N 1 / A 2 / SA 0**, that is, no consensus

## prior_art - grade 2.00 (fired in 7 of 15 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/1/1  -> 1.33
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 1/1/1  -> 1.00
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          2/0/0  -> 0.67
  [11] 5. Impact on the Standard                    1/1/1  -> 1.00
  [12] 6. Future work                               2/2/2  -> 2.00
  [13] 7. Proposed Wording                          0/0/1  -> 0.33
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Amended by [P3179R8] for C++26 to only take into account the elements that are actually copied.
candidate 2 (found by 3 of 45 passes): With this option we would simply drop the *Preconditions* clauses, but we would not be proposing any change to the effects of the algorithms.
candidate 3 (found by 3 of 45 passes): E3 was the principal alternative to E2 considered by the group.
candidate 4 (found by 3 of 45 passes): For `copy_n`, it establishes new preconditions, matching existing practice and resolving [LWG3089].

## vehicle - grade 0.00 (fired in 0 of 15 sections, strong in 0)
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

## coordination - grade 0.33 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 2/0/0  -> 0.67
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 0/0/0  -> 0.00
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): Existing implementations ([Godbolt](https://godbolt.org/z/ab6Y1fK3e)) in fact use `memmove` for contiguous ranges of trivially copyable types, which silently produces the *correct* result

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
  [9] 2. Extension E2: all contiguous iterator ... 0/1/0  -> 0.33
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Existing implementations ([Godbolt](https://godbolt.org/z/ab6Y1fK3e)) in fact use `memmove` for contiguous ranges of trivially copyable types, which silently produces the *correct* result:
candidate 2 (found by 1 of 45 passes): As mentioned above, right now Standard Library implementations employ `memmove` (or similar) when copying/moving trivially copyable types, and `memmove` already yields the correct result

-->
