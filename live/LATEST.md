# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:28:27.511887Z`  
Current process started UTC: `2026-09-20T10:24:26.836654Z`  
1-second metadata polls in this process: **232**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=NPSHYD|generation` = **274** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=OTHER|generation` = **473** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=PS|generation` = **-702** (n=1527, 2026-09-20T10:25:31.923827Z)
- `FUELINST|fuelType=WIND|generation` = **14031** (n=1527, 2026-09-20T10:25:31.923827Z)
- `IMBALNGC|TOTAL|imbalance` = **-4140** (n=251, 2026-09-20T10:19:35.299200Z)
- `INDDEM|TOTAL|demand` = **-12466** (n=251, 2026-09-20T10:19:35.299200Z)
- `INDGEN|TOTAL|generation` = **16026** (n=251, 2026-09-20T10:19:35.299200Z)
- `MELNGC|TOTAL|margin` = **39778** (n=251, 2026-09-20T10:19:19.340337Z)
- `NDF|TOTAL|demand` = **19666** (n=257, 2026-09-20T10:17:11.038096Z)
- `TSDF|TOTAL|demand` = **20166** (n=257, 2026-09-20T10:17:11.038096Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T10:28:26.546617Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:25.546509Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:24.546395Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:23.546315Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:22.546178Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:21.546036Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:20.545914Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:19.545791Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:18.545660Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:17.545546Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:16.545477Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:14.401200Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:14.401200Z` — **FREQ**: 5761 rows; marker `2026-09-20T10:27:45Z`
- `2026-09-20T10:28:13.401094Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:28:12.400964Z` — **MID**: 0 rows; marker `2026-09-20T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
