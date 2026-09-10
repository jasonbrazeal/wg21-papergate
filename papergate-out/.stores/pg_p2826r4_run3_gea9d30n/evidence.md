# What the paper offers

## why it matters: not addressed

## who is affected: not addressed

## prior art and alternatives: supported with specifics
> Roughly related were Parametric Expressions [P1221R1], but they didn’t interact with overload sets very well.

## why the standard: supported with specifics
> Expression aliases don’t need cross-TU mangling and have no linkage.

## coordination and interoperability: supported with specifics
> This refactoring also becomes ABI stable, as we basically gain true function aliases.

## why a library will not do: supported with specifics
> The second example results in a separate function for each format string (which is, say, one per log statement). The expression alias provably never instantiates different function bodies for different format strings.

## implementation experience: asserted, with nothing supporting it
> Hana Dusíková for implementing the paper and many discussions, comments, and collaboration.
