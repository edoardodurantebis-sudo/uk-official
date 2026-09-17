# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T20:22:00.774339Z`  
Current process started UTC: `2026-09-17T20:18:00.712574Z`  
1-second metadata polls in this process: **172**  
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

- `FUELINST|fuelType=INTVKL|generation` = **728** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=NPSHYD|generation` = **561** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3320** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=OCGT|generation` = **38** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=OTHER|generation` = **755** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=PS|generation` = **503** (n=826, 2026-09-17T20:20:29.412257Z)
- `FUELINST|fuelType=WIND|generation` = **15646** (n=826, 2026-09-17T20:20:29.412257Z)
- `IMBALNGC|TOTAL|imbalance` = **9708** (n=136, 2026-09-17T19:53:01.099555Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=136, 2026-09-17T19:52:45.276545Z)
- `INDGEN|TOTAL|generation` = **26522** (n=136, 2026-09-17T19:52:45.276545Z)
- `MELNGC|TOTAL|margin` = **36451** (n=137, 2026-09-17T20:20:13.977200Z)
- `NDF|TOTAL|demand` = **16314** (n=140, 2026-09-17T20:18:03.614644Z)
- `TSDF|TOTAL|demand` = **16814** (n=140, 2026-09-17T20:18:03.614644Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T20:21:59.400118Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:58.079320Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:56.788933Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:55.455133Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:54.133479Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:52.826494Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:51.055475Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:49.775747Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:48.407980Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:47.050432Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:45.750186Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:44.462602Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:43.195135Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:41.890795Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T20:21:40.521786Z` — **MID**: 0 rows; marker `2026-09-17T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
