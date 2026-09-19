# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T16:14:32.852664Z`  
Current process started UTC: `2026-09-19T16:10:31.849096Z`  
1-second metadata polls in this process: **153**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=NPSHYD|generation` = **350** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=OTHER|generation` = **816** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=PS|generation` = **439** (n=1308, 2026-09-19T16:10:31.849107Z)
- `FUELINST|fuelType=WIND|generation` = **14625** (n=1308, 2026-09-19T16:10:31.849107Z)
- `IMBALNGC|TOTAL|imbalance` = **-3173** (n=215, 2026-09-19T15:55:57.730913Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=215, 2026-09-19T15:55:23.733569Z)
- `INDGEN|TOTAL|generation` = **16779** (n=215, 2026-09-19T15:55:23.733569Z)
- `MELNGC|TOTAL|margin` = **37049** (n=215, 2026-09-19T15:51:29.825057Z)
- `NDF|TOTAL|demand` = **19452** (n=220, 2026-09-19T15:48:36.959931Z)
- `TSDF|TOTAL|demand` = **19952** (n=220, 2026-09-19T15:48:36.959931Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T16:14:31.360283Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:28.977798Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:27.286198Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:25.821898Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:24.347797Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:21.724260Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:20.207182Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:18.709594Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:17.274869Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:15.816373Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:14.123333Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:12.513373Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:11.059288Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:09.467553Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:14:05.627715Z` — **MID**: 0 rows; marker `2026-09-19T16:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
