## 5 Design Overview

### 5.1 Transcoding Views

Invoking `begin()` or `end()` on a transcoding view constructs an instance of an exposition-only `to_utf_view::*iterator*` type.

The `to_utf_view::*iterator*` stores an iterator pointing to the start of the character it’s transcoding, and a back-pointer to the underlying range in order to bounds check its beginning and end (which is required for correctness, not just safety).

The `to_utf_view::*iterator*` maintains a small buffer (`buf_`) containing the current character, transcoded into the target encoding. If the underlying range models `forward_range`, the buffer may additionally contain the transcoded code units of one or more characters following the current one: an implementation is permitted to transcode a whole chunk of input at a time (for example, using SIMD instructions) and serve subsequent increments — or, when iterating backward, decrements — out of the buffer. If the underlying range is single-pass, the buffer contains the code units of exactly one character (between one and four code units), because reading ahead in a single-pass range is destructive and therefore observable.

It also maintains an index (`buf_index_`) into this buffer, which it increments or decrements when `operator++` or `operator--` is invoked, respectively. If it runs out of code units in the buffer, it reads more elements from the underlying view. `operator*` provides the current element of the buffer.

Below is an approximate block diagram of the iterator. Bold lines denote actual data members of the iterator; dashed lines are just function calls.
