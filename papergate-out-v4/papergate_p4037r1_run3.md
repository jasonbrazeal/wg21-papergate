Verdict: Strong (9/14)

The paper gives a reasonably solid account of why the current restriction is problematic and shows genuine implementation experience, but its case thins considerably when it tries to demonstrate who is affected and how the proposed change fits into the broader ecosystem.

- The strongest support comes from the concrete implementation experience in libstdc++ and libc++, which lends practical weight to the proposed relaxation.
- The paper also clearly establishes why the status quo matters by pointing to undefined behavior and the value of octet generation.
- The evidence for real-world use relies on code-search claims and assertions of usefulness that point in the right direction but fall short of a firm demonstration of scope.
- The most glaring omission is any explanation of why this cannot be addressed by a library, leaving an essential part of the standardization rationale unaddressed.
