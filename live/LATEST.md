# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:42:30.349628Z`  
Current process started UTC: `2026-09-20T03:38:29.212897Z`  
1-second metadata polls in this process: **199**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.87 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.95 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.14 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.50 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.19 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.24 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-5.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-5.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=OTHER|generation` = **507** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1446, 2026-09-20T03:40:34.881036Z)
- `FUELINST|fuelType=WIND|generation` = **15069** (n=1446, 2026-09-20T03:40:34.881036Z)
- `IMBALNGC|TOTAL|imbalance` = **-3815** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDDEM|TOTAL|demand` = **-12287** (n=238, 2026-09-20T03:20:58.508066Z)
- `INDGEN|TOTAL|generation` = **16137** (n=238, 2026-09-20T03:20:58.508066Z)
- `MELNGC|TOTAL|margin` = **37545** (n=238, 2026-09-20T03:19:19.206204Z)
- `NDF|TOTAL|demand` = **19452** (n=243, 2026-09-20T03:17:24.742276Z)
- `TSDF|TOTAL|demand` = **19952** (n=243, 2026-09-20T03:17:24.742276Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T03:42:29.206836Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:26.247794Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:25.082378Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:23.917816Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:22.748442Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:21.609193Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:20.469448Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:19.324408Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:18.173709Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:16.994179Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:15.844059Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:14.695910Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:13.571693Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:12.408592Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:42:09.908533Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
