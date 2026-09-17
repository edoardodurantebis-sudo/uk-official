# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T22:28:13.736064Z`  
Current process started UTC: `2026-09-17T22:24:13.429703Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **343** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=NPSHYD|generation` = **453** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=OTHER|generation` = **1436** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=PS|generation` = **52** (n=851, 2026-09-17T22:25:33.668711Z)
- `FUELINST|fuelType=WIND|generation` = **15177** (n=851, 2026-09-17T22:25:33.668711Z)
- `IMBALNGC|TOTAL|imbalance` = **9711** (n=141, 2026-09-17T22:22:56.309718Z)
- `INDDEM|TOTAL|demand` = **-11161** (n=141, 2026-09-17T22:23:12.245605Z)
- `INDGEN|TOTAL|generation` = **26525** (n=141, 2026-09-17T22:23:12.245605Z)
- `MELNGC|TOTAL|margin` = **36437** (n=141, 2026-09-17T22:20:44.633510Z)
- `NDF|TOTAL|demand` = **16314** (n=144, 2026-09-17T22:17:57.884209Z)
- `TSDF|TOTAL|demand` = **16814** (n=144, 2026-09-17T22:17:57.884209Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T22:28:12.019307Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:10.311117Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:08.560606Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:06.862689Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:05.157381Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:03.460004Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:01.766626Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:28:00.061700Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:57.940723Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:56.190938Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:54.479923Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:52.766970Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:51.061943Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:49.359581Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T22:27:47.658600Z` — **MID**: 0 rows; marker `2026-09-17T22:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
