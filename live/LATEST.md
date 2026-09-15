# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T23:57:59.722713Z`  
Current process started UTC: `2026-09-15T23:53:59.164147Z`  
1-second metadata polls in this process: **239**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **249** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=NPSHYD|generation` = **425** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=OTHER|generation` = **220** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=PS|generation` = **108** (n=324, 2026-09-15T23:55:34.887041Z)
- `FUELINST|fuelType=WIND|generation` = **10512** (n=324, 2026-09-15T23:55:34.887041Z)
- `IMBALNGC|TOTAL|imbalance` = **5865** (n=54, 2026-09-15T23:50:54.652718Z)
- `INDDEM|TOTAL|demand` = **-12080** (n=54, 2026-09-15T23:50:54.652718Z)
- `INDGEN|TOTAL|generation` = **24986** (n=54, 2026-09-15T23:50:54.652718Z)
- `MELNGC|TOTAL|margin` = **35662** (n=54, 2026-09-15T23:49:18.398374Z)
- `NDF|TOTAL|demand` = **18621** (n=55, 2026-09-15T23:47:27.510265Z)
- `TSDF|TOTAL|demand` = **19121** (n=55, 2026-09-15T23:47:27.510265Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-15T23:56:23.146761Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:55:45Z`
- `2026-09-15T23:55:34.887041Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:55:00Z`
- `2026-09-15T23:54:31.167862Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:53:45Z`
- `2026-09-15T23:52:13.370303Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:51:45Z`
- `2026-09-15T23:50:54.652718Z` — **INDGEN**: 1008 rows; marker `2026-09-15T23:47:00Z`
- `2026-09-15T23:50:54.652718Z` — **INDDEM**: 1008 rows; marker `2026-09-15T23:47:00Z`
- `2026-09-15T23:50:54.652718Z` — **IMBALNGC**: 1008 rows; marker `2026-09-15T23:47:00Z`
- `2026-09-15T23:50:22.645027Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:50:00Z`
- `2026-09-15T23:50:06.496386Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:49:45Z`
- `2026-09-15T23:49:18.398374Z` — **MELNGC**: 1008 rows; marker `2026-09-15T23:47:00Z`
- `2026-09-15T23:48:15.099685Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:47:45Z`
- `2026-09-15T23:47:27.510265Z` — **TSDF**: 1008 rows; marker `2026-09-15T23:47:00Z`
- `2026-09-15T23:47:27.510265Z` — **NDF**: 56 rows; marker `2026-09-15T23:47:00Z`
- `2026-09-15T23:46:08.273901Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:45:45Z`
- `2026-09-15T23:45:36.280731Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:45:00Z`
