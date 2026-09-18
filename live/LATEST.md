# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:43:17.184019Z`  
Current process started UTC: `2026-09-18T09:39:16.929166Z`  
1-second metadata polls in this process: **227**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **WINDFOR** `TOTAL` `generation` — wind forecast [TOTAL] generation: value=7845, delta=-11023, z=-4.38 -> renewable cushion down / residual-load pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=OTHER|generation` = **911** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=PS|generation` = **-420** (n=986, 2026-09-18T09:40:38.706727Z)
- `FUELINST|fuelType=WIND|generation` = **11812** (n=986, 2026-09-18T09:40:38.706727Z)
- `IMBALNGC|TOTAL|imbalance` = **8100** (n=162, 2026-09-18T09:20:18.018457Z)
- `INDDEM|TOTAL|demand` = **-13185** (n=162, 2026-09-18T09:19:45.552785Z)
- `INDGEN|TOTAL|generation` = **27193** (n=162, 2026-09-18T09:19:45.552785Z)
- `MELNGC|TOTAL|margin` = **36209** (n=162, 2026-09-18T09:19:13.657509Z)
- `NDF|TOTAL|demand` = **16454** (n=166, 2026-09-18T09:17:04.819417Z)
- `TSDF|TOTAL|demand` = **19093** (n=166, 2026-09-18T09:17:21.227303Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:43:16.218702Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:15.218619Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:14.218506Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:13.091090Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:12.091011Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:11.090944Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:10.090824Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:09.090692Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:08.090620Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:06.342376Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:05.342296Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:04.342158Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:03.342035Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:02.341922Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:43:01.341812Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
