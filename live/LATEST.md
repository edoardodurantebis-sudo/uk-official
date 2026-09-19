# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:28:35.595878Z`  
Current process started UTC: `2026-09-19T19:24:34.268669Z`  
1-second metadata polls in this process: **193**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.07 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=16.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.12 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=1, z=19.10 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=0, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=403, delta=-1, z=22.31 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=99, delta=16, z=5.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=404, delta=175, z=28.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=63, z=4.37 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=229, delta=229, z=17.80 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=0, delta=92, z=-0.01 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-92, delta=10, z=-8.47 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-31, delta=73, z=-2.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.18 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.40 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=NPSHYD|generation` = **524** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=OTHER|generation` = **494** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=PS|generation` = **825** (n=1347, 2026-09-19T19:25:38.200432Z)
- `FUELINST|fuelType=WIND|generation` = **13820** (n=1347, 2026-09-19T19:25:38.200432Z)
- `IMBALNGC|TOTAL|imbalance` = **-3754** (n=222, 2026-09-19T19:22:47.836433Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=222, 2026-09-19T19:22:31.393542Z)
- `INDGEN|TOTAL|generation` = **16198** (n=222, 2026-09-19T19:22:31.393542Z)
- `MELNGC|TOTAL|margin` = **36176** (n=222, 2026-09-19T19:20:20.972192Z)
- `NDF|TOTAL|demand` = **19452** (n=227, 2026-09-19T19:18:02.472274Z)
- `TSDF|TOTAL|demand` = **19952** (n=227, 2026-09-19T19:18:02.472274Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T19:28:33.988313Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:32.781724Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:31.597224Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:30.407143Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:29.236702Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:28.054849Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:26.868227Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:25.728202Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:24.538108Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:23.357746Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:22.180988Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:21.003667Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:18.417427Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:28:18.417427Z` — **FREQ**: 5761 rows; marker `2026-09-19T19:27:45Z`
- `2026-09-19T19:28:17.228323Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
