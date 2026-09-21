Verdict: Strong (10/14)

The paper provides a reasonable amount of concrete support for its standardization, particularly through implementation experience and references to prior work, but it leaves several important parts of the case unstated. The thinnest areas are the absence of any discussion of who is affected by the change and why a library-only solution would be insufficient.

- The strongest support comes from the linked Clang implementation and compiler explorer demonstration, which shows the feature is more than a design sketch.
- The paper grounds itself in prior proposals and explains the core technical motivation with a specific example involving string literals and cross-translation-unit pointer identity.
- The most glaring omission is the lack of any discussion of the affected audience or practical impact on users.
- The paper also does not address why a library-based approach cannot achieve the same goal, leaving a key part of the standardization argument unexamined.
