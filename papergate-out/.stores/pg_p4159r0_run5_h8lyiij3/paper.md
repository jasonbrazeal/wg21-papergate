---
title: "Make sender_in and receiver_of exposition-only"
document: P4159R0
date: 2026-03-27
audience: LWG
reply-to:
  - "Tim Song <t.canens.cpp@gmail.com>"
---

## 1 Introduction

In response to LEWG direction on [LWG4361], this paper provides wording to make the `receiver_of` and `sender_to` concepts exposition-only for C++26.

## 2 Wording

Instructions to the editor:

After applying *all other papers* moved during the Croydon meeting *except [P4154R0]*, make the following changes in Clause 33 [[exec]](https://eel.is/c++draft/exec):

- Add an `// exposition only` comment to the declaration of `sender_to` in 33.4 [[execution.syn]](https://eel.is/c++draft/execution.syn) and its definition in 33.9.3 [[exec.snd.concepts]](https://eel.is/c++draft/exec.snd.concepts).
- Add an `// exposition only` comment to the declaration of `receiver_of` in 33.4 [[execution.syn]](https://eel.is/c++draft/execution.syn) and its definition in 33.7.1 [[exec.recv.concepts]](https://eel.is/c++draft/exec.recv.concepts).
- Replace all instances of `sender_to` with `*sender-to*`.
- Replace all instances of `receiver_of` with `*receiver-of*`.

## 3 References

[LWG4361] Lewis Baker. awaitable-receiver::set_value should use Mandates instead of constraints.

[P4154R0] Tim Song, Ruslan Arutyunyan, Arthur O’Dwyer. 2026. Renaming various execution things.
