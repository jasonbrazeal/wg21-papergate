Verdict: Adequate (6/14)

The paper offers solid support in the areas where it can point to existing practice and prior discussion, but it leaves several essential parts of the standardization case almost entirely unaddressed. The thinnest support concerns the affected audience, coordination with other parts of the standard, and why a library-level solution would be insufficient.

- The strongest support comes from implementation experience, where the paper shows that existing standard libraries already use `memmove` and produce the correct result for the cases in question.
- The paper also establishes meaningful prior art and alternatives, including the C++26 change to `copy_n` and the considered option of simply dropping the preconditions.
- The argument for why the change matters is credited, particularly the observation that current preconditions offer no optimization benefit and that existing code may already be relying on the runtime behavior.
- The most glaring omission is the absence of any established account of who is affected, how the change coordinates with other standardization work, or why a library cannot address the problem.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.33/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.33 of 14. Unsupported quotes rejected: 7. Replies missing: 0. Sections: 15. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.33   corroborated 6.33   accumulate 6.33   max 6.33

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 2.00  vehicle 0.33  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 97 of 105 section-criterion pairs unanimous (92%)
single-sample totals would have been: 6.00 / 7.00 / 6.00   (all 3 samples: 6.33)
headings: h2 10 + bold numbered 4
on threshold: implementation
splits: motivation[2] 2/1/2  motivation[11] 1/1/0  motivation[12] 0/1/1  prior_art[6] 1/1/0
        prior_art[10] 0/2/0  prior_art[13] 0/1/0  vehicle[7] 0/1/0  vehicle[9] 0/1/0
## END SUMMARY

## motivation - grade 2.00 (fired in 8 of 15 sections, strong in 4)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/1/2  -> 1.67
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                2/2/2  -> 2.00
  [5] 3. Proposal                                  1/1/1  -> 1.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 2/2/2  -> 2.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          1/1/1  -> 1.00
  [11] 5. Impact on the Standard                    1/1/0  -> 0.67
  [12] 6. Future work                               0/1/1  -> 0.67
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): they are incomplete, and they do not enable any useful optimization.
candidate 2 (found by 3 of 45 passes): As argued above, the current preconditions offer no optimization benefit and cannot even guarantee a correct result.
candidate 3 (found by 3 of 45 passes): We are concerned that *there may be existing code that is accidentally relying on this runtime behavior*; with the proposed change we would be introducing a regression in it.
candidate 4 (found by 3 of 45 passes): Having a right overlap today is already undefined behavior; changing e.g. `std::copy` from doing left-to-right assignments to right-to-left assignments in this case is therefore not subject to any form of source compatibility.

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

## prior_art - grade 2.00 (fired in 7 of 15 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                1/1/1  -> 1.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 1/1/0  -> 0.67
  [7] 2. Option B: remove the preconditions, bu... 0/0/0  -> 0.00
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 2/2/2  -> 2.00
  [10] 4. Design decisions                          0/2/0  -> 0.67
  [11] 5. Impact on the Standard                    1/1/1  -> 1.00
  [12] 6. Future work                               2/2/2  -> 2.00
  [13] 7. Proposed Wording                          0/1/0  -> 0.33
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 45 passes): Amended by [P3179R8] for C++26 to only take into account the elements that are actually copied.
candidate 2 (found by 3 of 45 passes): E3 was the principal alternative to E2 considered by the group.
candidate 3 (found by 3 of 45 passes): For `copy_n`, it establishes new preconditions, matching existing practice and resolving [LWG3089].
candidate 4 (found by 2 of 45 passes): With this option we would simply drop the *Preconditions* clauses, but we would not be proposing any change to the effects of the algorithms.

## vehicle - grade 0.33 (fired in 2 of 15 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.33   accumulate 0.33   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 1. Changelog                                 0/0/0  -> 0.00
  [4] 2. Motivation                                0/0/0  -> 0.00
  [5] 3. Proposal                                  0/0/0  -> 0.00
  [6] 1. Option A: "just remove" the preconditi... 0/0/0  -> 0.00
  [7] 2. Option B: remove the preconditions, bu... 0/1/0  -> 0.33
  [8] 1. Extension E1: contiguous iterators ove... 0/0/0  -> 0.00
  [9] 2. Extension E2: all contiguous iterator ... 0/1/0  -> 0.33
  [10] 4. Design decisions                          0/0/0  -> 0.00
  [11] 5. Impact on the Standard                    0/0/0  -> 0.00
  [12] 6. Future work                               0/0/0  -> 0.00
  [13] 7. Proposed Wording                          0/0/0  -> 0.00
  [14] 8. Acknowledgements                          0/0/0  -> 0.00
  [15] References                                   0/0/0  -> 0.00
candidate 1 (found by 1 of 45 passes): We are concerned that *there may be existing code that is accidentally relying on this runtime behavior*; with the proposed change we would be introducing a regression in it.
candidate 2 (found by 1 of 45 passes): Apart from the technical aspects, we may also foresee concerns about teachability, as well as managing users' expectations: for instance, we’d have to teach that `std::copy` "normally" performs left-to-right assignments, except when the iterators are contiguous

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
