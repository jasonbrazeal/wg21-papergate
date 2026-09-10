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

## 4 Proposal Details

There are a lot of interesting rules that we need to discuss about a `do` expression behaves.

### 4.1 Scope

A `do` expression does introduce a new block scope - as the braces might suggest. But it does *not* introduce a new function scope. There is no new stack frame. Which is what allows external control flow to work (see below).

### 4.2 `do_return` statement

The new `do_return` statement has the same form as the `return` statement we have today: `do_return *expr-or-braced-init-list*<sub>opt</sub>;`. Its behavior corresponds closely to that of `return`, in unsurprising ways - `do_return` yields from a `do` expression in the same way that `return` returns from a function.

While `do_return *value*;` and `return *value*;` do look quite close together and mean fairly different things, the leading `do` we think should be sufficiently clear, and we think it is a good spelling for this statement.

Other alternative spellings we’ve considered:

- `do return` (in the previous revision of this paper, which has an ambiguity with `do ... while` loops)
- `do_yield` (presented to EWG in Issaquah as the initial pre-publication draft of this proposal)
- `do yield`
- `do break` (similarly to `return`, we are breaking out of this expression, but is less likely to conflict since `break` is less likely to be used than `return` and also the corresponding `break *value*;` is invalid today)
- `=>` (or some other arrow, like `<-` or `<=`)

### 4.3 Type and Value Category

The expression `do { do_return 42; }` is a prvalue of type `int`. We deduce the type from all of the (non-discarded) `do_return` statements, in the same way that `auto` return type deduction works for functions and lambdas.

An explicit `*trailing-return-type*` can be provided to override this:

> ```cpp
> do -> long { do_return 42; }
> ```

If no (non-discarded) `do_return` statement appears in the body of the `do` expression, or every (non-discarded) `do_return` statement is of the form `do_return;`, then the expression is a prvalue of type `void`.

Falling off the end of a `do` expression behaves like an implicit `do_return;` - if this is incompatible with the type of the `do` expression, the expression is ill-formed. This is the one key difference with functions: this case is not undefined behavior. This will be discussed in more detail later.

This makes the pattern matching cases [[P2688R4]](https://wg21.link/P2688R4) work pretty naturally:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">P2688R4</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Proposed</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>x match {
    0 =&gt; { cout &lt;&lt; &quot;got zero&quot;; };
    1 =&gt; { cout &lt;&lt; &quot;got one&quot;; };
    _ =&gt; { cout &lt;&lt; &quot;don&#x27;t care&quot;; };
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>x match {
    0 =&gt; do { cout &lt;&lt; &quot;got zero&quot;; };
    1 =&gt; do { cout &lt;&lt; &quot;got one&quot;; };
    _ =&gt; do { cout &lt;&lt; &quot;don&#x27;t care&quot;; };
}</code></pre></td>
</tr>
</table>

Here, the whole `match` expression has type `void` because each arm has type `void` because none of the `do` expressions have a `do_return` statement.

Yes, this requires an extra `do` for each arm, but it means we have a language that’s much easier to explain because it’s consistent - `do { cout << "don't care"; }` is a `void` expression in *any* context. We don’t have a `*compound-statement*` that happens to be a `void` expression just in this one spot.

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">P2688R4</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Proposed</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto f(int i) {
    return i match -&gt; std::pair&lt;int, int&gt; {
        0 =&gt; {1, 2};          // ill-formed
        _ =&gt; std::pair{3, 4}; // ok
    }
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto f(int i) {
    return i match -&gt; std::pair&lt;int, int&gt; {
        0 =&gt; {1, 2};          // ok
        _ =&gt; std::pair{3, 4}; // ok
    }
}</code></pre></td>
</tr>
</table>

Here, the existing pattern matching cannot support a `*braced-init-list*` because `{` is used for the special `void`-statement-case. But if we had `do` expressions, the grammar of pattern matching can use `*expr-or-braced-init-list*` in the same way that we already do in many other places in the C++ grammar. This example just works.

### 4.4 Copy Elision

All the rules for initializing from `do` expression, and the way the expression that appears in a `do_return` statement is treated, are the same as what the rules are for `return`.

Implicit move applies, for variables declared within the body of the `do` expression. In the following example, `r` is an unparenthesized `*id-expression*` that names an automatic storage variable declared within the statement, so it’s implicitly moved:

```cpp
std::string s = do {
    std::string r = "hello";
    r += "world";
    do_return r;
};
```

Note that automatic storage variables declared within the function that the `do` expression appears, but not declared within the statement-expression itself, are *not* implicitly moved (since they can be used later).

### 4.5 Control Flow

In a regular function, there are four ways to escape the function scope:

1. a `return` statement
2. `throw`ing an exception
3. invoking a `[[noreturn]]` function, `std::abort()` and `std::unreachable()`
4. falling off the end of the function (undefined behavior if the return type is not `void`)

The same is true for coroutines, except substituting `return` for `co_return` (and likewise falling off the end is undefined behavior if there is no `return_void()` function on the promise type).

For a `do` expression, we have two different directions where we can escape (in a non-exception, non-`[[noreturn]]` case): we either yield an expression, or we escape the *outer* scope. That is, we can also:

1. `return` from the enclosing function (or `co_return` from the enclosing coroutine)
2. `break` or `continue` from the innermost enclosing loop (if any, ill-formed otherwise)

Additionally, for point (4) while we could simply (for consistency) propagate the same rules for falling-off-the-end as functions, then lambdas (C++11), then coroutines (C++20), we would like to consider not introducing another case for undefined behavior here. We would prefer that if an implementation cannot prove that control doesn’t fall off the end of a function, that the user simply provide more information themselves (e.g. in the form of a call to `std::unreachable()`, which worst-case just adds clarity to the situation explicitly).

That is, the rule we propose is that the implementation form a control flow graph of the `do` expression and consider each one of the six escaping kinds described above. All (non-discarded) `do_return` statements (including the implicit `do_return;` introduced by falling off the end, if the implementation cannot prove that it does not happen) need to either have the same type (if no `*trailing-return-type*`) or be compatible with the provided return type (if provided). Anything else is ill-formed.

Let’s go through some examples.

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Example</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Discussion</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto a = do {
    if (cond) {
        do_return 1;
    } else {
        do_return 2;
    }
};</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: All yielding control paths have the same type. There’s no falling off the end.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto b = do {
    if (cond) {
        do_return 1;
    } else {
        do_return 2.0;
    }
};</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Ill-formed: The yielding control paths have different types and there is no provided <code class="sourceCode cpp"><em>trailing-return-type</em></code>. This would be okay if it were <code class="sourceCode cpp"><span class="cf">do</span> <span class="op">-&gt;</span> <span class="dt">int</span> <span class="op">{</span> <span class="op">...</span> <span class="op">}</span></code> or <code class="sourceCode cpp"><span class="cf">do</span> <span class="op">-&gt;</span> <span class="dt">double</span> <span class="op">{</span> <span class="op">...</span> <span class="op">}</span></code> or <code class="sourceCode cpp"><span class="cf">do</span> <span class="op">-&gt;</span> <span class="dt">float</span> <span class="op">{</span> <span class="op">...</span> <span class="op">}</span></code>, etc.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto c = do {
    if (cond) {
        do_return 1;
    }
&#10;
    do_return 2;
};</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: Similar to <code class="sourceCode cpp">a</code>, all yielding control paths yield the same type. There is no falling off the end here, it is not important that a yielding <code class="sourceCode cpp"><span class="cf">if</span></code> has an <code class="sourceCode cpp"><span class="cf">else</span></code>.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto d = do {
    if (cond) {
        do_return 1;
    }
};</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Ill-formed: There are two yielding control paths here: the <code class="sourceCode cpp"><span class="cf">do_return</span> <span class="dv">1</span><span class="op">;</span></code> and the implicit <code class="sourceCode cpp"><span class="cf">do_return</span><span class="op">;</span></code> from falling off the end, those types are incompatible. The equivalent in functions and coroutines would be undefined behavior if <code class="sourceCode cpp"><em>cond</em></code> is <code class="sourceCode cpp"><span class="kw">false</span></code>.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>int e = (do {
    if (cond) {
        do_return;
    }
}, 1);</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: As above, there are two yielding control paths here, but both the explicit and the implicit ones are <code class="sourceCode cpp"><span class="cf">do_return</span><span class="op">;</span></code> which are compatible.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>int f = do {
    if (cond) {
        do_return 1;
    }
&#10;
    throw 2;
};</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: We no longer fall off the end here, since we always escape. There is only one yielding path.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>int outer() {
    int g = do {
        if (cond) {
            do_return 1;
        }
&#10;
        return 3;
    };
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: Similar to the above, it’s just that we’re escaping by returning from the outer function instead of throwing. Still not falling off the end.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>int h = do {
    if (cond) {
        do_return 1;
    }
&#10;
    std::abort();
};</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: <code class="sourceCode cpp">std<span class="op">::</span>abort<span class="op">()</span></code> means that we cannot fall off the end, see discussion on <code class="sourceCode cpp"><span class="op">[[</span><span class="at">noreturn</span><span class="op">]]</span></code> below.</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>enum Color {
    Red,
    Green,
    Blue
};
&#10;
void func(Color c) {
    std::string_view name = do {
        switch (c) {
        case Red:   do_return &quot;Red&quot;sv;
        case Green: do_return &quot;Green&quot;sv;
        case Blue:  do_return &quot;Blue&quot;sv;
        }
    };
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Ill-formed: This is probably the most interesting case when it comes to falling off the end. Here, the user knows that <code class="sourceCode cpp">c</code> only has three values, but the implementation does not, so it could still fall off the end. gcc does warn on the equivalent function form of this, clang does not. The typical solution here might be to add <code class="sourceCode cpp"><span class="fu">__builtin_unreachable</span><span class="op">()</span></code>, now <code class="sourceCode cpp">std<span class="op">::</span>unreachable<span class="op">()</span></code>, to the end of the function, but for this to work we have to discuss <code class="sourceCode cpp"><span class="op">[[</span><span class="at">noreturn</span><span class="op">]]</span></code> below. Barring that, the user would have to add either some default value or some other kind of control flow (like an exception, etc).</td>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>void func() {
    for (;;) {
        int j = do {
            if (cond) {
                break;
            }
&#10;
            for (something) {
                if (cond) {
                    do_return 1;
                }
            }
&#10;
            do_return 2;
        };
    }
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">OK: The first break escapes the do expression and breaks from the outer loop. Otherwise, we have two yielding statements which both yield int. If the do_return 2; statement did not exist, this would be ill-formed unless the compiler could prove that the loop itself did not terminate. If the loop were <code class="sourceCode cpp"><span class="cf">for</span> <span class="op">(;;)</span></code>, then the lack of <code class="sourceCode cpp"><span class="cf">do_return</span> <span class="dv">2</span><span class="op">;</span></code> would be fine - but anything more complicated than that would require some kind of final yield (or <code class="sourceCode cpp"><span class="cf">throw</span></code>, etc.)</td>
</tr>
</table>

To reiterate: the implementation produces a control flow graph of the `do` expression and considers all yielding statements (*including* the implicit `do_return;` on falling off the end, if the implementation considers that to be a possible path) in order to determine correctness of the statement-expression. The kinds of control flow that escape the statement entirely (exceptions, `return`, `break`, `continue`, `co_return`) do not need to be considered for purposes of consistency of yields (since they do not yield values).

#### 4.5.1 `noreturn` functions

The language currently has several kinds of escaping control flow that it recognizes. As mentioned, exceptions, `return`, `continue`, `break`, and `co_return`. And, allegedly, `goto`.

But there’s one kind of escaping control flow that it *does not* currently recognize: functions marked `[[noreturn]]`. A call to `std::abort()` or `std::terminate()` or `std::unreachable()` escapes control flow, for sure, but today this is just an attribute:

> ```cpp
> int i = do {
>     if (cond) {
>         do_return 5;
>     }
> 
>     std::abort();
> 
>     // we know control flow never gets here, so we should not need to
>     // insert an implicit "do_return;"
> };
> ```

Pattern Matching has this same problem - it needs to support arms that might `std::terminate()` or are `std::unreachable()`, so that proposal currently is introducing a dedicated syntax to mark an arm as non-returning: `!{ std::terminate(); }`. Which is… less than ideal.

However, the rule in 9.13.10 Noreturn attribute [[dcl.attr.noreturn]/2](https://eel.is/c++draft/dcl.attr.noreturn#2) is:

> 2 If a function `f` is called where `f` was previously declared with the `noreturn` attribute and `f` eventually returns, the behavior is undefined.

That is normative wording which we can rely on. The above `do` expression can only fall off the end if `std::abort` returns, which is *already* undefined behavior. We can avoid introducing any new undefined behavior ourselves as part of this feature.

That is: invoking a function marked `[[noreturn]]` can be considered an escaping control flow in exactly the same way that `return`, `break`, `throw`, etc., are already.

Note that this violates the so-called Second Ignorability Rule suggested in [[P2552R2] (On the ignorability of standard attributes)](https://wg21.link/p2552r2), which is a great reason to ignore that rule.

#### 4.5.2 Always-escaping expressions

Consider:

> ```cpp
> int i = do -> int {
>     throw 42;
> };
> ```

This is weird, but might end up as a result of template instantiation where maybe other control paths (guarded with an `if constexpr`) actually had `do_return` statements in them. So it needs to be allowed.

It does lead to an interesting question: what is `decltype(do { return; })`? We already define `decltype(throw 42)` to be `void`, so would this also be `void`? It’s kind of an odd choice, and it would be nice if we had a specific type for an escaping expression. While we could come up with the right language facility to allow the conditional operator (`?:`) and pattern matching to work correctly by ignoring arms that are always-escaping, user-defined code would have no way of differentiating between a real void expression (`std::print("Hello {}!", "EWG")` is actually an expression of type `void`) and an artificial one (`std::abort()` is not really the same thing).

We could instead introduce a new type, `std::noreturn_t` (as an easier-to-type spelling of `⊥`), change `decltype(throw e)` to be `std::noreturn_t` (since nobody actually writes this - code search results are exclusively in compiler test suites) and treat the return types of `[[noreturn]]` functions as `std::noreturn_t`. Then the type system gains understanding of always-escaping expressions/statements and the rules for pattern matching, the conditional operator, `do` expressions, and arbitrary user-defined libraries just fall out.

See reflector discussion [here](https://lists.isocpp.org/ext/2023/05/21202.php) and more thorough discussion in [[P3549R0] (Diverging expressions)](https://wg21.link/p3549r0).

#### 4.5.3 `goto`

Using `goto` in a `do` expression has some unique problems.

Jumping *within* a `do` expression should follow whatever restrictions we already have (see 8.10 Declaration statement [[stmt.dcl]](https://eel.is/c++draft/stmt.dcl)). Jumping *into* a `do` expression should be completely disallowed (we would call the `*statement*` of a `do` expression a control-flow limited statement).

Jumping *out* of a `do` expression is potentially useful though, in the same way that `break`, `continue`, and `return` are:

> ```cpp
>     for (loop1) {
>         for (loop2) {
>             int i = do {
>                 if (cond) {
>                     goto done;
>                 }
> 
>                 do_return value;
>             };
>         }
>     }
> done:
> ```

Breaking out of multiple loops is one of the uses of `goto` that has no real substitute today. The above example should be fine. But referring to any label that is in scope of the variable we’re initializing needs to be disallowed - since we wouldn’t have actually initialized the variable. We need to ensure that the 8.10 Declaration statement [[stmt.dcl]](https://eel.is/c++draft/stmt.dcl) rule is extended to cover this case.

Also, while computed goto is not a standard C++ feature, it would be nice to disallow this example, courtesy of (of course) JF Bastien (in this case, we are referring to a label that is within `v`’s scope. We’re not jumping to it directly, but the ability to jump to it indirectly is still problematic):

> ```cpp
> #include <stdio.h>
> 
> struct label {
>     static inline void* e;
>     int v;
> 
>     label()
>     try
>         : v(({
>             fprintf(stderr, "oh\n");
>             e = &&awesome;
>             throw 1;
>             42;
>         }))
>     {
>         fprintf(stderr, "no\n");
>         awesome:
>         fprintf(stderr, "you\n");
>     } catch(...) {
>         fprintf(stderr, "don't\n");
>         goto *e;
>     }
> };
> 
> int main() {
>     label l;
> }
> ```

### 4.6 Lifetime

One important question is: when are local variables declared within a `do` expression destroyed?

Let’s start with this example:

> ```cpp
> int i = do {
>         std::lock_guard _(mtx);
>         do_return get(0);
>     } + do {
>         std::lock_guard _(mtx);
>         do_return get(1);
>     };
> ```

Each `do` expression is locking the same mutex, `mtx`. We believe that it is the overwhelming presumption of C++ that both `lock_guard`s will be destroyed at their nearest `}` (i.e. this will not deadlock). There really is no other reasonable alternative.

However, consider this example, courtesy of Lauri Vasama in the context of discussing lifetime questions in control flow operator ([[P2561R2]](https://wg21.link/p2561r2)). Consider this set of functions, where `find_interesting` returns some `span` into the given `vector` (or returns an `unexpected`):

> ```cpp
> auto get_data() -> std::vector<int>;
> auto find_interesting(std::vector<int> const&) -> std::expected<std::span<int const>, std::string>;
> auto best_of(std::span<int const>) -> int;
> ```

With `do` expressions, it would be tempting to implement a `TRY` macro similar to Rust’s `try!` macro. In this case, we could try to do it this way (note that in this case decaying is irrelevant, so we just return everything by value):

> ```cpp
> #define TRY(expr) do {                          \
>     auto __r = expr;                            \
>     if (not __r) {                              \
>         return std::unexpected(__r.error());    \
>     }                                           \
>     do_return *__r;                             \
> }
> 
> auto do_something() -> std::expected<int, std::string> {
>     int value = best_of(TRY(find_interesting(get_data())));
>     return value;
> }
> ```

This *looks* reasonable. Sure, `get_data()` is a temporary `vector`, but it *looks* like it persists until the `;`. But that’s not what would actually happen. If we expand the macro, and add the explicit return type for clarity, this evaluates as:

> ```cpp
> auto do_something() -> std::expected<int, std::string> {
>     int value = best_of(do -> std::span<int const> {
>         auto __r = find_interesting(get_data());
>         //                                     ^
>         //                              vector destroyed here
>         if (not __r) {
>             return std::unexpected(__r.error());
>         }
>         do_return *__r;
>     });
>     return value;
> }
> ```

The temporary `std::vector<int>` doesn’t persist through the whole `do` expression, it gets destroyed too soon — so our `__r` would be holding a dangling `span` (in the non-error case). That’s… bad.

So we need some way to “persist” that temporary through the end of the outer expression. And it definitely cannot happen automatically, as just pointed out, so it has to be explicit in some way. We can think of three approaches to doing this:

1. We can annotate the local variable `__r` somehow, such that any temporaries in its initializer persist through the outer full-expression.
2. We can annotate the `do` expression with some kind of anti-capture list, as in `do [__r=e] { ... }`
3. We can allow the `do` expression itself to carry a sequence of init-statements expressly for this purpose.

Having an annotation on a variable retroactively change its lifetime just doesn’t seem like a great idea. For the other two, the comparison looks like this:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Init-Hoist</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Init-Statement</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>do [__r=expr] -&gt; decltype(auto) {
    if (not __r) {
        return std::unexpected(__r.error());
    }
    do_return *FWD(__r);
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>do (auto&amp;&amp; __r = expr;) -&gt; decltype(auto) {
    if (not __r) {
        return std::unexpected(__r.error());
    }
    do_return *FWD(__r);
}</code></pre></td>
</tr>
</table>

Both syntaxes would provide declarations whose lifetime extends to the end of the full-expression containing the `do` expression. Any temporaries in those declarations’ initializers are likewise extended to that full-expression. Which means that in this case, the temporary `get_data()` will not be inside of a new full-expression (the body of the `do` expression), it will be in the place where it needs to be. We think this is the right approach to addressing lifetime issues, in a way that likely scales better.

Between these, we prefer the init-hoist approach (so named because it’s kind of the opposite of an init-capture), since only one form of *init-statement* even makes sense here. The downside is that we would need `auto&&` semantics here rather than `auto` semantics which lambda init-capture has. It’s inconsistent, but with very strong motivation for the difference — since lambdas can actually escape but `do` expressions cannot.

The proposed form [works](https://compiler-explorer.com/z/vMforYcGP).

#### 4.6.1 What about Pattern Matching?

The primary motivation for having an init-hoist is largely around being able to define macros for expressions in ways that actually work properly and to be able to desugar the control flow operator ([[P2561R2]](https://wg21.link/p2561r2)) into a `do` expression.

But, interestingly enough, pattern matching (a future revision) offers a [different way](https://godbolt.org/z/fTxWc1ssb) to solve both problems that wouldn’t need such a feature:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Init-Hoist</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Pattern Matching</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>do [__r=expr] -&gt; decltype(auto) {
    if (not __r) {
        return std::unexpected(__r.error());
    }
    do_return *FWD(__r);
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>expr match -&gt; decltype(auto) {
    case auto&amp;&amp; __r =&gt; do -&gt; decltype(auto) {
        if (not __r) {
            return std::unexpected(__r.error());
        }
        do_return *FWD(__r);
    }
}</code></pre></td>
</tr>
</table>

On the right, `expr` is obviously evaluated outside of the `do` expression, and so any temporaries within it obviously last until the end of the full-expression. We don’t need anything special to make that work, it just falls out.

The question is: do we need to add an init-hoist feature for `do` expressions (a feature in no small part motivated by pattern matching) if pattern matching could solve it for us?

We think it’s probably a good hedge to do it anyway. We’ll probably ship `do` expressions first, so the pattern matching paper can simply remove it. Hopefully we just get both in C++29.

#### 4.6.2 Conditional Lifetime Extension

An interesting sub-question on lifetimes is what does this do:

> ```cpp
> auto prvalue() -> T;
> 
> auto f() -> void {
>     // lifetime extension, reference bound to temporary
>     T const& r1 = prvalue();
> 
>     // dangling
>     T const& r2 = []() -> T const& { return prvalue(); }();
> 
>     // lifetime extension??
>     T const& r3 = do -> T const& { do_return prvalue(); };
> }
> ```

`r1` is our familiar lifetime extension case - a reference is bound to a temporary. `r2` is definitely dangling. The temporary is destroyed and definitely does not last as long as `r2`. But what about `r3`, is it more like `r1` or `r2`?

In this case, we see the entire `do` expression - so unlike the general callable case, it may actually be possible for lifetime extension to work here.

But as we’re thinking about it, let’s make the example slightly more complicated:

> ```cpp
> auto lvalue() -> T const&;
> auto prvalue() -> T;
> 
> auto g(bool c) -> void {
>     T const& r4 = do -> T const& {
>         if (c) {
>             do_return lvalue();
>         } else {
>             do_return prvalue();
>         }
>     };
> 
>     T const& r5 = do -> T const& {
>         if (c) {
>             do_return lvalue();
>         } else {
>             T x = prvalue();
>             do_return x;
>         }
>     };
> }
> ```

If `r3` doesn’t dangle (and we do lifetime extension), does `r4`? Well, presumably. But here we have a form of runtime-conditional lifetime extension. That’s still seemingly doable - we would effectively have an `optional<T> __storage` that is declared before `r4` and then `r4` is either a reference into that or whatever we got from `lvalue()`.

But even if we made `r4` work, `r5` now almost certainly cannot - now we’re definitely not binding a temporary to a reference, this is quite adrift from our usual rules.

Which makes us wonder if there’s really any value in being adventurous here - and instead probably consider that there is no lifetime extension in any of these cases, not in `r3`, not in `r4`, and definitely not in `r5`.

### 4.7 SFINAE-Friendliness

The only part of a `do` expression that is in the immediate context of a template substitution is the trailing-return-type (if any). Any alternative choice would require SFINAE on statements, which the language does not currently support and we are not trying to tackle in this paper.

This is consistent with lambdas, where the lambda body is not in the immediate context.

### 4.8 Grammar Disambiguation

We have to disambiguate between a `do` expression and a `do`-`while` loop.

In an expression-only context, the latter isn’t possible, so we’re fine there.

In a statement context, a `do` expression is completely pointless - you can just write statements. So we disambiguate in favor of the `do`-`while` loop. If somebody really, for some reason, wants to write a `do` expression statement, they can parenthesize it: `(do { do_return 42; });`. A statement that begins with a `(` has to then be an expression, so we’re now in an expression-only context.

A previous iteration of the paper used `do return` (with a space), which would lead to an ambiguity in the following in the context of a `do` expression:

> ```cpp
> do return value; while (cond);
> ```

This could have been parsed as a `do return` statement followed by an infinite loop (that would never be executed because we’ve already returned out of the expression) or as a `do`-`while` loop containing a single, unbraced, return statement. If we use the `do_return` spelling, there’s no such ambiguity, since the above can only be a `do ... while` loop.

Also because we would unconditionally parse a statement as beginning with `do` as a `do`-`while` loop, code like this would not work:

> ```cpp
> do { do_return X{}; }.foo();
> ```

Such code would also have to be parenthesized to disambiguate, which doesn’t seem like a huge burden on the user.

### 4.9 Implicit Last Value

Let’s take the example motivating case from [[P2561R2] (A control flow operator)](https://wg21.link/p2561r2) and compare implicit last expression to explicit return:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Implicit Last Value</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Explicit Return</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto foo(int i) -&gt; std::expected&lt;int, E&gt;
&#10;
auto bar(int i) -&gt; std::expected&lt;int, E&gt; {
    int j = do {
        auto r = foo(i);
        if (not r) {
            return std::unexpected(r.error());
        }
        *r // &lt;== NB: no semicolon
    };
&#10;
    return j * j;
}</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>auto foo(int i) -&gt; std::expected&lt;int, E&gt;
&#10;
auto bar(int i) -&gt; std::expected&lt;int, E&gt; {
    int j = do {
        auto r = foo(i);
        if (not r) {
            return std::unexpected(r.error());
        }
        do_return *r;
    };
&#10;
    return j * j;
}</code></pre></td>
</tr>
</table>

In the simple cases, implicit last value (on the left) will be shorter than an explicit return (on the right). But implicit last value is more limited. We cannot do early return (by design), which means that a `do` expression would not be able to return from a loop either. We would have to extend the language to support `if` expressions, so that at the very least the first example above could be made easier - which would add more complexity to the design.

Which is to say — the `do_return` statement is still a valuable and necessary addition, given that we do not have `if` or loop expressions, and we are unlikely to add them.

However, for many common uses of `do` expressions, we don’t actually need early return, so paying the syntactic cost might seem unnecessary. Which is why [[P2806R4]](https://wg21.link/p2806r4) proposed both `do_return` and implicit last value.

On the other hand, as you can tell from the above example, `do` expressions are useful precisely when you want to have at least one statement. Otherwise, you’d just write `E` — nobody is writing `do { E }`. And once you have at least one statement, you’re likely formatting your `do` expression across multiple lines. Once you do that though, is there really any syntactic/visual noise benefit of being able to avoid the `do_return`? It’s already on its own line. Making that line shorter doesn’t seem like it has any value at all. Regardless of any other issues with this idea (such as inconsistency with lambdas, wherein being able to omit `return` actually does seem quite valuable). As such, this proposal now proposes that the only way to produce a value from a `do` expression is through the `do_return` statement.

Note that Rust also allows both (you can label a block expression and then `break` out of it).

### 4.10 Prior Art

GCC has had an extension called [statement-expressions](https://gcc.gnu.org/onlinedocs/gcc/Statement-Exprs.html) for decades, which look very similar to what we’re proposing here:

<!-- tomd:mixed-table -->
<table border="1" rules="all" cellpadding="6" cellspacing="0" style="border-collapse: collapse; width: 100%;">
<tr>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">gcc</th>
<th style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;">Proposed</th>
</tr>
<tr>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>({
    int y = foo();
    int z;
    if (y &gt; 0) z = y;
    else z = -y;
    z;
})</code></pre></td>
<td style="border: 1px solid #999; padding: 6px 10px; vertical-align: top; width: 50%;"><pre style="margin: 0;"><code>do {
    int y = foo();
    if (y &gt; 0) {
        do_return y;
    } else {
        do_return -y;
    }
}</code></pre></td>
</tr>
</table>

The reason we’re not simply proposing to standardize the existing extension is that there are two features we see that are lacking in it that are not easy to add:

1. The ability to specify a return type, which is critical for allowing statement-expressions to be lvalues.
2. The ability to support yielding out of different branches of `if`, due to the implicit nature of the yield.

For (1), there is simply no obvious place to put the `*trailing-return-type*`. For (2), you can’t turn `if`s into expressions in any meaningful way. It is fairly straightforward to answer both questions for our proposed form.

Moreover, as discussed in the implicit last value section, there simply isn’t much value to supporting implicit last value. The specific form of the statement expression extension is particularly problematic as something like `do { std::cout << "hi"; }` would become ill-formed due to trying to copy the `ostream`.

We’re just generalizing to make the feature more flexible.

### 4.11 What About Reflection?

A question that often comes up, for any language feature: if we had reflection and, in particular, code injection: would we need this facility?

The answer is not only yes, but reflection is a good motivating use-case for this facility. Because the language does not have any kind of block expression today, adding support for one would increase the amount of ways that code injection could work.

One example might be, again, the control flow operator proposal in [[P2561R2] (A control flow operator)](https://wg21.link/p2561r2). If reflection allows me to write a hygienic macro that does code injection, perhaps we could write a library such that `try_(E)` would inject an expression that would evaluate in the way that that paper proposes. But in order to do such a thing, we would need to be able to have a block expression to inject. This paper provides such a block expression.

### 4.12 Where can `do` expressions appear

gcc’s statement-expressions are not usable in all expression contexts. Trying to use them at namespace-scope, or in a default member initializer, etc, fails:

> ```cpp
> int i = ({      // error: statement-expressions are not allowed outside functions
>     int j = 2;  //        nor in template-argument lists
>     j;
> });
> ```

In such contexts, there is a much smaller difference between a statement-expression and an immediately invoked lambda since you don’t have any other interesting control flow that you can do - the expression either yields a value or the program terminates.

But if we’re going to add a new language feature, it seems better to allow it to be used in all expression contexts - we would just have to say what happens in this case. Especially since if we’re adding a feature to subsume immediately invoked lambdas, it would be preferable to subsume *all* immediately invoked lambdas, not just some or most.

We can think of a `do` expression as simply behaving like an immediately invoked lambda in such contexts. Not in the sense of allowing `return` statements (there’s still no enclosing function to return out of), but the sense that any local variables declared would exist in a function stack. But this is probably more of a compiler implementation detail rather than a language design detail.

In short: `do` expressions should be usable in any expression context.

### 4.13 Implementation Experience

This is [implemented in clang](https://github.com/brevzin/llvm-project/commit/ca322b0267ba042db01b111e1380bc7352c2a57d) and can be seen on [compiler explorer](https://compiler-explorer.com/z/vMforYcGP). This example shows the combination of a `do` expression with an init-hoist and `TRY` macro with the correct lifetime semantics.

[Here](https://compiler-explorer.com/z/4nnbGGxKn) is a more involved example showing a more complicated `TRY` macro illustrating that clang can still warn on dangling references in the right places.

## 5 Wording

### 5.1 Lex / Intro

Add the keyword `do_return` to the table of keywords in 5.12 Keywords [[lex.key]](https://eel.is/c++draft/lex.key):

> ```cpp
>   constinit
>   const_cast
>   continue
>   contract_assert
>   co_await
>   co_return
>   co_yield
>   decltype
>   default
>   delete
>   do
> + do_return
>   double
>   dynamic_cast
>   else
>   enum
>   explicit
>   export
> ```

Add a note to 6.10.1 Sequential execution [[intro.execution]](https://eel.is/c++draft/intro.execution):

> :::wording
> 
> 5 A *full-expression* is
> 
> - (5.1) an unevaluated operand ([[expr.context]](https://eel.is/c++draft/expr.context)),
> - (5.2) a `*constant-expression*` ([[expr.const]](https://eel.is/c++draft/expr.const)),
> - (5.3) an immediate invocation ([[expr.const]](https://eel.is/c++draft/expr.const)),
> - (5.4) an `*init-declarator*` ([[dcl.decl]](https://eel.is/c++draft/dcl.decl)) (including such introduced by a structured binding ([[dcl.struct.bind]](https://eel.is/c++draft/dcl.struct.bind))) or a `*mem-initializer*` ([[class.base.init]](https://eel.is/c++draft/class.base.init)), including the constituent expressions of the initializer,
> - (5.5) an invocation of a destructor generated at the end of the lifetime of an object other than a temporary object ([[class.temporary]](https://eel.is/c++draft/class.temporary)) whose lifetime has not been extended,
> - (5.6) the predicate of a contract assertion ([[basic.contract]](https://eel.is/c++draft/basic.contract)), or
> - (5.7) an expression that is not a subexpression of another expression and that is not otherwise part of a full-expression.
> 
> […]
> 
> > [ *Note 1:* An expression `E` in the `*compound-statement*` of a `*do-expression*` `D` ([expr.prim.do]) can still be a full-expression even though `D` itself is an expression, because `E` is not a subexpression of `D`. By contrast, the constituent expressions of an `*initializer*` in the `*init-hoist-introducer*` of `D` are part of the full-expression that contains `D`. — *end note* ]
> 
> :::

### 5.2 Expressions

Add `*do-expression*` to the grammar in 7.5.1 Grammar [[expr.prim.grammar]](https://eel.is/c++draft/expr.prim.grammar):

:::wording

> ```cpp
> primary-expression:
>   literal
>   this
>   ( expression )
>   id-expression
>   lambda-expression
>   fold-expression
>   requires-expression
>   splice-expression
> + do-expression
> ```

:::

Extend the rule for move-eligible expressions in 7.5.5.2 Unqualified names [[expr.prim.id.unqual]](https://eel.is/c++draft/expr.prim.id.unqual):

:::wording

> 15 An *implicitly movable entity* is a variable with automatic storage duration that is either a non-volatile object or an rvalue reference to a non-volatile object type. An `*id-expression*` or `*splice-expression*` ([[expr.prim.splice]](https://eel.is/c++draft/expr.prim.splice)) is *move-eligible* if
> 
> - (15.1) it designates an implicitly movable entity,
> - (15.2) it is the (possibly parenthesized) operand of a `return` ([[stmt.return]](https://eel.is/c++draft/stmt.return)) <del>or</del> , `co_return` ([[stmt.return.coroutine]](https://eel.is/c++draft/stmt.return.coroutine)), or `do_return` ([stmt.do.return]) statement, or of a `*throw-expression*` ([[expr.throw]](https://eel.is/c++draft/expr.throw)), and
> - (15.3) each intervening scope between the declaration of the entity and the innermost enclosing scope of the expression is a block scope and, for a `*throw-expression*`, is not the block scope of a `*try-block*` or `*function-try-block*`, and
> - (15.4) for a `do_return` statement, the entity belongs to the block scope of the `*compound-statement*` of its associated `*do-expression*` ([stmt.do.return]), or to a block scope contained by that block scope.

:::

Add a new clause [expr.prim.do] after 7.5.8.5 Nested requirements [[expr.prim.req.nested]](https://eel.is/c++draft/expr.prim.req.nested):

:::wording

> **Do expressions [expr.prim.do]**
> 
> 1 A *do-expression* provides a way to combine multiple statements into a single expression without introducing a new function scope. A `do_return` statement ([stmt.do.return]) produces the result of the `*do-expression*`. Other jump statements can transfer control out of a `*do-expression*` without producing a value.
> 
> > [ *Example 1:* 
> > 
> > ```cpp
> > constexpr int f(int i) {
> >     int half = do {
> >         if (i % 2 != 0) {
> >             return -1;              // returns from f
> >         }
> >         do_return i / 2;            // produces the value of the do-expression
> >     };
> >     return half;
> > }
> > 
> > static_assert(f(5) == -1);
> > static_assert(f(4) == 2);
> > ```
> > 
> >  — *end example* ]
> 
> ```cpp
> do-expression:
>     do init-hoist-introduceropt trailing-return-typeopt compound-statement
> 
> init-hoist-introducer:
>     [ init-hoist-list ]
> 
> init-hoist-list:
>     init-hoist
>     init-hoist-list , init-hoist
> 
> init-hoist:
>     identifier initializer
> ```
> 
> 2 The `*init-hoist-introducer*`, if any, of a `*do-expression*` allows declarations to be introduced within an expression. A `*do-expression*` with an `*init-hoist-introducer*` introduces a block scope ([[basic.scope.block]](https://eel.is/c++draft/basic.scope.block)) that includes the `*init-hoist-list*` and the `*compound-statement*`. Each `*init-hoist*` declares a variable; its type is deduced as if from a declaration of the form `auto&& *init-hoist* ;` ([[dcl.spec.auto]](https://eel.is/c++draft/dcl.spec.auto)), and the variable is so initialized. The point of declaration of the `*identifier*` of an `*init-hoist*` is immediately after its `*initializer*` ([[basic.scope.pdecl]](https://eel.is/c++draft/basic.scope.pdecl)). The variables declared by the `*init-hoist-list*` are initialized in order before the `*compound-statement*` is executed.
> 
> 3 The constituent expressions of the `*initializer*` of an `*init-hoist*` are part of the full-expression ([[intro.execution]](https://eel.is/c++draft/intro.execution)) that contains the `*do-expression*`. [ *Note 1:* Consequently, a temporary created during the initialization of such a variable is destroyed at the end of that full-expression ([[class.temporary]](https://eel.is/c++draft/class.temporary)), not at the end of the `*do-expression*`. — *end note* ]
> 
> 4 A `do_return` statement ([stmt.do.return]) whose associated `*do-expression*` has an `*init-hoist-introducer*` does not exit the block scope introduced by that `*init-hoist-introducer*`. The variables declared in the `*init-hoist-list*` are destroyed, in reverse order of their construction, at the end of the full-expression that contains the `*do-expression*`; if control instead exits that block scope by any other means, those variables are destroyed as that scope is exited ([[stmt.jump]](https://eel.is/c++draft/stmt.jump)). [ *Note 2:* Because each such variable has reference type, a temporary bound to it ([[class.temporary]](https://eel.is/c++draft/class.temporary)) is likewise destroyed at the end of the full-expression that contains the `*do-expression*`. — *end note* ]
> 
> > [ *Example 2:* 
> > 
> > ```cpp
> > constexpr int f() {
> >     return do [x = 1, y = 2] { x + y };
> > }
> > static_assert(f() == 3); // OK
> > 
> > constexpr int const& id(int const& r) { return r; }
> > constexpr int const* ptr(int const& r) { return &r; }
> > 
> > constexpr int h() {
> >     return do [p = ptr(id(42))] { *p };
> > }
> > static_assert(h() == 42); // OK, no dangling
> > ```
> > 
> >  — *end example* ]
> 
> 5 The `*compound-statement*` of a `*do-expression*` is a control-flow-limited statement ([[stmt.label]](https://eel.is/c++draft/stmt.label)).
> 
> 6 A `return` statement ([[stmt.return]](https://eel.is/c++draft/stmt.return)) appearing in a `*do-expression*` transfers control to the caller of the function that lexically contains the `*do-expression*`. A `co_return`, `co_await`, or `co_yield` statement or expression appearing in a `*do-expression*` acts on the coroutine that lexically contains the `*do-expression*`. [ *Note 3:* That is, a `*do-expression*` is transparent to the enclosing function or coroutine. — *end note* ]
> 
> 7 A `break` or `continue` statement appearing in a `*do-expression*` refers to an enclosing `*iteration-statement*` or `switch` statement that contains the `*do-expression*`. [ *Note 4:* A `break` or `continue` statement cannot be used to exit a `*do-expression*` itself. — *end note* ]
> 
> 8 A `*do-expression*` that is not within a function shall not contain a `return` statement, a `co_return` statement, a `co_await` expression, or a `co_yield` expression.
> 
> 9 The type `*DO-TYPE*` of a `*do-expression*` is determined as follows:
> 
> - (9.1) If there is a `*trailing-return-type*` that does not contain a placeholder type ([[dcl.spec.auto]](https://eel.is/c++draft/dcl.spec.auto)), then `*DO-TYPE*` is the type specified by that `*trailing-return-type*`.
> - (9.2) Otherwise, `*DO-TYPE*` is deduced from the non-discarded `do_return` statements associated with the `*do-expression*`:
>   - (9.2.1) If there is no non-discarded `do_return` statement associated with the `*do-expression*`, or every non-discarded `do_return` statement associated with the `*do-expression*` has no operand, `*DO-TYPE*` is `void`.
>   - (9.2.2) Otherwise, `*DO-TYPE*` is deduced as if from a `return` statement using the rules in [[dcl.spec.auto.general]](https://eel.is/c++draft/dcl.spec.auto.general). All non-discarded `do_return` statements associated with the `*do-expression*` shall deduce to the same type; otherwise, the program is ill-formed.
> 
> > [ *Example 3:* 
> > 
> > ```cpp
> > auto a = do { do_return 1; };           // OK, deduces int
> > auto b = do -> long { do_return 1; };   // OK, explicit type is long
> > auto c = do {                           // error: inconsistent deduction
> >     if (cond) do_return 1;
> >     do_return 2.0;
> > };
> > ```
> > 
> >  — *end example* ]
> 
> 10 The type and value category of the `*do-expression*` are determined from `*DO-TYPE*` as follows:
> 
> - (10.1) If `*DO-TYPE*` is `T&`, the `*do-expression*` is an lvalue of type `T`.
> - (10.2) Otherwise, if `*DO-TYPE*` is `T&&`, the `*do-expression*` is an xvalue of type `T`.
> - (10.3) Otherwise, the `*do-expression*` is a prvalue of type `*DO-TYPE*`.
> 
> 11 If control can flow off the end of the `*compound-statement*` of a `*do-expression*` whose type is not `*cv* void`, the program is ill-formed. [ *Note 5:* Control flows off the end if there exists any path through the compound statement that does not terminate with a `do_return` statement, a `throw` expression, a call to a `[[noreturn]]` function, or a jump statement that exits the `*do-expression*`. — *end note* ]
> 
> > [ *Example 4:* 
> > 
> > ```cpp
> > extern bool cond;
> > void f() {
> >     auto a = do {                       // error: control may flow off the end
> >         if (cond) do_return 1;
> >     };
> > 
> >     auto b = do {                       // OK, all paths yield or exit
> >         if (cond) do_return 1;
> >         throw 2;
> >     };
> > 
> >     auto c = do {                       // OK, return exits the do-expression
> >         if (cond) do_return 1;
> >         return;
> >     };
> > 
> >     (do -> void {                       // OK, void type allows flow off the end
> >         if (cond) do_return;
> >     });
> > }
> > ```
> > 
> >  — *end example* ]
> 
> 12 The initialization of the returned reference or prvalue result object of a `*do-expression*` is sequenced before the destruction of temporaries at the end of the full-expression established by the operand of the executed `do_return` statement, which, in turn, is sequenced before the destruction of local variables ([[stmt.jump]](https://eel.is/c++draft/stmt.jump)) whose scope is exited by the `do_return` statement. [ *Note 6:* A copy or move operation associated with a `do_return` statement can be elided or converted to a move operation the same as for a `return` statement ([[class.copy.elision]](https://eel.is/c++draft/class.copy.elision)). — *end note* ]
> 
> 13 A `*do-expression*` can appear in any context where an expression is permitted, including at namespace scope. [ *Note 7:* At namespace scope or in a default member initializer, there is no enclosing function, so `return`, `break`, `continue`, and coroutine statements/expressions cannot be used. — *end note* ]

:::

### 5.3 Statements

Change 8.1 Preamble [[stmt.pre]](https://eel.is/c++draft/stmt.pre) to make the `*compound-statement*` of a `*do-expression*` transparent to the enclosing statement:

:::wording

> 3 A `*statement*` `S1` encloses a `*statement*` `S2` if
> 
> - (3.1) `S2` is a substatement of `S1`,
> - (3.2) `S1` is a `*selection-statement*`, `*iteration-statement*`, or `*expansion-statement*`, and `S2` is the `*init-statement*` of `S1`,
> - (3.3) `S1` is a `*try-block*` and `S2` is its `*compound-statement*` or any of the `*compound-statement*`s of its `*handler*`s, <del>or</del>
> - (3.4) `S1` encloses a statement `S3` and `S3` encloses `S2`<del>.</del> , or
> - (3.5) `S2` is the `*compound-statement*` of a `*do-expression*` `E` ([expr.prim.do]), `E` appears within `S1`, and `E` does not appear within an intervening `*lambda-expression*` or function body.

:::

Change 8.3 Expression statement [[stmt.expr]](https://eel.is/c++draft/stmt.expr) to disambiguate a `*do-expression*` from a `do`-`while` loop:

:::wording

> 1 Expression statements have the form
> 
> ```cpp
> expression-statement:
>   expressionopt;
> ```
> 
> The expression is a *discarded-value expression* ([[expr.context]](https://eel.is/c++draft/expr.context)). All side effects from an expression statement are completed before the next statement is executed. An expression statement with the expression missing is called a *null statement*. The `*expression*` shall not be a `*do-expression*`.
> 
> [ *Note 1:* A statement beginning with the keyword `do` is always parsed as a `do`-`while` statement ([[stmt.do]](https://eel.is/c++draft/stmt.do)). A `*do-expression*` used as a statement must be parenthesized. — *end note* ]

:::

Add to the grammar in 8.8.1 General [[stmt.jump.general]](https://eel.is/c++draft/stmt.jump.general):

> 1 Jump statements unconditionally transfer control.
> 
> ```cpp
> jump-statement:
>     break ;
>     continue ;
>     return expr-or-braced-init-listopt ;
> +   do_return expr-or-braced-init-listopt ;
>     coroutine-return-statement
>     goto identifier ;
> ```
> 
> 2 […]

Change 8.8.2 The break statement [[stmt.break]](https://eel.is/c++draft/stmt.break) to prohibit its use in `*do-expression*`s in confusing places:

:::wording

> 1 A `break` statement shall be enclosed by ([[stmt.pre]](https://eel.is/c++draft/stmt.pre)) an `*iteration-statement*` ([[stmt.iter]](https://eel.is/c++draft/stmt.iter)), an `*expansion-statement*` ([[stmt.expand]](https://eel.is/c++draft/stmt.expand)), or a `switch` statement ([[stmt.switch]](https://eel.is/c++draft/stmt.switch)). The `break` statement causes termination of the innermost such enclosing statement; control passes to the statement following the terminated statement, if any.
> 
> 2 A `break` statement shall not appear in a `*do-expression*` ([expr.prim.do]) that is a subexpression of:
> 
> - (2.1) the `*init-statement*`, `*condition*`, or `*expression*` of a `for` statement ([[stmt.for]](https://eel.is/c++draft/stmt.for)),
> - (2.2) the `*condition*` of a `while` statement ([[stmt.while]](https://eel.is/c++draft/stmt.while)),
> - (2.3) the `*init-statement*`, `*for-range-declaration*`, or `*for-range-initializer*` of a range-based `for` statement ([[stmt.ranged]](https://eel.is/c++draft/stmt.ranged)),
> - (2.4) the `*expression*` of a `do` statement ([[stmt.do]](https://eel.is/c++draft/stmt.do)), or
> - (2.5) the `*init-statement*` or `*condition*` of a `switch` statement ([[stmt.switch]](https://eel.is/c++draft/stmt.switch))
> 
> unless the enclosing `*iteration-statement*` or `switch` statement of that `break` statement is also within the same `*do-expression*`.

:::

Change 8.8.3 The continue statement [[stmt.cont]](https://eel.is/c++draft/stmt.cont) similarly:

:::wording

> 1 A `continue` statement shall be enclosed by ([[stmt.pre]](https://eel.is/c++draft/stmt.pre)) an `*iteration-statement*` ([[stmt.iter]](https://eel.is/c++draft/stmt.iter)) or an `*expansion-statement*` ([[stmt.expand]](https://eel.is/c++draft/stmt.expand)). […]
> 
> 2 A `continue` statement shall not appear in a `*do-expression*` ([expr.prim.do]) that is a subexpression of:
> 
> - (2.1) the `*init-statement*`, `*condition*`, or `*expression*` of a `for` statement ([[stmt.for]](https://eel.is/c++draft/stmt.for)),
> - (2.2) the `*condition*` of a `while` statement ([[stmt.while]](https://eel.is/c++draft/stmt.while)),
> - (2.3) the `*init-statement*`, `*for-range-declaration*`, or `*for-range-initializer*` of a range-based `for` statement ([[stmt.ranged]](https://eel.is/c++draft/stmt.ranged)), or
> - (2.4) the `*expression*` of a `do` statement ([[stmt.do]](https://eel.is/c++draft/stmt.do))
> 
> unless the enclosing `*iteration-statement*` of that `continue` statement is also within the same `*do-expression*`.

:::

Add a new subclause [stmt.do.return] “The `do_return` statement” after 8.8.5 The co_return statement [[stmt.return.coroutine]](https://eel.is/c++draft/stmt.return.coroutine):

:::wording

> **The `do_return` statement [stmt.do.return]**
> 
> 1 A `do_return` statement shall appear only within the `*compound-statement*` of a `*do-expression*` ([expr.prim.do]), and not within an intervening `*lambda-expression*` or function body. The innermost such `*do-expression*` is the `do_return` statement’s *associated* `*do-expression*`.
> 
> > [ *Example 1:* 
> > 
> > ```cpp
> > int f() {
> >     return do {
> >         auto g = []() {
> >             do_return 1;        // error: crosses lambda boundary
> >         };
> >         do_return 2;            // OK
> >     };
> > }
> > ```
> > 
> >  — *end example* ]
> 
> 2 The `*expr-or-braced-init-list*` of a `do_return` statement is called its operand. A `do_return` statement with no operand shall be used only if its associated `*do-expression*` has type `*cv* void`. A `do_return` statement with an operand of type `void` shall be used only if its associated `*do-expression*` has type `*cv* void`. A `do_return` statement with any other operand shall be used only if its associated `*do-expression*` has type other than `*cv* void`; the `do_return` statement initializes the returned reference or prvalue result object of its associated `*do-expression*` by copy-initialization ([[dcl.init]](https://eel.is/c++draft/dcl.init)) from the operand.
> 
> 3 A `do_return` statement that binds
> 
> - (3.1) a returned reference or
> - (3.2) a constituent reference ([[intro.object]](https://eel.is/c++draft/intro.object)) of a returned object
> 
> to a temporary expression ([[class.temporary]](https://eel.is/c++draft/class.temporary)) is ill-formed.
> 
> > [ *Example 2:* 
> > 
> > ```cpp
> > int& f();
> > auto a = do -> int const& { do_return f(); };     // OK
> > auto b = do -> int const& { do_return 42; };      // error: binds reference to temporary
> > ```
> > 
> >  — *end example* ]

:::

### 5.4 Feature-Test Macro

Add to 15.12 Predefined macro names [[cpp.predefined]](https://eel.is/c++draft/cpp.predefined):

> ```cpp
> + __cpp_do_expressions 20XXXXL
> ```

## 6 References

[P2552R2] Timur Doumler. 2023-05-19. On the ignorability of standard
attributes.

https://wg21.link/p2552r2

[P2561R2] Barry Revzin. 2023-05-18. A control flow operator.

https://wg21.link/p2561r2

[P2688R4] Michael Park. 2024-12-17. Pattern Matching:

match

Expression.

https://wg21.link/P2688R4

[P2806R0] Barry Revzin, Bruno Cardoso Lopez, Zach Laine, Michael Park.
2023-02-14. do expressions.

https://wg21.link/p2806r0

[P2806R1] Barry Revzin, Bruno Cardoso Lopez, Zach Laine, Michael Park.
2023-03-12. do expressions.

https://wg21.link/p2806r1

[P2806R2] Barry Revzin, Bruno Cardoso Lopez, Zach Laine, Michael Park.
2023-11-16. do expressions.

https://wg21.link/p2806r2

[P2806R3] Barry Revzin, Bruno Cardoso Lopez, Zach Laine, Michael Park.
2025-01-12. do expressions.

https://wg21.link/p2806r3

[P2806R4] Barry Revzin, Bruno Cardoso Lopez, Zach Laine, Michael Park.
2026-07-15. do expressions.

https://wg21.link/p2806r4

[P3549R0] Barry Revzin, Michael Park, Zach Laine, Bruno Cardoso Lopes.
2025-01-12. Diverging expressions.

https://wg21.link/p3549r0
