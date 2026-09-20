# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:38:01.507442Z`  
Current process started UTC: `2026-09-20T13:34:00.770864Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **129** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=OTHER|generation` = **379** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=PS|generation` = **-392** (n=1565, 2026-09-20T13:35:35.397109Z)
- `FUELINST|fuelType=WIND|generation` = **10674** (n=1565, 2026-09-20T13:35:35.397109Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDGEN|TOTAL|generation` = **15373** (n=257, 2026-09-20T13:23:35.682760Z)
- `MELNGC|TOTAL|margin` = **35771** (n=257, 2026-09-20T13:20:30.066297Z)
- `NDF|TOTAL|demand` = **20604** (n=263, 2026-09-20T13:18:20.388440Z)
- `TSDF|TOTAL|demand` = **21104** (n=263, 2026-09-20T13:18:20.388440Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:38:00.468606Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:59.395899Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:58.395828Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:57.131287Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:56.103715Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:55.092758Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:54.086656Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:53.066908Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:52.066813Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:51.056936Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:49.718262Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:48.683503Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:47.683432Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:46.679030Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:37:45.677316Z` — **MID**: 0 rows; marker `2026-09-20T13:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
