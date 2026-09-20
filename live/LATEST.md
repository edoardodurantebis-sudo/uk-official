# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T11:56:36.380070Z`  
Current process started UTC: `2026-09-20T11:52:35.812956Z`  
1-second metadata polls in this process: **231**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=NPSHYD|generation` = **286** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=OTHER|generation` = **452** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=PS|generation` = **-664** (n=1545, 2026-09-20T11:55:31.899510Z)
- `FUELINST|fuelType=WIND|generation` = **12660** (n=1545, 2026-09-20T11:55:31.899510Z)
- `IMBALNGC|TOTAL|imbalance` = **-5732** (n=254, 2026-09-20T11:54:11.922528Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=254, 2026-09-20T11:53:56.361979Z)
- `INDGEN|TOTAL|generation` = **15372** (n=254, 2026-09-20T11:53:56.361979Z)
- `MELNGC|TOTAL|margin` = **35780** (n=254, 2026-09-20T11:50:51.530998Z)
- `NDF|TOTAL|demand` = **20604** (n=260, 2026-09-20T11:48:14.448744Z)
- `TSDF|TOTAL|demand` = **21104** (n=260, 2026-09-20T11:48:14.448744Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T11:56:35.197014Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:34.196899Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:33.196787Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:32.196657Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:31.196571Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:30.196438Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:29.196324Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:28.196195Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:27.196087Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:26.195997Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:25.195879Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:24.195759Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:23.195647Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:22.195516Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:56:21.178535Z` — **MID**: 0 rows; marker `2026-09-20T11:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
