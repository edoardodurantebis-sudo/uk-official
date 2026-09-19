# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:45:25.497487Z`  
Current process started UTC: `2026-09-19T19:41:23.533971Z`  
1-second metadata polls in this process: **135**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=19.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.18 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=NPSHYD|generation` = **518** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=OTHER|generation` = **432** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=PS|generation` = **824** (n=1351, 2026-09-19T19:45:22.201574Z)
- `FUELINST|fuelType=WIND|generation` = **13779** (n=1351, 2026-09-19T19:45:22.201574Z)
- `IMBALNGC|TOTAL|imbalance` = **-3754** (n=222, 2026-09-19T19:22:47.836433Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=222, 2026-09-19T19:22:31.393542Z)
- `INDGEN|TOTAL|generation` = **16198** (n=222, 2026-09-19T19:22:31.393542Z)
- `MELNGC|TOTAL|margin` = **36176** (n=222, 2026-09-19T19:20:20.972192Z)
- `NDF|TOTAL|demand` = **19452** (n=227, 2026-09-19T19:18:02.472274Z)
- `TSDF|TOTAL|demand` = **19952** (n=227, 2026-09-19T19:18:02.472274Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T19:45:22.201574Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:22.201574Z` — **FUELINST**: 80 rows; marker `2026-09-19T19:45:00Z`
- `2026-09-19T19:45:20.484996Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:18.795880Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:16.991436Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:15.134202Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:13.427365Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:11.723004Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:09.953634Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:08.232738Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:05.874347Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:04.174408Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:02.455872Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:45:00.757827Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:44:59.042577Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
