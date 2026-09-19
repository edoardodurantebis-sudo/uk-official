# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T17:39:26.232638Z`  
Current process started UTC: `2026-09-19T17:35:25.295555Z`  
1-second metadata polls in this process: **170**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=NPSHYD|generation` = **437** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=OTHER|generation` = **1755** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=PS|generation` = **796** (n=1325, 2026-09-19T17:35:42.082235Z)
- `FUELINST|fuelType=WIND|generation` = **14451** (n=1325, 2026-09-19T17:35:42.082235Z)
- `IMBALNGC|TOTAL|imbalance` = **-3136** (n=218, 2026-09-19T17:23:37.629192Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=218, 2026-09-19T17:23:37.629192Z)
- `INDGEN|TOTAL|generation` = **16816** (n=218, 2026-09-19T17:23:37.629192Z)
- `MELNGC|TOTAL|margin` = **36252** (n=218, 2026-09-19T17:20:30.338001Z)
- `NDF|TOTAL|demand` = **19452** (n=223, 2026-09-19T17:17:59.057425Z)
- `TSDF|TOTAL|demand` = **19952** (n=223, 2026-09-19T17:18:14.750483Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T17:39:24.924726Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:23.492807Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:22.155307Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:20.859078Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:18.835840Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:17.506238Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:16.172940Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:14.867313Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:13.566072Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:12.258193Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:10.967977Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:09.617620Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:08.312162Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:06.969015Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:39:05.664650Z` — **MID**: 0 rows; marker `2026-09-19T17:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
