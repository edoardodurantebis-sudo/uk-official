# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T15:11:00.799140Z`  
Current process started UTC: `2026-09-20T15:07:00.776921Z`  
1-second metadata polls in this process: **230**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1309** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=NPSHYD|generation` = **281** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=OTHER|generation` = **397** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=PS|generation` = **-786** (n=1584, 2026-09-20T15:10:41.917233Z)
- `FUELINST|fuelType=WIND|generation` = **9008** (n=1584, 2026-09-20T15:10:41.917233Z)
- `IMBALNGC|TOTAL|imbalance` = **-5158** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDGEN|TOTAL|generation` = **15452** (n=260, 2026-09-20T14:53:20.202311Z)
- `MELNGC|TOTAL|margin` = **35910** (n=260, 2026-09-20T14:50:25.474421Z)
- `NDF|TOTAL|demand` = **20110** (n=266, 2026-09-20T14:48:04.209492Z)
- `TSDF|TOTAL|demand` = **20610** (n=266, 2026-09-20T14:48:04.209492Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T15:10:59.817235Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:58.817102Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:57.543394Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:56.543319Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:55.543183Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:54.543050Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:53.542928Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:52.542796Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:51.542668Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:50.542546Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:49.542434Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:48.542306Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:47.542196Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:46.542081Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:10:45.541969Z` — **MID**: 0 rows; marker `2026-09-20T15:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
