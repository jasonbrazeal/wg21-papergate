Verdict: Strong (8/14)

The paper offers a solid foundation for its standardization case in the areas of motivation, prior art, and implementation experience, but it leaves several important arguments asserted rather than demonstrated. The thinnest support is in explaining why a library solution cannot suffice, which is not addressed at all, and the claims about affected users, the need for a standard feature, and interoperability are stated without concrete evidence.

- The strongest support comes from the concrete implementation in Clang and the clear contrast with prior proposals like P1819 and P3412.
- The motivation is well grounded in the practical difficulties of ordering replacement fields in `std::format` and the debugging value of the equals suffix.
- The paper asserts that string interpolation is widely popular and that the feature would be embedded-friendly, but does not establish who specifically is affected or why standardization is necessary.
- The most glaring omission is the absence of any argument for why a library-based approach cannot achieve the same goals.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (7.83/14)

Provisionally addressed: 6 of 7. Provisional points: 7.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 7.83   corroborated 8.67   accumulate 7.83   max 9.33

## SUMMARY
grades: motivation 2.00  audience 0.33  prior_art 2.00  vehicle 0.83  coordination 0.67  insufficiency 0.00  implementation 2.00
sample agreement: 45 of 49 section-criterion pairs unanimous (92%)
single-sample totals would have been: 7.50 / 7.50 / 8.50   (all 3 samples: 7.83)
headings: h2 5
on threshold: none
splits: audience[3] 1/1/0  vehicle[4] 0/0/1  vehicle[6] 2/0/2  coordination[4] 0/2/2
## END SUMMARY

## motivation - grade 2.00 (fired in 3 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       2/2/2  -> 2.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 2 of 21 passes): Because the object approach preserves all the information in the original format string, you can do things like structured logging (as in the JSON example from earlier).
candidate 3 (found by 1 of 21 passes): One nice debugging feature that Python’s f-strings (and template strings) have is the equals suffix... The ability to support this on the other hand is *very* useful for debugging
candidate 4 (found by 1 of 21 passes): One nice debugging feature that Python’s f-strings (and template strings) have is the equals suffix... The ability to support this on the other hand is *very* useful for debugging.

## audience - grade 0.33 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.33   corroborated 0.67   accumulate 0.33   max 0.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/0  -> 0.67
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): String interpolation is a wildly popular language feature due to the ease with which it allows users to express complex ideas.

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 4)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [5] 3 Design  (part 2 of 2)                      2/2/2  -> 2.00
  [6] 4 Alternate Approaches                       2/2/2  -> 2.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different. `interp` is already a `std::string`
candidate 2 (found by 3 of 21 passes): This is a difference in the logic proposed in [[P3412R3]](https://wg21.link/p3412r3), which looks specifically for the *token* (not character) `:`.
candidate 3 (found by 3 of 21 passes): For this problem, [[P3412R3]](https://wg21.link/p3412r3) has an easier path to supporting `gettext`, since in that paper an f-literal is an expression-list, and so it should be possible to preprocess your way to wrapping just the format string part.
candidate 4 (found by 3 of 21 passes): As I mentioned earlier, P3412 is really two language features: a string interpolation feature whose intermediate representation is an expression-list, and a feature which just calls `std::format` on that expression-list.

## vehicle - grade 0.83 (fired in 2 of 7 sections, strong in 0)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      0/0/1  -> 0.33
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       2/0/2  -> 1.33
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.
candidate 2 (found by 1 of 21 passes): Keep in mind that since a template string object is *just an object*, where most of the information are static data members, this ends up being a very embedded-friendly design too.

## coordination - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      0/2/2  -> 1.33
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): We can provide a nice API for it like this: ... auto query = SQLite::makeStatement(db, t"SELECT * FROM test WHERE name = {name}");
candidate 2 (found by 1 of 21 passes): We can use template strings to make it easy to build up a statement properly. This example uses SQLiteCpp, but the same idea can be used for any other SQL library really.

## insufficiency - grade 0.00 (fired in 0 of 7 sections, strong in 0)
under each rule: top2 0.00   corroborated 0.00   accumulate 0.00   max 0.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidates: (none validated)

## implementation - grade 2.00  [binary: max] (fired in 2 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      2/2/2  -> 2.00
  [6] 4 Alternate Approaches                       2/2/2  -> 2.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): I implemented this in Clang, on top of the p2996 reflection branch. Code can be found in my fork in the `template-strings` branch [here](https://github.com/brevzin/llvm-project/tree/template-strings)
candidate 2 (found by 3 of 21 passes): This is actually [implementable](https://compiler-explorer.com/z/b6jdavTW1) in the expression-list model, but not easily:

-->
