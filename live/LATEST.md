# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:00:16.708672Z`  
Current process started UTC: `2026-09-20T12:56:16.347209Z`  
1-second metadata polls in this process: **234**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=OTHER|generation` = **518** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=PS|generation` = **-669** (n=1557, 2026-09-20T12:55:16.869618Z)
- `FUELINST|fuelType=WIND|generation` = **12085** (n=1557, 2026-09-20T12:55:16.869618Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=256, 2026-09-20T12:54:13.127676Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=256, 2026-09-20T12:53:56.150495Z)
- `INDGEN|TOTAL|generation` = **15373** (n=256, 2026-09-20T12:53:56.150495Z)
- `MELNGC|TOTAL|margin` = **35771** (n=256, 2026-09-20T12:50:50.610978Z)
- `NDF|TOTAL|demand` = **20604** (n=262, 2026-09-20T12:48:26.154558Z)
- `TSDF|TOTAL|demand` = **21104** (n=262, 2026-09-20T12:48:26.154558Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:00:15.749304Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:14.749229Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:13.749149Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:12.542419Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:11.542310Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:10.542174Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:09.542096Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:08.538649Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:07.481708Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:06.481587Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:05.481509Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:04.481427Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:02.912346Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:01.912224Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:00:00.678986Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
