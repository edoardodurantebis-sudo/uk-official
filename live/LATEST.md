# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T11:48:17.670723Z`  
Current process started UTC: `2026-09-20T11:44:15.518125Z`  
1-second metadata polls in this process: **218**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=NPSHYD|generation` = **286** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=OTHER|generation` = **457** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=PS|generation` = **-667** (n=1543, 2026-09-20T11:45:35.073945Z)
- `FUELINST|fuelType=WIND|generation` = **12802** (n=1543, 2026-09-20T11:45:35.073945Z)
- `IMBALNGC|TOTAL|imbalance` = **-5732** (n=253, 2026-09-20T11:24:21.965190Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=253, 2026-09-20T11:23:50.776605Z)
- `INDGEN|TOTAL|generation` = **15372** (n=253, 2026-09-20T11:23:50.776605Z)
- `MELNGC|TOTAL|margin` = **35780** (n=253, 2026-09-20T11:20:39.027170Z)
- `NDF|TOTAL|demand` = **20604** (n=260, 2026-09-20T11:48:14.448744Z)
- `TSDF|TOTAL|demand` = **21104** (n=260, 2026-09-20T11:48:14.448744Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T11:48:14.448744Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:14.448744Z` — **TSDF**: 1440 rows; marker `2026-09-20T11:47:00Z`
- `2026-09-20T11:48:14.448744Z` — **NDF**: 80 rows; marker `2026-09-20T11:47:00Z`
- `2026-09-20T11:48:14.448744Z` — **FREQ**: 5761 rows; marker `2026-09-20T11:47:45Z`
- `2026-09-20T11:48:13.435295Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:12.248017Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:11.246920Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:10.216339Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:09.010953Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:07.655859Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:06.089488Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:04.652709Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:03.528583Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:02.528513Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:48:01.514041Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
