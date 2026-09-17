# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T22:32:27.650607Z`  
Current process started UTC: `2026-09-17T22:28:27.521868Z`  
1-second metadata polls in this process: **168**  
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

- `FUELINST|fuelType=INTVKL|generation` = **343** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=NPSHYD|generation` = **454** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=OTHER|generation` = **1439** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=PS|generation` = **53** (n=852, 2026-09-17T22:30:37.893201Z)
- `FUELINST|fuelType=WIND|generation` = **15135** (n=852, 2026-09-17T22:30:37.893201Z)
- `IMBALNGC|TOTAL|imbalance` = **9711** (n=141, 2026-09-17T22:22:56.309718Z)
- `INDDEM|TOTAL|demand` = **-11161** (n=141, 2026-09-17T22:23:12.245605Z)
- `INDGEN|TOTAL|generation` = **26525** (n=141, 2026-09-17T22:23:12.245605Z)
- `MELNGC|TOTAL|margin` = **36437** (n=141, 2026-09-17T22:20:44.633510Z)
- `NDF|TOTAL|demand` = **16314** (n=144, 2026-09-17T22:17:57.884209Z)
- `TSDF|TOTAL|demand` = **16814** (n=144, 2026-09-17T22:17:57.884209Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T22:32:26.325545Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:25.043412Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:23.246146Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:21.898090Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:20.265132Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:18.971930Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:16.091564Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:16.091564Z` — **FREQ**: 5761 rows; marker `2026-09-17T22:31:45Z`
- `2026-09-17T22:32:14.735327Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:13.458690Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:12.112638Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:10.831822Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:09.557715Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:08.244376Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:32:06.914404Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
