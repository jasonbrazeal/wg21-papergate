# Diagnostics

Verdict: Excellent (14/14)

Criteria addressed: 7 of 7. Points: 14 of 14. Unsupported quotes rejected: 30. Replies missing: 0.

## motivation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/2/2  chunk 3: 0/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/2/2  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: Such implicitly defined identification labels would make possible programmatically identifying, in the contract-violation handler, whether the violated implicit contract assertion is related to an out-of-bounds issue, an arithmetic issue, and so forth

## audience - grade 2
votes: chunk 1: 0/0/0  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: We found 81 instances of explicit language UB introduced with phrases containing the word “undefined” ... and one instance of explicit language UB introduced with a phrase containing the word “assume”

## prior_art - grade 2
votes: chunk 1: 2/2/2  chunk 2: 2/2/2  chunk 3: 2/2/2  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 2/2/2  chunk 11: 2/2/2  chunk 12: 2/2/2  chunk 13: 0/0/0
quote: Notably, the [P3400R4] approach has an important advantage over using the `detection_mode` enum, as proposed in [P3081R2] and in earlier versions of this paper: a single implicit contract assertion can belong to multiple groups.

## vehicle - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/1/1  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/1  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: Such a control mechanism for runtime checks (or for other tools in our toolbox such as language subsetting) needs to be designed carefully and take into account the overall strategy (Figure 4).

## coordination - grade 2
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 0/0/0  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: For example, all Clang sanitisers have a callback, `__sanitizer_set_death_callback`, but this callback takes no arguments.

## insufficiency - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/0/2  chunk 3: 2/2/2  chunk 4: 0/0/0  chunk 5: 2/2/2  chunk 6: 0/0/0  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/0/0  chunk 10: 0/0/0  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: In fact, in our entire list of 82 cases of UB, we cannot identify *any* cases that can unconditionally be diagnosed at compile time.

## implementation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 0/0/0  chunk 2: 0/0/0  chunk 3: 0/0/0  chunk 4: 2/2/2  chunk 5: 2/2/2  chunk 6: 2/2/2  chunk 7: 0/0/0  chunk 8: 0/0/0  chunk 9: 0/2/2  chunk 10: 2/2/2  chunk 11: 0/0/0  chunk 12: 0/0/0  chunk 13: 0/0/0
quote: A companion paper, [P4277R0], contains significant additional commentary on all of the wording changes, along with details on the implementation experience with introducing runtime checks for each of these undefined behaviours.
