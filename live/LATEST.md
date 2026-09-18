# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:28:34.207060Z`  
Current process started UTC: `2026-09-18T06:24:32.971514Z`  
1-second metadata polls in this process: **156**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=NPSHYD|generation` = **421** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=OTHER|generation` = **1009** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=PS|generation` = **674** (n=947, 2026-09-18T06:25:39.532012Z)
- `FUELINST|fuelType=WIND|generation` = **14446** (n=947, 2026-09-18T06:25:39.532012Z)
- `IMBALNGC|TOTAL|imbalance` = **10652** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDGEN|TOTAL|generation` = **27466** (n=157, 2026-09-18T06:20:37.859791Z)
- `MELNGC|TOTAL|margin` = **37963** (n=157, 2026-09-18T06:19:23.801804Z)
- `NDF|TOTAL|demand` = **16314** (n=160, 2026-09-18T06:17:14.273486Z)
- `TSDF|TOTAL|demand` = **16814** (n=160, 2026-09-18T06:17:14.273486Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:28:32.714052Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:31.260174Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:29.797314Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:28.342607Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:26.886563Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:23.856190Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:23.856190Z` — **FREQ**: 5761 rows; marker `2026-09-18T06:27:45Z`
- `2026-09-18T06:28:22.405126Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:20.954821Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:19.523161Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:18.047071Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:16.606940Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:15.155931Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:13.689833Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:28:12.230041Z` — **MID**: 0 rows; marker `2026-09-18T06:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
