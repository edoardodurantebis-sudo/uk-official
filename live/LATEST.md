# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:07:32.440773Z`  
Current process started UTC: `2026-09-19T19:03:31.983444Z`  
1-second metadata polls in this process: **206**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=63, z=4.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=229, delta=229, z=17.80 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=NPSHYD|generation` = **508** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=OCGT|generation` = **83** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=OTHER|generation` = **912** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1343, 2026-09-19T19:05:26.290481Z)
- `FUELINST|fuelType=WIND|generation` = **14065** (n=1343, 2026-09-19T19:05:26.290481Z)
- `IMBALNGC|TOTAL|imbalance` = **-3742** (n=221, 2026-09-19T18:54:47.042884Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=221, 2026-09-19T18:54:31.530560Z)
- `INDGEN|TOTAL|generation` = **16210** (n=221, 2026-09-19T18:54:31.530560Z)
- `MELNGC|TOTAL|margin` = **36202** (n=221, 2026-09-19T18:51:13.295596Z)
- `NDF|TOTAL|demand` = **19452** (n=226, 2026-09-19T18:48:41.702714Z)
- `TSDF|TOTAL|demand` = **19952** (n=226, 2026-09-19T18:48:41.702714Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T19:07:31.373013Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:30.372940Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:29.355964Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:28.354080Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:27.321189Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:26.291643Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:25.249740Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:24.241515Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:23.210674Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:22.186266Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:21.146281Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:20.100788Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:18.585939Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:17.574309Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:07:16.557639Z` — **MID**: 0 rows; marker `2026-09-19T19:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
