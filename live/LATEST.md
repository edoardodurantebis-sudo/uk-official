# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:02:14.068432Z`  
Current process started UTC: `2026-09-18T06:58:11.845318Z`  
1-second metadata polls in this process: **218**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=NPSHYD|generation` = **411** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=OTHER|generation` = **1764** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=PS|generation` = **884** (n=954, 2026-09-18T07:00:19.328321Z)
- `FUELINST|fuelType=WIND|generation` = **13543** (n=954, 2026-09-18T07:00:19.328321Z)
- `IMBALNGC|TOTAL|imbalance` = **10565** (n=158, 2026-09-18T06:50:20.667031Z)
- `INDDEM|TOTAL|demand` = **-11405** (n=158, 2026-09-18T06:50:04.574079Z)
- `INDGEN|TOTAL|generation` = **27379** (n=158, 2026-09-18T06:50:04.574079Z)
- `MELNGC|TOTAL|margin` = **37954** (n=158, 2026-09-18T06:49:07.667660Z)
- `NDF|TOTAL|demand` = **16314** (n=161, 2026-09-18T06:47:15.091718Z)
- `TSDF|TOTAL|demand` = **16814** (n=161, 2026-09-18T06:47:15.091718Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:02:11.724450Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:11.724450Z` — **FREQ**: 5761 rows; marker `2026-09-18T07:01:45Z`
- `2026-09-18T07:02:10.676853Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:09.652787Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:08.616734Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:07.550156Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:06.416636Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:05.391900Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:04.334981Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:03.294497Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:02.218073Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:02:01.088401Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:01:59.979263Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:01:58.960053Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:01:57.926916Z` — **MID**: 0 rows; marker `2026-09-18T06:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
