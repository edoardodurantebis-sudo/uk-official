# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T08:56:10.915893Z`  
Current process started UTC: `2026-09-19T08:52:10.666517Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDDEM** `TOTAL` `demand` — indicated demand [TOTAL] demand: value=-10744, delta=3052, z=1.92 -> demand pressure up
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **910** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=NPSHYD|generation` = **352** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=OTHER|generation` = **363** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=PS|generation` = **-697** (n=1221, 2026-09-19T08:55:39.581718Z)
- `FUELINST|fuelType=WIND|generation` = **15141** (n=1221, 2026-09-19T08:55:39.581718Z)
- `IMBALNGC|TOTAL|imbalance` = **8932** (n=201, 2026-09-19T08:50:08.297112Z)
- `INDDEM|TOTAL|demand` = **-12086** (n=201, 2026-09-19T08:50:08.297112Z)
- `INDGEN|TOTAL|generation` = **26734** (n=201, 2026-09-19T08:50:08.297112Z)
- `MELNGC|TOTAL|margin` = **37592** (n=201, 2026-09-19T08:49:20.449715Z)
- `NDF|TOTAL|demand` = **15940** (n=206, 2026-09-19T08:47:31.231970Z)
- `TSDF|TOTAL|demand` = **17802** (n=206, 2026-09-19T08:47:59.721944Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T08:56:09.950040Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:08.949929Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:07.945042Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:06.944931Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:05.944798Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:04.944686Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:03.944621Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:02.944488Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:01.944378Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:56:00.944261Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:55:59.944179Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:55:58.936593Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:55:57.936507Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:55:56.907420Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T08:55:55.501597Z` — **MID**: 0 rows; marker `2026-09-19T08:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
