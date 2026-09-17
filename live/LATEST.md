# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:49:35.535898Z`  
Current process started UTC: `2026-09-17T18:45:35.281596Z`  
1-second metadata polls in this process: **221**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.58 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=0, z=4.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=NPSHYD|generation` = **628** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3319** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=OCGT|generation` = **79** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=OTHER|generation` = **1830** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=PS|generation` = **280** (n=807, 2026-09-17T18:45:37.753709Z)
- `FUELINST|fuelType=WIND|generation` = **15067** (n=807, 2026-09-17T18:45:37.753709Z)
- `IMBALNGC|TOTAL|imbalance` = **9682** (n=133, 2026-09-17T18:24:32.722523Z)
- `INDDEM|TOTAL|demand` = **-11254** (n=133, 2026-09-17T18:24:12.670545Z)
- `INDGEN|TOTAL|generation` = **26496** (n=133, 2026-09-17T18:24:12.670545Z)
- `MELNGC|TOTAL|margin` = **36584** (n=133, 2026-09-17T18:21:20.240550Z)
- `NDF|TOTAL|demand` = **16314** (n=137, 2026-09-17T18:48:33.698047Z)
- `TSDF|TOTAL|demand` = **16814** (n=137, 2026-09-17T18:48:33.698047Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:49:34.505399Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:33.459938Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:32.417425Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:31.387877Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:30.359908Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:29.308957Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:28.232274Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:27.197775Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:26.174826Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:25.151444Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:24.111597Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:23.033579Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:22.014082Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:20.742249Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:49:19.695805Z` — **MID**: 0 rows; marker `2026-09-17T18:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
