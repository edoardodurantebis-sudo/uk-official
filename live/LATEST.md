# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T13:46:25.484147Z`  
Current process started UTC: `2026-09-20T13:42:24.112129Z`  
1-second metadata polls in this process: **139**  
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

- `FUELINST|fuelType=INTVKL|generation` = **129** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=NPSHYD|generation` = **264** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=OTHER|generation` = **490** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=PS|generation` = **-655** (n=1567, 2026-09-20T13:45:45.580706Z)
- `FUELINST|fuelType=WIND|generation` = **10406** (n=1567, 2026-09-20T13:45:45.580706Z)
- `IMBALNGC|TOTAL|imbalance` = **-5731** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=257, 2026-09-20T13:23:51.098438Z)
- `INDGEN|TOTAL|generation` = **15373** (n=257, 2026-09-20T13:23:35.682760Z)
- `MELNGC|TOTAL|margin` = **35771** (n=257, 2026-09-20T13:20:30.066297Z)
- `NDF|TOTAL|demand` = **20604** (n=263, 2026-09-20T13:18:20.388440Z)
- `TSDF|TOTAL|demand` = **21104** (n=263, 2026-09-20T13:18:20.388440Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T13:46:23.847741Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:22.181646Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:20.526521Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:16.935644Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:16.935644Z` — **FREQ**: 5761 rows; marker `2026-09-20T13:45:45Z`
- `2026-09-20T13:46:15.279537Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:13.628507Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:11.973325Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:10.367528Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:08.696458Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:06.821504Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:05.166309Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:03.543244Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:46:01.571600Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T13:45:59.886058Z` — **MID**: 0 rows; marker `2026-09-20T13:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
