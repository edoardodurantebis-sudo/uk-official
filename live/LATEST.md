# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:04:27.265127Z`  
Current process started UTC: `2026-09-20T13:00:26.712186Z`  
1-second metadata polls in this process: **224**  
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

- `FUELINST|fuelType=INTVKL|generation` = **18** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=NPSHYD|generation` = **262** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=OTHER|generation` = **522** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=PS|generation` = **-671** (n=1558, 2026-09-20T13:00:26.712195Z)
- `FUELINST|fuelType=WIND|generation` = **12033** (n=1558, 2026-09-20T13:00:26.712195Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=256, 2026-09-20T12:54:13.127676Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=256, 2026-09-20T12:53:56.150495Z)
- `INDGEN|TOTAL|generation` = **15373** (n=256, 2026-09-20T12:53:56.150495Z)
- `MELNGC|TOTAL|margin` = **35771** (n=256, 2026-09-20T12:50:50.610978Z)
- `NDF|TOTAL|demand` = **20604** (n=262, 2026-09-20T12:48:26.154558Z)
- `TSDF|TOTAL|demand` = **21104** (n=262, 2026-09-20T12:48:26.154558Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:04:26.311974Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:23.181295Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:23.181295Z` — **FREQ**: 5761 rows; marker `2026-09-20T13:03:45Z`
- `2026-09-20T13:04:22.181176Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:21.181104Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:20.181005Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:19.180910Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:18.180801Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:17.180674Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:15.892148Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:14.892031Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:13.891949Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:12.891834Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:11.891753Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:04:10.891635Z` — **MID**: 0 rows; marker `2026-09-20T12:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
