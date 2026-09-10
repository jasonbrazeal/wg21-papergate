# Diagnostics

Verdict: Excellent (14/14)

Criteria addressed: 7 of 7. Points: 14 of 14. Unsupported quotes rejected: 27. Replies missing: 0.

## motivation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/2/2  chunk 3: 0/0/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 2/2/2  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: Such a label would be a vast improvement over today’s `[[assume]]` attribute since it would allow for *checkable* assumptions (see [P2064R0] for context), achieving the integration between assertions and assumptions that we failed to achieve in the C++20 cycle.

## audience - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” ... and one instance of explicit language UB introduced with a phrase containing the word “assume”

## prior_art - grade 2
votes: chunk 1: 2/2/2  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 2/2/2  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 2/2/2  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the *entire* C++ language specification, fundamentally changing the landscape of how undefined behaviour is approached in C++.

## vehicle - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/1  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: Such a control mechanism for runtime checks (or for other tools in our toolbox such as language subsetting) needs to be designed carefully and take into account the overall strategy (Figure 4).

## coordination - grade 2
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: This API provides not only a user callback in the form of a program-wide replaceable contract-violation handler, but also programmatically accessible information about the defect via the `contract_violation` object passed into the contract-violation handler.

## insufficiency - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: For example, GCC has an option `-fwrapv` which turns signed integer overflow into wraparound. We cannot make that the new behaviour of signed integer addition unconditionally for two reasons.

## implementation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/1  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/2/2  chunk 5: 2/2/2  chunk 6: 2/2/2  chunk 7: 0/0/0  chunk 8: 0/0/2  chunk 9: 0/0/2  chunk 10: 2/2/2  chunk 11: 0/0/1  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: For example, for signed integer overflow, the GCC flag `-ftrapv` is a conforming implementation of the *quick-enforce* semantic; sanitisers like ASan and UBSan are conforming implementations of the *enforce* semantic for those cases of UB that they identify.
