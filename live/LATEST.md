# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:07:27.363274Z`  
Current process started UTC: `2026-09-20T14:03:26.625087Z`  
1-second metadata polls in this process: **227**  
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

- `FUELINST|fuelType=INTVKL|generation` = **246** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=NPSHYD|generation` = **264** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=OTHER|generation` = **784** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=PS|generation` = **-739** (n=1571, 2026-09-20T14:05:38.423109Z)
- `FUELINST|fuelType=WIND|generation` = **9725** (n=1571, 2026-09-20T14:05:38.423109Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=258, 2026-09-20T13:53:04.012223Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=258, 2026-09-20T13:52:48.484578Z)
- `INDGEN|TOTAL|generation` = **15373** (n=258, 2026-09-20T13:52:48.484578Z)
- `MELNGC|TOTAL|margin` = **35798** (n=258, 2026-09-20T13:50:08.246114Z)
- `NDF|TOTAL|demand` = **20604** (n=264, 2026-09-20T13:48:00.146875Z)
- `TSDF|TOTAL|demand` = **21104** (n=264, 2026-09-20T13:48:15.662061Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:07:26.403724Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:25.403663Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:24.403559Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:23.403458Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:22.403350Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:21.403249Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:20.349782Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:19.349679Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:18.349574Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:17.349472Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:16.349373Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:15.349273Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:14.055168Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:13.055108Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:07:12.055038Z` — **MID**: 0 rows; marker `2026-09-20T14:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
