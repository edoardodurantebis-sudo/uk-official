# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T12:56:06.355112Z`  
Current process started UTC: `2026-09-20T12:52:05.906233Z`  
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

- `2026-09-20T12:56:04.189336Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:56:04.189336Z` — **FREQ**: 5761 rows; marker `2026-09-20T12:55:45Z`
- `2026-09-20T12:56:03.189250Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:56:02.189172Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:56:01.189045Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:56:00.151043Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:59.150973Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:58.150862Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:57.150772Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:56.150659Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:55.150578Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:54.150461Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:53.150335Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:52.125237Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:55:51.125109Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
