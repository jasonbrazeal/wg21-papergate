# What the paper offers

## why it matters: supported with specifics
> Such implicitly defined identification labels would make possible programmatically identifying, in the contract-violation handler, whether the violated implicit contract assertion is related to an out-of-bounds issue, an arithmetic issue, and so forth

## who is affected: supported with specifics
> We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” ... and one instance of explicit language UB introduced with a phrase containing the word “assume”

## prior art and alternatives: supported with specifics
> Notably, the [P3400R4] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R2] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups.

## why the standard: supported with specifics
> Such a control mechanism for runtime checks (or for other tools in our toolbox such as language subsetting) needs to be designed carefully and take into account the overall strategy (Figure 4).

## coordination and interoperability: supported with specifics
> For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

## why a library will not do: supported with specifics
> In fact, in our entire list of 82 cases of UB, we cannot identify *any* cases that can unconditionally be diagnosed at compile time.

## implementation experience: supported with specifics
> A companion paper, [P4277R0], contains significant additional commentary on all of the wording changes, along with details on the implementation experience with introducing runtime checks for each of these undefined behaviours.
