---
title: "C++ Concurrent Queues"
document: P0260R20
date: 2026-07-12
audience: LEWG
reply-to:
  - "Detlef Vollmann <dv@vollmann.ch>"
  - "Detlef Vollmann <dv@vollmann.ch>"
  - "Detlef Vollmann <dv@vollmann.ch>"
---


## Abstract

Concurrent queues are a fundamental structuring tool for concurrent programs. We propose concurrent queue concepts and a concrete implementation.


## 1. Acknowledgments

Thanks to David Goldblatt, Daniel Krügler, Dietmar Kühl, Jens Maurer and Gonzalo Brito for their help with the wording!


## 2. Revision History

This paper revises P0260R19 - 2025-06-18 as follows:

- added more rationale for concepts
- made concepts non-exposition-only as decided by SGI in Brno
- fixed some typos

P0260R19 revises P0260R18 - 2025-06-17 as follows:

- renamed `std::conqueue_errc` to `std::conqueue_status` as decided by LEWG in Sofia

P0260R18 revises P0260R17 - 2025-04-15 as follows:

- fixed wording based on feedback from Daniel Krügler
- added a paragraph in the design section that clearly states that the concepts don’t require FIFO ordering
- added missing note for unfairness of unblocking pop operations
- aligned spurious failure wording with `mutex::try_lock`
- added note about acquire/release SC-for-DRF

P0260R17 revises P0260R16 - 2025-02-18 as follows:

- added wording to specify the unblocking of waiters
- added more explanantion for `busy_async`

P0269R16 revises P0260R15 - 2025-02-13 as follows:

- removed exception support helpers
- removed discussion points and possible LEWG polls
- changed `try_pop` to not take an output parameter but return `expected`
- moved discussion for `expected` to historic contents
- introduced order `Q` for sequential consistency
- added wording to make clear that a value is removed from a queue if the constructor called by a pop operation throws an exception
- added list with wording still to be reviewed

P0260R15 revises P0260R14 - 2025-01-12 as follows:

- added more introductory description for the proposed wording
- updated examples and design section to reflect `set_error` for `async_push` and `async_pop`
- provided generally more rationale
- added wording for stop tokens
- added possible polls for LEWG
- fixed wording for `pop`
- removed `strongly happens before` for pop operations
- added `busy_async`
- added `get_await_completion_adapter_t` from P3570 with *error-as-optional* to return an `optional<T>` for coroutines form `async_pop`
- added *error-as-bool* to return a `bool` for coroutines from `async_push`

P0260R14 revises P0260R13 - 2024-12-10 as follows.

- updated wording based on feedback from Dietmar and Jens
- added example for non-blocking functions
- added discussion for std::expected
- added discussion for async sender behaviour
- wording now proposes for `async_push` and `async_pop` to call `set_error` on a closed queue

P0260R13 revises P0260R12 - 2024-11-21 as follows.

- added `success` to `conqueue_errc`
- updated error handling
- added rationale for concepts
- updated API (error handling, return types, emplace), including rationale
- updated examples

P0260R12 revises P0260R11 - 2024-10-12 as follows.

- Implemented feedback from LEWG and SG1 in St. Louis:
  - Added wording for allocator awareness
  - Added rationale for not providing single-ended interfaces
  - Added rationale for `bounded_queue` not being movable
  - Added rationale for `bounded_queue` not providing `emplace`
- Implemented feedback from SG1 in Wroclaw:
  - Fixed wording for sequential consistency
  - Fixed wording for `async_*`
  - Fixed ordering specification of `bounded_queue`
- Provided usage examples

P0260R11 revises P0260R10 - 2024-06-26 as follows.

- Implement feedback from LEWG and SG1 in St. Louis:
- Make concept exposition only
- Require async operations to run on the scheduler of the receiver of the operation
- Call `set_error` for async operations if queue is closed
- Reintroduced accidentally removed data-race freeness from R9
- Require sequential constistent semantics for `bounded_queue`
- Remove `experimental` leftovers

P0260R10 revises P0260R9 - 2024-05-19 as follows.

- Implement feedback from SG1 in St. Louis:
- Split concept into three
- Require `try_*` to be lockfree (w/ error code `busy`)
- Drop `is_always_lock_free`
- Drop `capacity()`
- Removed discussion points forSG1
- Removed TS ship vehicle
- General cleanup in the design part

P0260R9 revises P0260R8 - 2024-03-08 as follows.

- Added more wording
- Fixed `capacity`
- Changed push/pop wording to use "strongly happens before"
- Added discussion points
- Removed paragraph about ctors/dtors returning on same thread
- `try_*` now never blocks (even for contention on internal synchronization)
- Wording for spurious failures of `try_*`
- The constructors for `bounded_queue` that pre-fill the queue have been removed
- Reference to P3282 added
- Moved discussion about `try_push(T &&, T &)` to historic contents.

P0260R8 revises P0260R7 - 2023-06-15 as follows.

- Restructured document
- Fix typos
- Implement LEWG feedback to derive conqueue_errc from system_error
- Implement LEWG feedback to add range constructor and go back to InputIterator
- size_t capacity() added
- Added TBB concurrent_bounded_queue as existing practice
- Moved discussion about pop() interface to separate paper
- reintegrated P1958 `buffer_queue`
- Renamed `buffer_queue` to `bounded_queue`
- Added proposed wording (incomplete)
- Updated TS questions

Older revision history was moved to after the proposed wording.

### 2.1. Review Topics

#### 2.1.1. LEWG

- decision about named concepts


## 3. Introduction

Queues provide a mechanism for communicating data between components of a system.

The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations. So, concurrent pushes and pops on queues require a different interface to the queue structure.

Moreover, concurrency adds a new dimension for performance and semantics. Different queue implementation must trade off uncontended operation cost, contended operation cost, and element order guarantees. Some of these trade-offs will necessarily result in semantics weaker than a serial queue.

Concurrent queues come in a several different flavours, e.g.

- bounded vs. unbounded
- blocking vs. overwriting
- single-ended vs. multi-ended
- strict FIFO ordering vs. priority based ordering

The syntactic concepts proposed here should be valid for all of these flavours, while the concrete semantics might differ.


## 4. Existing Practice

### 4.1. Concept of a Bounded Queue

The basic concept of a bounded queue with potentially blocking push and pop operations is very old and widely used. It’s generally provided as an operating system level facility, like other concurrency primitives.

POSIX 2001 has `mq` message queues (with priorities and timeout).

FreeRTOS, Mbed, vxWorks provide bounded queues.

### 4.2. Bounded and Unbounded Queues with C++ Interface

#### 4.2.1. Literature

The first concurrent queue I’ve seen was in [Hughes97]. It was full of bugs and as such shows what will go wrong if C++ doesn’t provide a standard queue. It’s unbounded.

Anthony Williams provided a queue in C++ Concurrency in Action. It’s unbounded.

#### 4.2.2. Boost

Boost has a number of queues, as official library and as example uses of synchronization primitives.

[Boost Message Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/interprocess/message_queue_t.html) only transfers bytes, not objects. It’s bounded.

[Boost Lock-Free Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/queue.html) and [Boost Lock-Free SPSC Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/spsc_queue.html) have only non-blocking operations. [Boost Lock-Free Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/queue.html) is bounded or unbounded, [Boost Lock-Free SPSC Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/boost/lockfree/spsc_queue.html) is bounded.

[Boost Synchronized Queue](https://www.boost.org/doc/libs/1_85_0/doc/html/thread/sds.html) is an implementation of an early version of this proposal.

#### 4.2.3. TBB

TBB has `concurrent_bounded_queue` ([TBB Bounded Queue](https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_bounded_queue_cls.html)) and an unbounded version `concurrent_queue` [TBB Unbounded Queue](https://spec.oneapi.io/versions/latest/elements/oneTBB/source/containers/concurrent_queue_cls.html).


## 5. Examples and Implementation

### 5.1. Implementation

A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).

Another partial implementation is available at [gitlab.com/cppzs/bounded-queue](https://gitlab.com/cppzs/bounded-queue).

A free, open-source implementation of an earlier version of these interfaces is avaliable at the Google Concurrency Library project at [github.com/alasdairmackintosh/google-concurrency-library](https://github.com/alasdairmackintosh/google-concurrency-library). The original `buffer_queue` is in [..../blob/master/include/buffer_queue.h](https://github.com/alasdairmackintosh/google-concurrency-library/blob/master/include/buffer_queue.h). The concrete `lock_free_buffer_queue` is in [..../blob/master/include/lock_free_buffer_queue.h](https://github.com/alasdairmackintosh/google-concurrency-library/blob/master/include/lock_free_buffer_queue.h). The corresponding implementation of the conceptual tools is in [..../blob/master/include/queue_base.h](https://github.com/alasdairmackintosh/google-concurrency-library/blob/master/include/queue_base.h).

### 5.2. Examples

Here we provide some examples how the API may be used.

The examples are available at [https://gitlab.com/cppzs/bounded-queue/-/tree/master/demo](https://gitlab.com/cppzs/bounded-queue/-/tree/master/demo).

### 5.3. Find Files with String

This example was presented in Object-Oriented Multithreading Using C++. The programm searches for files that contain a specific string. The idea is to have one thread to collect the file names from the filesystem and have several threads that read these files and searches them for the string.

Here we have some global definitions:

```cpp
namespace fs = std::filesystem;
typedef std::bounded_queue<fs::path> FileList;
```

Here’s the function that searches for the files and pushes them into a queue:

```cpp
void searchFiles(FileList &files, fs::path dir)
{
    if (fs::exists(dir) && fs::is_directory(dir))
    {
        fs::directory_iterator end;
        for (fs::directory_iterator i(dir); i != end; ++i)
        {
            if (!fs::is_directory(*i))
            {
                files.push(*i);                    // A
            }
        }
    }
    else
    {
        cerr << "no such directory" << endl;
    }

    files.close();                                 // B
}
```

At

A

the files are pushed into the queue and after all files
are pushed at

B

the queue is closed.

Here’s the function that picks a file and searches it for the string:

```cpp
void searchWord(FileList &files, string_view str)
{
    std::optional<fs::path> fname;

    while((fname = files.pop(ec)))                 // C
    {
        std::ifstream f(*fname);

        string line;
        while (getline(f, line))
        {
            if (line.find(str) != line.npos)
            {
                cout << "found in " << fname->string() << endl;
                break;
            }
        }
    }
}
```

Don’t check for the queue being closed at

C

.
Instead

pop

, and if the queue was closed

and no files are still in the queue

the returned optional will be empty.

And here’s the `main` function to put everything together:

```cpp
int main(int argc, char *argv[])
{
    FileList files(100);                            // D

    std::thread a(searchFiles, std::ref(files), argv[2]);
    std::thread b1(searchWord, std::ref(files), argv[1]);
    std::thread b2(searchWord, std::ref(files), argv[1]);

    a.join();
    b1.join();
    b2.join();

    return 0;
}
```

The queue is created (

D

) before the threads are started.

### 5.4. Find Files with String (Async Coroutine Version)

Note: this async version is only presented to demonstrate the use of the interface. Without an async `getline` and an async `directory_iterator` this async version doesn’t make much sense.

For an async version (using coroutines) only very few things change:

`searchFiles` is now a coroutine returning `task<void>` that simply calls `co_await files.async_push(*i);` instead of `files.push(*i);`

`searchWord` has a few more changes:

```cpp
exec::task<void> searchWord(FileList &files,
                            stdexec::run_loop &loop,                     // A
                            string_view str)
{
    std::optional<fs::path> fname;

    while ((fname = co_await (files.async_pop()))) // B
    {
        // ... same as before ...
    }

    loop.finish();                                                       // D
}
```

At

B

we now

co_await async_pop

.

We now get a `run_loop` as parameter (*A*) on which we call `finish` (*C*) once we’re done.

`main` now sets up a `run_loop` and `async_scope` instead of starting threads:

```cpp
int
main(int argc, char *argv[])
{
    stdexec::run_loop loop;
    exec::async_scope scope;

    FileList files(100);

    scope.spawn(stdexec::on(loop.get_scheduler(), searchFiles(files, argv[2])));
    scope.spawn(stdexec::on(loop.get_scheduler(), searchWord(files, loop, argv[1])));

    loop.run();
    stdexec::sync_wait(scope.on_empty());

    return 0;
}
```

### 5.5. Find Files with String (Async S/R Version)

This version looks pretty different.

The function that creates the sender to search for files looks like this:

```cpp
template <class Case0, class Case1, class Case2>
exec::variant_sender<Case0, Case1, Case2>
branch(unsigned condition, Case0 sndr0, Case1 sndr1, Case2 sndr2)
{
    if (condition == 0) return std::move(sndr0);
    if (condition == 1) return std::move(sndr1);
    return std::move(sndr2);
}

unsigned iterSelect(fs::directory_iterator& i)
{
    unsigned ret = 2;
    if (i == fs::directory_iterator{})
    {
        ret = 0;
    }
    else
    {
        if (fs::is_directory(*i)) ret = 1;

        ++i;                                              // A
    }

    return ret;
}

stdexec::sender auto
searchForFiles(FileList& files, fs::path dir)
{
    return stdexec::let_value(                            // B
        stdexec::just(fs::directory_iterator(dir)),
        [&files] (fs::directory_iterator& i)              // C
        {
            stdexec::sender auto nextFile = stdexec::let_value(  // D
                stdexec::just(),
                [&i, &files]
                {
                    fs::path file;
                    if (i != fs::directory_iterator{})
                    {
                        file = *i;                        // E
                    }

                    return branch(                        // F
                        iterSelect(i),

                        // Sndr0: close                   // G
                        stdexec::then(stdexec::just(),
                                      [&files]
                                      {
                                          std::cout << "closing\n";
                                          files.close();
                                          return true;
                                      }),

                        // Sndr1: skip directory          // H
                        stdexec::just(false),

                        // Sndr2: push file               // I
                        stdexec::then(files.async_push(file),
                                      [] { return false; }));
                });

            return exec::repeat_effect_until(nextFile);   // J
        });
}
```

`let_value` at `B` ensures that the `i` at `C` is alive throughout its whole scope, i.e. for all iterations of `repeat_effect_until` at `J`. `let_value` at `D` ensures that `file` at `I` is alive for a single iteration.

`branch` at `F` is a helper that puts the correct sender into `variant_sender`. The correct sender is selected in `iterSelect` that also increments our iterator. We have three cases:

- The iterator is at the end, then we close the queue (`G`).
- The iterator points to a directory, then we skip the entry (`H`).
- Otherwise we push the entry into the queue (`I`).

The closing sender returns `true` to end the `repeat_effect_until`, the others return `false` to continue.

The function that creates the sender to search a single file for a string looks like this:

```cpp
stdexec::sender auto searchWord(FileList& files, std::string_view str)
{
    stdexec::sender auto popAndProcess =
        files.async_pop()                                  // A
        | stdexec::then(
            [str] (const fs::path& fname) noexcept -> bool // B
            {
                //std::cout << "searching " << fname.string() << std::endl;
                std::ifstream f(fname);
                std::string line;
                while (std::getline(f, line)) {
                    if (line.find(str) != line.npos) {
                        std::cout << "found in " << fname.string() << '\n';
                        break;
                    }
                }
                return false;
            })

        | stdexec::upon_error(                             // C
            [] (auto err) noexcept -> bool
            {
                return true;
            });

    return exec::repeat_effect_until(popAndProcess);
}
```

The sender created by `async_pop` sends either a `fs::path` or an error if the queue is empty and closed.

The first case is covered by the `then` algorithm at `B` and processes the file. The second case is covered by the `upon_error` algorithm at `C` and returns `true` to end the loop.

### 5.6. Logging

This is an example from an embedded system where no blocking is allowed.

Logging messages can be pushed into a queue from all kind of contexts, while a background task regularly pulls from the queue and sends messages to a serial interface.

This is the push function:

```cpp
void enqueueLogMessage(std::string &&msg)
{
    if (logQ.try_push(std::move(msg)) != conqueue_status::success)
    {
        ++lostLogMessages;
    }
}
```

This is the function that pulls the messages:

```cpp
void outputLogMessage()
{
    static std::string bufferedString;

    unsigned busyCnt = 0;

    while (outputBuffer.add(bufferedString) > 0) // returns free space
    {
        auto val = logQ.try_pop();
        if (val)
        {
            bufferedString = std::move(*val);
            continue;
        }

        conqueue_status ec(val.error());
        assert(ec != conqueue_status::closed);
        if (ec == conqueue_status::busy)
        {
            ++busyCnt;
            if (busyCnt > 2) break;
        }

        break;
    }
}
```
