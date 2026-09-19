# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T15:32:33.295036Z`  
Current process started UTC: `2026-09-19T15:28:32.961683Z`  
1-second metadata polls in this process: **137**  
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

- `FUELINST|fuelType=INTVKL|generation` = **702** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=OTHER|generation` = **1152** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=PS|generation` = **-190** (n=1300, 2026-09-19T15:30:28.502617Z)
- `FUELINST|fuelType=WIND|generation` = **14186** (n=1300, 2026-09-19T15:30:28.502617Z)
- `IMBALNGC|TOTAL|imbalance` = **-3172** (n=214, 2026-09-19T15:25:41.581336Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=214, 2026-09-19T15:25:25.854929Z)
- `INDGEN|TOTAL|generation` = **16780** (n=214, 2026-09-19T15:25:25.854929Z)
- `MELNGC|TOTAL|margin` = **37039** (n=214, 2026-09-19T15:22:01.787811Z)
- `NDF|TOTAL|demand` = **19452** (n=219, 2026-09-19T15:19:13.284533Z)
- `TSDF|TOTAL|demand` = **19952** (n=219, 2026-09-19T15:19:13.284533Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T15:32:30.843494Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:28.956593Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:27.355477Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:24.909223Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:23.029415Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:21.401656Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:19.609146Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:17.886294Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:16.296934Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:14.720785Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:13.135835Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:11.514612Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:07.758210Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T15:32:07.758210Z` — **FREQ**: 5761 rows; marker `2026-09-19T15:31:45Z`
- `2026-09-19T15:32:05.961905Z` — **MID**: 0 rows; marker `2026-09-19T15:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
