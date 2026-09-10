Verdict: Strong (10/14)

The paper provides uneven support for its own standardization, with the strongest material concentrated in the discussion of prior art, standard-library precedent, and the limitations of a library-only solution. The thinnest areas are the asserted practical motivation and the absence of any implementation experience or evidence that the proposed change addresses a demonstrated need.

- The paper grounds its design in concrete, closely related standard-library precedents such as `std::any_cast` and `std::get_if`, which gives the proposal a clear point of reference.
- The argument for why a library solution would be insufficient is specific about the semantic ambiguity of `T*`, supporting the case for a distinct return type.
- The claim that the current behavior is “quite clunky in practice” is asserted without examples, user reports, or code patterns showing real friction.
- The implementation experience section offers no evidence of actual use, prototyping, or feedback, leaving the practical case for standardization largely unsubstantiated.
