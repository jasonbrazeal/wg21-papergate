Verdict: Strong (9/14)

The paper offers a reasonably grounded case in some areas, particularly its discussion of prior art, alternatives, and implementation experience, but it leaves several central justifications more asserted than demonstrated. The thinnest support appears around the need for a standard language feature rather than a library solution, and around who would actually be affected by the change.

- The strongest support comes from the concrete implementation work in Clang and the comparison with P3412R3’s token-based approach.
- The paper also does well to situate its design alongside Python, Rust, and C# precedents, making the prior-art landscape clear.
- The argument that a library cannot provide the same capability rests mainly on the loss of expression names, but that claim is not developed into a persuasive limitation.
- The most glaring omission is the lack of established evidence that string interpolation’s popularity translates into a need affecting real C++ users in ways the paper specifies.


<!-- paperweight-diagnostics
# Diagnostics

Provisional: Strong (8.83/14)

Provisionally addressed: 7 of 7. Provisional points: 8.83 of 14. Unsupported quotes rejected: 3. Replies missing: 0. Sections: 7. Samples: 3.

Intra-section rule: mean of 3 samples. Inter-section rule in force: top2 (existence-asserting criteria always take the max).
Totals under every inter-section rule: top2 8.83   corroborated 10.00   accumulate 9.00   max 11.33

## SUMMARY
grades: motivation 2.00  audience 0.50  prior_art 2.00  vehicle 0.67  coordination 0.83  insufficiency 0.83  implementation 2.00
sample agreement: 41 of 49 section-criterion pairs unanimous (84%)
single-sample totals would have been: 8.50 / 9.00 / 9.50   (all 3 samples: 8.83)
headings: h2 5
on threshold: coordination, insufficiency
splits: motivation[4] 1/2/0  motivation[5] 1/1/0  prior_art[6] 2/2/0  vehicle[3] 0/2/1
        vehicle[4] 0/1/0  vehicle[6] 0/0/1  coordination[4] 2/1/2  insufficiency[6] 2/1/2
## END SUMMARY

## motivation - grade 2.00 (fired in 4 of 7 sections, strong in 2)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Design  (part 1 of 2)                      1/2/0  -> 1.00
  [5] 3 Design  (part 2 of 2)                      1/1/0  -> 0.67
  [6] 4 Alternate Approaches                       2/2/2  -> 2.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): With `std::format`, as the amount of replacement fields increases, it becomes increasingly difficult to ensure that they are all correctly ordered.
candidate 2 (found by 1 of 21 passes): The important thing is to expose all the relevant information to users to let them do whatever they want with it.
candidate 3 (found by 1 of 21 passes): There are many things you can do with a template string, so let’s just run through them.
candidate 4 (found by 1 of 21 passes): One question that comes up is the question of translation. How do we support `gettext`?

## audience - grade 0.50 (fired in 1 of 7 sections, strong in 0)
under each rule: top2 0.50   corroborated 1.00   accumulate 0.50   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               1/1/1  -> 1.00
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): String interpolation is a wildly popular language feature due to the ease with which it allows users to express complex ideas.

## prior_art - grade 2.00 (fired in 4 of 7 sections, strong in 3)
under each rule: top2 2.00   corroborated 2.00   accumulate 2.00   max 2.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               2/2/2  -> 2.00
  [4] 3 Design  (part 1 of 2)                      2/2/2  -> 2.00
  [5] 3 Design  (part 2 of 2)                      2/2/2  -> 2.00
  [6] 4 Alternate Approaches                       2/2/0  -> 1.33
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): This is a difference in the logic proposed in [[P3412R3]](https://wg21.link/p3412r3), which looks specifically for the *token* (not character) `:`.
candidate 2 (found by 3 of 21 passes): For this problem, [[P3412R3]](https://wg21.link/p3412r3) has an easier path to supporting `gettext`, since in that paper an f-literal is an expression-list, and so it should be possible to preprocess your way to wrapping just the format string part.
candidate 3 (found by 2 of 21 passes): This paper’s design is along the lines of Python’s template strings, Rust’s `format_args!`, and C#’s `FormattableString` idea.
candidate 4 (found by 2 of 21 passes): As I mentioned earlier, P3412 is really two language features: a string interpolation feature whose intermediate representation is an expression-list, and a feature which just calls `std::format` on that expression-list.

## vehicle - grade 0.67 (fired in 3 of 7 sections, strong in 0)
under each rule: top2 0.67   corroborated 1.00   accumulate 0.83   max 1.00
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/2/1  -> 1.00
  [4] 3 Design  (part 1 of 2)                      0/1/0  -> 0.33
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/1  -> 0.33
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): With the P3412R3 design, we wouldn’t be able to adopt those changes to the formatting functions because they would break string interpolation
candidate 2 (found by 1 of 21 passes): It’s not infeasible that some future language change gives us a better way to solve this problem.
candidate 3 (found by 1 of 21 passes): Keep in mind that since a template string object is *just an object*, where most of the information are static data members, this ends up being a very embedded-friendly design too.
candidate 4 (found by 1 of 21 passes): It seems incredibly unlikely that we will land something as expansive as token sequence injection in C++29 (if ever?), and a dedicated language feature for template string objects is pretty small and self-contained.

## coordination - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      2/1/2  -> 1.67
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       0/0/0  -> 0.00
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 1 of 21 passes): We can use template strings to make it easy to build up a statement properly.
candidate 2 (found by 1 of 21 passes): We can provide a nice API for it like this:
candidate 3 (found by 1 of 21 passes): We can use template strings to make it easy to build up a statement properly. This example uses SQLiteCpp, but the same idea can be used for any other SQL library really.

## insufficiency - grade 0.83 (fired in 1 of 7 sections, strong in 1)  (ON THRESHOLD)
under each rule: top2 0.83   corroborated 1.00   accumulate 0.83   max 1.67
votes by section:
  [1] (front matter: title, abstract and anythi... 0/0/0  -> 0.00
  [2] 1 Revision History                           0/0/0  -> 0.00
  [3] 2 Introduction                               0/0/0  -> 0.00
  [4] 3 Design  (part 1 of 2)                      0/0/0  -> 0.00
  [5] 3 Design  (part 2 of 2)                      0/0/0  -> 0.00
  [6] 4 Alternate Approaches                       2/1/2  -> 1.67
  [7] 5 References                                 0/0/0  -> 0.00
candidate 1 (found by 3 of 21 passes): The expression-list approach simply doesn’t have the “names” of the expressions anymore, so they’re not available for further use.

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
