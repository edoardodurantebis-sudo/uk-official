# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T17:22:38.321069Z`  
Current process started UTC: `2026-09-19T17:18:38.247553Z`  
1-second metadata polls in this process: **223**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=NPSHYD|generation` = **436** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=OTHER|generation` = **1838** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=PS|generation` = **683** (n=1322, 2026-09-19T17:20:30.338001Z)
- `FUELINST|fuelType=WIND|generation` = **14705** (n=1322, 2026-09-19T17:20:30.338001Z)
- `IMBALNGC|TOTAL|imbalance` = **-3150** (n=217, 2026-09-19T16:53:56.891666Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=217, 2026-09-19T16:53:41.181542Z)
- `INDGEN|TOTAL|generation` = **16802** (n=217, 2026-09-19T16:53:41.181542Z)
- `MELNGC|TOTAL|margin` = **36252** (n=218, 2026-09-19T17:20:30.338001Z)
- `NDF|TOTAL|demand` = **19452** (n=223, 2026-09-19T17:17:59.057425Z)
- `TSDF|TOTAL|demand` = **19952** (n=223, 2026-09-19T17:18:14.750483Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T17:22:37.336769Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:36.336643Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:35.336512Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:34.336441Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:33.336374Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:32.336284Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:31.336174Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:30.336084Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:29.319073Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:28.288372Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:27.288289Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:26.288221Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:25.288130Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:24.288056Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T17:22:21.768054Z` — **MID**: 0 rows; marker `2026-09-19T17:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
