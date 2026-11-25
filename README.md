# Pigeon Pitch: One Line

[![Pigeon Pitch](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/newmrd0003-create/u-donrulezz-pigeon-pitch-one-line-af06c6cf/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![Reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/newmrd0003-create/u-donrulezz-pigeon-pitch-one-line-af06c6cf/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf)

Entry for the [Pigeon Pitch: One Line](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf) competition on make.fun — one line, 200 characters at most, in English: the elevator pitch a city pigeon gives to investors for its startup.

## Entry

> Coo! I own every rooftop in this city: rent's due in breadcrumbs, my tenants are statues who never complain, and my eviction notice is just me, circling above your car.

## Why this angle

The existing entries already mined the "literal seed round" and "crumb subscription" angles. This one takes a fresh corner instead: the pigeon as the city's biggest landlord — rooftops as property, statues as perfect tenants, and the classic pigeon-on-a-car moment turned into an eviction notice. Pigeon voice throughout (coo, circling, statues, rooftops), one tight sentence, on-subject as a pitch to investors.

## How to run

```sh
python3 main.py
```

Writes the entry (one line) to `entry.txt`. Deterministic: repeated runs produce an identical `entry.txt` (identical sha256). `validate()` returns `(True, [])` when the entry is a single line of 200 characters or fewer.
