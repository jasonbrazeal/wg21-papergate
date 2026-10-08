Verdict: Strong (9/14)

The paper offers solid grounding in existing practice and a clear statement of the problem it addresses, but its case thins considerably when it comes to demonstrating who is affected, why the standard library is the right home, and why a library solution would not suffice. The strongest support comes from Boost’s long-standing implementation and the availability of a complete reference implementation, while the weakest areas are the largely anecdotal or survey-based claims about user impact and the absence of a developed argument for standardization over library adoption.

- The paper establishes meaningful implementation experience through Boost.SmartPtr’s shipping of all four casts since 2016 and a complete reference implementation.
- The paper establishes why the facility matters by pointing to independent code-review findings and industry use of type-erased deleters with `unique_ptr`.
- The paper only claims, without establishing, that the affected audience is broad, relying on a Slack anecdote and preliminary GitHub code-search observations.
- The paper leaves thinnest the argument for why this must be standardized rather than remain a library facility, offering only a brief assertion that the naive release-based approach is wrong.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 9. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 10.00   accumulate 9.17   max 11.67

## SUMMARY
grades: motivation 2.00  audience 0.83  prior_art 2.00  vehicle 1.00  coordination 0.83  insufficiency 0.50  implementation 2.00
sample agreement: 60 of 63 section-criterion pairs unanimous (95%)
single-sample totals would have been: 9.00 / 9.50 / 9.00   (all 3 samples: 9.17)
headings: h3 8   <- NOT h2, check the unit list
on threshold: vehicle, coordination
splits: audience[5] 1/1/0  coordination[5] 1/2/2  implementation[6] 0/1/1
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 1/1/1  -> 1.00
  [4] Prior Art                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): We propose `unique_ptr` overloads for `std::const_pointer_cast` and `std::dynamic_pointer_cast`.
candidate 2 (found by 3 of 27 passes): The need for pointer casts between `unique_ptr`s was spotted in code reviews from independent parties.
candidate 3 (found by 3 of 27 passes): It turns out that using `unique_ptr` with a type-erased deleter is not uncommon in the industry.

## audience - grade 0.83 (fired in 2 of 9 sections, strong in 0)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Prior Art                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/0  -> 0.67
  [6] Design                                       1/1/1  -> 1.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 2 of 27 passes): The [cpplang](https://cppalliance.org/slack/) Slack workspace rediscovers `dynamic_pointer_cast(std::unique_ptr<T>&&)` on a yearly basis
candidate 2 (found by 2 of 27 passes): According to our preliminary survey using GitHub code search, `static_cast`s between `unique_ptr`s using the `.release()` trick almost always perform downcast in the hope of gaining performance over `dynamic_cast` by sacrificing safety
candidate 3 (found by 1 of 27 passes): According to our preliminary survey using GitHub code search, `static_cast`s between `unique_ptr`s using the `.release()` trick almost always perform downcast in the hope of gaining performance over `dynamic_cast` by sacrificing safety, and `reinterpret_cast`s between `unique_ptr`s only retrieve byte sequences.

## prior_art - grade 2.00 (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Prior Art                                    1/1/1  -> 1.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       2/2/2  -> 2.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    1/1/1  -> 1.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): [Boost.SmartPtr](https://www.boost.org/doc/libs/1_63_0/boost/pointer_cast.hpp) ships all four casts (`dynamic_pointer_cast`, `static_pointer_cast`, `const_pointer_cast`, and `reinterpret_pointer_cast`) that create `std::unique_ptr<T>` by releasing `std::unique_ptr<U>` since 2016.
candidate 2 (found by 3 of 27 passes): Some of the work supports preserving the incoming deleter type. It's time to consider adopting the working parts from Boost and explore the recurring extension.
candidate 3 (found by 3 of 27 passes): It turns out that using `unique_ptr` with a type-erased deleter is not uncommon in the industry.
candidate 4 (found by 3 of 27 passes): Here is a full implementation: [51sjEjKcc](https://godbolt.org/z/51sjEjKcc)Compiler Explorer

## vehicle - grade 1.00 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 1.00   corroborated 1.00   accumulate 1.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Prior Art                                    0/0/0  -> 0.00
  [5] Motivation                                   2/2/2  -> 2.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): Standardize facilities that are otherwise non-trivial to get right: `unique_ptr<U>(dynamic_cast<U*>(p.release()))` is plain wrong, but that's just the appetizer.

## coordination - grade 0.83 (fired in 1 of 9 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Prior Art                                    0/0/0  -> 0.00
  [5] Motivation                                   1/2/2  -> 1.67
  [6] Design                                       0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): The need for pointer casts between `unique_ptr`s was spotted in code reviews from independent parties.

## insufficiency - grade 0.50 (fired in 1 of 9 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Prior Art                                    0/0/0  -> 0.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design                                       0/0/0  -> 0.00
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    0/0/0  -> 0.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): `unique_ptr<U>(dynamic_cast<U*>(p.release()))` is plain wrong, but that's just the appetizer.

## implementation - grade 2.00  [binary: max] (fired in 4 of 9 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] Changes                                      0/0/0  -> 0.00
  [3] Introduction                                 0/0/0  -> 0.00
  [4] Prior Art                                    2/2/2  -> 2.00
  [5] Motivation                                   1/1/1  -> 1.00
  [6] Design                                       0/1/1  -> 0.67
  [7] Wording                                      0/0/0  -> 0.00
  [8] Implementation Experience                    2/2/2  -> 2.00
  [9] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 27 passes): [Boost.SmartPtr](https://www.boost.org/doc/libs/1_63_0/boost/pointer_cast.hpp) ships all four casts (`dynamic_pointer_cast`, `static_pointer_cast`, `const_pointer_cast`, and `reinterpret_pointer_cast`) that create `std::unique_ptr<T>` by releasing `std::unique_ptr<U>` since 2016.
candidate 2 (found by 3 of 27 passes): The [cpplang](https://cppalliance.org/slack/) Slack workspace rediscovers `dynamic_pointer_cast(std::unique_ptr<T>&&)` on a yearly basis, albeit `boost::dynamic_pointer_cast(std::unique_ptr<T>&&)` existed before the group's birth.
candidate 3 (found by 3 of 27 passes): Here is a full implementation: [51sjEjKcc](https://godbolt.org/z/51sjEjKcc)Compiler Explorer
candidate 4 (found by 1 of 27 passes): According to our preliminary survey using GitHub code search, `static_cast`s between `unique_ptr`s using the `.release()` trick almost always perform downcast in the hope of gaining performance over `dynamic_cast` by sacrificing safety

-->
