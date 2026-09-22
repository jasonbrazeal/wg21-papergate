Verdict: Strong (9/14)

The paper gives firm support in the areas of motivation, prior art, and implementation experience, but its case thins considerably when it comes to showing who is affected and why the work cannot live in a library outside the standard. The strongest framing is around the safety problem with exception-based transcoding and the existence of a concrete reference implementation, while the weakest parts rely on repeated assertions rather than evidence about user reach or the necessity of standardization.

- The paper clearly establishes why exception-based Unicode handling is dangerous and why non-throwing replacement behavior matters for real-world UTF processing.
- It also offers solid grounding in existing practice, including Unicode’s substitution methodology and a working reference implementation.
- The claim about who is affected leans on thin evidence such as GitHub stars and does not demonstrate the breadth of users or codebases facing this problem.
- Most notably, the paper does not establish why this functionality cannot be delivered as a library, relying instead on restatements that it would replace deprecated facilities rather than showing a concrete barrier to out-of-standard adoption.
