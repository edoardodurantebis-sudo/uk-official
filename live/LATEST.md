# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:41:17.939506Z`  
Current process started UTC: `2026-09-20T05:37:17.212174Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.40 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=OTHER|generation` = **532** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=PS|generation` = **-807** (n=1470, 2026-09-20T05:40:33.881024Z)
- `FUELINST|fuelType=WIND|generation` = **15459** (n=1470, 2026-09-20T05:40:33.881024Z)
- `IMBALNGC|TOTAL|imbalance` = **-6811** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDDEM|TOTAL|demand` = **-12319** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDGEN|TOTAL|generation` = **13141** (n=242, 2026-09-20T05:20:37.923780Z)
- `MELNGC|TOTAL|margin` = **37520** (n=242, 2026-09-20T05:19:07.535945Z)
- `NDF|TOTAL|demand` = **19452** (n=247, 2026-09-20T05:17:31.650511Z)
- `TSDF|TOTAL|demand` = **19952** (n=247, 2026-09-20T05:17:31.650511Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T05:41:16.976910Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:15.976793Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:14.976763Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:13.976674Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:12.976558Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:11.976423Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:10.968766Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:09.968639Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:08.968513Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:07.968388Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:06.968257Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:05.760161Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:04.760024Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:03.759910Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:41:02.759794Z` — **MID**: 0 rows; marker `2026-09-20T05:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
