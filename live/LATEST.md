# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T15:02:37.178121Z`  
Current process started UTC: `2026-09-20T14:58:36.056000Z`  
1-second metadata polls in this process: **177**  
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

- `FUELINST|fuelType=INTVKL|generation` = **584** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=NPSHYD|generation` = **282** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=OTHER|generation` = **1113** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=PS|generation` = **-253** (n=1582, 2026-09-20T15:00:31.041175Z)
- `FUELINST|fuelType=WIND|generation` = **8563** (n=1582, 2026-09-20T15:00:31.041175Z)
- `IMBALNGC|TOTAL|imbalance` = **-5158** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=260, 2026-09-20T14:53:20.202311Z)
- `INDGEN|TOTAL|generation` = **15452** (n=260, 2026-09-20T14:53:20.202311Z)
- `MELNGC|TOTAL|margin` = **35910** (n=260, 2026-09-20T14:50:25.474421Z)
- `NDF|TOTAL|demand` = **20110** (n=266, 2026-09-20T14:48:04.209492Z)
- `TSDF|TOTAL|demand` = **20610** (n=266, 2026-09-20T14:48:04.209492Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T15:02:35.832019Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:34.493775Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:33.219540Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:31.953644Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:30.640710Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:29.316520Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:28.092832Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:26.792445Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:23.860714Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:23.860714Z` — **FREQ**: 5761 rows; marker `2026-09-20T15:01:45Z`
- `2026-09-20T15:02:22.581187Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:21.273899Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:19.998065Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:18.715927Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T15:02:17.460070Z` — **MID**: 0 rows; marker `2026-09-20T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
