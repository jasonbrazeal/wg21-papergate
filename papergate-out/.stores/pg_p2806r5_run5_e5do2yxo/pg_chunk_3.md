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
