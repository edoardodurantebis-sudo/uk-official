# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T12:00:48.104750Z`  
Current process started UTC: `2026-09-20T11:56:47.460672Z`  
1-second metadata polls in this process: **163**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=NPSHYD|generation` = **275** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=OTHER|generation` = **443** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=PS|generation` = **-667** (n=1546, 2026-09-20T12:00:34.319326Z)
- `FUELINST|fuelType=WIND|generation` = **12587** (n=1546, 2026-09-20T12:00:34.319326Z)
- `IMBALNGC|TOTAL|imbalance` = **-5732** (n=254, 2026-09-20T11:54:11.922528Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=254, 2026-09-20T11:53:56.361979Z)
- `INDGEN|TOTAL|generation` = **15372** (n=254, 2026-09-20T11:53:56.361979Z)
- `MELNGC|TOTAL|margin` = **35780** (n=254, 2026-09-20T11:50:51.530998Z)
- `NDF|TOTAL|demand` = **20604** (n=260, 2026-09-20T11:48:14.448744Z)
- `TSDF|TOTAL|demand` = **21104** (n=260, 2026-09-20T11:48:14.448744Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T12:00:46.684396Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:45.140202Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:43.735326Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:42.320623Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:40.922756Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:39.526502Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:38.155081Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:34.319326Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:34.319326Z` — **FUELHH**: 20 rows; marker `2026-09-20T12:00:00Z`
- `2026-09-20T12:00:34.319326Z` — **FUELINST**: 80 rows; marker `2026-09-20T12:00:00Z`
- `2026-09-20T12:00:32.871938Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:31.468381Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:30.050498Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:28.625784Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:00:27.232647Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
