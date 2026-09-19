# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:53:50.205934Z`  
Current process started UTC: `2026-09-19T19:49:49.221922Z`  
1-second metadata polls in this process: **170**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=11.75 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=12.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=13.19 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=4.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=14.15 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=96, delta=93, z=5.31 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=374, delta=374, z=30.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.02 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=0, z=15.34 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=16.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=NPSHYD|generation` = **514** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=OTHER|generation` = **363** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1352, 2026-09-19T19:50:38.058596Z)
- `FUELINST|fuelType=WIND|generation` = **13724** (n=1352, 2026-09-19T19:50:38.058596Z)
- `IMBALNGC|TOTAL|imbalance` = **-3790** (n=223, 2026-09-19T19:52:47.570321Z)
- `INDDEM|TOTAL|demand` = **-11873** (n=223, 2026-09-19T19:52:31.555589Z)
- `INDGEN|TOTAL|generation` = **16162** (n=223, 2026-09-19T19:52:47.570321Z)
- `MELNGC|TOTAL|margin` = **36216** (n=223, 2026-09-19T19:50:05.899376Z)
- `NDF|TOTAL|demand` = **19452** (n=228, 2026-09-19T19:48:04.844285Z)
- `TSDF|TOTAL|demand` = **19952** (n=228, 2026-09-19T19:48:04.844285Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T19:53:48.887132Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:47.592184Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:46.279591Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:44.952305Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:43.622095Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:42.332218Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:41.038765Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:39.722764Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:38.401094Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:36.787064Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:35.466383Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:34.158034Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:32.854913Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:31.496341Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:53:30.183530Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
