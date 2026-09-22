Verdict: Adequate (6/14)

The paper gives a reasonably clear account of why the restriction is surprising and why removing it would align the standard with existing practice, but it leans heavily on assertions about implementation status and user dependence rather than demonstrating them. The strongest material concerns the origin of the restriction and the precedent of CWG3003; the thinnest concerns the absence of any discussion of non-library solutions or formal implementation experience.

- The paper establishes why the restriction matters by pointing to common naming practices like `std::string` and the unnaturalness of requiring users to spell out underlying template specializations.
- The strongest supporting context is the acknowledgment that the original restriction was added for simplicity and lack of a use case, and that CWG3003 was a rushed minimal fix to avoid shipping a defect.
- The paper claims broad implementation acceptance and likely user dependence, but these claims are repeated rather than backed by concrete evidence or a survey of implementations.
- The paper offers no discussion of why a library-level solution would be inadequate or what coordination would be needed to standardize behavior already present in most implementations.
