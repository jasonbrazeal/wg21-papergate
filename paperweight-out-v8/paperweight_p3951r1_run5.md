Verdict: Strong (9/14)

The paper gives a reasonably solid account of why template strings would be useful and how they differ from the main alternative, but it leans on assertion rather than evidence for several parts of the standardization case, particularly around affected users, interoperability, and the limits of library-only solutions.

- The strongest support is for prior art and alternatives, where the paper carefully contrasts its object-based approach with P3412’s expression-list model and explains the practical consequences of that difference.
- The paper also clearly establishes why the feature belongs in the standard rather than waiting for a more general future mechanism, arguing that the dedicated feature is small and self-contained enough to justify near-term adoption.
- The implementation experience section is credible, with a working Clang implementation and a concrete demonstration of how the feature can be realized in practice.
- The thinnest part is the claim that a library cannot solve the problem, since the paper asserts that expression names are lost in library-level approaches but does not fully demonstrate that this limitation blocks the motivating use cases.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (9.17/14)

Provisionally addressed: 7 of 7. Provisional points: 9.17 of 14. Unsupported quotes rejected: 1. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 9.17   corroborated 9.33   accumulate 9.50   max 11.33

## SUMMARY
grades: motivation 2.00  audience 0.17  prior_art 2.00  vehicle 1.50  coordination 0.83  insufficiency 0.67  implementation 2.00
sample agreement: 42 of 49 section-criterion pairs unanimous (86%)
single-sample totals would have been: 10.00 / 9.00 / 9.00   (all 3 samples: 9.17)
headings: h2 5
on threshold: vehicle, coordination
splits: motivation[4] 2/1/1  motivation[5] 1/0/0  audience[3] 1/0/0  vehicle[3] 1/0/1
        vehicle[4] 2/1/0  coordination[4] 2/1/2  insufficiency[6] 1/2/1
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Design  (part 1 of 2)                      2/1/1  -> 1.33
  [5] 3 Design  (part 2 of 2)                      1/0/0  -> 0.33
  [6] 4 Alternate Approaches                       2/2/2  -> 2.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 3 of 21 passes): Because the object approach preserves all the information in the original format string, you can do things like structured logging (as in the JSON example from earlier).
candidate 3 (found by 2 of 21 passes): There are many things you can do with a template string, so let’s just run through them.
candidate 4 (found by 1 of 21 passes): One nice debugging feature that Python’s f-strings (and template strings) have is the equals suffix... The ability to support this on the other hand is *very* useful for debugging.

## audience - grade 0.17 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.17   corroborated 0.33   accumulate 0.17   max 0.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/0  -> 0.33
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): String interpolation is a wildly popular language feature due to the ease with which it allows users to express complex ideas.

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
candidate 1 (found by 3 of 21 passes): This is a difference in the logic proposed in [[P3412R3]](https://wg21.link/p3412r3), which looks specifically for the *token* (not character) `:`.
candidate 2 (found by 3 of 21 passes): For this problem, [[P3412R3]](https://wg21.link/p3412r3) has an easier path to supporting `gettext`, since in that paper an f-literal is an expression-list, and so it should be possible to preprocess your way to wrapping just the format string part.
candidate 3 (found by 3 of 21 passes): As I mentioned earlier, P3412 is really two language features: a string interpolation feature whose intermediate representation is an expression-list, and a feature which just calls `std::format` on that expression-list.
candidate 4 (found by 2 of 21 passes): In P1819, the `interp` is an object that is roughly equivalent to: ... In P3412, the behavior is very different. `interp` is already a `std::string`

## vehicle - grade 1.50 (fired in 3 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 1.50   corroborated 1.00   accumulate 1.83   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/0/1  -> 0.67
  [4] 3 Design  (part 1 of 2)                      2/1/0  -> 1.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       2/2/2  -> 2.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): So should we wait? It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.
candidate 2 (found by 1 of 21 passes): The solution to this problem is string interpolation: the ability to put the expression to be formatted inside of the format string.
candidate 3 (found by 1 of 21 passes): It’s not infeasible that some future language change gives us a better way to solve this problem. But with the P3412R3 design, we wouldn’t be able to adopt those changes to the formatting functions because they would break string interpolation
candidate 4 (found by 1 of 21 passes): We can use template strings to make it easy to build up a statement properly.

## coordination - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)  (SHARED PASSAGE)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      2/1/2  -> 1.67
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): We can use template strings to make it easy to build up a statement properly. This example uses SQLiteCpp, but the same idea can be used for any other SQL library really.
candidate 2 (found by 1 of 21 passes): We can use template strings to make it easy to build up a statement properly.

## insufficiency - grade 0.67 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.67   max 1.33
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       1/2/1  -> 1.33
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 2 of 21 passes): The expression-list approach simply doesn’t have the “names” of the expressions anymore, so they’re not available for further use.
candidate 2 (found by 1 of 21 passes): any structured logging use-cases that might require the names of the expressions is impossible in the expression-list approach.

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
