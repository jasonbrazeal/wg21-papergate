# Diagnostics

Verdict: Strong (9/14)

Criteria addressed: 5 of 7. Points: 9 of 14. Unsupported quotes rejected: 3. Replies missing: 0.

## motivation - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0
quote: The index operator in the C++ associative containers has a number of shortcomings compared to many other languages.

## audience - grade 2
votes: chunk 1: 2/2/2  chunk 2: 0/0/0
quote: Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.

## prior_art - grade 2
votes: chunk 1: 2/2/2  chunk 2: 2/2/2
quote: The name `get` was borrowed from the Python dictionary member of the same name. Other names considered were `try_at` , `lookup_at` , `get_optional` , and `lookup_optional` .

## vehicle - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0
quote: (none validated)

## coordination - grade 0
votes: chunk 1: 0/0/0  chunk 2: 0/0/0
quote: (none validated)

## insufficiency - grade 1
votes: chunk 1: 1/1/1  chunk 2: 0/0/0
quote: A global function is less intuitive because it puts `lookup` outside of the map interface.

## implementation - grade 2 (UNSTABLE: votes cross zero)
votes: chunk 1: 2/2/2  chunk 2: 0/1/1
quote: An implementation, with tests and usage examples, can be found at https://github.com/phalpern/WG21-halpern/tree/main/P3091-map_lookup/code.
