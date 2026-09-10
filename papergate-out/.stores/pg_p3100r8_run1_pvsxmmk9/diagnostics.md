# Diagnostics

Verdict: Excellent (14/14)

Criteria addressed: 7 of 7. Points: 14 of 14. Unsupported quotes rejected: 28. Replies missing: 0.

## motivation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/0/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/2/2  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: Such implicitly defined identification labels would make possible programmatically identifying, in the contract-violation handler, whether the violated implicit contract assertion is related to an out-of-bounds issue, an arithmetic issue, and so forth

## audience - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” ... and one instance of explicit language UB introduced with a phrase containing the word “assume”

## prior_art - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 0/2/2  chunk 5: 2/2/2  chunk 6: 2/2/2  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/2/2  chunk 11: 0/0/2  chunk 12: 1/2/2  chunk 13: 0/0/0
quote: Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the entire C++ language specification, fundamentally changing the landscape of how undefined behaviour is approached in C++.

## vehicle - grade 2
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 1/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: One benefit is that implementations of such runtime checks will be able to leverage a shared paradigm and shared terminology for reasoning about incorrect programs.

## coordination - grade 2
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: With our proposal, all these tools can instead hook into the standard contract-violationhandling API.

## insufficiency - grade 2
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: For example, GCC has an option `-fwrapv` which turns signed integer overflow into wraparound. We cannot make that the new behaviour of signed integer addition unconditionally for two reasons.

## implementation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/1  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 2/2/2  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/2/2  chunk 10: 2/2/2  chunk 11: 0/0/1  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: For example, for signed integer overflow, the GCC flag `-ftrapv` is a conforming implementation of the *quick-enforce* semantic; sanitisers like ASan and UBSan are conforming implementations of the *enforce* semantic for those cases of UB that they identify.
