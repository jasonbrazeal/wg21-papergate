Verdict: Adequate (4/14)

The paper offers only a narrow foundation for its own standardization, centered on implementation experience, while much of the surrounding case rests on assertions rather than demonstrated need. The thinnest areas are the absence of any argument for why the standard specifically must change and why a library solution is insufficient.

- The strongest support is the concrete implementation evidence, including work against nVidia’s reference implementation and confirmation from Intel’s maintainers that `when_all()` is well-formed in their implementation.
- The paper repeatedly asserts that banning `when_all()` creates an unnecessary special case, but it does not show who is concretely affected or why this matters in practice beyond that assertion.
- The discussion of alternatives is mostly descriptive, pointing to the current specification and existing implementations without establishing that standardization is the right path.
- Most glaringly, the paper does not establish why the standard must address this, nor why a library-level solution would not suffice.
