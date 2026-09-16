# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T18:36:10.917530Z`  
Current process started UTC: `2026-09-16T18:32:11.132741Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=692, delta=5, z=3.75 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.97 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=NPSHYD|generation` = **692** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3302** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=OTHER|generation` = **1909** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=PS|generation` = **906** (n=548, 2026-09-16T18:35:39.399796Z)
- `FUELINST|fuelType=WIND|generation` = **8367** (n=548, 2026-09-16T18:35:39.399796Z)
- `IMBALNGC|TOTAL|imbalance` = **6523** (n=90, 2026-09-16T18:22:50.880078Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=90, 2026-09-16T18:22:33.225505Z)
- `INDGEN|TOTAL|generation` = **25644** (n=90, 2026-09-16T18:22:33.225505Z)
- `MELNGC|TOTAL|margin` = **34182** (n=90, 2026-09-16T18:20:08.517649Z)
- `NDF|TOTAL|demand` = **18621** (n=92, 2026-09-16T18:18:04.757592Z)
- `TSDF|TOTAL|demand` = **19121** (n=92, 2026-09-16T18:18:04.757592Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T18:35:39.399796Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:35:00Z`
- `2026-09-16T18:34:19.839264Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:33:45Z`
- `2026-09-16T18:32:11.132751Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:31:45Z`
- `2026-09-16T18:30:40.963963Z` — **FUELHH**: 20 rows; marker `2026-09-16T18:30:00Z`
- `2026-09-16T18:30:40.963963Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:30:00Z`
- `2026-09-16T18:30:09.003998Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:29:45Z`
- `2026-09-16T18:28:17.230184Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:27:45Z`
- `2026-09-16T18:26:16.202934Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:25:45Z`
- `2026-09-16T18:25:28.404479Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:25:00Z`
- `2026-09-16T18:24:21.369403Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:23:45Z`
- `2026-09-16T18:22:50.880078Z` — **IMBALNGC**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:22:33.225505Z` — **INDGEN**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:22:33.225505Z` — **INDDEM**: 1206 rows; marker `2026-09-16T18:17:00Z`
- `2026-09-16T18:22:17.089281Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:21:45Z`
- `2026-09-16T18:20:24.813030Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:20:00Z`
