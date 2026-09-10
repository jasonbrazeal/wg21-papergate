
UTF-16 is rendered invalid by improper use of surrogates: a high surrogate not followed by a low surrogate or a low surrogate not preceded by a high surrogate. Note that the presence of any surrogate code points in UTF-32 is also invalid.

Finally, UTF-8, the most ubiquitous and most complex encoding. This uses 8-bit code units. If the high bit of the code unit is unset, the code unit represents its ASCII equivalent for backwards compatibility. Otherwise the code unit is either a start byte, which describes how long the subsequence is (two to four bytes long), or a continuation byte, which fills out the subsequence with the remaining data.
