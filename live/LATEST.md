# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T23:41:14.504945Z`  
Current process started UTC: `2026-09-15T23:37:14.490917Z`  
1-second metadata polls in this process: **238**  
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

- `FUELINST|fuelType=INTVKL|generation` = **249** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=NPSHYD|generation` = **425** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=OTHER|generation` = **269** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=PS|generation` = **115** (n=321, 2026-09-15T23:40:41.558136Z)
- `FUELINST|fuelType=WIND|generation` = **10628** (n=321, 2026-09-15T23:40:41.558136Z)
- `IMBALNGC|TOTAL|imbalance` = **5826** (n=53, 2026-09-15T23:21:00.094723Z)
- `INDDEM|TOTAL|demand` = **-12081** (n=53, 2026-09-15T23:21:00.094723Z)
- `INDGEN|TOTAL|generation` = **24948** (n=53, 2026-09-15T23:21:00.094723Z)
- `MELNGC|TOTAL|margin` = **35740** (n=53, 2026-09-15T23:19:08.626150Z)
- `NDF|TOTAL|demand` = **18621** (n=54, 2026-09-15T23:17:33.049938Z)
- `TSDF|TOTAL|demand` = **19121** (n=54, 2026-09-15T23:17:33.049938Z)
- `WINDFOR|TOTAL|generation` = **18072** (n=9, 2026-09-15T23:30:40.401005Z)

## Latest publication events

- `2026-09-15T23:40:41.558136Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:40:00Z`
- `2026-09-15T23:40:26.069308Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:39:45Z`
- `2026-09-15T23:38:18.622038Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:37:45Z`
- `2026-09-15T23:37:14.490926Z` — **MID**: 0 rows; marker `2026-09-15T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T23:37:14.490926Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:35:45Z`
- `2026-09-15T23:35:39.701476Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:35:00Z`
- `2026-09-15T23:34:19.817882Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:33:45Z`
- `2026-09-15T23:32:27.641877Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:31:45Z`
- `2026-09-15T23:30:40.401005Z` — **WINDFOR**: 73 rows; marker `2026-09-15T23:30:00Z`
- `2026-09-15T23:30:40.401005Z` — **FUELHH**: 20 rows; marker `2026-09-15T23:30:00Z`
- `2026-09-15T23:30:40.401005Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:30:00Z`
- `2026-09-15T23:30:24.379753Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:29:45Z`
- `2026-09-15T23:28:16.263576Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:27:45Z`
- `2026-09-15T23:26:27.147636Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:25:45Z`
- `2026-09-15T23:25:39.458826Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:25:00Z`
