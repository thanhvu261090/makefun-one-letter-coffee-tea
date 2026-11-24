# One Letter: Coffee or Tea

[![make.fun competition](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/thanhvu261090/makefun-one-letter-coffee-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/thanhvu261090/makefun-one-letter-coffee-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

Entry for the [One Letter: Coffee or Tea](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) bounty on make.fun.

## The entry

`main.py` (Python 3.13, standard library only, no network) writes exactly
one letter to `/output/entry.txt`: **A** — the kit's letter for coffee.

Coffee is the pick: it is the fuel of the all-night build grind, the drink
that keeps a builder going when the work runs past midnight, while tea is
the drink of slowing down. One byte, no newline, nothing else.

## Run

```sh
python3 main.py
wc -c /output/entry.txt   # 1
```

`main.py` self-checks after writing: the file must be exactly 1 byte holding
a single A–Z letter, or it exits with an error.
