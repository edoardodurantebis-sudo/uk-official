# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:28:38.850824Z`  
Current process started UTC: `2026-09-20T05:24:38.538523Z`  
1-second metadata polls in this process: **198**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.25 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.46 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.43 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-4.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=3, z=-4.49 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=NPSHYD|generation` = **297** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=OTHER|generation` = **405** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=PS|generation` = **-692** (n=1467, 2026-09-20T05:25:25.945241Z)
- `FUELINST|fuelType=WIND|generation` = **15561** (n=1467, 2026-09-20T05:25:25.945241Z)
- `IMBALNGC|TOTAL|imbalance` = **-6811** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDDEM|TOTAL|demand` = **-12319** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDGEN|TOTAL|generation` = **13141** (n=242, 2026-09-20T05:20:37.923780Z)
- `MELNGC|TOTAL|margin` = **37520** (n=242, 2026-09-20T05:19:07.535945Z)
- `NDF|TOTAL|demand` = **19452** (n=247, 2026-09-20T05:17:31.650511Z)
- `TSDF|TOTAL|demand` = **19952** (n=247, 2026-09-20T05:17:31.650511Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T05:28:37.680416Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:36.543951Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:35.366808Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:33.946522Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:32.784207Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:31.622805Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:30.432785Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:29.289152Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:28.163370Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:27.008974Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:25.805238Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:24.662056Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:23.499512Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:22.351481Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:28:21.154597Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
