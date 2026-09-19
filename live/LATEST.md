# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:21:25.146945Z`  
Current process started UTC: `2026-09-19T18:17:24.514715Z`  
1-second metadata polls in this process: **219**  
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
- `IMBALNGC|TOTAL|imbalance` = **-3139** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDGEN|TOTAL|generation` = **16813** (n=219, 2026-09-19T17:53:18.380714Z)
- `MELNGC|TOTAL|margin` = **36202** (n=220, 2026-09-19T18:20:22.618497Z)
- `NDF|TOTAL|demand` = **19452** (n=225, 2026-09-19T18:18:14.376223Z)
- `TSDF|TOTAL|demand` = **19952** (n=225, 2026-09-19T18:18:14.376223Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:21:24.198187Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:23.198094Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:22.197954Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:21.197889Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:20.197794Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:19.197712Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:18.197611Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:17.197484Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:16.197372Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:15.197206Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:14.197147Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:13.197009Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:12.196909Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:10.230945Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:21:09.230833Z` — **MID**: 0 rows; marker `2026-09-19T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
