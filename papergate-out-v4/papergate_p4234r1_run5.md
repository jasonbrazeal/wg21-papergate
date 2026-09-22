Verdict: Strong (10/14)

The paper’s strongest moments come when it documents existing practice: the broad compiler support, the Clang implementation attempt, and the concrete places where `$` already appears in toolchains and real code. It is less convincing when it needs to show who is burdened today, why the standard is the right remedy rather than continuing extensions, and why a library-level solution is impossible.

- The paper firmly establishes that allowing `$` in identifiers is a long-standing, widely implemented extension with direct implementation experience behind the proposed approach.
- The discussion of prior art and coordination is also grounded, especially in showing the construct is already used for linker-defined symbols and that standardization would clarify rather than invent behavior.
- The case for who is affected rests largely on general popularity claims and a single GitHub query, without showing that the affected population is substantial or that its needs are not already met.
- The paper never establishes why a library cannot address the problem, leaving that required part of the standardization argument entirely unaddressed.
