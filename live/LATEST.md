# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T07:09:55.696598Z`  
Current process started UTC: `2026-09-20T07:05:55.403038Z`  
1-second metadata polls in this process: **146**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1256** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=NPSHYD|generation` = **350** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=OTHER|generation` = **552** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=PS|generation` = **-799** (n=1487, 2026-09-20T07:05:33.320387Z)
- `FUELINST|fuelType=WIND|generation` = **15657** (n=1487, 2026-09-20T07:05:33.320387Z)
- `IMBALNGC|TOTAL|imbalance` = **-6802** (n=245, 2026-09-20T06:51:13.366134Z)
- `INDDEM|TOTAL|demand` = **-12302** (n=245, 2026-09-20T06:50:57.374716Z)
- `INDGEN|TOTAL|generation` = **13150** (n=245, 2026-09-20T06:50:57.374716Z)
- `MELNGC|TOTAL|margin` = **37681** (n=245, 2026-09-20T06:49:53.401212Z)
- `NDF|TOTAL|demand` = **19452** (n=250, 2026-09-20T06:47:34.462781Z)
- `TSDF|TOTAL|demand` = **19952** (n=250, 2026-09-20T06:47:34.462781Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T07:09:54.101550Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:52.547434Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:51.012933Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:49.464443Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:47.855249Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:46.304322Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:44.698531Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:42.915648Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:41.327518Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:39.679874Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:38.075276Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:36.516087Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:34.971499Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:33.426715Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:09:31.779304Z` — **MID**: 0 rows; marker `2026-09-20T07:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
