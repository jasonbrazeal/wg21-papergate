# What the paper offers

## why it matters: supported with specifics
> While I can initialize an `A` like `A{.a=1}`, I cannot designated-initialize `B`. An attempt like `B{{.a=1}, .b=2}` runs afoul of the rule that the initializers must either be all designated or none designated.

## who is affected: not addressed
> We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## prior art and alternatives: supported with specifics
> A previous revision of this paper proposed allowing only `b1` — coming up with a way to name the base class. This revision eschews that approach entirely.

## why the standard: not addressed
> Additionally, in many cases, the point of inheritance of aggregates is not because we actually need an “is-a” relationship but rather to compose aggregate members.

## coordination and interoperability: not addressed

## why a library will not do: not addressed

## implementation experience: not addressed
> I implemented this [in clang](https://github.com/llvm/llvm-project/compare/main...brevzin:llvm-project:p2287?expand=1) in a very literal way — by synthesizing a new designated-initializer-list to initialize the base classes in the situations where that comes up.
