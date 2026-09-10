# What the paper offers

## why it matters: supported with specifics
> The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator ([[P2561R2]](https://wg21.link/p2561r2)) into a `do` expression.

## who is affected: not addressed

## prior art and alternatives: supported with specifics
> It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.

## why the standard: supported with specifics
> This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature

## coordination and interoperability: supported with specifics
> The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator ([[P2561R2]]) into a `do` expression.

## why a library will not do: supported with specifics
> It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness.

## implementation experience: asserted, with nothing supporting it
> This is [implemented in clang](https://github.com/brevzin/llvm-project/commit/ca322b0267ba042db01b111e1380bc7352c2a57d) and can be seen on [compiler explorer](https://compiler-explorer.com/z/vMforYcGP).
