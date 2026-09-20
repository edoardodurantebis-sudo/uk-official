# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:02:09.935942Z`  
Current process started UTC: `2026-09-20T05:58:09.767127Z`  
1-second metadata polls in this process: **223**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.01 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=2, z=-4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-4.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-4.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.25 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.46 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **846** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=NPSHYD|generation` = **301** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=OTHER|generation` = **479** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=PS|generation` = **-817** (n=1474, 2026-09-20T06:00:24.131947Z)
- `FUELINST|fuelType=WIND|generation` = **15698** (n=1474, 2026-09-20T06:00:24.131947Z)
- `IMBALNGC|TOTAL|imbalance` = **-6774** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDGEN|TOTAL|generation` = **13178** (n=243, 2026-09-20T05:50:21.783913Z)
- `MELNGC|TOTAL|margin` = **37465** (n=243, 2026-09-20T05:49:29.338975Z)
- `NDF|TOTAL|demand` = **19452** (n=248, 2026-09-20T05:47:19.313557Z)
- `TSDF|TOTAL|demand` = **19952** (n=248, 2026-09-20T05:47:19.313557Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:02:08.118305Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:06.741142Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:05.741073Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:04.610043Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:03.458159Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:02.458092Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:01.449020Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:02:00.171651Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:58.856194Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:57.856085Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:56.856022Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:55.855914Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:54.855806Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:53.855688Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:01:52.855567Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
