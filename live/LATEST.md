# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:50:36.904324Z`  
Current process started UTC: `2026-09-20T04:46:36.524823Z`  
1-second metadata polls in this process: **224**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.43 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-4.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=3, z=-4.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.64 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.75 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=OTHER|generation` = **133** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=PS|generation` = **-701** (n=1460, 2026-09-20T04:50:32.525251Z)
- `FUELINST|fuelType=WIND|generation` = **15347** (n=1460, 2026-09-20T04:50:32.525251Z)
- `IMBALNGC|TOTAL|imbalance` = **-6777** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDDEM|TOTAL|demand` = **-12177** (n=241, 2026-09-20T04:50:32.525251Z)
- `INDGEN|TOTAL|generation` = **13175** (n=241, 2026-09-20T04:50:32.525251Z)
- `MELNGC|TOTAL|margin` = **37516** (n=241, 2026-09-20T04:49:13.726695Z)
- `NDF|TOTAL|demand` = **19452** (n=246, 2026-09-20T04:47:23.759382Z)
- `TSDF|TOTAL|demand` = **19952** (n=246, 2026-09-20T04:47:23.759382Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:50:35.925008Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:32.525251Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:32.525251Z` — **INDGEN**: 828 rows; marker `2026-09-20T04:46:00Z`
- `2026-09-20T04:50:32.525251Z` — **INDDEM**: 828 rows; marker `2026-09-20T04:47:00Z`
- `2026-09-20T04:50:32.525251Z` — **IMBALNGC**: 828 rows; marker `2026-09-20T04:47:00Z`
- `2026-09-20T04:50:32.525251Z` — **FUELINST**: 80 rows; marker `2026-09-20T04:50:00Z`
- `2026-09-20T04:50:31.525143Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:30.525025Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:29.524952Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:28.524871Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:27.524752Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:26.524629Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:25.524502Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:24.524390Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:50:23.524270Z` — **MID**: 0 rows; marker `2026-09-20T04:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
