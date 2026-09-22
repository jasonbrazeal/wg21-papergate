Verdict: Adequate (7/14, close to Strong)

The paper offers uneven support for its own standardization, strongest when it explains why a clearer contract than `const char*` might matter and when it locates itself in recent committee discussion, but it never closes the gap between that motivation and a standard-library need. The thinnest parts are the absence of any interoperability analysis and the repeated reliance on assertions about existing implementations without demonstrating what they actually agree on.

- The paper clearly establishes the motivating problem: authors who want a zero-terminated parameter currently must choose between an under-specified `const char*` and a `string_view` that only incidentally may be terminated.
- It credibly ties itself to prior work and current LEWG direction, showing that the topic has committee attention and a defined starting point.
- Its claim that the standard is the right home rests mainly on a general appeal to design principles rather than on a concrete case for why a library type cannot serve.
- The paper offers no assessment of how such a type would coordinate with existing string facilities, C APIs, or other in-flight proposals.
