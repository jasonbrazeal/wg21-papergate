# Diagnostics

Verdict: Excellent (12/14, close to Strong)

Criteria addressed: 6 of 7. Points: 12 of 14. Unsupported quotes rejected: 6. Replies missing: 0.

## motivation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/2/2  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.

## audience - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: (none validated)

## prior_art - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 2/2/2
quote: The most familiar example might be what Rust’s `?` operator (previously its `try!` macro) desugars as:

## vehicle - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature

## coordination - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/0/2  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator ([[P2561R2]](https://wg21.link/p2561r2)) into a `do` expression.

## insufficiency - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.

## implementation - grade 2
votes: chunk 1: 1/1/1  chunk 2: 0/0/0  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: This is [implemented in clang](https://github.com/brevzin/llvm-project/commit/ca322b0267ba042db01b111e1380bc7352c2a57d) and can be seen on [compiler explorer](https://compiler-explorer.com/z/vMforYcGP).
