Verdict: Strong (8/14)

The paper’s strongest support lies in its evidence about deployed practice: it shows that production hardened implementations terminate on these detected violations, and it documents implementation experience clearly. The case thins where the paper relies on that same deployment record to carry arguments about why the standard should specify the behavior, why a library cannot suffice, and how the design interoperates, without developing those points much further.

- The paper establishes from the surveyed implementation record that termination is the uniform production default across hardened implementations that detect core-language violations.
- It also establishes credible implementation experience, including the libc++ position that hardened checks must avoid exception-handling costs and that continuation is only an adoption aid.
- The least developed part is the standardization rationale: the paper asserts rather than demonstrates why this behavior belongs in the standard rather than remaining an implementation or library convention.
- The interoperability and library-alternative arguments are similarly thin, resting mainly on the deployment evidence rather than a separate account of coordination constraints or why a library response would be inadequate.
