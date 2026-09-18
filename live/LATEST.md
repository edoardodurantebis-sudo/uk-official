# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T02:45:46.192799Z`  
Current process started UTC: `2026-09-18T02:41:44.630857Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **976** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=NPSHYD|generation` = **404** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3330** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=OTHER|generation` = **370** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=PS|generation` = **434** (n=903, 2026-09-18T02:45:29.457686Z)
- `FUELINST|fuelType=WIND|generation` = **14013** (n=903, 2026-09-18T02:45:29.457686Z)
- `IMBALNGC|TOTAL|imbalance` = **10176** (n=149, 2026-09-18T02:21:02.468684Z)
- `INDDEM|TOTAL|demand` = **-11204** (n=149, 2026-09-18T02:20:46.650594Z)
- `INDGEN|TOTAL|generation` = **26990** (n=149, 2026-09-18T02:21:02.468684Z)
- `MELNGC|TOTAL|margin` = **38212** (n=149, 2026-09-18T02:19:51.484596Z)
- `NDF|TOTAL|demand` = **16314** (n=152, 2026-09-18T02:17:25.911508Z)
- `TSDF|TOTAL|demand` = **16814** (n=152, 2026-09-18T02:17:25.911508Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T02:45:44.498123Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:42.751851Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:41.045142Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:39.284966Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:37.576205Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:35.880207Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:34.178585Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:32.475512Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:29.457686Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:29.457686Z` — **FUELINST**: 80 rows; marker `2026-09-18T02:45:00Z`
- `2026-09-18T02:45:27.563761Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:25.861434Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:24.002763Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:22.307661Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:45:20.565204Z` — **MID**: 0 rows; marker `2026-09-18T02:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
