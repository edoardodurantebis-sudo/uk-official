# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T04:33:18.596173Z`  
Current process started UTC: `2026-09-20T04:29:17.766320Z`  
1-second metadata polls in this process: **136**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-2, z=-4.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1012, delta=3, z=-4.49 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.54 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.56 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.64 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-4.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.87 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.18 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **121** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=NPSHYD|generation` = **299** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=OTHER|generation` = **165** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=PS|generation` = **-697** (n=1456, 2026-09-20T04:30:28.367302Z)
- `FUELINST|fuelType=WIND|generation` = **15354** (n=1456, 2026-09-20T04:30:28.367302Z)
- `IMBALNGC|TOTAL|imbalance` = **-6763** (n=240, 2026-09-20T04:20:55.221625Z)
- `INDDEM|TOTAL|demand` = **-12315** (n=240, 2026-09-20T04:20:29.187132Z)
- `INDGEN|TOTAL|generation` = **13189** (n=240, 2026-09-20T04:20:29.187132Z)
- `MELNGC|TOTAL|margin` = **37513** (n=240, 2026-09-20T04:19:08.049420Z)
- `NDF|TOTAL|demand` = **19452** (n=245, 2026-09-20T04:17:31.726312Z)
- `TSDF|TOTAL|demand` = **19952** (n=245, 2026-09-20T04:17:31.726312Z)
- `WINDFOR|TOTAL|generation` = **2815** (n=41, 2026-09-20T03:30:37.063198Z)

## Latest publication events

- `2026-09-20T04:33:16.947780Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:15.129473Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:12.200566Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:10.574110Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:08.582978Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:06.815186Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:05.169681Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:03.522610Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:33:01.671182Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:32:59.749850Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:32:58.130748Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:32:55.793449Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:32:54.001140Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:32:52.280493Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T04:32:50.664126Z` — **MID**: 0 rows; marker `2026-09-20T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
