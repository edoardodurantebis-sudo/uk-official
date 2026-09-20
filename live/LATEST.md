# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:11:59.931591Z`  
Current process started UTC: `2026-09-20T04:07:58.920101Z`  
1-second metadata polls in this process: **150**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.04 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.09 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=NPSHYD|generation` = **298** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=OTHER|generation` = **302** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=PS|generation` = **-421** (n=1452, 2026-09-20T04:10:36.849815Z)
- `FUELINST|fuelType=WIND|generation` = **15031** (n=1452, 2026-09-20T04:10:36.849815Z)
- `IMBALNGC|TOTAL|imbalance` = **-6527** (n=239, 2026-09-20T03:50:44.576264Z)
- `INDDEM|TOTAL|demand` = **-12293** (n=239, 2026-09-20T03:50:27.802163Z)
- `INDGEN|TOTAL|generation` = **13425** (n=239, 2026-09-20T03:50:27.802163Z)
- `MELNGC|TOTAL|margin` = **37544** (n=239, 2026-09-20T03:49:22.537799Z)
- `NDF|TOTAL|demand` = **19452** (n=244, 2026-09-20T03:47:45.149657Z)
- `TSDF|TOTAL|demand` = **19952** (n=244, 2026-09-20T03:47:28.204703Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:11:58.360719Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:56.577133Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:55.048935Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:53.502001Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:51.948756Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:50.400662Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:48.826159Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:47.298388Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:45.742537Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:44.208236Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:42.657308Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:40.522325Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:38.960820Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:37.420528Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:11:35.873940Z` — **MID**: 0 rows; marker `2026-09-20T04:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
