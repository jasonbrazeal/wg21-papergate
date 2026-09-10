---
title: "Unicode in the Library, Part 1: UTF Transcoding"
document: P2728R14
date: 2026-06-10
audience: SG-16 Unicode,SG-9 Ranges,LEWG
reply-to:
  - "Eddie Nolan <eddiejnolan@gmail.com>"
---


## 1 High-Level Overview

This paper introduces views and ranges for transcoding between UTF formats:

`static_assert((u8"🙂" | views::to_utf32 | ranges::to<u32string>()) == U"🙂");`

It handles errors by replacing invalid subsequences with �:

`static_assert((u8"🙂" | views::take(3) | to_utf32 | ranges::to<std::u32string>()) == U"�");`

And by providing `or_error` views that provide `std::expected`:

```cpp
static_assert(
  *(u8"🙂" | views::take(3) | views::to_utf32_or_error).begin() ==
  unexpected{utf_transcoding_error::truncated_utf8_sequence});
```
