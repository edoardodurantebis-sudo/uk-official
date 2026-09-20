# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:49:59.743482Z`  
Current process started UTC: `2026-09-20T14:45:58.595483Z`  
1-second metadata polls in this process: **196**  
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

- `FUELINST|fuelType=INTVKL|generation` = **286** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=NPSHYD|generation` = **283** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=OTHER|generation` = **1389** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=PS|generation` = **-578** (n=1579, 2026-09-20T14:45:58.595494Z)
- `FUELINST|fuelType=WIND|generation` = **8939** (n=1579, 2026-09-20T14:45:58.595494Z)
- `IMBALNGC|TOTAL|imbalance` = **-5650** (n=259, 2026-09-20T14:24:26.270027Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=259, 2026-09-20T14:24:09.197108Z)
- `INDGEN|TOTAL|generation` = **15454** (n=259, 2026-09-20T14:24:09.197108Z)
- `MELNGC|TOTAL|margin` = **35389** (n=259, 2026-09-20T14:20:58.322467Z)
- `NDF|TOTAL|demand` = **20110** (n=266, 2026-09-20T14:48:04.209492Z)
- `TSDF|TOTAL|demand` = **20610** (n=266, 2026-09-20T14:48:04.209492Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:49:58.570084Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:57.406483Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:56.219990Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:55.050154Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:53.566979Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:52.395779Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:51.196261Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:50.003410Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:48.845826Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:47.663449Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:46.465649Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:45.271416Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:44.067836Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:42.883462Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:49:41.722744Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
