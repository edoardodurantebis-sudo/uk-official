# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:24:55.306403Z`  
Current process started UTC: `2026-09-20T04:20:55.221612Z`  
1-second metadata polls in this process: **175**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.64 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.87 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.95 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.00 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=OTHER|generation` = **213** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=PS|generation` = **-700** (n=1454, 2026-09-20T04:20:29.187132Z)
- `FUELINST|fuelType=WIND|generation` = **15182** (n=1454, 2026-09-20T04:20:29.187132Z)
- `IMBALNGC|TOTAL|imbalance` = **-6763** (n=240, 2026-09-20T04:20:55.221625Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=240, 2026-09-20T04:20:29.187132Z)
- `INDGEN|TOTAL|generation` = **13189** (n=240, 2026-09-20T04:20:29.187132Z)
- `MELNGC|TOTAL|margin` = **37513** (n=240, 2026-09-20T04:19:08.049420Z)
- `NDF|TOTAL|demand` = **19452** (n=245, 2026-09-20T04:17:31.726312Z)
- `TSDF|TOTAL|demand` = **19952** (n=245, 2026-09-20T04:17:31.726312Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:24:53.992635Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:52.684578Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:51.341512Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:50.016805Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:48.733616Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:47.413280Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:46.118625Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:44.800584Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:43.490352Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:42.171421Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:40.597544Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:39.307778Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:37.994545Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:36.660280Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:24:35.263210Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
