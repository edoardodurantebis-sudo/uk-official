# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T14:58:25.331487Z`  
Current process started UTC: `2026-09-20T14:54:23.587539Z`  
1-second metadata polls in this process: **180**  
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

- `FUELINST|fuelType=INTVKL|generation` = **294** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=OTHER|generation` = **1497** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=PS|generation` = **-354** (n=1581, 2026-09-20T14:55:27.586245Z)
- `FUELINST|fuelType=WIND|generation` = **8648** (n=1581, 2026-09-20T14:55:27.586245Z)
- `IMBALNGC|TOTAL|imbalance` = **-5158** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDGEN|TOTAL|generation` = **15452** (n=260, 2026-09-20T14:53:20.202311Z)
- `MELNGC|TOTAL|margin` = **35910** (n=260, 2026-09-20T14:50:25.474421Z)
- `NDF|TOTAL|demand` = **20110** (n=266, 2026-09-20T14:48:04.209492Z)
- `TSDF|TOTAL|demand` = **20610** (n=266, 2026-09-20T14:48:04.209492Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T14:58:22.572019Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:22.572019Z` — **FREQ**: 5761 rows; marker `2026-09-20T14:57:45Z`
- `2026-09-20T14:58:21.276118Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:20.005533Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:18.713194Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:17.433574Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:16.140428Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:14.841855Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:13.575640Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:12.304880Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:11.030403Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:09.732433Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:08.386424Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:06.839203Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T14:58:05.564073Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
