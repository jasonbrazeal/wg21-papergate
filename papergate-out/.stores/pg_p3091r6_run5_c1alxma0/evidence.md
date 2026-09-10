# What the paper offers

## why it matters: supported with specifics
> These limitations often force the user to resort to the `find` member function, which returns an iterator that points to a `pair` and typically leads to more complex code having at least one `if` statement and/or duplicate lookup operations.

## who is affected: supported with specifics
> Some of the functionality can be found in Meta’s [[Folly]](https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71) library.

## prior art and alternatives: supported with specifics
> The name `get` was borrowed from the Python dictionary member of the same name. Other names considered were `try_at` , `lookup_at` , `get_optional` , and `lookup_optional` .

## why the standard: not addressed
> A global function is less intuitive because it puts `lookup` outside of the map interface.

## coordination and interoperability: not addressed

## why a library will not do: asserted, with nothing supporting it
> A global function is less intuitive because it puts `lookup` outside of the map interface.

## implementation experience: supported with specifics
> [Folly] Meta. folly/folly/MapUtil.h. https://github.com/facebook/folly/blob/323e467e2375e535e10bda62faf2569e8f5c9b19/folly/MapUtil.h#L35-L71
