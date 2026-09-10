# Diagnostics

Verdict: Strong (11/14, close to Excellent)

Criteria addressed: 7 of 7. Points: 11 of 14. Unsupported quotes rejected: 4. Replies missing: 0.

## motivation - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.

## audience - grade 1
votes: chunk 1: 1/1/1  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: The basic concept of a bounded queue with potentially blocking push and pop operations is very old and widely used.

## prior_art - grade 2
votes: chunk 1: 2/2/2  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2
quote: P0260R4 revised P0260R3 - 2019-01-20 as follows. - Move the concrete queue proposal to a separate paper, [[P1958]](https://wg21.link/P1958).

## vehicle - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/1/1  chunk 2: 2/2/2  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## coordination - grade 1
votes: chunk 1: 0/0/0  chunk 2: 1/1/2  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: The concepts `basic_concurrent_queue` and `concurrent_queue` capture the common semantics of these widely different implementations and are therefore an important specification for users of such queues, even if the used implementation is not part of the C++ Standard.

## insufficiency - grade 1 (UNSTABLE: votes cross zero)
votes: chunk 1: 1/1/1  chunk 2: 0/0/1  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: The existing `deque` in the standard library is an inherently sequential data structure. Its reference-returning element access operations cannot synchronize access to those elements with other queue operations.

## implementation - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0
quote: A partial implementation is available at [github.com/GorNishanov/conqueue](https://github.com/GorNishanov/conqueue).
