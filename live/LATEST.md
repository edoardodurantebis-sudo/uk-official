# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:08:49.478304Z`  
Current process started UTC: `2026-09-19T18:04:49.182526Z`  
1-second metadata polls in this process: **226**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=NPSHYD|generation` = **457** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=OTHER|generation` = **1227** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1331, 2026-09-19T18:05:25.010072Z)
- `FUELINST|fuelType=WIND|generation` = **14254** (n=1331, 2026-09-19T18:05:25.010072Z)
- `IMBALNGC|TOTAL|imbalance` = **-3139** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=219, 2026-09-19T17:53:18.380714Z)
- `INDGEN|TOTAL|generation` = **16813** (n=219, 2026-09-19T17:53:18.380714Z)
- `MELNGC|TOTAL|margin` = **36302** (n=219, 2026-09-19T17:51:00.750598Z)
- `NDF|TOTAL|demand` = **19452** (n=224, 2026-09-19T17:48:18.539367Z)
- `TSDF|TOTAL|demand` = **19952** (n=224, 2026-09-19T17:48:18.539367Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:08:48.523972Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:47.523905Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:46.523743Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:45.523610Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:44.523493Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:43.523396Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:41.824173Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:40.824089Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:39.818106Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:38.774108Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:37.746980Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:36.746845Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:35.746776Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:34.746712Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:08:33.746620Z` — **MID**: 0 rows; marker `2026-09-19T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
