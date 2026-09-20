# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T01:51:29.200056Z`  
Current process started UTC: `2026-09-20T01:47:29.078758Z`  
1-second metadata polls in this process: **128**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-6.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-6.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.34 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-7.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-6.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-6.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=1, z=-6.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=3, z=-6.97 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-7.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-7.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-7.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-7.37 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **651** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=NPSHYD|generation` = **322** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=OTHER|generation` = **179** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=PS|generation` = **-819** (n=1424, 2026-09-20T01:50:28.103947Z)
- `FUELINST|fuelType=WIND|generation` = **15361** (n=1424, 2026-09-20T01:50:28.103947Z)
- `IMBALNGC|TOTAL|imbalance` = **-3757** (n=235, 2026-09-20T01:51:00.792913Z)
- `INDDEM|TOTAL|demand` = **-12197** (n=235, 2026-09-20T01:51:00.792913Z)
- `INDGEN|TOTAL|generation` = **16195** (n=235, 2026-09-20T01:51:00.792913Z)
- `MELNGC|TOTAL|margin` = **36018** (n=235, 2026-09-20T01:49:39.512104Z)
- `NDF|TOTAL|demand` = **19452** (n=240, 2026-09-20T01:47:46.889825Z)
- `TSDF|TOTAL|demand` = **19952** (n=240, 2026-09-20T01:47:46.889825Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T01:51:27.503687Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:25.801245Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:24.087878Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:22.380555Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:20.694687Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:18.971458Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:16.655928Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:14.951046Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:13.230383Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:11.536329Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:09.843572Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:08.144569Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:06.352594Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:00.792913Z` — **MID**: 0 rows; marker `2026-09-20T01:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T01:51:00.792913Z` — **INDGEN**: 936 rows; marker `2026-09-20T01:47:00Z`
