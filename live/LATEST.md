# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:15:47.621851Z`  
Current process started UTC: `2026-09-20T14:11:46.864129Z`  
1-second metadata polls in this process: **225**  
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

- `FUELINST|fuelType=INTVKL|generation` = **286** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=OTHER|generation` = **683** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=PS|generation` = **-785** (n=1573, 2026-09-20T14:15:33.266750Z)
- `FUELINST|fuelType=WIND|generation` = **9615** (n=1573, 2026-09-20T14:15:33.266750Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=258, 2026-09-20T13:53:04.012223Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=258, 2026-09-20T13:52:48.484578Z)
- `INDGEN|TOTAL|generation` = **15373** (n=258, 2026-09-20T13:52:48.484578Z)
- `MELNGC|TOTAL|margin` = **35798** (n=258, 2026-09-20T13:50:08.246114Z)
- `NDF|TOTAL|demand` = **20604** (n=264, 2026-09-20T13:48:00.146875Z)
- `TSDF|TOTAL|demand` = **21104** (n=264, 2026-09-20T13:48:15.662061Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:15:46.535599Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:45.535504Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:44.502734Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:43.480329Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:42.436842Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:41.402966Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:40.366886Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:39.333406Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:38.328464Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:37.316517Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:36.263152Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:35.190489Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:33.266750Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:15:33.266750Z` — **FUELINST**: 80 rows; marker `2026-09-20T14:15:00Z`
- `2026-09-20T14:15:32.247071Z` — **MID**: 0 rows; marker `2026-09-20T14:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
