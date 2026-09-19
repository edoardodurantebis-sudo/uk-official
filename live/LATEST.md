# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T16:06:10.097034Z`  
Current process started UTC: `2026-09-19T16:02:10.084428Z`  
1-second metadata polls in this process: **167**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1239** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=NPSHYD|generation` = **346** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=OTHER|generation` = **989** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=PS|generation` = **438** (n=1307, 2026-09-19T16:05:32.341322Z)
- `FUELINST|fuelType=WIND|generation` = **14381** (n=1307, 2026-09-19T16:05:32.341322Z)
- `IMBALNGC|TOTAL|imbalance` = **-3173** (n=215, 2026-09-19T15:55:57.730913Z)
- `INDDEM|TOTAL|demand` = **-11874** (n=215, 2026-09-19T15:55:23.733569Z)
- `INDGEN|TOTAL|generation` = **16779** (n=215, 2026-09-19T15:55:23.733569Z)
- `MELNGC|TOTAL|margin` = **37049** (n=215, 2026-09-19T15:51:29.825057Z)
- `NDF|TOTAL|demand` = **19452** (n=220, 2026-09-19T15:48:36.959931Z)
- `TSDF|TOTAL|demand` = **19952** (n=220, 2026-09-19T15:48:36.959931Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T16:06:08.755181Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:06:07.457762Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:06:06.138055Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:06:04.463857Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:06:03.159390Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:06:01.794126Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:06:00.414660Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:59.025867Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:57.740305Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:56.395202Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:54.991928Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:53.667244Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:52.355539Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:51.053647Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T16:05:49.699177Z` — **MID**: 0 rows; marker `2026-09-19T15:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
