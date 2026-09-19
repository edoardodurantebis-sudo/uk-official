# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:49:38.717544Z`  
Current process started UTC: `2026-09-19T19:45:38.604471Z`  
1-second metadata polls in this process: **213**  
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
- `NDF|TOTAL|demand` = **19452** (n=228, 2026-09-19T19:48:04.844285Z)
- `TSDF|TOTAL|demand` = **19952** (n=228, 2026-09-19T19:48:04.844285Z)
- `WINDFOR|TOTAL|generation` = **6980** (n=39, 2026-09-19T19:30:45.819998Z)

## Latest publication events

- `2026-09-19T19:49:37.772478Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:36.772364Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:35.772232Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:34.772110Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:33.771983Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:32.771865Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:31.771743Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:30.771612Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:29.771530Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:28.771460Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:27.771363Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:26.745531Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:25.745427Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:24.345334Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:49:23.326057Z` — **MID**: 0 rows; marker `2026-09-19T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
