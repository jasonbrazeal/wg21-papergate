Verdict: Adequate (5/14)

The paper offers some grounding in prior art and alternatives, but its own case for standardization is thin where it matters most: it does not establish who is affected, how the feature would coordinate with existing practice, or that there is any implementation experience behind the design. The strongest support is retrospective, showing that the proposed library objects can reproduce existing contract semantics, while the affirmative reasons for changing the standard remain largely asserted rather than demonstrated.

- The paper’s clearest support comes from its account of prior art and alternatives, including the relationship to P3400 label lookup and the reimplementation of C++26 contract behavior as library objects.
- The argument for why the standard should adopt this is only claimed, resting on removing a compiler-to-header dependency and avoiding standardization of the violation handler, without showing that these are problems the committee must solve.
- The paper does not establish who is affected by the current design or the proposed change, leaving the practical stakes of the proposal unclear.
- The most glaring omission is the absence of any implementation experience, which leaves the proposal without evidence that the design works in practice or that the claimed benefits are real.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (4.83/14)

Provisionally addressed: 4 of 7. Provisional points: 4.83 of 14. Unsupported quotes rejected: 6. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 4.83   corroborated 4.33   accumulate 5.33   max 6.00

## SUMMARY
grades: motivation 1.33  audience 0.00  prior_art 2.00  vehicle 1.33  coordination 0.00  insufficiency 0.17  implementation 0.00
sample agreement: 49 of 56 section-criterion pairs unanimous (88%)
single-sample totals would have been: 4.50 / 5.50 / 5.00   (all 3 samples: 4.83)
headings: h2 7
on threshold: motivation, vehicle
splits: motivation[4] 0/1/0  motivation[5] 2/2/1  prior_art[6] 2/1/1  prior_art[7] 1/1/0
        vehicle[5] 0/2/0  vehicle[7] 0/1/1  insufficiency[2] 0/0/1
## END SUMMARY

## motivation - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.50   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Reimplementing C++26 contract assertion... 0/0/0  -> 0.00
  [4] 4 Discussions and consequences               0/1/0  -> 0.33
  [5] 5 Specification alternatives                 2/2/1  -> 1.67
  [6] 6 Backwards compatibility to C++26 contracts 1/1/1  -> 1.00
  [7] 7 Reasons to not standardize C++26 contra... 0/0/0  -> 0.00
  [8] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): However, this meaning is so vaguely defined in C++26 that many codebases seem to not want to use C++26 contracts.
candidate 2 (found by 2 of 24 passes): Adding an include of this header is a refactoring that is somewhat tedious but not hard to do or error prone, and failing to do it causes compile time errors.
candidate 3 (found by 1 of 24 passes): This allows library vendors to ensure that contract violations in their code are handled according to their specification and not subjected to a global contract violation handler that can subvert the semantics that the library depends on.
candidate 4 (found by 1 of 24 passes): The main (only?) backwards compatibility issue is that the `<contracts>` header must be included to get the standard assertion object declarations.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Reimplementing C++26 contract assertion... 0/0/0  -> 0.00
  [4] 4 Discussions and consequences               0/0/0  -> 0.00
  [5] 5 Specification alternatives                 0/0/0  -> 0.00
  [6] 6 Backwards compatibility to C++26 contracts 0/0/0  -> 0.00
  [7] 7 Reasons to not standardize C++26 contra... 0/0/0  -> 0.00
  [8] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 2.00 (fired in 6 of 8 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   2/2/2  -> 2.00
  [3] 3 Reimplementing C++26 contract assertion... 1/1/1  -> 1.00
  [4] 4 Discussions and consequences               2/2/2  -> 2.00
  [5] 5 Specification alternatives                 2/2/2  -> 2.00
  [6] 6 Backwards compatibility to C++26 contracts 2/1/1  -> 1.33
  [7] 7 Reasons to not standardize C++26 contra... 1/1/0  -> 0.67
  [8] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): With this proposal the built in functionality of C++26 contracts can be reimplemented as standard library *assertion* *objects* without changing semantics.
candidate 2 (found by 3 of 24 passes): This is essentially the same rules as for [[P3400R2](https://wg21.link/p3400r2)] label lookup.
candidate 3 (found by 3 of 24 passes): An alternative specification would be that the three names used for C++26 contracts are retained and named assertion objects are treated just like the labels of P3400.
candidate 4 (found by 3 of 24 passes): In C++26 contracts can be used without including any header, which is logical as the names of the contract assertion kinds are built in.

## vehicle - grade 1.33 (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.67   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Reimplementing C++26 contract assertion... 0/0/0  -> 0.00
  [4] 4 Discussions and consequences               2/2/2  -> 2.00
  [5] 5 Specification alternatives                 0/2/0  -> 0.67
  [6] 6 Backwards compatibility to C++26 contracts 0/0/0  -> 0.00
  [7] 7 Reasons to not standardize C++26 contra... 0/1/1  -> 0.67
  [8] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 24 passes): By this definition the dependency from the compiler to the standard library header `<contracts>` is removed and contracts can be used without using the standard library.
candidate 2 (found by 2 of 24 passes): There is nothing wrong with the `contract_violation` type or the replaceable handler that would not benefit from not being standardized in C++26.
candidate 3 (found by 1 of 24 passes): Note that this is in contrast from C++26 contracts where *everything* in `<contracts>` is used directly by the compiler, except `invoke_default_contract_violation_handler`.
candidate 4 (found by 1 of 24 passes): The major reason this is not the promoted solution in this proposal is that the syntax is clumsier and invites defining macros to get back to the syntax the rest of this proposal.

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Reimplementing C++26 contract assertion... 0/0/0  -> 0.00
  [4] 4 Discussions and consequences               0/0/0  -> 0.00
  [5] 5 Specification alternatives                 0/0/0  -> 0.00
  [6] 6 Backwards compatibility to C++26 contracts 0/0/0  -> 0.00
  [7] 7 Reasons to not standardize C++26 contra... 0/0/0  -> 0.00
  [8] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.17 (fired in 1 of 8 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/1  -> 0.33
  [3] 3 Reimplementing C++26 contract assertion... 0/0/0  -> 0.00
  [4] 4 Discussions and consequences               0/0/0  -> 0.00
  [5] 5 Specification alternatives                 0/0/0  -> 0.00
  [6] 6 Backwards compatibility to C++26 contracts 0/0/0  -> 0.00
  [7] 7 Reasons to not standardize C++26 contra... 0/0/0  -> 0.00
  [8] 8 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 24 passes): The `ep` parameter must be of type `exception_pointers` as this is a magic type that can’t be reimplemented outside of the standard library.

## implementation - grade 0.00  [binary: max] (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 2 Proposal                                   0/0/0  -> 0.00
  [3] 3 Reimplementing C++26 contract assertion... 0/0/0  -> 0.00
  [4] 4 Discussions and consequences               0/0/0  -> 0.00
  [5] 5 Specification alternatives                 0/0/0  -> 0.00
  [6] 6 Backwards compatibility to C++26 contracts 0/0/0  -> 0.00
  [7] 7 Reasons to not standardize C++26 contra... 0/0/0  -> 0.00
  [8] 8 References                                 0/0/0  -> 0.00
candidates: (none validated)

-->
