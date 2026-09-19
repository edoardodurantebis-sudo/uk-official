# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T14:38:01.635305Z`  
Current process started UTC: `2026-09-19T14:34:00.477456Z`  
1-second metadata polls in this process: **144**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.20 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-102, delta=-202, z=-12.22 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-9.88 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=0, z=-10.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-104, delta=-15, z=-11.26 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-89, delta=-179, z=-10.03 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=100, delta=26, z=19.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=90, delta=-13, z=10.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=12.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=13.38 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=14.43 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=0, z=15.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=103, delta=1, z=17.60 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=NPSHYD|generation` = **266** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=OTHER|generation` = **1262** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=PS|generation` = **-532** (n=1289, 2026-09-19T14:35:38.213515Z)
- `FUELINST|fuelType=WIND|generation` = **13631** (n=1289, 2026-09-19T14:35:38.213515Z)
- `IMBALNGC|TOTAL|imbalance` = **-3230** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDDEM|TOTAL|demand` = **-11875** (n=212, 2026-09-19T14:25:35.374558Z)
- `INDGEN|TOTAL|generation` = **16779** (n=212, 2026-09-19T14:25:35.374558Z)
- `MELNGC|TOTAL|margin` = **36925** (n=212, 2026-09-19T14:20:59.619875Z)
- `NDF|TOTAL|demand` = **19509** (n=217, 2026-09-19T14:18:32.720132Z)
- `TSDF|TOTAL|demand` = **20009** (n=217, 2026-09-19T14:18:32.720132Z)
- `WINDFOR|TOTAL|generation` = **6655** (n=37, 2026-09-19T12:30:34.686513Z)

## Latest publication events

- `2026-09-19T14:38:00.080317Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:58.539183Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:56.986358Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:55.457760Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:53.928003Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:50.952842Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:49.407012Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:47.883452Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:46.214299Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:44.669140Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:43.012319Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:41.443259Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:39.892702Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:38.358390Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T14:37:36.522271Z` — **MID**: 0 rows; marker `2026-09-19T14:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
