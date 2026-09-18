# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:45:26.515523Z`  
Current process started UTC: `2026-09-18T06:41:25.514015Z`  
1-second metadata polls in this process: **132**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=NPSHYD|generation` = **409** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=OTHER|generation` = **1339** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=PS|generation` = **675** (n=950, 2026-09-18T06:40:29.285154Z)
- `FUELINST|fuelType=WIND|generation` = **14425** (n=950, 2026-09-18T06:40:29.285154Z)
- `IMBALNGC|TOTAL|imbalance` = **10652** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=157, 2026-09-18T06:20:37.859791Z)
- `INDGEN|TOTAL|generation` = **27466** (n=157, 2026-09-18T06:20:37.859791Z)
- `MELNGC|TOTAL|margin` = **37963** (n=157, 2026-09-18T06:19:23.801804Z)
- `NDF|TOTAL|demand` = **16314** (n=160, 2026-09-18T06:17:14.273486Z)
- `TSDF|TOTAL|demand` = **16814** (n=160, 2026-09-18T06:17:14.273486Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:45:24.802678Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:23.030985Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:21.311178Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:19.607816Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:17.890270Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:16.191840Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:14.439347Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:11.781209Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:10.074025Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:08.359821Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:06.658528Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:04.910391Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:03.177867Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:45:01.441675Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:44:59.679100Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
