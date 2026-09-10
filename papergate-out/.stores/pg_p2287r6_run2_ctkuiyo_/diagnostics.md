# Diagnostics

Verdict: Adequate (4/14, close to Weak)

Criteria addressed: 2 of 7. Points: 4 of 14. Unsupported quotes rejected: 3. Replies missing: 0.

## motivation - grade 2
votes: chunk 1: 2/2/2
quote: While I can initialize an `A` like `A{.a=1}`, I cannot designated-initialize `B`. An attempt like `B{{.a=1}, .b=2}` runs afoul of the rule that the initializers must either be all designated or none designated.

## audience - grade 0 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/1
quote: We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## prior_art - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/2/2
quote: A previous revision of this paper proposed allowing only `b1` — coming up with a way to name the base class. This revision eschews that approach entirely.

## vehicle - grade 0 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/1
quote: Additionally, in many cases, the point of inheritance of aggregates is not because we actually need an “is-a” relationship but rather to compose aggregate members.

## coordination - grade 0
votes: chunk 1: 0/0/0
quote: (none validated)

## insufficiency - grade 0
votes: chunk 1: 0/0/0
quote: (none validated)

## implementation - grade 0 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/2
quote: I implemented this [in clang](https://github.com/llvm/llvm-project/compare/main...brevzin:llvm-project:p2287?expand=1) in a very literal way — by synthesizing a new designated-initializer-list to initialize the base classes in the situations where that comes up.
