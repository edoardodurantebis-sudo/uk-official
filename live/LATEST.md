# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:28:27.795626Z`  
Current process started UTC: `2026-09-20T14:24:24.484927Z`  
1-second metadata polls in this process: **135**  
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

- `FUELINST|fuelType=INTVKL|generation` = **286** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=NPSHYD|generation` = **264** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=OTHER|generation` = **1020** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=PS|generation` = **-773** (n=1575, 2026-09-20T14:25:30.646784Z)
- `FUELINST|fuelType=WIND|generation` = **9386** (n=1575, 2026-09-20T14:25:30.646784Z)
- `IMBALNGC|TOTAL|imbalance` = **-5650** (n=259, 2026-09-20T14:24:26.270027Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=259, 2026-09-20T14:24:09.197108Z)
- `INDGEN|TOTAL|generation` = **15454** (n=259, 2026-09-20T14:24:09.197108Z)
- `MELNGC|TOTAL|margin` = **35389** (n=259, 2026-09-20T14:20:58.322467Z)
- `NDF|TOTAL|demand` = **20604** (n=265, 2026-09-20T14:18:25.070664Z)
- `TSDF|TOTAL|demand` = **21104** (n=265, 2026-09-20T14:18:25.070664Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:28:24.075527Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:24.075527Z` — **FREQ**: 5761 rows; marker `2026-09-20T14:27:45Z`
- `2026-09-20T14:28:22.378935Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:20.654706Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:18.952109Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:17.230624Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:15.512557Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:13.804902Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:12.104786Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:10.393410Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:08.437584Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:06.725932Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:04.992009Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:03.275605Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:28:01.574492Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
