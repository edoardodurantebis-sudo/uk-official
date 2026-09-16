# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T18:15:13.697209Z`  
Current process started UTC: `2026-09-16T18:11:13.921914Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=683, delta=-23, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=706, delta=17, z=3.89 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=687, delta=-2, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=50, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=689, delta=2, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=0, z=3.73 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.48 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=0, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.57 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=1, z=3.84 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=686, delta=1, z=3.88 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=NPSHYD|generation` = **683** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=OTHER|generation` = **1747** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=PS|generation` = **982** (n=543, 2026-09-16T18:10:30.827203Z)
- `FUELINST|fuelType=WIND|generation` = **7980** (n=543, 2026-09-16T18:10:30.827203Z)
- `IMBALNGC|TOTAL|imbalance` = **6470** (n=89, 2026-09-16T17:52:27.704081Z)
- `INDDEM|TOTAL|demand` = **-11776** (n=89, 2026-09-16T17:52:27.704081Z)
- `INDGEN|TOTAL|generation` = **25591** (n=89, 2026-09-16T17:52:27.704081Z)
- `MELNGC|TOTAL|margin` = **34093** (n=89, 2026-09-16T17:50:03.027017Z)
- `NDF|TOTAL|demand` = **18621** (n=91, 2026-09-16T17:47:44.789570Z)
- `TSDF|TOTAL|demand` = **19121** (n=91, 2026-09-16T17:47:59.877265Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T18:14:15.650368Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:13:45Z`
- `2026-09-16T18:12:22.930327Z` — **MID**: 0 rows; marker `2026-09-16T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T18:12:22.930327Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:11:45Z`
- `2026-09-16T18:10:30.827203Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:10:00Z`
- `2026-09-16T18:10:15.289265Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:09:45Z`
- `2026-09-16T18:08:07.766388Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:07:45Z`
- `2026-09-16T18:07:19.402238Z` — **MID**: 0 rows; marker `2026-09-16T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T18:06:04.626271Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:05:45Z`
- `2026-09-16T18:05:32.195482Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:05:00Z`
- `2026-09-16T18:04:11.762572Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:03:45Z`
- `2026-09-16T18:02:05.217404Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:01:45Z`
- `2026-09-16T18:00:44.953992Z` — **FUELHH**: 20 rows; marker `2026-09-16T18:00:00Z`
- `2026-09-16T18:00:44.953992Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:00:00Z`
- `2026-09-16T18:00:12.619884Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:59:45Z`
- `2026-09-16T17:58:36.965934Z` — **FREQ**: 5761 rows; marker `2026-09-16T17:57:45Z`
