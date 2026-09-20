# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T15:19:27.871886Z`  
Current process started UTC: `2026-09-20T15:15:26.648491Z`  
1-second metadata polls in this process: **131**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1323** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=OTHER|generation` = **408** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=PS|generation` = **-554** (n=1585, 2026-09-20T15:15:44.188202Z)
- `FUELINST|fuelType=WIND|generation` = **8977** (n=1585, 2026-09-20T15:15:44.188202Z)
- `IMBALNGC|TOTAL|imbalance` = **-5158** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDGEN|TOTAL|generation` = **15452** (n=260, 2026-09-20T14:53:20.202311Z)
- `MELNGC|TOTAL|margin` = **35910** (n=260, 2026-09-20T14:50:25.474421Z)
- `NDF|TOTAL|demand` = **20110** (n=267, 2026-09-20T15:17:54.992847Z)
- `TSDF|TOTAL|demand` = **20610** (n=267, 2026-09-20T15:17:54.992847Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T15:19:26.157371Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:24.435478Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:22.709664Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:21.012806Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:19.315776Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:17.612733Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:15.600232Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:13.877939Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:12.170747Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:10.459634Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:08.756053Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:07.043691Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:05.200045Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:03.441303Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:19:01.728266Z` — **MID**: 0 rows; marker `2026-09-20T15:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
