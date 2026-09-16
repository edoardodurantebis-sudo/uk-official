# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T18:48:47.717659Z`  
Current process started UTC: `2026-09-16T18:44:47.535842Z`  
1-second metadata polls in this process: **233**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.85 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **389** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=NPSHYD|generation` = **659** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3301** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=OTHER|generation` = **1722** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=PS|generation` = **906** (n=550, 2026-09-16T18:45:35.704891Z)
- `FUELINST|fuelType=WIND|generation` = **8555** (n=550, 2026-09-16T18:45:35.704891Z)
- `IMBALNGC|TOTAL|imbalance` = **6523** (n=90, 2026-09-16T18:22:50.880078Z)
- `INDDEM|TOTAL|demand` = **-11768** (n=90, 2026-09-16T18:22:33.225505Z)
- `INDGEN|TOTAL|generation` = **25644** (n=90, 2026-09-16T18:22:33.225505Z)
- `MELNGC|TOTAL|margin` = **34182** (n=90, 2026-09-16T18:20:08.517649Z)
- `NDF|TOTAL|demand` = **18621** (n=93, 2026-09-16T18:48:00.832960Z)
- `TSDF|TOTAL|demand` = **19121** (n=93, 2026-09-16T18:48:00.832960Z)
- `WINDFOR|TOTAL|generation` = **19485** (n=15, 2026-09-16T16:30:25.726572Z)

## Latest publication events

- `2026-09-16T18:48:16.609206Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:47:45Z`
- `2026-09-16T18:48:00.832960Z` — **TSDF**: 1188 rows; marker `2026-09-16T18:47:00Z`
- `2026-09-16T18:48:00.832960Z` — **NDF**: 66 rows; marker `2026-09-16T18:47:00Z`
- `2026-09-16T18:46:23.467456Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:45:45Z`
- `2026-09-16T18:45:35.704891Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:45:00Z`
- `2026-09-16T18:44:22.394998Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:43:45Z`
- `2026-09-16T18:42:14.245069Z` — **MID**: 0 rows; marker `2026-09-16T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T18:42:14.245069Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:41:45Z`
- `2026-09-16T18:40:38.229850Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:40:00Z`
- `2026-09-16T18:40:22.293736Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:39:45Z`
- `2026-09-16T18:38:14.845487Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:37:45Z`
- `2026-09-16T18:36:38.766129Z` — **MID**: 0 rows; marker `2026-09-16T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T18:36:23.355971Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:35:45Z`
- `2026-09-16T18:35:39.399796Z` — **FUELINST**: 80 rows; marker `2026-09-16T18:35:00Z`
- `2026-09-16T18:34:19.839264Z` — **FREQ**: 5761 rows; marker `2026-09-16T18:33:45Z`
