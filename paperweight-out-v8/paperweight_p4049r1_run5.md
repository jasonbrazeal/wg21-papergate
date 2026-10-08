Verdict: Adequate (6/14)

The paper’s strongest case rests on showing that the current rules provide no optimization benefit and that existing implementations already produce the correct behavior, but it leaves several essential justifications for standardization largely unaddressed. The support is thinnest around why a standard change is needed at all, how it coordinates with other specifications, and why a library-level solution would be insufficient.

- The paper convincingly establishes that the existing preconditions offer no optimization benefit and cannot guarantee correct results, while current implementations using `memmove` already behave as proposed.
- It also documents prior art and alternatives, including the committee’s consideration of E3 and the alignment of `copy_n` with the proposed `copy` semantics.
- The paper claims who is affected only through an inconclusive SG9 poll, without establishing the actual user population or impact.
- Most glaringly, it does not establish why the standard must change, how the change coordinates with related specifications, or why a library solution would not suffice.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.17/14)

Provisionally addressed: 4 of 7. Provisional points: 6.17 of 14. Unsupported quotes rejected: 4. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.17   corroborated 6.33   accumulate 6.17   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 0.00  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 100 of 105 section-criterion pairs unanimous (95%)
single-sample totals would have been: 6.50 / 6.00 / 6.00   (all 3 samples: 6.17)
headings: h2 10 + bold numbered 4
on threshold: implementation
splits: motivation[6] 1/0/1  motivation[11] 1/0/1  audience[9] 1/0/0  prior_art[4] 1/2/1
        prior_art[6] 1/0/1
## END SUMMARY

## motivation - grade 2.00 (fired in 9 of 15 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Proposal                                  1/1/1  -> 1.00
  [6] 1. Option A: "just remove" the preconditi... 1/0/1  -> 0.67
  [7] 2. Option B: remove the preconditions, bu... 2/2/2  -> 2.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          1/1/1  -> 1.00
  [11] 5. Impact on the Standard                    1/0/1  -> 0.67
  [12] 6. Future work                               1/1/1  -> 1.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): they are incomplete, and they do not enable any useful optimization.
candidate 2 (found by 3 of 45 passes): As argued above, the current preconditions offer no optimization benefit and cannot even guarantee a correct result.
candidate 3 (found by 3 of 45 passes): We are concerned that *there may be existing code that is accidentally relying on this runtime behavior*; with the proposed change we would be introducing a regression in it.
candidate 4 (found by 3 of 45 passes): Having a right overlap today is already undefined behavior; changing e.g. `std::copy` from doing left-to-right assignments to right-to-left assignments in this case is therefore not subject to any form of source compatibility.

## audience - grade 0.17 (fired in 1 of 15 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 1/0/0  -> 0.33
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): SG9 polled E3 for trivially copyable types (the exact wording is in the § 1 Changelog); the result was **SF 2 / F 1 / N 1 / A 2 / SA 0**, that is, no consensus

## prior_art - grade 2.00 (fired in 6 of 15 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                1/2/1  -> 1.33
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 1/0/1  -> 0.67
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          2/2/2  -> 2.00
  [11] 5. Impact on the Standard                    1/1/1  -> 1.00
  [12] 6. Future work                               2/2/2  -> 2.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Amended by [P3179R8] for C++26 to only take into account the elements that are actually copied.
candidate 2 (found by 3 of 45 passes): E3 was the principal alternative to E2 considered by the group.
candidate 3 (found by 3 of 45 passes): There is little reason for it to differ from `copy`; **we therefore propose to amend `copy_n`’s specification** so that it has the same preconditions and behavior (incl. the conditions for erroneous behavior) as `copy` after this paper.
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
