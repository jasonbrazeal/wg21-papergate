## 8. Proposed Wording

Suggested location of concurrent queues in the standard is [thread].

### 8.1. Header `<version>` synopsis [version.syn]

```cpp
#define __cpp_lib_conqueue <editor supplied value> // also in <conqueue>
```

### 8.2. Concurrent Queues [conqueues]

#### 8.2.1. General [conqueues.general]

Concurrent queues provide a mechanism to transfer objects from one point in a program to another without producing data races. Push operations insert objects into a queue from one execution context and pop operations retrieve them typically from another execution context. Push and pop operations can be blocking, non-blocking or asynchronous. If a queue gets closed, any subsequent push operations will fail with a respective queue status. Any pop operations after a close will succeed while there are still objects in the queue and fail afterwards. Any pending operations will be resumed on a close with a failure indication.

#### 8.2.2. Header `<conqueue>` synopsis [conqueues.syn]

```cpp
namespace std {
  enum class conqueue_status {
    success = unspecified,
    empty = unspecified,
    full = unspecified,
    closed = unspecified,
    busy = unspecified,
    busy_async = unspecified
  };

  template <class Q>
    concept basic_concurrent_queue;
  template <class Q>
    concept concurrent_queue;
  template <class Q>
    concept async_concurrent_queue;

  struct error-as-optional-t { see below }; // exposition only
  struct error-as-bool-t { see below }; // exposition only

  inline constexpr error-as-optional-t error-as-optional; // exposition only
  inline constexpr error-as-bool-t error-as-bool; // exposition only

  struct async-pop-env { // exposition only
    auto query(get_await_completion_adapter_t) const -> error-as-optional-t {
      return {};
    }
  }
  struct async-push-env { // exposition only
    auto query(get_await_completion_adapter_t) const -> error-as-bool-t {
      return {};
    }
  }

  template <class T, class Allocator = allocator<T>>
  class bounded_queue;

  namespace pmr {
    template<class T>
    using bounded_queue = std::bounded_queue<T, polymorphic_allocator<T>>;
}
}
```

#### 8.2.3. Concurrent Queue Concepts [conqueue.concept]

##### 8.2.3.1. Basic Concurrent Queue Concept [conqueue.concept.basic]

1. The concept `basic_concurrent_queue` defines the requirements for a basic queue type.

   ```cpp
   namespace std {
     template <class Q>
       concept basic_concurrent_queue =
         move_constructible<typename Q::value_type> &&
         requires (Q q, const Q cq, typename Q::value_type &&t) {
           { cq.is_closed() } noexcept -> same_as<bool>;
           { q.close() } noexcept -> same_as<void>;
           { q.push(std::forward<typename Q::value_type>(t)) } -> same_as<bool>;
           { []<class... Args>(Q &q, Args... args) { bool b{q.emplace(std::forward<Args>(args)...)}; } };
           { q.pop() } -> same_as<optional<typename Q::value_type>>;
         };
   }
   ```
2. In the following description, `Q` denotes a type modeling the `basic_concurrent_queue` concept, `q` denotes an object of type `Q`, and `t` denotes an object convertible to `Q::value_type`.
3. The expression `q.is_closed()` has the following semantics:
   1. *Returns:* `true` if the queue is closed, `false` otherwise.
4. The expression `q.close()` has the following semantics:
   1. *Effects:* Closes the queue.
5. `q.push(std::forward<T>(t))` and `q.emplace(std::forward<Args>(args)...)` are *push operations* and `q.pop()` is a *pop operation*.
6. A push operation *deposits* an object into a queue. Hereby it is made available to be *extracted* from the queue. A pop operation extracts and returns an object from a queue. *push-deposited* is the event when the object is made available. *pop-claimed* is the event when a pop operation decides to extract the object.
7. If an object `t` is deposited by a push operation and there is at least one pop operation blocked on `q`, one of those pop operations will be unblocked. [*Note:* This unblocking is not required to be fair.]
8. If an object `t` is extracted by a pop operation and there is at least one push operation blocked on `q`, one of those push operations will be unblocked. [*Note:* This unblocking is not required to be fair.]
9. If an object `t` is deposited by a push operation, the call of the constructor of this object inside the queue’s storage strongly happens before the return of the pop operation that extracts `t`. A pop operation on a queue shall only extract objects that were deposited into the same queue and each object shall only be extracted once.

   [*Note:* This doesn’t specify when the *push-deposited* actually happens during the push operation, and likewise the *pop-claimed* during the pop operation. So it can happen that a pop operation already claimed a specific object but is blocked because the constructor of the object hasn’t finished yet. -- end note]
10. Calls to operations (except constructor and destructor) on the same queue from different threads of execution do not introduce data races.
11. [*Note:* This concept doesn’t specify whether a push may block for space available in the queue (bounded queue) or whether a push may allocate new space (unbounded queue). -- end note]
12. The expression `q.emplace(args...)` has the following semantics:
    1. *Effects:* If the queue is not closed, a value is deposited into `q`. In this case the value in the queue storage is direct-non-list-initialized with `std::forward<Args>(args)...`.
    2. *Returns:*
       - `true` if `t` was deposited into `q`; `false` otherwise.
    3. *Throws:* Any exception thrown by the selected constructor of `T`. An `emplace` may throw additional exceptions. If an exception is thrown, no value is deposited into `q`.
13. The expression `q.push(t)` is equivalent to `return q.emplace(std::forward<T>(t))`.
14. The expression `q.pop()` has the following semantics:
    1. *Effects:* Blocks the current thread until there is an object available in the queue or until the queue is closed. If there is an object available in the queue, extracts the object and returns an `optional<T>` with a move-constructed value. Otherwise, if the queue is closed returns a default constructed `optional<T>`.
    2. *Returns:* as specified above.
    3. *Throws:* Any exception thrown by the selected constructor of `T`. A `pop` may throw additional exceptions. Even if an exception is thrown, the value is extracted from `q`.

##### 8.2.3.2. Concurrent Queue Concept [conqueue.concept.concurrent]

1. The concept `concurrent_queue` defines the requirements for a concurrent queue type.

   ```cpp
   namespace std {
     template <class Q>
       concept concurrent_queue =
         basic_concurrent_queue<Q> &&
         requires (Q q, typename Q::value_type &&t, conqueue_status ec) {
           { q.try_push(std::forward<typename Q::value_type>(t)) } -> same_as<conqueue_status>;
           { []<class... Args>(Q &q, Args... args) { conqueue_status e{q.try_emplace(std::forward<Args>(args)...)}; } }  ;
           { q.try_pop() } -> same_as<expected<typename Q::value_type, conqueue_status>>;
         };
   }
   ```
2. `try_push`, `try_emplace` and `try_pop` are `noexcept` if the selected constructor of `T` is `noexcept`.
3. In the following description, `Q` denotes a type modeling the `concurrent_queue` concept, `q` denotes an object of type `Q`, `t` denotes an object convertible to `Q::value_type` and `ec` denotes an object of type `conqueue_status`.
4. `try_push` and `try_emplace` are push operations if they deposit an object into the queue and `try_pop` is a pop operation if it extracts an object from a queue.
5. `try_push` or `try_emplace` may return `conqueue_status::full` even if the queue has space for the element. Similarly `try_pop` may return an `unexpected` with values `conqueue_status::empty` even if the queue has an element to be extracted. [*Note:* This spurious failure is normally uncommon but allows for more implementation options. -- end note] An implementation should ensure that thes functions do not consistently spuriously fail in the absence of contending such operations.
6. The expression `q.try_emplace(t)` has the following semantics:
   1. *Effects:* If the queue is not closed, and space is available in the queue, a value is deposited into `q`. In this case the value in the queue storage is direct-non-list-initialized with `std::forward<Args>(args)...` without blocking.
   2. *Returns:*
      - `conqueue_status::success` if `t` was deposited into `q`,
      - `conqueue_status::closed` if the queue is closed,
      - `conqueue_status::full` if the queue doesn’t have space,
      - `conqueue_status::busy` if the operation would block for internal synchronization,
      - `conqueue_status::busy_async` if the queue also models the `async_concurrent_queue` concept, the operation would have to schedule the continuation of an `async_pop`, and the implementation can not detect if this scheduling would block for internal synchronization of the scheduler.
   
      [*Note:* An implementation may return consistently `conqueue_status::busy_async` if there are only `async_pop` operations waiting.]
   3. *Throws:* Any exception thrown by the selected constructor of `T`. A `try_emplace` may throw additional exceptions. If an exception is thrown, no value is deposited into `q`.
7. The expression `q.try_push(t)` is equivalent to `return q.try_emplace(std::forward<T>(t))`.
8. The expression `q.try_pop()` has the following semantics:
   1. *Effects:* If there is an object available in the queue it will be extracted from the queue and returned without blocking.
   2. *Returns:* An object of type `expected<T, conqueue_status>`. The return value will contain a move-constructed value of type `T` if a value could be extracted. Otherwise an `unexpected` will be returned with the value:
      - `conqueue_status::closed` if the queue is closed,
      - `conqueue_status::empty` if the queue doesn’t have an object available,
      - `conqueue_status::busy` if the operation would block for internal synchronization,
      - `conqueue_status::busy_async` if the queue also models the `async_concurrent_queue` concept, the operation would have to schedule the continuation of an `async_push`, and the implementation can not detect if this scheduling would block for internal synchronization of the scheduler.
   
      [*Note:* An implementation may return consistently `conqueue_status::busy_async` if there are only `async_push` operations waiting.]
   3. *Throws:* Any exception thrown by the selected constructor of `T`. A `try_pop` may throw additional exceptions. Even if an exception is thrown, the value is extracted from `q`.

##### 8.2.3.3. Asynchronous Queue Concept [conqueue.concept.async]

1. The concept `async_concurrent_queue` defines the requirements for an asynchronous queue type.

   ```cpp
   namespace std {
     template <class Q>
       concept async_concurrent_queue =
         basic_concurrent_queue<Q> &&
         requires (Q q, typename Q::value_type &&t) {
           { q.async_push(std::forward<typename Q::value_type>(t)) } noexcept;
           { q.async_emplace(std::forward<typename Q::value_type>(t)) } noexcept;
           { []<class... Args>(Q &q, Args... args) { q.async_emplace(std::forward<Args>(args)...)}; };
           { q.async_pop() } noexcept;
         };
   }
   ```
2. The exposition only name *error-as-optional* denotes a pipeable sender adaptor object. For a subexpression `sndr`, let `Sndr` be `decltype((sndr))`. The expression *error-as-optional*`(sndr)` is expression-equivalent to:

   ```cpp
   transform_sender(
     get-domain-early(sndr),
     make-sender(error-as-optional, {}, sndr))
   ```

   except that `sndr` is only evaluated once.
3. Let `sndr` and `env` be subexpressions such that `Sndr` is `decltype((sndr))` and `Env` is `decltype((env))`. The expression *error-as-optional*`.transform_sender(sndr, env)` is equivalent to:

   ```cpp
   auto&& [_, _, child] = sndr;
   return let_error(
     then(std::forward_like<Sndr>(child),
          [](T &&) noexcept(is_nothrow_move_constructible_v<T>) {
            return optional<T>(in_place, std::move(t));
          }),
     [](auto e) noexcept {
       if constexpr (is_same_v<decltype(e), conqueue_status>) {
         return just(optional<T>());
       } else {
         return just_error(e);
       }
     });
   ```
4. The exposition only name *error-as-bool* denotes a pipeable sender adaptor object. For a subexpression `sndr`, let `Sndr` be `decltype((sndr))`. The expression *error-as-bool*`(sndr)` is expression-equivalent to:

   ```cpp
   transform_sender(
     get-domain-early(sndr),
     make-sender(error-as-bool, {}, sndr))
   ```

   except that `sndr` is only evaluated once.
5. Let `sndr` and `env` be subexpressions such that `Sndr` is `decltype((sndr))` and `Env` is `decltype((env))`. The expression *error-as-bool*`.transform_sender(sndr, env)` is equivalent to:

   ```cpp
   auto&& [_, _, child] = sndr;
   return let_error(
     then(std::forward_like<Sndr>(child),
          []() noexcept { return just(true); }),
     [](auto e) noexcept {
       if constexpr (is_same_v<decltype(e), conqueue_status>) {
         return just(false);
       } else {
         return just_error(e);
       }
     });
     []() noexcept { return false; });
   ```
6. In the following description, `Q` denotes a type modeling the `async_concurrent_queue` concept, `q` denotes an object of type `Q` and `t` denotes an object convertible to `Q::value_type`.
7. `async_push` and `async_emplace` are push operations and `async_pop` is a pop operations.
8. The expression `q.async_emplace(args...)` has the following semantics:
   1. Let `w` be a sender object returned by the expression, `op` be an operation state obtained from connecting `w` to a receiver `r` and `st` be a stop token returned from `get_stop_token(get_env(w))`.
   2. *Returns:* A sender object `w` that behaves as follows:
      1. After `op.start()` is called, a completion function of `r` is called when there s space in the queue or when the queue is closed.
      2. If `st.stop_requested()` returns `true` `set_stopped(r)` will be called.
      3. If there is space in the queue `t` will be deposited into the queue and `set_value(r)` will be called. The value in the queue storage is direct-non-list-initialized with `std::forward<Args>(args)...`.
      4. If the selected constructor throws an exception, `set_error(r, current_exception())` will be called. No value will be deposited into `q`.
      5. If the queue is closed `set_error(r, conqueue_status::closed)` will be called.
      6. `set_value()`, `set_stopped()` or `set_error()` will be called on the scheduler of `r`.
      7. `get_env(w)` returns an object of tye *async-push-env*.
9. The expression `q.async_push(t)` is equivalent to `return q.async_emplace(std::forward<T>(t))`.
10. The expression `q.async_pop()` has the following semantics:
    1. Let `w` be a sender object returned by the expression, `op` be an operation state obtained from connecting `w` to a receiver `r` and `st` be a stop token returned from `get_stop_token(get_env(w))`.
    2. *Returns:* A sender object `w` that behaves as follows:
       1. After `op.start()` is called, a completion function of `r` is called when there is an object available in the queue or when the queue is closed.
       2. If `st.stop_requested()` returns `true` `set_stopped(r)` will be called.
       3. If there is an object `t` available in the queue it will be extracted and `set_value(r, std::move(t))` will be called.
       4. If the selected constructor for `set_value` throws an exception, `set_error(r, current_exception())` will be called. The value will be extracted from the queue nevertheless.
       5. If the queue is closed `set_error(r, conqueue_status::closed)` will be called.
       6. `set_value()`, `set_stopped()` or `set_error()` will be called on the scheduler of `r`.
       7. `get_env(w)` returns an object of tye *async-pop-env*.

#### 8.2.4. Class template `bounded_queue` [bounded.queue]

##### 8.2.4.1. General [bounded.queue.general]

1. A `bounded_queue` models `concurrent_queue` and `async_concurrent_queue` and can hold a fixed number of objects which is given at construction time.
2.
   ```cpp
   template <class T,
     class Allocator = allocator<T>>
   class bounded_queue
   {
     bounded_queue(bounded_queue&&) = delete;
   
   public:
     using value_type = T;
     using allocator_type = Allocator;
   
     // construct/destroy
     explicit bounded_queue(size_t max_elems, const Allocator& alloc = {});
   
     ~bounded_queue();
   
     // observers
     bool is_closed() const noexcept;
   
     allocator_type get_allocator() const;
   
     // modifiers
     void close() noexcept;
   
     bool push(const T& x);
     bool push(T&& x);
     template <class... Args> bool emplace(Args &&... as);
   
     conqueue_status try_push(const T& x);
     conqueue_status try_push(T&& x);
     template <class... Args> conqueue_status try_emplace(Args &&... as);
   
     sender auto async_push(const T&);
     sender auto async_push(T&&);
     template <class... Args> sender auto async_emplace(Args &&... as);
   
     optional<T> pop();
     expected<T, conqueue_status> try_pop();
     sender auto async_pop();
   
   private:
     allocator_type alloc;      // exposition only
   };
   ```
3. `T` shall be a type that meets the *Cpp17Destructible* requirements (Table [tab:cpp17.destructible]).
4. Template argument `Allocator` shall satisfy the *Cpp17Allocator* requirements ([allocator.requirements]). An instance of `Allocator` is maintained by the `bounded_queue` object during the lifetime of the object. The allocator instance is set at `bounded_queue` object creation time.
5. The values inside the storage of the queue deposited by push operations are constructed using `allocator_traits<Allocator>::construct(alloc, p, std::forward<T>(x))`, where `p` is the address of the element being constructed.

##### 8.2.4.2. Constructor [bounded.queue.ctor]

```cpp
explicit bounded_queue(size_t max_elems, const Allocator& alloc = Allocator());
```

1. *Effects*: Constructs an object with no elements, but with storage for `max_elems`. The storage for the elements will be allocated using `alloc`.
2. *Remarks*: The operations of `bounded_queue` will not allocate any memory outside the constructor.

##### 8.2.4.3. Destructor [bounded.queue.dtor]

```cpp
~bounded_queue();
```

1. *Effects*: Destroys all objects in the queue and deallocates the storage for the elements using `alloc`.

##### 8.2.4.4. Allocator [bounded.queue.alloc]

```cpp
allocator_type get_allocator() const;
```

1. *Returns*: A copy of the `Allocator` that was passed to the object’s constructor.

##### 8.2.4.5. Modifiers [bounded.queue.modifiers]

1. The push and pop operations of `bounded_queue` provide sequentially consistent semantics.

```cpp
void push(const T& x);
void push(T&& x);
template <class... Args> bool emplace(Args &&... as);
```

1. *Effects*: Blocks the current thread until there is space in the queue or until the queue is closed.
2. Let *Push1* and *Push2* be push operations and *Pop1* and *Pop2* be pop operations, where *Pop1* returns the value of the parameter given to *Push1* and *Pop2* returns the value of the parameter given to *Push2*. There is a total order `Q` shared by all `bounded_queue` objects consistent with the single total order `S` of `memory_order::seq_cst` operations [atomics.order]p4 of *push-deposited* and *pop-claimed* of *Push1*, *Push2*, *Pop1* and *Pop2*, and moreover if *push-deposited* of *Push1* is before *push-deposited* of *Push2* in that order, then *pop-claimed* of *Pop1* is before *pop-claimed* of *Pop2* in that order. [*Note:* This paragraph’s intent is enabling implementations based on acquire and release operations under the SC-for-DRF theorem. --end note]
3. It is unspecified whether the constructors and destructors of the objects in the internal storage of the queue run under a lock of the queue implementation.
4. [*Note:* This guarantees FIFO behaviour, but for two concurrent pushes the constructors cannot determine the order in which the values are enqueued, and the constructors can run concurrently as well. -- end note]
5. [*Note:* This does not guarantee that constructors or destructors may ever run concurrently. An implementation may decide that two pushes (or two pops) never run concurrently. -- end note]
6. [*Note:* A constructor or destructor can deadlock if it tries a push or pop on the same queue. -- end note]

```cpp
T pop();
optional<T> pop();
expected<T, conqueue_status> try_pop();
sender auto async_pop();
```

1. *Effects*: The object in the queue is destroyed using `allocator_traits<Allocator>::destroy`.
2. *Remarks:* The constructor of the returned object and the destructor of the internal object run on the same thread of execution.

```cpp
bool is_closed() const noexcept;
void close() noexcept;
conqueue_status try_push(const T& x);
conqueue_status try_push(T&& x);
template <class... Args> conqueue_status try_emplace(Args &&... as);
sender auto async_push(const T&);
sender auto async_push(T&&);
template <class... Args> sender auto async_emplace(Args &&... as);
```

1. These functions behave as described in the respective concepts.


## 9. Old Revision History

P0260R6 revises P0260R5 - 2023-01-15 as follows.

- Fixing typos.
- Added a scope for the target TS.
- Added questions to be answered by a TS.
- Added asynchronous interface

P0260R5 revises P0260R4 - 2020-01-12 as follows.

- Added more introductory material.
- Added response to feedback by LEWGI at Prague meeting 2020.
- Added section on existing practice.
- Replaced `value_pop` with `pop`.
- Replaced `is_lock_free` with `is_always_lockfree`.
- Removed `is_empty` and `is_full`.
- Added move-into parameter to `try_push(Element&&)`
- Added note that exception thrown by the queue operations themselves are derived from `std::exception`.
- Added a note that the wording is partly invalid.
- Moved more contents into the "Abandoned" part to avoid confusion.

P0260R4 revised P0260R3 - 2019-01-20 as follows.

- Remove the binding of `queue_op_status::success` to a value of zero.
- Correct stale use of the `Queue` template parameter in `shared_queue_front` to `Value`.
- Change the return type of `share_queue_ends` from a `pair` to a custom struct.
- Move the concrete queue proposal to a separate paper, [[P1958]](https://wg21.link/P1958).

P0260R3 revised P0260R2 - 2017-10-15 as follows.

- Convert `queue_wrapper` to a `function`-like interface. This conversion removes the `queue_base` class. Thanks to Zach Lane for the approach.
- Removed the requirement that element types have a default constructor. This removal implies that statically sized buffers cannot use an array implmentation and must grow a vector implementation to the maximum size.
- Added a discussion of checking for output iterator end in the wording.
- Fill in synopsis section.
- Remove stale discussion of `queue_owner`.
- Move all abandoned interface discussion to a new section.
- Update paper header to current practice.

P0260R2 revised P0260R1 - 2017-02-05 as follows.

- Emphasize that non-blocking operations were removed from the proposed changes.
- Correct syntax typos for noexcept and template alias.
- Remove `static` from `is_lock_free` for `generic_queue_back` and `generic_queue_front`.

P0260R1 revised P0260R0 - 2016-02-14 as follows.

- Remove pure virtuals from `queue_wrapper`.
- Correct `queue::pop` to `value_pop`.
- Remove nonblocking operations.
- Remove non-locking buffer queue concrete class.
- Tighten up push/pop wording on closed queues.
- Tighten up push/pop wording on synchronization.
- Add note about possible non-FIFO behavior.
- Define `buffer_queue` to be FIFO.
- Make wording consistent across attributes.
- Add a restriction on element special methods using the queue.
- Make `is_lock_free()` for only non-waiting functions.
- Make `is_lock_free()` static for non-indirect classes.
- Make `is_lock_free() noexcept`.
- Make `has_queue() noexcept`.
- Make destructors `noexcept`.
- Replace "throws nothing" with `noexcept`.
- Make the remarks about the usefulness of `is_empty()` and `is_full` into notes.
- Make the non-static member functions `is_...` and `has_...` functions `const`.

P0260R0 revised N3533 - 2013-03-12 as follows.

- Update links to source code.
- Add wording.
- Leave the name facility out of the wording.
- Leave the push-front facility out of the wording.
- Leave the reopen facility out of the wording.
- Leave the storage iterator facility out of the wording.

N3532 revised N3434 = 12-0124 - 2012-09-23 as follows.

- Add more exposition.
- Provide separate non-blocking operations.
- Add a section on the lock-free queues.
- Argue against push-back operations.
- Add a cautionary note on the usefulness of `is_closed()`.
- Expand the cautionary note on the usefulness of `is_empty()`. Add `is_full()`.
- Add a subsection on element type requirements.
- Add a subsection on exception handling.
- Clarify ordering constraints on the interface.
- Add a subsection on a lock-free concrete queue.
- Add a section on content iterators, distinct from the existing streaming iterators section.
- Swap front and back names, as requested.
- General expository cleanup.
- Add an "Revision History" section.

N3434 revised N3353 = 12-0043 - 2012-01-14 as follows.

- Change the inheritance-based interface to a pure conceptual interface.
- Put `try_...` operations into a separate subsection.
- Add a subsection on non-blocking operations.
- Add a subsection on push-back operations.
- Add a subsection on queue ordering.
- Merge the "Binary Interface" and "Managed Indirection" sections into a new "Conceptual Tools" section. Expand on the topics and their rationale.
- Add a subsection to "Conceptual Tools" that provides for type erasure.
- Remove the "Synopsis" section.
- Add an "Implementation" section.
