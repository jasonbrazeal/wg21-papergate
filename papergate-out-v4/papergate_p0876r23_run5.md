Verdict: Strong (9/14)

The paper offers solid support in several areas central to justifying standardization, particularly in explaining why the facility matters, showing prior art, establishing implementation experience, and arguing that only core language or standard library integration can provide portable stack switching. The case is much thinner, however, on coordination with existing and planned standards features and on showing that third-party libraries cannot cover the need adequately in practice, where the paper mostly asserts impossibility rather than demonstrating it.

- The strongest support is the repeated, credited argument that creating and switching between function call stacks cannot be written in portable C++, along with the tooling benefits that would follow from standardization.
- The paper also credibly establishes implementation experience through constexpr coroutine work and a libstdc++ presentation, which grounds the design in real use.
- Prior art and alternatives are well covered by references to earlier proposals and observed ABI and exception-handling divergences.
- The most glaring omission is interoperability and coordination with other standard facilities and ecosystems, for which no support is established at all.
