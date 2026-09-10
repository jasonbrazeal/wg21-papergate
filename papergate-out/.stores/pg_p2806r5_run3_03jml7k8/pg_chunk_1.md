---
title: "do expressions"
document: P2806R5
date: 2026-08-12
audience: EWG
reply-to:
  - "Bruno Cardoso Lopes <bruno.cardoso@gmail.com>"
  - "Zach Laine <whatwasthataddress@gmail.com>"
  - "Michael Park <mcypark@gmail.com>"
  - "Barry Revzin <barry.revzin@gmail.com>"
---


## 1 Revision History

Since [[P2806R4]](https://wg21.link/p2806r4), rewrote prose, and removed the implicit last value option introduced in the previous revision.

Since [[P2806R3]](https://wg21.link/p2806r3), implementation, wording, introducing implicit last value, and adding an optional init-hoist to `do` expressions to address lifetime issues.

Since [[P2806R2]](https://wg21.link/p2806r2), wording and referencing a longer discussion on divergence in [[P3549R0] (Diverging expressions)](https://wg21.link/p3549r0).

Since [[P2806R1]](https://wg21.link/p2806r1), switched syntax from `do return` to `do_return` to avoid ambiguity. Added section on lifetime.

Since [[P2806R0]](https://wg21.link/p2806r0), some more discussion about implicit last value vs explicit return, reflection, and a grammar fix to the still-incomplete wording.


## 2 Abstract

We propose the addition of a new kind of expression, called a `do` expression. In its simplest form:

> ```cpp
> int x = do { do_return 42; };
> ```

A `do` expression consists of a sequence of statements, but is still, itself, an expression (and thus has a value and a type). It is similar to an immediately invoked lambda with a capture of `[&]`, except using the `do_return` keyword to produce a value instead of `return`.


## 3 Introduction

C++ is a language built on statements. `if` is not an expression, loops aren’t expressions, statements aren’t expressions (except maybe in the specific case of `*expression*;`).

However, sometimes a single expression is insufficient — we want an expression, but also want to execute multiple statements. The current best C++ answer to that situation is an immediately invoked lambda. Immediately invoked lambdas are decent enough solutions for that problem, but they are not perfect. Two problems they have are:

- it is not obvious at the beginning of a lambda that it will actually be immediately invoked — you see `[&]{` and then the trailing `}()` part is arbitrarily far in the future.
- the lambda machinery is surprisingly expensive to compile, and in this particular context the compiler has to do work that we know we don’t even need (because we’re immediately invoking it).

Nevertheless, they are fine. If all we were proposing were a slightly more expressive/cheaper immediately invoked lambda, that’d be a mild improvement at best:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Immediately Invoked Lambda</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Do Expression</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto x = [&amp;]{
    S1;
    S2;
    return E;
}();</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto x = do {
    S1;
    S2;
    do_return E;
};</code></pre></td>
</tr>
</table>

The *bigger* problem with immediately invoked lambdas as a solution to the “expression but with statements” problem is dealing with control flow. It becomes impossible to `break` or `continue` out of loop, and attempting to `return` from the enclosing function or `co_await`, `co_yield`, or `co_return` from the enclosing coroutine becomes an exercise in cleverness. We need to encode in the result of that lambda both the actual value we wanted to produce and also any control flow we wanted to have, and then act on it.

This problem surfaces especially brightly in the context of [[P2688R4] (Pattern Matching: `match` Expression)](https://wg21.link/P2688R4), where the current design is built upon a sequence of:

> ```cpp
> pattern => expression;
> ```

It is idiomatic in languages that have pattern matching to allow control flow out of those expressions. We want to be able to have a pattern match `return` out of a function while another does not, or `continue` to the next iteration of a loop.

The most familiar example might be what Rust’s `?` operator (previously its `try!` macro) desugars as:

> ```rust
> let x = match result {
>     Ok(val) => val,
>     Err(err) => return Err(err),
> };
> ```

This is functionality that immediately invoked lambda expressions *cannot* provide, but something we want to add a new kind of expression to support — in a way that is orthogonal to the pattern matching feature (which otherwise previously attempted to solve this problem with a bespoke, pattern-matching-specific sort of block expression).
