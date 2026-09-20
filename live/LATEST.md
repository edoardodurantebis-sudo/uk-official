# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:25:28.567136Z`  
Current process started UTC: `2026-09-20T13:21:27.946509Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **129** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=NPSHYD|generation` = **262** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=OTHER|generation` = **304** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=PS|generation` = **-673** (n=1562, 2026-09-20T13:20:30.066297Z)
- `FUELINST|fuelType=WIND|generation` = **11689** (n=1562, 2026-09-20T13:20:30.066297Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDGEN|TOTAL|generation` = **15373** (n=257, 2026-09-20T13:23:35.682760Z)
- `MELNGC|TOTAL|margin` = **35771** (n=257, 2026-09-20T13:20:30.066297Z)
- `NDF|TOTAL|demand` = **20604** (n=263, 2026-09-20T13:18:20.388440Z)
- `TSDF|TOTAL|demand` = **21104** (n=263, 2026-09-20T13:18:20.388440Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:25:27.248916Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:25.866533Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:24.571719Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:23.224250Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:21.884883Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:20.605814Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:19.342068Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:18.099523Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:16.815709Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:14.955334Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:13.691624Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:12.277053Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:11.004089Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:09.750653Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:25:08.423440Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
