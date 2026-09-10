## 10. Historic Contents

**The Contents in this section is for historic reference only.**

### 10.1. Abandoned Interfaces

#### 10.1.1. Re-opening a Queue

There are use cases for opening a queue that is closed. While we are not aware of an implementation in which the ability to reopen a queue would be a hardship, we also imagine that such an implementation could exist. Open should generally only be called if the queue is closed and empty, providing a clean synchronization point, though it is possible to call open on a non-empty queue. An open operation following a close operation is guaranteed to be visible after the close operation and the queue is guaranteed to be open upon completion of the open call. (But of course, another close call could occur immediately thereafter.)

`void queue::open();`

**Open the queue.**

Note that when `is_closed()` returns false, there is no assurance that any subsequent operation finds the queue closed because some other thread may close it concurrently.

If an open operation is not available, there is an assurance that once closed, a queue stays closed. So, unless the programmer takes care to ensure that all other threads will not close the queue, only a return value of true has any meaning.

Given these concerns with reopening queues, we do not propose wording to reopen a queue.

#### 10.1.2. Non-Blocking Operations

For cases when blocking for mutual exclusion is undesirable, one can consider non-blocking operations. The interface is the same as the try operations but is allowed to also return `queue_op_status::busy` in case the operation is unable to complete without blocking.

`queue_op_status queue::nonblocking_push(const Element&);`\ `queue_op_status queue::nonblocking_push(Element&&);`

**If the operation would block, return `queue_op_status::busy`.
Otherwise, if the queue is full, return `queue_op_status::full`.
Otherwise, push the `Element` onto the queue. Return
`queue_op_status::success`.**

`queue_op_status queue::nonblocking_pop(Element&);`

**If the operation would block, return `queue_op_status::busy`.
Otherwise, if the queue is empty, return `queue_op_status::empty`.
Otherwise, pop the `Element` from the queue. The element will be
moved out of the queue in preference to being copied. Return
`queue_op_status::success`.**

These operations will neither wait nor block. However, they may do nothing.

The non-blocking operations highlight a terminology problem. In terms of synchronization effects, `nonwaiting_push` on queues is equivalent to `try_lock` on mutexes. And so one could conclude that the existing `try_push` should be renamed `nonwaiting_push` and `nonblocking_push` should be renamed `try_push`. However, at least Thread Building Blocks uses the existing terminology. Perhaps better is to not use `try_push` and instead use `nonwaiting_push` and `nonblocking_push`.

**In November 2016, the Concurrency Study Group chose to defer non-blocking operations. Hence, the proposed wording does not include these functions. In addition, as these functions were the only ones that returned `busy`, that enumeration is also not included.**

#### 10.1.3. Push Front Operations

Occasionally, one may wish to return a popped item to the queue. We can provide for this with `push_front` operations.

`void queue::push_front(const Element&);`\ `void queue::push_front(Element&&);`

**Push the `Element` onto the back of the queue, i.e. in at the end of
the queue that is normally popped. Return
`queue_op_status::success`.**

`queue_op_status queue::try_push_front(const Element&);`\ `queue_op_status queue::try_push_front(Element&&);`

**If the queue was full, return `queue_op_status::full`. Otherwise,
push the `Element` onto the front of the queue, i.e. in at the end
of the queue that is normally popped. Return
`queue_op_status::success`.**

`queue_op_status queue::nonblocking_push_front(const Element&);`\ `queue_op_status queue::nonblocking_push_front(Element&&);`

**If the operation would block, return `queue_op_status::busy`.
Otherwise, if the queue is full, return `queue_op_status::full`.
Otherwise, push the `Element` onto the front queue. i.e. in at the
end of the queue that is normally popped. Return
`queue_op_status::success`.**

This feature was requested at the Spring 2012 meeting. However, we do not think the feature works.

- The name `push_front` is inconsistent with existing \"push back\" nomenclature.
- The effects of `push_front` are only distinguishable from a regular push when there is a strong ordering of elements. Highly concurrent queues will likely have no strong ordering.
- The `push_front` call may fail due to full queues, closed queues, etc. In which case the operation will suffer contention, and may succeed only after interposing push and pop operations. The consequence is that the original push order is not preserved in the final pop order. So, `push_front` cannot be directly used as an 'undo'.
- The operation implies an ability to reverse internal changes at the front of the queue. This ability implies a loss efficiency in some implementations.

In short, we do not think that in a concurrent environment `push_front` provides sufficient semantic value to justify its cost. Consequently, the proposed wording does not provide this feature.

#### 10.1.4. Queue Names

It is sometimes desirable for queues to be able to identify themselves. This feature is particularly helpful for run-time diagnotics, particularly when 'ends' become dynamically passed around between threads. See Managed Indirection.

`const char* queue::name();`

**Return the name string provided as a parameter to queue
construction.**

There is some debate on this facility, but we see no way to effectively replicate the facility. However, in recognition of that debate, the wording does not provide the name facility.

#### 10.1.5. Lock-Free Buffer Queue

We provide a concrete concurrent queue in the form of a fixed-size `lock_free_buffer_queue`. It meets the `NonWaitingConcurrentQueue` concept. The queue is still under development, so details may change.

**In November 2016, the Concurrency Study Group chose to defer lock-free queues. Hence, the proposed wording does not include a concrete lock-free queue.**

#### 10.1.6. Storage Iterators

In addition to iterators that stream data into and out of a queue, we could provide an iterator over the storage contents of a queue. Such and iterator, even when implementable, would mostly likely be valid only when the queue is otherwise quiecent. We believe such an iterator would be most useful for debugging, which may well require knowledge of the concrete class. Therefore, we do not propose wording for this feature.

#### 10.1.7. Empty and Full Queues

It is sometimes desirable to know if a queue is empty.

`bool queue::is_empty() const noexcept;`

**Return true iff the queue is empty.**

This operation is useful only during intervals when the queue is known to not be subject to pushes and pops from other threads. Its primary use case is assertions on the state of the queue at the end if its lifetime, or when the system is in quiescent state (where there no outstanding pushes).

We can imagine occasional use for knowing when a queue is full, for instance in system performance polling. The motivation is significantly weaker though.

`bool queue::is_full() const noexcept;`

**Return true iff the queue is full.**

Not all queues will have a full state, and these would always return false.

#### 10.1.8. Queue Ordering

The conceptual queue interface makes minimal guarantees.

- The queue is not empty if there is an element that has been pushed but not popped.
- A push operation *synchronizes with* the pop operation that obtains that element.
- A close operation *synchronizes with* an operation that observes that the queue is closed.
- There is a sequentially consistent order of operations.

In particular, the conceptual interface does not guarantee that the sequentially consistent order of element pushes matches the sequentially consistent order of pops. Concrete queues could specify more specific ordering guarantees.

#### 10.1.9. Lock-Free Implementations

Lock-free queues will have some trouble waiting for the queue to be non-empty or non-full. Therefore, we propose two closely-related concepts. A full concurrent queue concept as described above, and a non-waiting concurrent queue concept that has all the operations except `push`, `wait_push`, `value_pop` and `wait_pop`. That is, it has only non-waiting operations (presumably emulated with busy wait) and non-blocking operations, but no waiting operations. We propose naming these `WaitingConcurrentQueue` and `NonWaitingConcurrentQueue`, respectively.

Note: Adopting this conceptual split requires splitting some of the facilities defined later.

For generic code it's sometimes important to know if a concurrent queue has a lock free implementation.

`constexpr static bool queue::is_always_lock_free() noexcept;`

**Return true iff the has a lock-free implementation of the
non-waiting operations.**

### 10.2. Abandoned Additional Conceptual Tools

There are a number of tools that support use of the conceptual interface. These tools are not part of the queue interface, but provide restricted views or adapters on top of the queue useful in implementing concurrent algorithms.

#### 10.2.1. Fronts and Backs

Restricting an interface to one side of a queue is a valuable code structuring tool. This restriction is accomplished with the classes `generic_queue_front` and `generic_queue_back` parameterized on the concrete queue implementation. These act as pointers with access to only the front or the back of a queue. The front of the queue is where elements are popped. The back of the queue is where elements are pushed.

```cpp
void send( int number, generic_queue_back<buffer_queue<int>> arv );
```

These fronts and backs are also able to provide `begin` and `end` operations that unambiguously stream data into or out of a queue.

#### 10.2.2. Streaming Iterators

In order to enable the use of existing algorithms streaming through concurrent queues, they need to support iterators. Output iterators will push to a queue and input iterators will pop from a queue. Stronger forms of iterators are in general not possible with concurrent queues.

Iterators implicitly require waiting for the advance, so iterators are only supportable with the `WaitingConcurrentQueue` concept.

```cpp
void iterate(
    generic_queue_back<buffer_queue<int>>::iterator bitr,
    generic_queue_back<buffer_queue<int>>::iterator bend,
    generic_queue_front<buffer_queue<int>>::iterator fitr,
    generic_queue_front<buffer_queue<int>>::iterator fend,
    int (*compute)( int ) )
{
    while ( fitr != fend && bitr != bend )
        *bitr++ = compute(*fitr++);
}
```

Note that contrary to existing iterator algorithms, we check both iterators for reaching their end, as either may be closed at any time.

Note that with suitable renaming, the existing standard front insert and back insert iterators could work as is. However, there is nothing like a pop iterator adapter.

#### 10.2.3. Binary Interfaces

The standard library is template based, but it is often desirable to have a binary interface that shields client from the concrete implementations. For example, `std::function` is a binary interface to callable object (of a given signature). We achieve this capability in queues with type erasure.

We provide a `queue_base` class template parameterized by the value type. Its operations are virtual. This class provides the essential independence from the queue representation.

We also provide `queue_front` and `queue_back` class templates parameterized by the value types. These are essentially `generic_queue_front<queue_base<Value>>` and `generic_queue_front<queue_base<Value>>`, respectively.

To obtain a pointer to `queue_base` from an non-virtual concurrent queue, construct an instance the `queue_wrapper` class template, which is parameterized on the queue and derived from `queue_base`. Upcasting a pointer to the `queue_wrapper` instance to a `queue_base` instance thus erases the concrete queue type.

```cpp
extern void seq_fill( int count, queue_back<int> b );

buffer_queue<int> body( 10 /*elements*/, /*named*/ "body" );
queue_wrapper<buffer_queue<int>> wrap( body );
seq_fill( 10, wrap.back() );
```

#### 10.2.4. Managed Indirection

Long running servers may have the need to reconfigure the relationship between queues and threads. The ability to pass 'ends' of queues between threads with automatic memory management eases programming.

To this end, we provide `shared_queue_front` and `shared_queue_back` template classes. These act as reference-counted versions of the `queue_front` and `queue_back` template classes.

The `share_queue_ends(Args ... args)` template function will provide a pair of `shared_queue_front` and `shared_queue_back` to a dynamically allocated `queue_object` instance containing an instance of the specified implementation queue. When the last of these fronts and backs are deleted, the queue itself will be deleted. Also, when the last of the fronts or the last of the backs is deleted, the queue will be closed.

```cpp
auto x = share_queue_ends<buffer_queue<int>>( 10, "shared" );
shared_queue_back<int> b(x.back);
shared_queue_front<int> f(x.front);
f.push(3);
assert(3 == b.value_pop());
```

### 10.3. API Discussions

#### 10.3.1. `try_push(T&&, T&)`

**REVISITED in Varna**

The following version was introduced in response to LEWG-I concerns about loosing the element if an rvalue cannot be stored in the queue.

`queue_op_status queue::try_push(T&&, T&);`

However, SG1 reaffirmed the APIs above with the following rationale:

It seems that it is possible not to loose the element in both versions:

```cpp
T x = get_something();
if (q.try_push(std::move(x))) ...
```

With two parameter version:

```cpp
T x;
if (q.try_push(get_something(), x)) ...
```

Ergonomically they are roughly identical. API is slightly simpler with one argument version, therefore, we reverted to original one argument version.

#### 10.3.2. `try_pop` Queue Status Return

This is the interface agreed on in St. Louis, based on discussion in [[P2921R0]](https://wg21.link/p2921r0):

POLL: LEWG would like to add a `std::expected` interface for concurrent queues.

| SF | F | N | A | SA |
| --- | --- | --- | --- | --- |
| 0 | 2 | 5 | 3 | 2 |

However, [[P2921R0]](https://wg21.link/p2921r0) mainly compares `std::expected` vs. exceptions. Now concurrent queue operations don’t throw own exceptions anymore (they might forward exceptions from constructors).

For `try_pop` [[P2921R0]](https://wg21.link/p2921r0) has the following example:

##### 10.3.2.1. Drain the queue without blocking

```cpp
conqueue_errc ec;
while (auto val = q.try_pop(ec))
   println("got {}", *val);
if (ec == conqueue_errc::closed)
  return;
// do something else.
```

`std::expected` based has unfortunate duplication since we want to know why the pop failed and we have to move `val` out of the loop condition.

```cpp
auto val = q.try_pop();
while (val) {
  println("got {}", *val);
  val = q.try_pop();
}
if (val.error() == conqueue_errc::closed)
  return;
// do something else
```

So for `while` loops with the `try_pop` inside the loop condition the separate output parameter has advantages.

The logging example above shows a case where `expected` might be considered to be superior. So it might make sense to revisit the decision from St. Louis.


## References

### Non-Normative References

**[BoostLFQ]**
: [Boost Lock-Free Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/queue.html). URL: [https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/queue.html](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/queue.html)

**[BoostLFSPSCQ]**
: [Boost Lock-Free SPSC Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/spsc_queue.html). URL: [https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/spsc_queue.html](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/spsc_queue.html)

**[BoostMQ]**
: [Boost Message Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/interprocess/message_queue_t.html). URL: [https://www.boost.org/doc/libs/1_85_0/doc/html/boost/interprocess/message_queue_t.html](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/interprocess/message_queue_t.html)

**[BoostSQ]**
: [Boost Synchronized Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html). URL: [https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html)

**[Hughes97]**
: Cameron Hughes; Tracey Hughes. Object-Oriented Multithreading Using C++.

**[P0387R1]**
: [Memory Model Issues for Concurrent Data Structures (P0387R1)](https://wg21.link/P0387R1). URL: [https://wg21.link/P0387R1](https://wg21.link/P0387R1)

**[P0495]**
: [Concurrency Safety in C++ Data Structures (P0495)](https://wg21.link/P0495). URL: [https://wg21.link/P0495](https://wg21.link/P0495)

**[P1958]**
: [C++ Concurrent Buffer Queue (P1958)](https://wg21.link/P1958). URL: [https://wg21.link/P1958](https://wg21.link/P1958)

**[P2921R0]**
: Gor Nishanov, Detlef Vollmann. [Exploring std::expected based API alternatives for buffer_queue](https://wg21.link/p2921r0). 5 July 2023. URL: [https://wg21.link/p2921r0](https://wg21.link/p2921r0)

**[P3570]**
: [P3570R0: optional variants in sender/receiver](https://wg21.link/P3570). URL: [https://wg21.link/P3570](https://wg21.link/P3570)

**[P3669]**
: [Non-Blocking Support for `std::execution` (P3669)](https://wg21.link/P3668). URL: [https://wg21.link/P3668](https://wg21.link/P3668)

**[P4295]**
: [Single Ends for C++ Concurrent Queues (P4295)](https://wg21.link/P4295). URL: [https://wg21.link/P4295](https://wg21.link/P4295)

**[TBBQB]**
: [TBB Bounded Queue](https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_bounded_queue_cls.html). URL: [https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_bounded_queue_cls.html](https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_bounded_queue_cls.html)

**[TBBQUB]**
: [TBB Unbounded Queue](https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_queue_cls.html). URL: [https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_queue_cls.html](https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_queue_cls.html)

**[Williams17]**
: Anthony Williams. C++ Concurrency in Action.
