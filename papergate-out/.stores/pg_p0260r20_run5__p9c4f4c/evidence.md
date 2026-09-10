# What the paper offers

## why it matters: supported with specifics
> The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.

## who is affected: asserted, with nothing supporting it
> The basic concept of a bounded queue with potentially blocking push and pop operations is very old and widely used.

## prior art and alternatives: supported with specifics
> P0260R4 revised P0260R3 - 2019-01-20 as follows. - Move the concrete queue proposal to a separate paper, [[P1958]](https://wg21.link/P1958).

## why the standard: supported with specifics
> The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## coordination and interoperability: asserted, with nothing supporting it
> The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## why a library will not do: asserted, with nothing supporting it
> The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.

## implementation experience: supported with specifics
> A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).
