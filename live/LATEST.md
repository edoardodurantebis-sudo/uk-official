# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:03:34.180380Z`  
Current process started UTC: `2026-09-20T03:59:33.946290Z`  
1-second metadata polls in this process: **172**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.09 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.14 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.50 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **151** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=NPSHYD|generation` = **300** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=OTHER|generation` = **517** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=PS|generation` = **-690** (n=1450, 2026-09-20T04:00:38.239272Z)
- `FUELINST|fuelType=WIND|generation` = **15183** (n=1450, 2026-09-20T04:00:38.239272Z)
- `IMBALNGC|TOTAL|imbalance` = **-6527** (n=239, 2026-09-20T03:50:44.576264Z)
- `INDDEM|TOTAL|demand` = **-12293** (n=239, 2026-09-20T03:50:27.802163Z)
- `INDGEN|TOTAL|generation` = **13425** (n=239, 2026-09-20T03:50:27.802163Z)
- `MELNGC|TOTAL|margin` = **37544** (n=239, 2026-09-20T03:49:22.537799Z)
- `NDF|TOTAL|demand` = **19452** (n=244, 2026-09-20T03:47:45.149657Z)
- `TSDF|TOTAL|demand` = **19952** (n=244, 2026-09-20T03:47:28.204703Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:03:32.859987Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:31.003235Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:29.722211Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:28.031777Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:26.731677Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:25.279936Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:23.964882Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:22.451979Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:21.089906Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:19.809684Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:18.215602Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:16.886169Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:15.593771Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:14.322982Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:03:12.796672Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
