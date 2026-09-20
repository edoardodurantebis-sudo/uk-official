# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:32:40.594186Z`  
Current process started UTC: `2026-09-20T14:28:39.313914Z`  
1-second metadata polls in this process: **177**  
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

- `FUELINST|fuelType=INTVKL|generation` = **286** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=NPSHYD|generation` = **267** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=OTHER|generation` = **1068** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=PS|generation` = **-596** (n=1576, 2026-09-20T14:30:47.005830Z)
- `FUELINST|fuelType=WIND|generation` = **9357** (n=1576, 2026-09-20T14:30:47.005830Z)
- `IMBALNGC|TOTAL|imbalance` = **-5650** (n=259, 2026-09-20T14:24:26.270027Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=259, 2026-09-20T14:24:09.197108Z)
- `INDGEN|TOTAL|generation` = **15454** (n=259, 2026-09-20T14:24:09.197108Z)
- `MELNGC|TOTAL|margin` = **35389** (n=259, 2026-09-20T14:20:58.322467Z)
- `NDF|TOTAL|demand` = **20604** (n=265, 2026-09-20T14:18:25.070664Z)
- `TSDF|TOTAL|demand` = **21104** (n=265, 2026-09-20T14:18:25.070664Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:32:39.296995Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:37.543286Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:35.833602Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:34.486005Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:32.917655Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:31.278697Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:29.599877Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:28.293278Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:26.516007Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:24.971549Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:22.281745Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:22.281745Z` — **FREQ**: 5761 rows; marker `2026-09-20T14:31:45Z`
- `2026-09-20T14:32:20.585240Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:18.897930Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:32:17.594245Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
