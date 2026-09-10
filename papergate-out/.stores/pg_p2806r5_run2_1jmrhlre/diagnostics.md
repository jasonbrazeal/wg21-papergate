# Diagnostics

Verdict: Excellent (12/14, close to Strong)

Criteria addressed: 6 of 7. Points: 12 of 14. Unsupported quotes rejected: 9. Replies missing: 0.

## motivation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/0/1  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: The current best C++ answer to that situation is an immediately invoked lambda. Immediately invoked lambdas are decent enough solutions for that problem, but they are not perfect.

## audience - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: (none validated)

## prior_art - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/0/2  chunk 3: 0/0/0  chunk 4: 2/2/2
quote: [P2552R2] Timur Doumler. 2023-05-19. On the ignorability of standard attributes. [P2561R2] Barry Revzin. 2023-05-18. A control flow operator. [P2688R4] Michael Park. 2024-12-17. Pattern Matching: match Expression. [P2806R0] Barry Revzin, Bruno Cardoso Lopez, Zach Laine, Michael Park. 2023-02-14. do expressions.

## vehicle - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature

## coordination - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of: `pattern => expression;`

## insufficiency - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/0/1  chunk 3: 0/2/2  chunk 4: 0/0/0
quote: It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.

## implementation - grade 2
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 2/2/2  chunk 4: 0/0/0
quote: This is [implemented in clang](https://github.com/brevzin/llvm-project/commit/ca322b0267ba042db01b111e1380bc7352c2a57d) and can be seen on [compiler explorer](https://compiler-explorer.com/z/vMforYcGP).
