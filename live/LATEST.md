# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:59:21.754607Z`  
Current process started UTC: `2026-09-20T03:55:21.739899Z`  
1-second metadata polls in this process: **135**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.78 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=NPSHYD|generation` = **300** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=OTHER|generation` = **438** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=PS|generation` = **-693** (n=1449, 2026-09-20T03:55:37.423781Z)
- `FUELINST|fuelType=WIND|generation` = **15133** (n=1449, 2026-09-20T03:55:37.423781Z)
- `IMBALNGC|TOTAL|imbalance` = **-6527** (n=239, 2026-09-20T03:50:44.576264Z)
- `INDDEM|TOTAL|demand` = **-12293** (n=239, 2026-09-20T03:50:27.802163Z)
- `INDGEN|TOTAL|generation` = **13425** (n=239, 2026-09-20T03:50:27.802163Z)
- `MELNGC|TOTAL|margin` = **37544** (n=239, 2026-09-20T03:49:22.537799Z)
- `NDF|TOTAL|demand` = **19452** (n=244, 2026-09-20T03:47:45.149657Z)
- `TSDF|TOTAL|demand` = **19952** (n=244, 2026-09-20T03:47:28.204703Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T03:59:20.047560Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:17.941140Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:16.228323Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:14.487816Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:12.769527Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:11.068567Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:09.354242Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:07.614017Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:05.903857Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:04.201614Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:02.125873Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:59:00.429166Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:58:58.709686Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:58:57.005990Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:58:55.300236Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
