# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T18:54:57.173801Z`  
Current process started UTC: `2026-09-19T18:50:56.783282Z`  
1-second metadata polls in this process: **155**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=NPSHYD|generation` = **501** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=OTHER|generation` = **833** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1340, 2026-09-19T18:50:36.086416Z)
- `FUELINST|fuelType=WIND|generation` = **14165** (n=1340, 2026-09-19T18:50:36.086416Z)
- `IMBALNGC|TOTAL|imbalance` = **-3742** (n=221, 2026-09-19T18:54:47.042884Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=221, 2026-09-19T18:54:31.530560Z)
- `INDGEN|TOTAL|generation` = **16210** (n=221, 2026-09-19T18:54:31.530560Z)
- `MELNGC|TOTAL|margin` = **36202** (n=221, 2026-09-19T18:51:13.295596Z)
- `NDF|TOTAL|demand` = **19452** (n=226, 2026-09-19T18:48:41.702714Z)
- `TSDF|TOTAL|demand` = **19952** (n=226, 2026-09-19T18:48:41.702714Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T18:54:55.703222Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:54.280651Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:52.837168Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:51.343363Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:49.930333Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:47.042884Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:47.042884Z` — **IMBALNGC**: 1188 rows; marker `2026-09-19T18:48:00Z`
- `2026-09-19T18:54:45.566845Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:44.062994Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:42.630398Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:41.177243Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:39.737583Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:38.280778Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:36.823342Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T18:54:35.386328Z` — **MID**: 0 rows; marker `2026-09-19T18:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
