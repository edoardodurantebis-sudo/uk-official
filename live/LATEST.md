# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T23:02:57.020860Z`  
Current process started UTC: `2026-09-19T22:58:55.634709Z`  
1-second metadata polls in this process: **128**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-686, delta=-60, z=-12.25 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-694, delta=-9, z=-9.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-1, z=-10.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=0, z=-10.86 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-684, delta=1, z=-11.36 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-11.96 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-626, delta=-522, z=-16.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-12.63 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-13.44 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=0, z=-14.42 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-685, delta=-10, z=-15.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-675, delta=-337, z=-16.96 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-338, delta=-235, z=-8.76 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=94, delta=-6, z=4.60 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1171** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=NPSHYD|generation` = **360** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=OTHER|generation` = **705** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=PS|generation` = **-134** (n=1390, 2026-09-19T23:00:31.097059Z)
- `FUELINST|fuelType=WIND|generation` = **15571** (n=1390, 2026-09-19T23:00:31.097059Z)
- `IMBALNGC|TOTAL|imbalance` = **-3939** (n=229, 2026-09-19T22:51:53.188955Z)
- `INDDEM|TOTAL|demand` = **-11888** (n=229, 2026-09-19T22:51:36.708891Z)
- `INDGEN|TOTAL|generation` = **16013** (n=229, 2026-09-19T22:51:36.708891Z)
- `MELNGC|TOTAL|margin` = **36059** (n=229, 2026-09-19T22:49:52.818755Z)
- `NDF|TOTAL|demand` = **19452** (n=234, 2026-09-19T22:47:40.553583Z)
- `TSDF|TOTAL|demand` = **19952** (n=234, 2026-09-19T22:47:40.553583Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T23:02:55.299833Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:53.466663Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:51.718804Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:49.871055Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:48.079347Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:46.325751Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:44.046753Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:42.304817Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:40.406847Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:38.614914Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:36.874003Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:35.142875Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:33.396424Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:31.546534Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T23:02:26.760995Z` — **MID**: 0 rows; marker `2026-09-19T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
