# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T04:14:07.475559Z`  
Current process started UTC: `2026-09-18T04:10:06.576984Z`  
1-second metadata polls in this process: **142**  
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

- `FUELINST|fuelType=INTVKL|generation` = **451** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=NPSHYD|generation` = **419** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=OTHER|generation` = **248** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=PS|generation` = **276** (n=920, 2026-09-18T04:10:23.202160Z)
- `FUELINST|fuelType=WIND|generation` = **13827** (n=920, 2026-09-18T04:10:23.202160Z)
- `IMBALNGC|TOTAL|imbalance` = **10690** (n=152, 2026-09-18T03:51:20.747341Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=152, 2026-09-18T03:51:20.747341Z)
- `INDGEN|TOTAL|generation` = **27504** (n=152, 2026-09-18T03:51:20.747341Z)
- `MELNGC|TOTAL|margin` = **38174** (n=152, 2026-09-18T03:49:58.549270Z)
- `NDF|TOTAL|demand` = **16314** (n=155, 2026-09-18T03:48:12.841517Z)
- `TSDF|TOTAL|demand` = **16814** (n=155, 2026-09-18T03:47:55.952290Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T04:14:05.837849Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:14:04.071792Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:14:02.289288Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:59.804033Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:58.241405Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:56.682308Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:55.052946Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:53.462814Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:51.868613Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:50.315755Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:48.668571Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:47.065687Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:45.517636Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:42.478348Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:13:40.903188Z` — **MID**: 0 rows; marker `2026-09-18T04:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
