# Papergate LLM judge: first run against the human reviews

Run: `papergate-llm-judge.py --model anthropic`, 2026-09-11. Backend
`claude-fable-5-1`, effort `high`, one whole-paper request per run, five runs
per paper, ten papers. Outputs in `papergate-llm-judge-out/anthropic/`
(`scores.md`, `requests.jsonl`).

## Run health

- 50/50 requests succeeded on the first attempt; no retries, no parse
  failures. Every response was bare JSON with all seven criteria in range.
- All supporting quotes checked on the first paper were verbatim in the
  markdown and under the 40-word limit.
- 2,400,080 input tokens and 101,205 output tokens (thinking included),
  about $29 in total. Per-paper input ranged from 9,079 (p2826r4) to
  168,691 (p3045r9) tokens.

## Run-to-run consistency

Four papers (p3045r9, p1040r11, p3100r8, p3091r6) received the identical
score on all five runs. Five more had a total range of 1-2 points. The widest
spread was p2719r7 at 11-13. No criterion flipped between 0 and 2 across runs
on any paper.

## Agreement with the two human reviewers

Judge score per criterion is the median over the five runs. 70 cells
(10 papers x 7 criteria).

| comparison | exact match | within 1 point | mean bias | MAE on totals |
|---|---|---|---|---|
| judge vs A | 0.71 | 0.96 | +0.24 | 1.7 |
| judge vs B | 0.47 | 0.87 | +0.57 | 4.0 |
| A vs B | 0.59 | 0.94 | +0.33 | 2.7 |

Against reviewer A the judge agrees more often than the two reviewers agree
with each other. Against reviewer B it agrees less, and the gap is almost
entirely bias: B is the strict rater and the judge is the lenient one. On the
41 cells where A and B agree, the judge matches them 71% of the time.

### Per criterion

| criterion | judge = A | judge = B | A = B | judge mean | A mean | B mean |
|---|---|---|---|---|---|---|
| motivation | 0.8 | 0.8 | 0.8 | 2.0 | 1.8 | 1.6 |
| audience | 0.6 | 0.1 | 0.5 | 1.1 | 0.9 | 0.6 |
| prior_art | 0.6 | 0.7 | 0.7 | 2.0 | 1.6 | 1.7 |
| vehicle | 0.6 | 0.3 | 0.6 | 1.4 | 1.1 | 0.8 |
| coordination | 0.7 | 0.6 | 0.6 | 1.1 | 1.0 | 0.5 |
| insufficiency | 0.7 | 0.2 | 0.3 | 1.5 | 1.0 | 0.4 |
| implementation | 1.0 | 0.6 | 0.6 | 1.8 | 1.8 | 1.3 |

The judge gives a flat 2 for motivation and prior_art on every paper and
every run. Implementation is its best criterion (10/10 with A).

### Totals

| paper | A | B | judge (median) | judge run range |
|---|---|---|---|---|
| p3045r9 | 12 | 10 | 14 | 14-14 |
| p2728r14 | 5 | 3 | 9 | 8-9 |
| p0260r20 | 8 | 3 | 12 | 10-12 |
| p1040r11 | 14 | 11 | 14 | 14-14 |
| p3091r6 | 8 | 6 | 8 | 8-8 |
| p2806r5 | 9 | 9 | 10 | 9-11 |
| p3100r8 | 14 | 9 | 14 | 14-14 |
| p2826r4 | 7 | 4 | 9 | 9-10 |
| p2287r6 | 6 | 8 | 8 | 6-8 |
| p2719r7 | 9 | 6 | 11 | 11-13 |

The largest gaps (p0260r20, p2728r14) are the two papers the reviewers also
split on most.

### Cells where the judge disagrees with both humans

16 of 70. In 14 the judge is higher; in 2 it is lower.

| paper | criterion | judge | A | B |
|---|---|---|---|---|
| p3045r9 | insufficiency | 2 | 0 | 0 |
| p2728r14 | motivation | 2 | 1 | 0 |
| p2728r14 | audience | 1 | 0 | 0 |
| p2728r14 | prior_art | 2 | 1 | 1 |
| p2728r14 | coordination | 1 | 0 | 0 |
| p0260r20 | motivation | 2 | 1 | 0 |
| p0260r20 | vehicle | 2 | 0 | 0 |
| p0260r20 | coordination | 2 | 1 | 0 |
| p3091r6 | audience | 0 | 1 | 1 |
| p3091r6 | prior_art | 2 | 1 | 1 |
| p2806r5 | vehicle | 2 | 1 | 1 |
| p2826r4 | vehicle | 1 | 0 | 0 |
| p2287r6 | audience | 1 | 0 | 0 |
| p2719r7 | audience | 1 | 0 | 0 |
| p2719r7 | vehicle | 1 | 2 | 0 |
| p2719r7 | insufficiency | 2 | 0 | 0 |

The recurring pattern is a 1 for vehicle, coordination or audience where
both humans gave 0. In the p2826r4 case examined directly, the quote offered
for vehicle was "which is exactly why we need this capability": a passing
assertion credited as "addressed by assertion" where both reviewers read it
as not addressed. If the other cells follow the same pattern, the 0/1
boundary in the prompt needs to say that an incidental mention is not an
argument. The 1/2 boundary looks well calibrated against reviewer A already.

## Human review scores used

Reviewer A:

| paper | motivation | audience | prior_art | vehicle | coordination | insufficiency | implementation | total |
|---|---|---|---|---|---|---|---|---|
| p3045r9 | 2 | 2 | 2 | 2 | 2 | 0 | 2 | 12 |
| p2728r14 | 1 | 0 | 1 | 1 | 0 | 0 | 2 | 5 |
| p0260r20 | 1 | 1 | 2 | 0 | 1 | 1 | 2 | 8 |
| p1040r11 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| p3091r6 | 2 | 1 | 1 | 1 | 0 | 1 | 2 | 8 |
| p2806r5 | 2 | 0 | 2 | 1 | 0 | 2 | 2 | 9 |
| p3100r8 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 14 |
| p2826r4 | 2 | 1 | 1 | 0 | 0 | 2 | 1 | 7 |
| p2287r6 | 2 | 0 | 1 | 0 | 1 | 0 | 2 | 6 |
| p2719r7 | 2 | 0 | 2 | 2 | 2 | 0 | 1 | 9 |

Reviewer B:

| paper | motivation | audience | prior_art | vehicle | coordination | insufficiency | implementation | total |
|---|---|---|---|---|---|---|---|---|
| p3045r9 | 2 | 1 | 1 | 2 | 2 | 0 | 2 | 10 |
| p2728r14 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 3 |
| p0260r20 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 3 |
| p1040r11 | 2 | 2 | 2 | 2 | 0 | 1 | 2 | 11 |
| p3091r6 | 2 | 1 | 1 | 0 | 0 | 0 | 2 | 6 |
| p2806r5 | 2 | 1 | 2 | 1 | 0 | 1 | 2 | 9 |
| p3100r8 | 2 | 1 | 2 | 2 | 1 | 1 | 0 | 9 |
| p2826r4 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 4 |
| p2287r6 | 2 | 0 | 2 | 1 | 0 | 1 | 2 | 8 |
| p2719r7 | 2 | 0 | 2 | 0 | 2 | 0 | 0 | 6 |
