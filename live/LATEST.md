# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T00:00:29.497350Z`  
Current process started UTC: `2026-09-17T23:56:28.694578Z`  
1-second metadata polls in this process: **173**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=80, delta=-38, z=3.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=97, delta=-21, z=4.20 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.28 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=118, delta=27, z=6.23 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.48 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.59 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=0, z=5.70 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=118, delta=-1, z=5.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=0, z=6.01 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=91, delta=9, z=5.18 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=119, delta=11, z=6.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=108, delta=29, z=5.66 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.08 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **608** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=NPSHYD|generation` = **451** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3316** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=OTHER|generation` = **272** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=PS|generation` = **56** (n=869, 2026-09-17T23:55:24.446661Z)
- `FUELINST|fuelType=WIND|generation` = **14273** (n=869, 2026-09-17T23:55:24.446661Z)
- `IMBALNGC|TOTAL|imbalance` = **10139** (n=144, 2026-09-17T23:53:42.397703Z)
- `INDDEM|TOTAL|demand` = **-11183** (n=144, 2026-09-17T23:53:26.100029Z)
- `INDGEN|TOTAL|generation` = **26953** (n=144, 2026-09-17T23:53:26.100029Z)
- `MELNGC|TOTAL|margin` = **36515** (n=144, 2026-09-17T23:50:34.020814Z)
- `NDF|TOTAL|demand` = **16314** (n=147, 2026-09-17T23:48:05.570317Z)
- `TSDF|TOTAL|demand` = **16814** (n=147, 2026-09-17T23:48:22.184365Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T00:00:27.911618Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:26.584523Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:25.235484Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:23.862791Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:21.882957Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:20.598822Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:19.213457Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:17.883709Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:16.562304Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:15.261742Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:13.963240Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:12.655700Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:11.288443Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:09.944719Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T00:00:08.577790Z` — **MID**: 0 rows; marker `2026-09-17T23:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
