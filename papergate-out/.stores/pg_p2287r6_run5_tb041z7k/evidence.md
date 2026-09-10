# What the paper offers

## why it matters: supported with specifics
> However, the two do not mix: a designated initializer can currently only refer to a direct non-static data members.

## who is affected: asserted, with nothing supporting it
> We actually had some code break while upgrading to C++20 that initialized aggregates in this way.

## prior art and alternatives: not addressed
> A previous revision of this paper proposed allowing only `b1` — coming up with a way to name the base class. This revision eschews that approach entirely.

## why the standard: asserted, with nothing supporting it
> Additionally, in many cases, the point of inheritance of aggregates is not because we actually need an “is-a” relationship but rather to compose aggregate members.

## coordination and interoperability: not addressed

## why a library will not do: not addressed

## implementation experience: not addressed
