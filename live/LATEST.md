# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:49:23.244607Z`  
Current process started UTC: `2026-09-19T15:45:22.668460Z`  
1-second metadata polls in this process: **196**  
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

- `FUELINST|fuelType=INTVKL|generation` = **702** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=OTHER|generation` = **1609** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=PS|generation` = **156** (n=1303, 2026-09-19T15:45:22.668469Z)
- `FUELINST|fuelType=WIND|generation` = **14300** (n=1303, 2026-09-19T15:45:22.668469Z)
- `IMBALNGC|TOTAL|imbalance` = **-3172** (n=214, 2026-09-19T15:25:41.581336Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=214, 2026-09-19T15:25:25.854929Z)
- `INDGEN|TOTAL|generation` = **16780** (n=214, 2026-09-19T15:25:25.854929Z)
- `MELNGC|TOTAL|margin` = **37039** (n=214, 2026-09-19T15:22:01.787811Z)
- `NDF|TOTAL|demand` = **19452** (n=220, 2026-09-19T15:48:36.959931Z)
- `TSDF|TOTAL|demand` = **19952** (n=220, 2026-09-19T15:48:36.959931Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:49:22.284537Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:21.284417Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:20.284337Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:19.284251Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:18.284139Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:17.284003Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:16.141627Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:15.141558Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:14.141468Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:13.141350Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:12.141232Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:11.141106Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:09.383549Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:08.185519Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:49:06.686669Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
