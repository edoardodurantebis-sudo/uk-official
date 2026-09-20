# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:24:07.256775Z`  
Current process started UTC: `2026-09-20T05:20:05.999459Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.54 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=NPSHYD|generation` = **297** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=OTHER|generation` = **363** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=PS|generation` = **-696** (n=1466, 2026-09-20T05:20:22.488863Z)
- `FUELINST|fuelType=WIND|generation` = **15493** (n=1466, 2026-09-20T05:20:22.488863Z)
- `IMBALNGC|TOTAL|imbalance` = **-6811** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDDEM|TOTAL|demand` = **-12319** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDGEN|TOTAL|generation` = **13141** (n=242, 2026-09-20T05:20:37.923780Z)
- `MELNGC|TOTAL|margin` = **37520** (n=242, 2026-09-20T05:19:07.535945Z)
- `NDF|TOTAL|demand` = **19452** (n=247, 2026-09-20T05:17:31.650511Z)
- `TSDF|TOTAL|demand` = **19952** (n=247, 2026-09-20T05:17:31.650511Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T05:24:05.664659Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:24:04.023157Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:24:02.268634Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:24:00.664242Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:59.045722Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:57.083043Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:55.478259Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:53.863614Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:52.140182Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:50.471388Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:48.898842Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:47.279337Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:45.638218Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:43.941831Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:23:42.331583Z` — **MID**: 0 rows; marker `2026-09-20T05:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
