# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T07:18:20.744291Z`  
Current process started UTC: `2026-09-20T07:14:19.416305Z`  
1-second metadata polls in this process: **216**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1262** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=NPSHYD|generation` = **350** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=OTHER|generation` = **417** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=PS|generation` = **-807** (n=1489, 2026-09-20T07:15:37.176402Z)
- `FUELINST|fuelType=WIND|generation` = **15728** (n=1489, 2026-09-20T07:15:37.176402Z)
- `IMBALNGC|TOTAL|imbalance` = **-6802** (n=245, 2026-09-20T06:51:13.366134Z)
- `INDDEM|TOTAL|demand` = **-12302** (n=245, 2026-09-20T06:50:57.374716Z)
- `INDGEN|TOTAL|generation` = **13150** (n=245, 2026-09-20T06:50:57.374716Z)
- `MELNGC|TOTAL|margin` = **37681** (n=245, 2026-09-20T06:49:53.401212Z)
- `NDF|TOTAL|demand` = **19452** (n=251, 2026-09-20T07:17:28.599471Z)
- `TSDF|TOTAL|demand` = **19952** (n=251, 2026-09-20T07:17:28.599471Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T07:18:19.382364Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:17.942722Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:16.938620Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:15.626114Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:14.600828Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:13.566440Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:12.555866Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:11.543035Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:10.181351Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:09.149431Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:08.114518Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:07.103252Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:05.700542Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:04.588066Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:18:03.552866Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
