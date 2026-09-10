| {intro. progress. stops} | [intro.progress]/1: The implementation may assume that any thread will eventually do one of the following: terminate, invoke the function `std::this_thread::yield` ([thread.thread.this]), make a call to a library I/O function, perform an access through a volatile glvalue, perform an atomic or synchronization operation other than an atomic modify-write operation ([atomics.order]), or continue execution of a trivial infinite loop ([stmt.iter.general]). | No | No | No checking strategy exists as whether a thread will make progress is undecidable | None |

### VI. Sequencing

| Identifier | Wording | Runtimecheckable | Locally checkable | Runtime checking strategy | Replacement behaviour |
| --- | --- | --- | --- | --- | --- |
| {intro. execution. unsequenced. modification} | [intro.execution]/10: The behavior is undefined if a side effect on a memory location ([intro.memory]) or starting or ending the lifetime of an object in a memory location is unsequenced relative to another side effect on the same memory location, starting or ending the lifetime of an object occupying storage that overlaps with the memory location, or a value computation using the value of any object in the same memory location, and the two evaluations are not potentially concurrent ([intro.multithread]). | Yes | Yes | Identify all potential read operations that are not sequenced with respect to each given write operation; insert checks to identify if those operations are referencing the same address | Sequence operations in some unspecified order |

### VII. Assumptions

| Identifier | Wording | Runtimecheckable | Locally checkable | Runtime checking strategy | Replacement behaviour |
| --- | --- | --- | --- | --- | --- |
| {dcl.attr. assume.false} | [dcl.attr.assume]/1: If the converted expression would evaluate to true at the point where the assumption appears, the assumption has no effect. Otherwise, evaluation of the assumption has runtime undefined behavior. | No | Yes, if checkable at all | No automatic checking strategy is possible because the predicate cannot be, in general, proven to be free of side effects; instead, the user has to change `[[assume(x)]]` to `contract_assert<may_be_assumed>(x)` and select an appropriate evaluation semantic | Ignore the assumption |

### VIII. Control Flow

| Identifier | Wording | Runtimecheckable | Locally checkable | Runtime checking strategy | Replacement behaviour |
| --- | --- | --- | --- | --- | --- |
| {basic.start. main.exit. during. destruction} | [basic.start.main]/4: If `std::exit` is invoked during the destruction of an object with static or thread storage duration, the program has undefined behavior. | Yes | No | Track whether static or thread-local objects are currently being destroyed | None |
| {basic.start. term.use.after. destruction} | [basic.start.term]/4: If a function contains a block variable of static or thread storage duration that has been destroyed and the function is called during the destruction of an object with static or thread storage duration, the program has undefined behavior if the flow of control passes through the definition of the previously destroyed block variable. | Yes | No | Track the lifetime of static objects | None |
| {stmt.return. flow.off} | [stmt.return]/4: Otherwise, flowing off the end of a function that is neither `main` ([basic.start.main]) nor a coroutine ([dcl.fct.def.coroutine]) results in undefined behavior. | Yes | Yes | Insert `contract_assert(false)` at end of *function-body* | Only for built-in return types: return erroneous value |
| {stmt.dcl. local.static. init.recursive} | [stmt.dcl]/3: If control re-enters the declaration recursively while the variable is being initialized, the behavior is undefined. | Yes | No | Insert a recursion counter into a guard for static and thread-local object construction | None |
| {dcl.attr. noreturn. eventually. returns} | [dcl.attr.noreturn]/2: If a function `f` is invoked where `f` was previously declared with the `noreturn` attribute and that invocation eventually returns, the behavior is runtime-undefined. | Yes | Yes | Insert `post(false)` | None |

### IX. Replacement Functions

| Identifier | Wording | Runtimecheckable | Locally checkable | Runtime checking strategy | Replacement behaviour |
| --- | --- | --- | --- | --- | --- |
| {basic.stc. alloc.dealloc. constraint} | [basic.stc.dynamic.general]/3: If the behavior of an allocation or deallocation function does not satisfy the semantic constraints specified in [basic.stc.dynamic.allocation] and [basic.stc.dynamic.deallocation], the behavior is undefined. | Partially | No | Insert checks where possible | None |
| {expr.new. non.allocating. null} | [expr.new]/22: If the allocation function is a non-allocating form ([new.delete.placement]) that returns null, the behavior is undefined. | Yes | Yes | Insert `post(r:` `r)` | None |

### X. Coroutines

| Identifier | Wording | Runtimecheckable | Locally checkable | Runtime checking strategy | Replacement behaviour |
| --- | --- | --- | --- | --- | --- |
| {stmt.return. coroutine.flow. off} | [stmt.return.coroutine]/3: If a search for the name `return_void` in the scope of the promise type finds any declarations, flowing off the end of a coroutine’s *function-body* is equivalent to a `co_return` with no operand; otherwise flowing off the end of a coroutine’s *function-body* results in undefined behavior. | Yes | Yes | Insert `contract_assert(false)` at end of *function-body* if no `return_void` function is provided | Only for built-in return types: return erroneous value |
| {dcl.fct.def. coroutine. resume.not. suspended} | [dcl.fct.def.coroutine]/9: Invoking a resumption member function for a coroutine that is not suspended results in undefined behavior. | Yes | No | Track the suspension state associated with every coroutine handle | None |
| {dcl.fct.def. coroutine. destroy.not. suspended} | [dcl.fct.def.coroutine]/12: If `destroy` is called for a coroutine that is not suspended, the program has undefined behavior. | Yes | No | Track the suspension state associated with every coroutine handle | None |
