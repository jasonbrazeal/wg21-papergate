# What the paper offers

## why it matters: supported with specifics
> The index operator in the C++ associative containers has a number of shortcomings compared to many other languages.

## who is affected: supported with specifics
> Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.

## prior art and alternatives: supported with specifics
> The name `get` was borrowed from the Python dictionary member of the same name. Other names considered were `try_at` , `lookup_at` , `get_optional` , and `lookup_optional` .

## why the standard: not addressed

## coordination and interoperability: not addressed

## why a library will not do: supported with specifics
> A global function is less intuitive because it puts `lookup` outside of the map interface.

## implementation experience: supported with specifics
> An implementation, with tests and usage examples, can be found at https://github.com/phalpern/WG21-halpern/tree/main/P3091-map_lookup/code.
