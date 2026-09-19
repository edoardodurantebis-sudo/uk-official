# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:25:36.562658Z`  
Current process started UTC: `2026-09-19T18:21:35.587062Z`  
1-second metadata polls in this process: **221**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=NPSHYD|generation` = **500** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=OTHER|generation` = **1163** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1334, 2026-09-19T18:20:38.758704Z)
- `FUELINST|fuelType=WIND|generation` = **14322** (n=1334, 2026-09-19T18:20:38.758704Z)
- `IMBALNGC|TOTAL|imbalance` = **-3750** (n=220, 2026-09-19T18:22:57.004790Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=220, 2026-09-19T18:22:40.062173Z)
- `INDGEN|TOTAL|generation` = **16202** (n=220, 2026-09-19T18:22:40.062173Z)
- `MELNGC|TOTAL|margin` = **36202** (n=220, 2026-09-19T18:20:22.618497Z)
- `NDF|TOTAL|demand` = **19452** (n=225, 2026-09-19T18:18:14.376223Z)
- `TSDF|TOTAL|demand` = **19952** (n=225, 2026-09-19T18:18:14.376223Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:25:35.548287Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:34.527058Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:33.465723Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:32.434978Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:31.412342Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:30.380496Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:29.374117Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:28.355144Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:27.337491Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:26.291551Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:25.273849Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:24.257471Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:23.234274Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:22.226936Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:25:20.621117Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
