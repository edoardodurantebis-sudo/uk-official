# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:49:30.775650Z`  
Current process started UTC: `2026-09-20T10:45:29.376583Z`  
1-second metadata polls in this process: **138**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=NPSHYD|generation` = **271** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3343** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=OTHER|generation` = **524** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=PS|generation` = **-924** (n=1531, 2026-09-20T10:45:29.376590Z)
- `FUELINST|fuelType=WIND|generation` = **13797** (n=1531, 2026-09-20T10:45:29.376590Z)
- `IMBALNGC|TOTAL|imbalance` = **-4140** (n=251, 2026-09-20T10:19:35.299200Z)
- `INDDEM|TOTAL|demand` = **-12466** (n=251, 2026-09-20T10:19:35.299200Z)
- `INDGEN|TOTAL|generation` = **16026** (n=251, 2026-09-20T10:19:35.299200Z)
- `MELNGC|TOTAL|margin` = **39778** (n=251, 2026-09-20T10:19:19.340337Z)
- `NDF|TOTAL|demand` = **20604** (n=258, 2026-09-20T10:48:26.920343Z)
- `TSDF|TOTAL|demand` = **21104** (n=258, 2026-09-20T10:48:42.282443Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T10:49:29.110147Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:27.474889Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:25.839805Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:24.189400Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:22.539738Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:20.910224Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:19.265630Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:17.661932Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:16.021841Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:14.135664Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:12.509626Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:10.874856Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:09.226355Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:07.455536Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:49:05.421303Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
