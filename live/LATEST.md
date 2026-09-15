# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T18:20:25.203613Z`  
Current process started UTC: `2026-09-15T18:16:24.625405Z`  
1-second metadata polls in this process: **238**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=49, delta=42, z=20.85 -> generation-mix component moved
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **-799** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=NPSHYD|generation` = **496** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3315** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=OCGT|generation` = **49** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=OTHER|generation` = **2775** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=PS|generation` = **804** (n=256, 2026-09-15T18:15:42.315983Z)
- `FUELINST|fuelType=WIND|generation` = **10042** (n=256, 2026-09-15T18:15:42.315983Z)
- `IMBALNGC|TOTAL|imbalance` = **5775** (n=42, 2026-09-15T17:52:13.914766Z)
- `INDDEM|TOTAL|demand` = **-11918** (n=42, 2026-09-15T17:52:13.914766Z)
- `INDGEN|TOTAL|generation` = **24896** (n=42, 2026-09-15T17:52:13.914766Z)
- `MELNGC|TOTAL|margin` = **35655** (n=43, 2026-09-15T18:19:51.344206Z)
- `NDF|TOTAL|demand` = **18621** (n=44, 2026-09-15T18:17:44.134215Z)
- `TSDF|TOTAL|demand` = **19121** (n=44, 2026-09-15T18:18:00.136071Z)
- `WINDFOR|TOTAL|generation` = **17795** (n=7, 2026-09-15T16:30:51.506988Z)

## Latest publication events

- `2026-09-15T18:20:23.625291Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:19:45Z`
- `2026-09-15T18:19:51.344206Z` — **MELNGC**: 1206 rows; marker `2026-09-15T18:17:00Z`
- `2026-09-15T18:18:15.976849Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:17:45Z`
- `2026-09-15T18:18:00.136071Z` — **TSDF**: 1206 rows; marker `2026-09-15T18:17:00Z`
- `2026-09-15T18:17:44.134215Z` — **NDF**: 67 rows; marker `2026-09-15T18:17:00Z`
- `2026-09-15T18:16:24.625413Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:15:45Z`
- `2026-09-15T18:15:42.315983Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:15:00Z`
- `2026-09-15T18:14:22.543926Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:13:45Z`
- `2026-09-15T18:12:15.022978Z` — **MID**: 0 rows; marker `2026-09-15T18:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T18:12:15.022978Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:11:45Z`
- `2026-09-15T18:10:40.012007Z` — **FUELINST**: 80 rows; marker `2026-09-15T18:10:00Z`
- `2026-09-15T18:10:08.023554Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:09:45Z`
- `2026-09-15T18:08:16.110433Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:07:45Z`
- `2026-09-15T18:07:31.873786Z` — **MID**: 0 rows; marker `2026-09-15T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T18:06:11.699913Z` — **FREQ**: 5761 rows; marker `2026-09-15T18:05:45Z`
