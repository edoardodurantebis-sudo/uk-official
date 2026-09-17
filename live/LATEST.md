# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:56:45.304838Z`  
Current process started UTC: `2026-09-17T19:52:45.276537Z`  
1-second metadata polls in this process: **171**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=NPSHYD|generation` = **594** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=OCGT|generation` = **69** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=OTHER|generation` = **365** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=PS|generation` = **503** (n=821, 2026-09-17T19:55:28.822297Z)
- `FUELINST|fuelType=WIND|generation` = **15879** (n=821, 2026-09-17T19:55:28.822297Z)
- `IMBALNGC|TOTAL|imbalance` = **9708** (n=136, 2026-09-17T19:53:01.099555Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=136, 2026-09-17T19:52:45.276545Z)
- `INDGEN|TOTAL|generation` = **26522** (n=136, 2026-09-17T19:52:45.276545Z)
- `MELNGC|TOTAL|margin` = **36519** (n=136, 2026-09-17T19:50:44.130170Z)
- `NDF|TOTAL|demand` = **16314** (n=139, 2026-09-17T19:48:10.710850Z)
- `TSDF|TOTAL|demand` = **16814** (n=139, 2026-09-17T19:48:10.710850Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T19:56:43.994887Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:42.665863Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:41.361853Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:40.049048Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:38.712036Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:37.422045Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:36.120845Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:34.786712Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:32.886297Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:31.582847Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:30.279551Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:28.952422Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:27.597641Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:26.278301Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:56:24.986345Z` — **MID**: 0 rows; marker `2026-09-17T19:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
