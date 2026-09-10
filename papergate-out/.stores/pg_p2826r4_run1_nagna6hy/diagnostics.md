# Diagnostics

Verdict: Strong (9/14)

Criteria addressed: 5 of 7. Points: 9 of 14. Unsupported quotes rejected: 3. Replies missing: 0.

## motivation - grade 0
votes: chunk 1: 0/0/0
quote: (none validated)

## audience - grade 0
votes: chunk 1: 0/0/0
quote: (none validated)

## prior_art - grade 2
votes: chunk 1: 2/2/2
quote: Roughly related were Parametric Expressions [P1221R1], but they didn’t interact with overload sets very well.

## vehicle - grade 2
votes: chunk 1: 2/2/2
quote: The standard library replaced `operator>>(istream&, char*)` with `operator>>(istream&, char(&)[N])` for obvious safety reasons. Adding support for `std::array` or `std::span` to benefit from the same safety would be trivial and avoid new instantiations of the actual I/O logic.

## coordination - grade 2
votes: chunk 1: 2/2/2
quote: This capability would make wrapping C APIs much easier, since we could just make overload sets out of individually-named functions.

## insufficiency - grade 2
votes: chunk 1: 2/2/2
quote: The second example results in a separate function for each format string (which is, say, one per log statement). The expression alias provably never instantiates different function bodies for different format strings.

## implementation - grade 1
votes: chunk 1: 1/1/1
quote: Hana Dusíková for implementing the paper and many discussions, comments, and collaboration.
