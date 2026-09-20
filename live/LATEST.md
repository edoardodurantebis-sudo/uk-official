# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:42:11.850475Z`  
Current process started UTC: `2026-09-20T13:38:11.124841Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **129** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=OTHER|generation` = **422** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=PS|generation` = **-495** (n=1566, 2026-09-20T13:40:33.404939Z)
- `FUELINST|fuelType=WIND|generation` = **10492** (n=1566, 2026-09-20T13:40:33.404939Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDGEN|TOTAL|generation` = **15373** (n=257, 2026-09-20T13:23:35.682760Z)
- `MELNGC|TOTAL|margin` = **35771** (n=257, 2026-09-20T13:20:30.066297Z)
- `NDF|TOTAL|demand` = **20604** (n=263, 2026-09-20T13:18:20.388440Z)
- `TSDF|TOTAL|demand` = **21104** (n=263, 2026-09-20T13:18:20.388440Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:42:10.849714Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:09.846285Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:08.841214Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:07.454176Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:06.454086Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:05.447810Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:04.425959Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:03.403570Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:02.403470Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:01.372677Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:42:00.372606Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:41:59.356950Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:41:58.356876Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:41:57.345370Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:41:56.329563Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
