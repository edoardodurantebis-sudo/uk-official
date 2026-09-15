# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T17:59:22.217214Z`  
Current process started UTC: `2026-09-15T17:55:21.861524Z`  
1-second metadata polls in this process: **237**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=651, delta=-3, z=4.41 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=654, delta=1, z=4.66 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=653, delta=17, z=4.87 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=636, delta=88, z=4.75 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=3.95 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.09 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.26 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=7, delta=2, z=5.40 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.44 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.65 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=7, delta=0, z=4.90 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-777** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=NPSHYD|generation` = **651** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3312** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=OTHER|generation` = **2814** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=PS|generation` = **507** (n=252, 2026-09-15T17:55:21.861532Z)
- `FUELINST|fuelType=WIND|generation` = **10431** (n=252, 2026-09-15T17:55:21.861532Z)
- `IMBALNGC|TOTAL|imbalance` = **5775** (n=42, 2026-09-15T17:52:13.914766Z)
- `INDDEM|TOTAL|demand` = **-11918** (n=42, 2026-09-15T17:52:13.914766Z)
- `INDGEN|TOTAL|generation` = **24896** (n=42, 2026-09-15T17:52:13.914766Z)
- `MELNGC|TOTAL|margin` = **35671** (n=42, 2026-09-15T17:49:53.726350Z)
- `NDF|TOTAL|demand` = **18621** (n=43, 2026-09-15T17:48:01.468438Z)
- `TSDF|TOTAL|demand` = **19121** (n=43, 2026-09-15T17:48:01.468438Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T17:58:18.045801Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:57:45Z`
- `2026-09-15T17:56:09.513488Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:55:45Z`
- `2026-09-15T17:55:21.861532Z` — **FUELINST**: 80 rows; marker `2026-09-15T17:55:00Z`
- `2026-09-15T17:54:06.568467Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:53:45Z`
- `2026-09-15T17:52:13.914766Z` — **INDGEN**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:52:13.914766Z` — **INDDEM**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:52:13.914766Z` — **IMBALNGC**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:52:13.914766Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:51:45Z`
- `2026-09-15T17:50:25.381008Z` — **FUELINST**: 80 rows; marker `2026-09-15T17:50:00Z`
- `2026-09-15T17:50:09.935022Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:49:45Z`
- `2026-09-15T17:49:53.726350Z` — **MELNGC**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:48:01.468438Z` — **TSDF**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:48:01.468438Z` — **NDF**: 68 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:48:01.468438Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:47:45Z`
- `2026-09-15T17:46:25.676502Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:45:45Z`
