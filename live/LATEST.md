# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T18:27:49.090992Z`  
Current process started UTC: `2026-09-16T18:23:49.130709Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=692, delta=2, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.03 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=690, delta=4, z=3.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=686, delta=3, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.16 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=683, delta=-23, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.23 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=706, delta=17, z=3.89 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.31 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=687, delta=-2, z=4.02 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=50, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=689, delta=2, z=3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.39 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=687, delta=0, z=3.73 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=NPSHYD|generation` = **692** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3303** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=OTHER|generation` = **1794** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=PS|generation` = **906** (n=546, 2026-09-16T18:25:28.404479Z)
- `FUELINST|fuelType=WIND|generation` = **8433** (n=546, 2026-09-16T18:25:28.404479Z)
- `IMBALNGC|TOTAL|imbalance` = **6523** (n=90, 2026-09-16T18:22:50.880078Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=90, 2026-09-16T18:22:33.225505Z)
- `INDGEN|TOTAL|generation` = **25644** (n=90, 2026-09-16T18:22:33.225505Z)
- `MELNGC|TOTAL|margin` = **34182** (n=90, 2026-09-16T18:20:08.517649Z)
- `NDF|TOTAL|demand` = **18621** (n=92, 2026-09-16T18:18:04.757592Z)
- `TSDF|TOTAL|demand` = **19121** (n=92, 2026-09-16T18:18:04.757592Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T18:26:16.202934Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:25:45Z`
- `2026-09-16T18:25:28.404479Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:25:00Z`
- `2026-09-16T18:24:21.369403Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:23:45Z`
- `2026-09-16T18:22:50.880078Z` — **IMBALNGC**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:22:33.225505Z` — **INDGEN**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:22:33.225505Z` — **INDDEM**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:22:17.089281Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:21:45Z`
- `2026-09-16T18:20:24.813030Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:20:00Z`
- `2026-09-16T18:20:08.517649Z` — **MELNGC**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:20:08.517649Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:19:45Z`
- `2026-09-16T18:18:21.108466Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:17:45Z`
- `2026-09-16T18:18:04.757592Z` — **TSDF**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:18:04.757592Z` — **NDF**: 67 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:16:12.908134Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:15:45Z`
- `2026-09-16T18:15:24.363039Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:15:00Z`
