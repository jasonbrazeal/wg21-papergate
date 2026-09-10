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
