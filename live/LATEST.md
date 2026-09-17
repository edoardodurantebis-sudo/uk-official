# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T23:22:50.108859Z`  
Current process started UTC: `2026-09-17T23:18:49.054193Z`  
1-second metadata polls in this process: **164**  
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

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=NPSHYD|generation` = **451** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3318** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=OTHER|generation` = **612** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=PS|generation` = **55** (n=862, 2026-09-17T23:20:43.837845Z)
- `FUELINST|fuelType=WIND|generation` = **14818** (n=862, 2026-09-17T23:20:43.837845Z)
- `IMBALNGC|TOTAL|imbalance` = **9745** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=143, 2026-09-17T23:22:08.151476Z)
- `INDGEN|TOTAL|generation` = **26559** (n=143, 2026-09-17T23:22:08.151476Z)
- `MELNGC|TOTAL|margin` = **36572** (n=143, 2026-09-17T23:20:11.082648Z)
- `NDF|TOTAL|demand` = **16314** (n=146, 2026-09-17T23:18:11.234096Z)
- `TSDF|TOTAL|demand` = **16814** (n=146, 2026-09-17T23:18:11.234096Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T23:22:48.687680Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:47.350626Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:45.964355Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:44.658675Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:43.342902Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:41.983826Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:40.254341Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:38.879835Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:37.536577Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:36.230783Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:34.921069Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:33.521244Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:32.165893Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:30.815902Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T23:22:29.479868Z` — **MID**: 0 rows; marker `2026-09-17T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
