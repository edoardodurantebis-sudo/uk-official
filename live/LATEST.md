# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:29:39.540808Z`  
Current process started UTC: `2026-09-20T13:25:39.024304Z`  
1-second metadata polls in this process: **197**  
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

- `FUELINST|fuelType=INTVKL|generation` = **129** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=OTHER|generation` = **311** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=PS|generation` = **-667** (n=1563, 2026-09-20T13:25:39.024315Z)
- `FUELINST|fuelType=WIND|generation` = **11370** (n=1563, 2026-09-20T13:25:39.024315Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDGEN|TOTAL|generation` = **15373** (n=257, 2026-09-20T13:23:35.682760Z)
- `MELNGC|TOTAL|margin` = **35771** (n=257, 2026-09-20T13:20:30.066297Z)
- `NDF|TOTAL|demand` = **20604** (n=263, 2026-09-20T13:18:20.388440Z)
- `TSDF|TOTAL|demand` = **21104** (n=263, 2026-09-20T13:18:20.388440Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:29:38.253658Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:37.077733Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:35.895339Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:34.472609Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:33.310605Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:32.140009Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:30.977274Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:29.804692Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:28.635751Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:27.445887Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:26.232609Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:25.027318Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:23.826470Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:22.637541Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:29:21.473685Z` — **MID**: 0 rows; marker `2026-09-20T13:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
