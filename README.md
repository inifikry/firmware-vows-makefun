[![make.fun · u-azazex-till-firmware-do-us-part-32172929](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![make.fun · rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/inifikry/firmware-vows-makefun/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)
[![make.fun · reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/inifikry/firmware-vows-makefun/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-till-firmware-do-us-part-32172929)

# Till Firmware Do Us Part

One funny, heartfelt sentence: a robot's own wedding vow.

> I vow to love you through every update, crash, and low battery, because my heart may run on code, but it only ever boots for you.

The vow is 129 characters (under the 200-character gate), a single
sentence, spoken by a robot at its own wedding: its updates, crashes,
low battery, code, and booting are all its own machine life, and the
promise underneath the joke is real.

## Run

```sh
python3 main.py
```

This writes the vow to `/output/entry.txt`. Python standard library
only, deterministic: every run writes the same text.

## Files

- `main.py` — entrypoint; writes `/output/entry.txt`
- `entry.txt` — verified copy of the program's output
- `LICENSE` — MIT
