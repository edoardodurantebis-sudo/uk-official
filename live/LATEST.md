# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-16T20:20:57.829600Z`  
Current process started UTC: `2026-09-16T20:16:57.733511Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.28 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.51 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.55 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.60 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.80 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.85 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.91 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=692, delta=5, z=3.75 -> generation-mix component moved
- **FUELHH** `fuelType=INTGRNL` `generation` — half-hour generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=4.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTGRNL` `generation` — instantaneous generation mix [fuelType=INTGRNL] generation: value=120, delta=0, z=3.97 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **292** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=NPSHYD|generation` = **444** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3306** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=OTHER|generation` = **565** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=569, 2026-09-16T20:20:25.526434Z)
- `FUELINST|fuelType=WIND|generation` = **10131** (n=569, 2026-09-16T20:20:25.526434Z)
- `IMBALNGC|TOTAL|imbalance` = **6640** (n=93, 2026-09-16T19:52:04.923339Z)
- `INDDEM|TOTAL|demand` = **-11763** (n=93, 2026-09-16T19:51:48.845809Z)
- `INDGEN|TOTAL|generation` = **25761** (n=93, 2026-09-16T19:51:48.845809Z)
- `MELNGC|TOTAL|margin` = **34353** (n=94, 2026-09-16T20:19:37.893919Z)
- `NDF|TOTAL|demand` = **18621** (n=96, 2026-09-16T20:17:45.795333Z)
- `TSDF|TOTAL|demand` = **19121** (n=96, 2026-09-16T20:17:45.795333Z)
- `WINDFOR|TOTAL|generation` = **19445** (n=16, 2026-09-16T19:30:31.948327Z)

## Latest publication events

- `2026-09-16T20:20:25.526434Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:20:00Z`
- `2026-09-16T20:20:25.526434Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:19:45Z`
- `2026-09-16T20:19:37.893919Z` — **MELNGC**: 1134 rows; marker `2026-09-16T20:17:00Z`
- `2026-09-16T20:18:17.943586Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:17:45Z`
- `2026-09-16T20:17:45.795333Z` — **TSDF**: 1134 rows; marker `2026-09-16T20:17:00Z`
- `2026-09-16T20:17:45.795333Z` — **NDF**: 63 rows; marker `2026-09-16T20:17:00Z`
- `2026-09-16T20:16:14.091636Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:15:45Z`
- `2026-09-16T20:15:26.329200Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:15:00Z`
- `2026-09-16T20:14:21.961354Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:13:45Z`
- `2026-09-16T20:12:20.994012Z` — **MID**: 0 rows; marker `2026-09-16T20:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-16T20:12:20.994012Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:11:45Z`
- `2026-09-16T20:10:28.741211Z` — **FUELINST**: 80 rows; marker `2026-09-16T20:10:00Z`
- `2026-09-16T20:10:12.534392Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:09:45Z`
- `2026-09-16T20:08:20.183721Z` — **FREQ**: 5761 rows; marker `2026-09-16T20:07:45Z`
- `2026-09-16T20:06:28.289834Z` — **MID**: 0 rows; marker `2026-09-16T20:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
