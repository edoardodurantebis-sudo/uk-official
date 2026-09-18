# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T04:01:30.506439Z`  
Current process started UTC: `2026-09-18T03:57:29.841346Z`  
1-second metadata polls in this process: **188**  
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

- `FUELINST|fuelType=INTVKL|generation` = **861** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=NPSHYD|generation` = **404** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=OTHER|generation` = **122** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=PS|generation` = **227** (n=918, 2026-09-18T04:00:25.411374Z)
- `FUELINST|fuelType=WIND|generation` = **13791** (n=918, 2026-09-18T04:00:25.411374Z)
- `IMBALNGC|TOTAL|imbalance` = **10690** (n=152, 2026-09-18T03:51:20.747341Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=152, 2026-09-18T03:51:20.747341Z)
- `INDGEN|TOTAL|generation` = **27504** (n=152, 2026-09-18T03:51:20.747341Z)
- `MELNGC|TOTAL|margin` = **38174** (n=152, 2026-09-18T03:49:58.549270Z)
- `NDF|TOTAL|demand` = **16314** (n=155, 2026-09-18T03:48:12.841517Z)
- `TSDF|TOTAL|demand` = **16814** (n=155, 2026-09-18T03:47:55.952290Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T04:01:28.823201Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:27.426119Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:26.264287Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:25.048646Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:23.884272Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:22.683384Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:21.492177Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:19.917572Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:18.173039Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:16.518776Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:14.552628Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:12.945163Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:11.757630Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:10.597543Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T04:01:09.151835Z` — **MID**: 0 rows; marker `2026-09-18T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
