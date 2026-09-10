# What the paper offers

## why it matters: supported with specifics
> Such implicitly defined identification labels would make possible programmatically identifying, in the contract-violation handler, whether the violated implicit contract assertion is related to an out-of-bounds issue, an arithmetic issue, and so forth

## who is affected: supported with specifics
> We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” ... and one instance of explicit language UB introduced with a phrase containing the word “assume”

## prior art and alternatives: supported with specifics
> Building on Contracts as adopted for C++26, we provide a generic framework for applying these two techniques across the *entire* C++ language specification, fundamentally changing the landscape of how undefined behaviour is approached in C++.

## why the standard: supported with specifics
> We therefore do not consider, in this paper, efforts that operate largely outside of the C++ abstract machine and the specification tools afforded by the C++ Standard.

## coordination and interoperability: supported with specifics
> For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

## why a library will not do: supported with specifics
> For example, GCC has an option `-fwrapv` which turns signed integer overflow into wraparound. We cannot make that the new behaviour of signed integer addition unconditionally for two reasons.

## implementation experience: supported with specifics
> For example, for signed integer overflow, the GCC flag `-ftrapv` is a conforming implementation of the *quick-enforce* semantic; sanitisers like ASan and UBSan are conforming implementations of the *enforce* semantic for those cases of UB that they identify.
