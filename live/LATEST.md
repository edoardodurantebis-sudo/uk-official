# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:58:00.388794Z`  
Current process started UTC: `2026-09-20T05:54:00.188537Z`  
1-second metadata polls in this process: **201**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.01 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=2, z=-4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-4.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-4.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.25 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.46 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=OTHER|generation` = **540** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=PS|generation` = **-815** (n=1473, 2026-09-20T05:55:19.878248Z)
- `FUELINST|fuelType=WIND|generation` = **15647** (n=1473, 2026-09-20T05:55:19.878248Z)
- `IMBALNGC|TOTAL|imbalance` = **-6774** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDDEM|TOTAL|demand` = **-12309** (n=243, 2026-09-20T05:50:21.783913Z)
- `INDGEN|TOTAL|generation` = **13178** (n=243, 2026-09-20T05:50:21.783913Z)
- `MELNGC|TOTAL|margin` = **37465** (n=243, 2026-09-20T05:49:29.338975Z)
- `NDF|TOTAL|demand` = **19452** (n=248, 2026-09-20T05:47:19.313557Z)
- `TSDF|TOTAL|demand` = **19952** (n=248, 2026-09-20T05:47:19.313557Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T05:57:58.908013Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:57.768897Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:56.638136Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:55.477580Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:54.333833Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:53.203547Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:52.027520Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:50.861198Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:49.672309Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:48.546498Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:47.401855Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:46.259461Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:45.132276Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:43.992380Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:57:42.533355Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
