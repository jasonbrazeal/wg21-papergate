Verdict: Strong (10/14)

The paper offers substantial support for standardizing the proposed behavior, with its strongest evidence coming from real-world usage data, existing implementation extensions, and a clearly demonstrated practical need for random byte generation. The thinnest support appears in the arguments for why standardization is necessary rather than leaving the work to library extensions or resolving it through other means, where the paper asserts more than it demonstrates.

- The paper convincingly establishes that current restrictions on `signed char` and `unsigned char` in `<random>` are widely violated in practice, with thousands of files using these types and both major standard libraries already supporting them as extensions.
- The strongest established ground comes from the implementation experience section, showing that libc++ and libstdc++ have already worked out the feasibility of supporting these types, reducing the risk of standardizing untested behavior.
- The paper does not adequately establish why a library solution would be insufficient, since it acknowledges that `uniform_int_distribution<unsigned int>(0, 255)` already provides functional equivalence for the primary use case of generating octets.
- The most glaring omission is the failure to demonstrate why the standard itself must change, beyond asserting that the paper "resolves all these known defects and discrepancies in one fell swoop" without substantiating that claim.
