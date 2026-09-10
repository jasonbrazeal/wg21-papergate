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