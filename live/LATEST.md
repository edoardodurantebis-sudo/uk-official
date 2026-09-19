# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T19:24:22.444650Z`  
Current process started UTC: `2026-09-19T19:20:20.972184Z`  
1-second metadata polls in this process: **146**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-8.91 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1426** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=NPSHYD|generation` = **519** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=OCGT|generation` = **99** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=OTHER|generation` = **463** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=PS|generation` = **825** (n=1346, 2026-09-19T19:20:38.740575Z)
- `FUELINST|fuelType=WIND|generation` = **13834** (n=1346, 2026-09-19T19:20:38.740575Z)
- `IMBALNGC|TOTAL|imbalance` = **-3754** (n=222, 2026-09-19T19:22:47.836433Z)
- `INDDEM|TOTAL|demand` = **-11872** (n=222, 2026-09-19T19:22:31.393542Z)
- `INDGEN|TOTAL|generation` = **16198** (n=222, 2026-09-19T19:22:31.393542Z)
- `MELNGC|TOTAL|margin` = **36176** (n=222, 2026-09-19T19:20:20.972192Z)
- `NDF|TOTAL|demand` = **19452** (n=227, 2026-09-19T19:18:02.472274Z)
- `TSDF|TOTAL|demand` = **19952** (n=227, 2026-09-19T19:18:02.472274Z)
- `WINDFOR|TOTAL|generation` = **6861** (n=38, 2026-09-19T16:30:54.253544Z)

## Latest publication events

- `2026-09-19T19:24:20.921272Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:19.404109Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:17.872570Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:16.354601Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:14.826993Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:13.287401Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:11.762509Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:10.240157Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:08.195083Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:06.662231Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:05.139564Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:03.605677Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:02.053598Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:24:00.521216Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T19:23:58.991339Z` — **MID**: 0 rows; marker `2026-09-19T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
