## 6. Conceptual Interface

We provide basic queue operations, and then extend those operations to cover other important use cases.

Due to performance issues, the conceptual interface is split into three separate interfaces. The `basic_concurrent_queue` concept provides the interface `push` and `pop` and closing the queue. The `concurrent_queue` concept is based on `basic_concurrent_queue` and provides the additional interface `try_push` and `try_pop`. The `async_concurrent_queue` concept is also based on `basic_concurrent_queue` and provides the additional interface `async_push` and `async_pop`.

The concrete queue `bounded_queue` models all these concepts. `bounded_queue` guarantees FIFO order. The concepts deliberately don’t. This allows for priority based queues, but also for specific implementation strategies that don’t guarantee FIFO order.

### 6.1. Why Concepts?

Concurrent queues are nothing new. They are existing practice since decades of concurrent programming. However, these queues differ in their trade-offs for specific properties, and therefore in their semantics.

There’s no single queue implementation that can handle all use cases efficiently. Also not all use cases require both `try_*` and `async_*` interfaces, and only providing one of them allows for more efficient implementations. Therefore it’s expected that there will be many different implementations of these concepts with different trade-offs. Some of them might be standardized, most will be not.

The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

`bounded_queue` is one specific implementation that’s provided by the Standard Library, with specific semantics, but many C++ programmers will use other implementions but still want to know what they can rely on.

The existence of the concepts allows for adapters (like single-ended interfaces) to be used with different implementations.

LEWG requested in St. Louis to make these concepts exposition-only, as this proposal doesn’t include any adapters using these concepts. LWG didn’t want to specify the exposition-only concepts but only the concrete `bounded_queue`. Based on this SG1 requested in Brno to make these concepts non-exposition-only again, as was the status when P0260 was forwarded to LEWG.

#### 6.1.1. Logging With Queue Ends and Derived Concept

The logging example may easily be templated on the queue type. The functions only use a specific end of the queue, so it may be useful to constrain the template to a single end:

```cpp
template <class QE>
concept MyConcurrentQueueFrontConcept =
    stdown::concurrent_queue<typename QE::queue_type> &&
    requires (QE q)
    {
        { q.try_pop() } -> std::same_as<std::expected<typename QE::queue_type::value_type, conqueue_status>>;
    };

template <class QE>
concept MyConcurrentQueueBackConcept =
    stdown::concurrent_queue<typename QE::queue_type> &&
    requires (QE q, typename QE::queue_type::value_type &&t)
    {
        { q.try_push(std::forward<typename QE::queue_type::value_type>(t)) } -> std::same_as<conqueue_status>;
    };
```

These concepts are based on the general queue concept. The additional constraint is purely syntactical and can be provided locally.

Based on these local concepts, the functions can be provided as constrained templates:

```cpp
template <MyConcurrentQueueBackConcept QE>
void enqueueLogMessage(QE &qTail, std::string &&msg)
{
    if (qTail.try_push(std::move(msg)) != conqueue_status::success)
    {
        ++lostLogMessages;
    }
}

template <MyConcurrentQueueFrontConcept QE>
void outputLogMessage(QE &qHead)
{
    static std::string buffer;

    auto msg = qHead.try_pop();
    if (msg)
    {
        buffer += *msg;
    }
    else
    {
        assert(msg.error() != conqueue_status::closed);
    }

    if (!buffer.empty())
    {
        outputBuffer.add(buffer);
    }
}
```

#### 6.1.2. Queue Implementations that Differ From `bounded_queue` semantics

- `PriorityQueue`: not FIFO
- unbounded queue: allocates on `push`

### 6.2. Status Enum

We introduce an `enum class` to define the possible states that operations on the queue may return.

```cpp
enum class conqueue_status { success, empty, full, closed, busy, busy_async };
```

### 6.3. Basic Operations

The essential solution to the problem of concurrent queuing is to shift to value-based operations, rather than reference-based operations.

The basic operations are:

```cpp
bool queue::push(const T& x);
bool queue::push(T&& x);
template <typename... Args> bool emplace(Args &&... as);
```

Pushes `x` onto the queue via copy, move or argument based construction (and possibly blocks). It returns `true` on success, and `false` if the queue is closed.

```cpp
std::optional<T> queue::pop();
```

Pops a value from the queue via move construction into the return value. If the queue is empty and closed, returns `std::nullopt`. If queue is empty and open, the operation blocks until an element is available.

### 6.4. Non-Waiting Operations

Waiting on a full or empty queue can take a while, which has an opportunity cost. Avoiding that wait enables algorithms to do other work rather than wait for a push on a full queue, and to do other work rather than wait for a pop on an empty queue. More importantly, there are contexts with weakly parallel forward progress that don’t allow blocking synchronization, but where pushing into and popping from a queue is still desired. Also, blocking can really kill perfomance.

For all these reasons we provide `try_` versions of push and pop operations. These operations will never block. If they would have to wait for internal synchronization the queue status is `conqueue_status::busy`. If they would have to schedule a continuation of an async operation the queue status is `conqueue_status::busy_async`.

`busy_async` is an unfortunate case. The problem is that notification of an event to an async operation either means to schedule the continuation of the operation or to run it. The latter is really not an option for `try_push` as it runs arbitray work which is potentially blocking. But scheduling generally means to enqueue the continuation into some work list, and this may not be possible without blocking. The current scheduler interface doesn’t have any way to detect that the scheduling would block, so the way out is simply to return `busy_async`. [Non-Blocking Support for `std::execution` (P3669)](https://wg21.link/P3668) tries to fix the problem in the scheduler interface. Then `busy_async` may not be needed anymore.

```cpp
conqueue_status queue::try_push(const T& x);
conqueue_status queue::try_push(T&& x);
template <typename... Args> conqueue_status try_emplace(Args &&... as);
```

Note: the return type has changed from earlier versions. Returning a `bool` and providing the reason for a failure in an extra output parameter feels wrong.

If no object could be placed into the queue, returns the respective status. Otherwise, pushes the value onto the queue via copy, move or argument based construction and returns `conqueue_status::success`.

```cpp
expected<T, conqueue_status> queue::try_pop();
```

If no object could be obtained from the queue, returns an `expected` with an `unexpected` that contains the queue status. Otherwise, pops the element from the queue via move construction into the `expected`.

This is the interface agreed on in LEWG in Hagenberg.

### 6.5. Asynchronous Operations

```cpp
sender auto queue::async_push(T& x);
sender auto queue::async_push(T&& x);
template <typename... Args> sender auto async_emplace(Args &&... as);

sender auto queue::async_pop();
```

These operations return a sender that will push or pop the element. The operations support cancellation and if the receiver is currently waiting on a push or pop operation and no longer interested in performing the operation, it should be removed from any waiting queues, if any, and be completed with `std::execution::set_stopped`.

Sender based async interfaces have two main ways of usage: native S/R with receivers and coroutines where the receivers are provided by the coroutine library.

In Wroclaw only the coroutine usage was shown and LEWG voted there for an interface that favours coroutines. The sender returned by `async_pop()` would call `set_value(optional<T>)` which mirrors the synchronous `pop()`.

Afterwards it was pointed out that this interface is suboptimal for native receivers that can have multiple `set_value()` overloads. So R12 proposed to call `set_value(T)` if a value was retrieved and `set_value(void)` otherwise.

One change from R12 as presented in a telecon in December 2024 is that the close case takes the `set_error` path and not `set_value(void)`. One reason for this is that if the queue is closed, the pop fails to provide a value. In many cases it’s not really an error, but it’s still some kind of failure, and using the `set_value` channel for this feels wrong.

The native sender/receiver usage could look like this:

```cpp
files.async_pop()
| stdexec::then(
    [str] (const fs::path& fname) noexcept
    {
        //...
        return false;
    })
| stdexec::upon_error(
    [] (auto err) noexcept -> bool
    {
        return true;
    });
```

But a native sender/receiver usage could also provide an application specific receiver that now can handle the value case and the closed case completely separately.

Another reason for using `set_error` is a practical one. If `async_pop` returns a value you often want to handle this value using more than one pipeline stage:

```cpp
files.async_pop()
| stdexec::then(
    [str] (T1 v1) noexcept
    {
        //...
        return T2{...};
    })
| some_worker.async_consume()
| stdexec::upon_error(
    [] (auto err) noexcept -> bool
    {
        return true;
    });
```

If the closed case would call the `set_value` channel, it would be harder to write such chains, and it’s much easier to handle all failure cases with a single `upon_error` at the end.

By symmetry, `async_push` (and `async_emplace`) also call `set_error(conqueue_status)` on a closed queue. For success they simply call `set_value(void)`.

[P3570R0: optional variants in sender/receiver](https://wg21.link/P3570) provides a mechanism to return different values for coroutines than for direct receivers. This revision proposes to use this mechanism.

For the coroutine use it provides an exposition-only adapter *error-as-optional* that returns an `optional<T>` that contains a value if a value was retrieved and an empty `optiona<T>` if the queue was closed.

For `async_push` an exposition-only adapter *error-as-bool* is provided that returns for coroutines `true` if the push succeeded and `false` if the queue was closed.

### 6.6. Closed Queues

Threads using a queue for communication need some mechanism to signal when the queue is no longer needed. The usual approach is add an additional out-of-band signal. However, this approach suffers from the flaw that threads waiting on either full or empty queues need to be woken up when the queue is no longer needed. To do that, you need access to the condition variables used for full/empty blocking, which considerably increases the complexity and fragility of the interface. It also leads to performance implications with additional mutexes or atomics. Rather than require an out-of-band signal, we chose to directly support such a signal in the queue itself, which considerably simplifies coding.

To achieve this signal, a thread may `close` a queue. Once closed, no new elements may be pushed onto the queue. Push operations on a closed queue will return `false` or `conqueue_status::closed`. Elements already on the queue may be popped. When a queue is empty and closed, pop operations will either (`pop`) return an empty `optional` or (`try_pop`) return an `expected` with an `unexpected` result with value `conqueue_status::closed`.

The additional operations are as follows:

```cpp
void queue::close() noexcept;
```

Close the queue.

```cpp
bool queue::is_closed() const noexcept;
```

Return true iff the queue is closed.

### 6.7. `emplace`

As queues have a `push` operation, it might be plausible to add an `emplace` operation as well. However, this might be misleading. `emplace` typically exists for performance reason for types that don’t provide cheap move construction. So for containers where objects are meant to stay it makes sense to construct the objects in place. But queues aren’t containers. Queues are mechanisms to push objects into them to be popped out again as soon as possible. So if the move of an object is expensive, it might be efficient to construct it inside a queue, but the pop would still be expensive. In such cases it might be more efficient to push a `unique_ptr` or similar through a queue instead of the actual values.

Providing an `emplace` operation might lead users to use a queue with object values and believe that’s efficient.

However, `try_emplace` is definitely useful as no object is created at all if it’s not inserted into the queue.

And if `try_emplace` exists, for symmetry `emplace` and `async_emplace` should be provided as well, so this revision proposes them.

### 6.8. Element Type Requirements

The above operations require element types with copy/move constructors, and destructor. These operations may be trivial. The copy/move constructors operators may throw, but must leave the objects in a valid state for subsequent operations.

### 6.9. "Error" Handling

It’s extremely hard to define what results of a queue function actually constitutes an error. Instead of trying so, this proposal takes the approach that nothing is really an error.

Instead different function results due to different queue states are delivered by special return types.

`pop()` returns `optional<T>` (as decided in Wroclaw): empty `optional` for the `closed` state, and an optional containing a `T` otherwise.

`push()` returns `bool`: `false` for `closed` and `true` for successful enqueuing.

`try_pop` returns `expected<T, conqueue_status>`: a `T` on success and the queue state otherwise. This was decided in LEWG in Hagenberg.

`try_push` returns as `conqueue_status` the queue state directly.

`async_pop()` returns a sender that calls `set_value(T)` if a value could be obtained from the queue and `set_error(conqueue_status)` if the queue was closed.

`async_push()` returns a sender that calls `set_value(void)` if the value could be deposited and `set_error(conqueue_status)` if the queue was closed.

Concurrent queues cannot completely hide the effect of exceptions thrown by the element type, in part because changes cannot be transparently undone when other threads are observing the queue.

Queues operations may rethrow exceptions from storage allocation or mutexes.

If the element type operations required do not throw exceptions, then only the exceptions above are rethrown. In practice, for a `bounded_queue` storage allocation only happens on construction and mutex `lock` and `unlock` generally only throw on deadlock detection.

When an element copy/move may throw, some queue operations have additional behavior.

- A push operation shall rethrow and the state of the queue is unaffected.
- A pop operation shall rethrow and the element is popped from the queue. The value popped is effectively lost. (Doing otherwise would likely clog the queue with a bad element.)

### 6.10. Single-Ended Interfaces

In many applications one part only uses one end of a queue, while a different purt uses the other end. I.e. producer and consumer are logically separated. So it makes a lot of sense to provide interface types that only provide either the push or the pop interface.

But providing such separate interfaces requires additional overhead to ensure there arise no lifetime issues. So requiring such interfaces is not part of the proposed concept.

And then it’s assumed that a lot of different implementations of the concept will exist, with different tradeoffs. A separate type for the single-ended interfaces that works for all these implementation is more efficent in terms of implementation. Such a type is not part of this proposal but is a separate proposal [Single Ends for C++ Concurrent Queues (P4295)](https://wg21.link/P4295). And as separate type it can easily be added later.


## 7. Concrete Queues

In addition to the concepts, the standard needs at least one concrete queue. This will not provide the most efficient implementation but serves all synchronization use cases. For this reason it’s bounded to allow for slowing down producers that are too fast.

This paper proposes a fixed-size `bounded_queue`. It meets all three concepts for queues. The constructor takes a parameter specifying the maximum number of elements in the queue and an optional allocator.

`bounded_queue` is only allowed to allocate in its constructor.

### 7.1. Movability

The `bounded_queue` implementation will probably contain synchronization mechanisms like `std::mutes` and `std::condition_variable`. These are not movable, so `bounded_queue` isn’t movable either.

### 7.2. Memory Order Guarantees

`bounded_queue` provides sequentially consistent semantics.

The reasoning for this is that for a queue (as high-level data structure) provided by the IS usage safety should be more important than efficiency. Background on this is found in [Memory Model Issues for Concurrent Data Structures (P0387R1)](https://wg21.link/P0387R1) and [Concurrency Safety in C++ Data Structures (P0495)](https://wg21.link/P0495).

The example from P0387R1 illustrates the problem clearly:

`q` and `log` are concurrent queues:

<!-- tomd:lossy-table -->
| Thread 1 | Thread 2 |
| --- | --- |
| `q.push(1);` `log.push("pushed 1");` | `log.push("pushed 2");` `q.push(2);` |

With only acquire/release this could result in `log` having `"pushed 1"` and `"pushed 2"`, while `q` has `2` and `1`.

`bounded_queue` will probably need a mutex based locking implementation anyway, which provides sequential consistency for free.
