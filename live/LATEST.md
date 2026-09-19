# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T20:02:14.762018Z`  
Current process started UTC: `2026-09-19T19:58:13.884339Z`  
1-second metadata polls in this process: **203**  
HTTP/data errors in this process: **1**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=100, delta=4, z=5.22 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=378, delta=4, z=13.61 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=105, delta=5, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=251, delta=-152, z=6.63 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=100, delta=1, z=4.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=11.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=11.75 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=12.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=13.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=14.15 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=96, delta=93, z=5.31 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=NPSHYD|generation` = **499** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=OCGT|generation` = **105** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=OTHER|generation` = **400** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=PS|generation` = **825** (n=1354, 2026-09-19T20:00:39.859424Z)
- `FUELINST|fuelType=WIND|generation` = **13880** (n=1354, 2026-09-19T20:00:39.859424Z)
- `IMBALNGC|TOTAL|imbalance` = **-3790** (n=223, 2026-09-19T19:52:47.570321Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=223, 2026-09-19T19:52:31.555589Z)
- `INDGEN|TOTAL|generation` = **16162** (n=223, 2026-09-19T19:52:47.570321Z)
- `MELNGC|TOTAL|margin` = **36216** (n=223, 2026-09-19T19:50:05.899376Z)
- `NDF|TOTAL|demand` = **19452** (n=228, 2026-09-19T19:48:04.844285Z)
- `TSDF|TOTAL|demand` = **19952** (n=228, 2026-09-19T19:48:04.844285Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T20:02:13.798549Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:12.234216Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:11.234117Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:10.234054Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:09.233955Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:08.233891Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:07.233827Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:06.233759Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:05.195257Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:04.195188Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:03.195125Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:02.195058Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:01.194962Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:02:00.194886Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T20:01:59.194824Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
