# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T10:04:17.310111Z`  
Current process started UTC: `2026-09-18T10:00:16.941317Z`  
1-second metadata polls in this process: **217**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=NPSHYD|generation` = **340** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=OTHER|generation` = **927** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=PS|generation` = **-490** (n=990, 2026-09-18T10:00:36.369604Z)
- `FUELINST|fuelType=WIND|generation` = **11776** (n=990, 2026-09-18T10:00:36.369604Z)
- `IMBALNGC|TOTAL|imbalance` = **7801** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDDEM|TOTAL|demand` = **-13189** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDGEN|TOTAL|generation` = **26894** (n=163, 2026-09-18T09:49:53.694216Z)
- `MELNGC|TOTAL|margin` = **36164** (n=163, 2026-09-18T09:49:19.963149Z)
- `NDF|TOTAL|demand` = **16454** (n=167, 2026-09-18T09:47:20.937653Z)
- `TSDF|TOTAL|demand` = **19093** (n=167, 2026-09-18T09:47:20.937653Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T10:04:16.297873Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:15.297748Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:14.297624Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:13.297496Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:12.297365Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:11.297218Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:10.297061Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:07.989165Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:07.989165Z` — **FREQ**: 5761 rows; marker `2026-09-18T10:03:45Z`
- `2026-09-18T10:04:06.748909Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:05.466958Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:04.466807Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:03.466729Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:02.466641Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T10:04:01.466558Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
