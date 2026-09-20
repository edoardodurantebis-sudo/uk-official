# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T03:50:56.702916Z`  
Current process started UTC: `2026-09-20T03:46:55.458965Z`  
1-second metadata polls in this process: **144**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-5.29 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **161** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=OTHER|generation` = **435** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1448, 2026-09-20T03:50:27.802163Z)
- `FUELINST|fuelType=WIND|generation` = **15059** (n=1448, 2026-09-20T03:50:27.802163Z)
- `IMBALNGC|TOTAL|imbalance` = **-6527** (n=239, 2026-09-20T03:50:44.576264Z)
- `INDDEM|TOTAL|demand` = **-12293** (n=239, 2026-09-20T03:50:27.802163Z)
- `INDGEN|TOTAL|generation` = **13425** (n=239, 2026-09-20T03:50:27.802163Z)
- `MELNGC|TOTAL|margin` = **37544** (n=239, 2026-09-20T03:49:22.537799Z)
- `NDF|TOTAL|demand` = **19452** (n=244, 2026-09-20T03:47:45.149657Z)
- `TSDF|TOTAL|demand` = **19952** (n=244, 2026-09-20T03:47:28.204703Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T03:50:55.171521Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:53.626008Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:52.099449Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:50.562765Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:49.019619Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:47.474349Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:44.576264Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:44.576264Z` — **IMBALNGC**: 864 rows; marker `2026-09-20T03:47:00Z`
- `2026-09-20T03:50:43.038323Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:41.502835Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:39.965146Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:38.425817Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:36.884053Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:35.331208Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T03:50:33.764135Z` — **MID**: 0 rows; marker `2026-09-20T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
