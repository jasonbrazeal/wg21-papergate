# What the paper offers

## why it matters: supported with specifics
> The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.

## who is affected: asserted, with nothing supporting it
> Boost has a number of queues, as official library and as example uses of synchronization primitives.

## prior art and alternatives: supported with specifics
> [P3570R0: optional variants in sender/receiver](https://wg21.link/P3570) provides a mechanism to return different values for coroutines than for direct receivers.

## why the standard: supported with specifics
> The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## coordination and interoperability: asserted, with nothing supporting it
> The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## why a library will not do: asserted, with nothing supporting it
> The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.

## implementation experience: supported with specifics
> A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).
