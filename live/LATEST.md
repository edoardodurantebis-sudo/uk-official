# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:05:11.647197Z`  
Current process started UTC: `2026-09-17T20:01:10.840792Z`  
1-second metadata polls in this process: **222**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1242** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=NPSHYD|generation` = **591** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=OTHER|generation` = **402** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=PS|generation` = **503** (n=822, 2026-09-17T20:00:31.976541Z)
- `FUELINST|fuelType=WIND|generation` = **15895** (n=822, 2026-09-17T20:00:31.976541Z)
- `IMBALNGC|TOTAL|imbalance` = **9708** (n=136, 2026-09-17T19:53:01.099555Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=136, 2026-09-17T19:52:45.276545Z)
- `INDGEN|TOTAL|generation` = **26522** (n=136, 2026-09-17T19:52:45.276545Z)
- `MELNGC|TOTAL|margin` = **36519** (n=136, 2026-09-17T19:50:44.130170Z)
- `NDF|TOTAL|demand` = **16314** (n=139, 2026-09-17T19:48:10.710850Z)
- `TSDF|TOTAL|demand` = **16814** (n=139, 2026-09-17T19:48:10.710850Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:05:10.574439Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:09.571796Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:08.527812Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:07.521468Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:06.515481Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:05.488105Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:04.445345Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:03.428619Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:02.371618Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:01.316974Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:05:00.270796Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:04:59.202638Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:04:58.186393Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:04:56.682843Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:04:55.626642Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
