# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T18:49:51.657816Z`  
Current process started UTC: `2026-09-15T18:45:51.121594Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.98 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=7.77 -> generation-mix component moved
- **FUELHH** `fuelType=OTHER` `generation` — half-hour generation mix [fuelType=OTHER] generation: value=2942, delta=440, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=39, delta=32, z=16.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=8.90 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=10.72 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=7, z=14.50 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=49, delta=42, z=20.85 -> generation-mix component moved
- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=626, delta=138, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3110, delta=296, z=3.86 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=616, delta=-35, z=3.63 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=651, delta=-3, z=4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=654, delta=1, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=653, delta=17, z=4.87 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-799** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=NPSHYD|generation` = **510** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=OCGT|generation` = **56** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=OTHER|generation` = **2906** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=PS|generation` = **803** (n=262, 2026-09-15T18:45:37.572715Z)
- `FUELINST|fuelType=WIND|generation` = **9916** (n=262, 2026-09-15T18:45:37.572715Z)
- `IMBALNGC|TOTAL|imbalance` = **5737** (n=43, 2026-09-15T18:21:59.581565Z)
- `INDDEM|TOTAL|demand` = **-11909** (n=43, 2026-09-15T18:21:59.581565Z)
- `INDGEN|TOTAL|generation` = **24858** (n=43, 2026-09-15T18:21:59.581565Z)
- `MELNGC|TOTAL|margin` = **35590** (n=44, 2026-09-15T18:49:36.986440Z)
- `NDF|TOTAL|demand` = **18621** (n=45, 2026-09-15T18:47:44.580419Z)
- `TSDF|TOTAL|demand` = **19121** (n=45, 2026-09-15T18:47:44.580419Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T18:49:36.986440Z` — **MELNGC**: 1188 rows; marker `2026-09-15T18:47:00Z`
- `2026-09-15T18:48:16.647387Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:47:45Z`
- `2026-09-15T18:47:44.580419Z` — **TSDF**: 1188 rows; marker `2026-09-15T18:47:00Z`
- `2026-09-15T18:47:44.580419Z` — **NDF**: 66 rows; marker `2026-09-15T18:47:00Z`
- `2026-09-15T18:46:09.123847Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:45:45Z`
- `2026-09-15T18:45:37.572715Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:45:00Z`
- `2026-09-15T18:44:01.917350Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:43:45Z`
- `2026-09-15T18:42:10.445993Z` — **MID**: 0 rows; marker `2026-09-15T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T18:42:10.445993Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:41:45Z`
- `2026-09-15T18:40:31.968440Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:40:00Z`
- `2026-09-15T18:40:15.881578Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:39:45Z`
- `2026-09-15T18:38:07.858393Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:37:45Z`
- `2026-09-15T18:36:16.832737Z` — **MID**: 0 rows; marker `2026-09-15T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T18:36:16.832737Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:35:45Z`
- `2026-09-15T18:35:44.828541Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:35:00Z`
