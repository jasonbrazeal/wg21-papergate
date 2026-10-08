Verdict: Adequate (7/14)

The paper gives a partial account of itself: it explains the motivating problem and shows some implementation work, but it leaves several essential parts of the standardization case almost entirely unaddressed. The thinnest areas are the absence of any identified user population, the lack of discussion about coordination or interoperability, and the failure to explain why a library solution would not suffice.

- The strongest support comes from the concrete implementation experience, including a linked example and a compiler fork demonstrating the feature.
- The paper also establishes the core motivation clearly, particularly the fragility of index-based access when variant alternatives are reordered or inserted.
- The discussion of prior art and alternatives is credited, though it leans heavily on the authors’ own limited implementation experience rather than broader comparison.
- The most glaring omission is the complete lack of evidence about who is affected, leaving the proposal without a demonstrated constituency or need beyond the authors’ own context.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Adequate (6.67/14, close to Strong)

Provisionally addressed: 4 of 7. Provisional points: 6.67 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 8. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 6.67   corroborated 7.00   accumulate 6.83   max 7.67

## SUMMARY
grades: motivation 2.00  audience 0.00  prior_art 1.83  vehicle 0.83  coordination 0.00  insufficiency 0.00  implementation 2.00
sample agreement: 53 of 56 section-criterion pairs unanimous (95%)
single-sample totals would have been: 7.00 / 6.00 / 7.00   (all 3 samples: 6.67)
headings: h2 7
on threshold: vehicle, implementation
splits: prior_art[3] 2/1/2  vehicle[3] 2/1/2  implementation[8] 0/2/0
## END SUMMARY

## motivation - grade 2.00 (fired in 2 of 8 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                2/2/2  -> 2.00
  [3] 2. What about unscoped enum ?                2/2/2  -> 2.00
  [4] 3. Feature                                   0/0/0  -> 0.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): A common issue with `std::variant` is index-based access: if `variant<Dog, Tanuki, Cat>` is later augmented with `variant<Dog, Tanuki, Racoon, Cat>`, or the alternatives are shuffled, an index-based switch table will break silently.
candidate 2 (found by 3 of 24 passes): Synthesizing enumerators of a scoped enum is a fairly simple operation, on the other hand rewiring the proper context for enumerators of an unscoped enum is quite more troublesome and error sensitive.

## audience - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                0/0/0  -> 0.00
  [3] 2. What about unscoped enum ?                0/0/0  -> 0.00
  [4] 3. Feature                                   0/0/0  -> 0.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## prior_art - grade 1.83 (fired in 3 of 8 sections, strong in 2)  (SHARED PASSAGE)
under each rule: top2 1.83   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                1/1/1  -> 1.00
  [3] 2. What about unscoped enum ?                2/1/2  -> 1.67
  [4] 3. Feature                                   2/2/2  -> 2.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): The generative capability of reflection as they were introduced in C++26 are limited to `define_aggregate`, with no quick paths to more powerful facilities (See [p3294r2] for example).
candidate 2 (found by 3 of 24 passes): Our rationale behind this conservative approach is entirely rooted in our implementation experience (granted not extensive).
candidate 3 (found by 3 of 24 passes): Diverging with the original design of `define_aggregate()`, annotations and attributes are directly supported here via `.annotations` and `.attributes`.

## vehicle - grade 0.83 (fired in 1 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                0/0/0  -> 0.00
  [3] 2. What about unscoped enum ?                2/1/2  -> 1.67
  [4] 3. Feature                                   0/0/0  -> 0.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidate 1 (found by 3 of 24 passes): Our rationale behind this conservative approach is entirely rooted in our implementation experience (granted not extensive).

## coordination - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                0/0/0  -> 0.00
  [3] 2. What about unscoped enum ?                0/0/0  -> 0.00
  [4] 3. Feature                                   0/0/0  -> 0.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## insufficiency - grade 0.00 (fired in 0 of 8 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                0/0/0  -> 0.00
  [3] 2. What about unscoped enum ?                0/0/0  -> 0.00
  [4] 3. Feature                                   0/0/0  -> 0.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 3 of 8 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1. Motivation                                2/2/2  -> 2.00
  [3] 2. What about unscoped enum ?                1/1/1  -> 1.00
  [4] 3. Feature                                   0/0/0  -> 0.00
  [5] 4. Wording                                   0/0/0  -> 0.00
  [6] 5. Status                                    0/0/0  -> 0.00
  [7] 6. Acknowledgements                          0/0/0  -> 0.00
  [8] References                                   0/2/0  -> 0.67
candidate 1 (found by 3 of 24 passes): See [this example](https://godbolt.org/z/5a3Yenz8d) where we also leverage annotations on enumerators.
candidate 2 (found by 3 of 24 passes): Our rationale behind this conservative approach is entirely rooted in our implementation experience (granted not extensive).
candidate 3 (found by 1 of 24 passes): Aurelien Cassagnes. [define_enum](https://github.com/bloomberg/clang-p2996/pull/263). URL: [https://github.com/bloomberg/clang-p2996/pull/263](https://github.com/bloomberg/clang-p2996/pull/263)

-->
