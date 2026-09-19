# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:41:00.061240Z`  
Current process started UTC: `2026-09-19T15:36:59.884579Z`  
1-second metadata polls in this process: **157**  
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

- `FUELINST|fuelType=INTVKL|generation` = **702** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=OTHER|generation` = **1293** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=PS|generation` = **127** (n=1302, 2026-09-19T15:40:34.264278Z)
- `FUELINST|fuelType=WIND|generation` = **14270** (n=1302, 2026-09-19T15:40:34.264278Z)
- `IMBALNGC|TOTAL|imbalance` = **-3172** (n=214, 2026-09-19T15:25:41.581336Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=214, 2026-09-19T15:25:25.854929Z)
- `INDGEN|TOTAL|generation` = **16780** (n=214, 2026-09-19T15:25:25.854929Z)
- `MELNGC|TOTAL|margin` = **37039** (n=214, 2026-09-19T15:22:01.787811Z)
- `NDF|TOTAL|demand` = **19452** (n=219, 2026-09-19T15:19:13.284533Z)
- `TSDF|TOTAL|demand` = **19952** (n=219, 2026-09-19T15:19:13.284533Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:40:58.669971Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:57.178588Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:55.769092Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:54.343170Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:52.875387Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:49.683083Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:48.237583Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:46.818027Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:45.390057Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:43.950395Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:42.524982Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:41.051177Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:39.615186Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:38.193308Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:40:36.692113Z` — **MID**: 0 rows; marker `2026-09-19T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
