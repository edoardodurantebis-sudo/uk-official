# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T09:51:41.501637Z`  
Current process started UTC: `2026-09-18T09:47:40.788675Z`  
1-second metadata polls in this process: **125**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=NPSHYD|generation` = **345** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=OTHER|generation` = **938** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=PS|generation` = **-454** (n=988, 2026-09-18T09:50:42.979882Z)
- `FUELINST|fuelType=WIND|generation` = **11826** (n=988, 2026-09-18T09:50:42.979882Z)
- `IMBALNGC|TOTAL|imbalance` = **7801** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDDEM|TOTAL|demand` = **-13189** (n=163, 2026-09-18T09:49:53.694216Z)
- `INDGEN|TOTAL|generation` = **26894** (n=163, 2026-09-18T09:49:53.694216Z)
- `MELNGC|TOTAL|margin` = **36164** (n=163, 2026-09-18T09:49:19.963149Z)
- `NDF|TOTAL|demand` = **16454** (n=167, 2026-09-18T09:47:20.937653Z)
- `TSDF|TOTAL|demand` = **19093** (n=167, 2026-09-18T09:47:20.937653Z)
- `WINDFOR|TOTAL|generation` = **7699** (n=28, 2026-09-18T08:30:36.379150Z)

## Latest publication events

- `2026-09-18T09:51:39.777073Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:38.072941Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:36.341478Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:34.622452Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:32.045322Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:30.319675Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:28.605592Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:26.858138Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:25.099979Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:23.392030Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:21.688017Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:19.970173Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:18.273378Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:16.193255Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T09:51:14.472448Z` — **MID**: 0 rows; marker `2026-09-18T09:42:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
