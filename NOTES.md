# One-Line Laugh-Off — Notes

- **Bounty:** One-Line Laugh-Off (`u-zkhiel-one-line-laugh-off-714618ae`)
- **Prize:** $2 (winner takes all)
- **Deadline:** 26 Nov 2026, 20:45 WIB (2026-11-26T13:45:00.000Z)
- **Fee status:** FREE — `entryFeeUsd` verified `null` via API before building (26 Nov 2026 ~13:51 WIB)
- **opensAt:** 2026-11-25T01:46:16.000Z (opened before this session started)
- **submissionCount at build time:** 2595
- **Rounds:** blind rounds; final at the deadline; top 500 on the dev board go to the final heat (3 Swiss rounds + playoff among top 3)

## The entry

> I told my toddler babies come from the cloud. Now she asks Alexa for a little brother.

86 characters, single line, original (authored from the brief, no older entries consulted).

## Calibration (top-1 standard)

The judge is an AI model (z-ai/glm-5.3-flash) comparing two lines head-to-head, weighing in order: (1) genuinely funny, (2) how hard and suddenly the line lands on a cold read, (3) surprise of the turn, (4) economy of words, (5) freshness — no recycled setups. Blind rounds: no live leaderboard or top entries are visible, so calibration is to the winner standard in the kit brief itself.

Design choices for this line:
- **Cold-read landing:** the setup ("babies come from the cloud") reads as a familiar parental white lie; the punchline lands in the second sentence with no extra setup.
- **Surprise:** the toddler takes the lie literally and applies modern-tech logic — asking a voice assistant to order a sibling like a delivery.
- **Economy:** 86 characters, two short sentences, nothing trimmable.
- **Freshness:** no recycled joke setup (no chicken, no bar, no "walks into"); a current-tech premise (cloud + Alexa) unlikely to be duplicated verbatim among the 2,595 entries.

## How it runs

`main.py` is deterministic (no network, no randomness): it writes the joke line to `entry.txt` next to itself and to `/output/entry.txt` when that directory is mounted by the harness.
