# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T18:07:47.334901Z`  
Current process started UTC: `2026-09-15T18:03:47.215831Z`  
1-second metadata polls in this process: **235**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=NPSHYD` `generation` — half-hour generation mix [fuelType=NPSHYD] generation: value=626, delta=138, z=4.73 -> generation-mix component moved
- **FUELINST** `fuelType=OTHER` `generation` — instantaneous generation mix [fuelType=OTHER] generation: value=3110, delta=296, z=3.86 -> generation-mix component moved
- **FUELINST** `fuelType=NPSHYD` `generation` — instantaneous generation mix [fuelType=NPSHYD] generation: value=616, delta=-35, z=3.63 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-791** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=NPSHYD|generation` = **614** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3311** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=OTHER|generation` = **2926** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=PS|generation` = **738** (n=254, 2026-09-15T18:05:40.117297Z)
- `FUELINST|fuelType=WIND|generation` = **10224** (n=254, 2026-09-15T18:05:40.117297Z)
- `IMBALNGC|TOTAL|imbalance` = **5775** (n=42, 2026-09-15T17:52:13.914766Z)
- `INDDEM|TOTAL|demand` = **-11918** (n=42, 2026-09-15T17:52:13.914766Z)
- `INDGEN|TOTAL|generation` = **24896** (n=42, 2026-09-15T17:52:13.914766Z)
- `MELNGC|TOTAL|margin` = **35671** (n=42, 2026-09-15T17:49:53.726350Z)
- `NDF|TOTAL|demand` = **18621** (n=43, 2026-09-15T17:48:01.468438Z)
- `TSDF|TOTAL|demand` = **19121** (n=43, 2026-09-15T17:48:01.468438Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T18:07:31.873786Z` — **MID**: 0 rows; marker `2026-09-15T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T18:06:11.699913Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:05:45Z`
- `2026-09-15T18:05:40.117297Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:05:00Z`
- `2026-09-15T18:04:19.461332Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:03:45Z`
- `2026-09-15T18:02:17.392561Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:01:45Z`
- `2026-09-15T18:00:41.113029Z` — **FUELHH**: 20 rows; marker `2026-09-15T18:00:00Z`
- `2026-09-15T18:00:41.113029Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:00:00Z`
- `2026-09-15T18:00:24.900640Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:59:45Z`
- `2026-09-15T17:58:18.045801Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:57:45Z`
- `2026-09-15T17:56:09.513488Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:55:45Z`
- `2026-09-15T17:55:21.861532Z` — **FUELINST**: 80 rows; marker `2026-09-15T17:55:00Z`
- `2026-09-15T17:54:06.568467Z` — **FREQ**: 5761 rows; marker `2026-09-15T17:53:45Z`
- `2026-09-15T17:52:13.914766Z` — **INDGEN**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:52:13.914766Z` — **INDDEM**: 1224 rows; marker `2026-09-15T17:47:00Z`
- `2026-09-15T17:52:13.914766Z` — **IMBALNGC**: 1224 rows; marker `2026-09-15T17:47:00Z`
