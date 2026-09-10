# What the paper offers

## why it matters: not addressed

## who is affected: not addressed

## prior art and alternatives: supported with specifics
> Roughly related were Parametric Expressions [P1221R1], but they didn’t interact with overload sets very well.

## why the standard: supported with specifics
> The standard library replaced `operator>>(istream&, char*)` with `operator>>(istream&, char(&)[N])` for obvious safety reasons. Adding support for `std::array` or `std::span` to benefit from the same safety would be trivial and avoid new instantiations of the actual I/O logic.

## coordination and interoperability: supported with specifics
> This capability would make wrapping C APIs much easier, since we could just make overload sets out of individually-named functions.

## why a library will not do: supported with specifics
> The second example results in a separate function for each format string (which is, say, one per log statement). The expression alias provably never instantiates different function bodies for different format strings.

## implementation experience: asserted, with nothing supporting it
> Hana Dusíková for implementing the paper and many discussions, comments, and collaboration.
