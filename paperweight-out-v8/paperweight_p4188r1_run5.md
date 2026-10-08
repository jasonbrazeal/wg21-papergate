Verdict: Strong (9/14)

The paper offers solid grounding for its motivation and shows credible implementation experience, but its case thins considerably when it moves from explaining the problem to demonstrating who is affected and why only the standard library can solve it. The strongest material is concrete and verifiable, while the weakest relies on assertion and indirect evidence rather than demonstrated need.

- The paper clearly establishes why the absence of a standard extension mechanism matters and why the solution must originate in the standard library itself.
- The implementation experience is well supported by a cross-compiler proof of concept and references to existing libraries that implement similar machinery.
- The discussion of prior art and alternatives is thorough, including engagement with related proposals and existing practice.
- The most glaring omission is the lack of established evidence for who is affected and why a library solution will not do, since the usage statistics and the claim that user code cannot provide the mechanism are asserted rather than demonstrated.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 20. Replies missing: 0. Sections: 6. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 8.67   accumulate 9.50   max 11.67

## SUMMARY
grades: motivation 1.50  audience 1.00  prior_art 2.00  vehicle 1.00  coordination 0.33  insufficiency 1.33  implementation 2.00
sample agreement: 37 of 42 section-criterion pairs unanimous (88%)
single-sample totals would have been: 9.00 / 9.00 / 10.00   (all 3 samples: 9.17)
headings: h2 5
on threshold: motivation, audience, insufficiency, implementation
splits: prior_art[6] 1/0/0  vehicle[2] 2/0/0  coordination[2] 0/0/2  insufficiency[3] 0/1/1
        implementation[2] 0/2/2
## END SUMMARY

## motivation - grade 1.50 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.50   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 2 Impact on the Standard                     2/2/2  -> 2.00
  [4] 3 Design Principles                          0/0/0  -> 0.00
  [5] 4 General Specifications for built-in ari... 1/1/1  -> 1.00
  [6] 5 Technical Specification                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): This proposal therefore chooses to leave `std``::``math``::``sqrt` undefined for integral types, keeping this design space open for future improvements that could align with or build on that work.
candidate 2 (found by 2 of 18 passes): Since the core problem is the absence of a standard extension mechanism, the solution must be introduced by the standard library itself. It cannot be provided by user code or third-party libraries alone.
candidate 3 (found by 1 of 18 passes): Since the core problem is the absence of a standard extension mechanism, the solution must be introduced by the standard library itself.

## audience - grade 1.00 (fired in 1 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Impact on the Standard                     0/0/0  -> 0.00
  [4] 3 Design Principles                          0/0/0  -> 0.00
  [5] 4 General Specifications for built-in ari... 0/0/0  -> 0.00
  [6] 5 Technical Specification                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Using GitHub search functionality shows 115k C++ files using the idiom `using` `std``::``pow;` for 3.5M C++ files calling `pow``(`, of which 741k C++ files calling explicitly `std``::``pow``(`.

## prior_art - grade 2.00 (fired in 3 of 6 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/0  -> 0.00
  [3] 2 Impact on the Standard                     0/0/0  -> 0.00
  [4] 3 Design Principles                          2/2/2  -> 2.00
  [5] 4 General Specifications for built-in ari... 2/2/2  -> 2.00
  [6] 5 Technical Specification                    1/0/0  -> 0.33
candidate 1 (found by 3 of 18 passes): Specifically, if [[P2806R3]](https://wg21.link/p2806r3) (do expressions) and [[P2826R3]](https://wg21.link/p2826r3) (expression aliases) are accepted for C++29, the implementation of `std::math::sqrt` reduces significantly.
candidate 2 (found by 3 of 18 passes): [[P3605R1]](https://wg21.link/p3605r1) separately explores this question, proposing a different name for reasons that are similar to the motivations for a separate namespace in this proposal.
candidate 3 (found by 1 of 18 passes): [boost-units-sqrt] Boost Developers. Boost.Units: sqrt Implementation.

## vehicle - grade 1.00 (fired in 3 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.33   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/0/0  -> 0.67
  [3] 2 Impact on the Standard                     1/1/1  -> 1.00
  [4] 3 Design Principles                          1/1/1  -> 1.00
  [5] 4 General Specifications for built-in ari... 0/0/0  -> 0.00
  [6] 5 Technical Specification                    0/0/0  -> 0.00
candidate 1 (found by 3 of 18 passes): Since the core problem is the absence of a standard extension mechanism, the solution must be introduced by the standard library itself. It cannot be provided by user code or third-party libraries alone.
candidate 2 (found by 3 of 18 passes): By combining both, the new code can benefit from the new approach in the new namespace with a new contract, while the compatibility layer in `std` remains available for targeted, case-by-case opt-ins.
candidate 3 (found by 1 of 18 passes): The existence of multiple widely-used C++ libraries implementing exactly this machinery is evidence that there are real use-cases and that the status quo is encouraging unnecessary duplication.

## coordination - grade 0.33 (fired in 1 of 6 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/0/2  -> 0.67
  [3] 2 Impact on the Standard                     0/0/0  -> 0.00
  [4] 3 Design Principles                          0/0/0  -> 0.00
  [5] 4 General Specifications for built-in ari... 0/0/0  -> 0.00
  [6] 5 Technical Specification                    0/0/0  -> 0.00
candidate 1 (found by 1 of 18 passes): The existence of multiple widely-used C++ libraries implementing exactly this machinery is evidence that there are real use-cases and that the status quo is encouraging unnecessary duplication.

## insufficiency - grade 1.33 (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.33   corroborated 1.00   accumulate 1.33   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     2/2/2  -> 2.00
  [3] 2 Impact on the Standard                     0/1/1  -> 0.67
  [4] 3 Design Principles                          0/0/0  -> 0.00
  [5] 4 General Specifications for built-in ari... 0/0/0  -> 0.00
  [6] 5 Technical Specification                    0/0/0  -> 0.00
candidate 1 (found by 2 of 18 passes): The idiomatic workaround is to enable ADL via a `using` declaration: ... However, this idiom has a critical limitation: it requires a statement, and is therefore unavailable in contexts that only accept expressions.
candidate 2 (found by 2 of 18 passes): Since the core problem is the absence of a standard extension mechanism, the solution must be introduced by the standard library itself. It cannot be provided by user code or third-party libraries alone.
candidate 3 (found by 1 of 18 passes): The idiomatic workaround is to enable ADL via a `using` declaration: ... this idiom has a critical limitation: it requires a statement, and is therefore unavailable in contexts that only accept expressions.

## implementation - grade 2.00  [binary: max] (fired in 2 of 6 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Abstract                                     0/2/2  -> 1.33
  [3] 2 Impact on the Standard                     0/0/0  -> 0.00
  [4] 3 Design Principles                          0/0/0  -> 0.00
  [5] 4 General Specifications for built-in ari... 0/0/0  -> 0.00
  [6] 5 Technical Specification                    2/2/2  -> 2.00
candidate 1 (found by 3 of 18 passes): A proof of concept implementing std::math::sqrt, std::math::abs, std::math::norm_order, and the compatibility layer, verified under GCC, Clang, and MSVC, is available at [extmath-poc].
candidate 2 (found by 1 of 18 passes): mp-units adds an explicit member function check. [[mp-units]](https://github.com/mpusz/mp-units/blob/b0e72810b983841b260d570b241c52586aa78999/src/core/include/mp-units/framework/representation_concepts.h#L227-L262)
candidate 3 (found by 1 of 18 passes): The library **nholthaus/units**, for instance, provides `units``::``math``::``sqrt` which calls `std``::``sqrt` directly on the underlying scalar value, which means it does not enable ADL resolution and thus does not extend to custom underlying types. [[nholthaus-units]](https://github.com/nholthaus/units)

-->
