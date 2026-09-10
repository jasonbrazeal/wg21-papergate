Verdict: Adequate (7/14, close to Strong)

The paper offers only a narrow, anecdotal basis for its proposal, with the strongest material going to explaining the inconvenience and sketching possible API shapes rather than building a standardization case. The thinnest areas are the complete absence of discussion about why this belongs in the standard, how it would interact with existing specifications, or whether a library-level solution could suffice.

- The clearest support is the concrete description of the current workaround—constructing a container solely to extract a node—as an unnecessary and awkward step.
- The paper does gesture at alternative designs, such as factory functions or additional constructors, which at least frames the design space.
- The claim that this annoyance has been encountered multiple times is asserted without examples, context, or evidence of broader user impact.
- The most glaring omission is the lack of any argument for why the standard, rather than a library facility, is the right place for this feature.
