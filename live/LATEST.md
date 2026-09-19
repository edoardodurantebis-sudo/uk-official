# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T06:16:23.238379Z`  
Current process started UTC: `2026-09-19T06:12:21.897386Z`  
1-second metadata polls in this process: **145**  
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

- `FUELINST|fuelType=INTVKL|generation` = **357** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=OTHER|generation` = **352** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=PS|generation` = **-542** (n=1189, 2026-09-19T06:15:35.677847Z)
- `FUELINST|fuelType=WIND|generation` = **15861** (n=1189, 2026-09-19T06:15:35.677847Z)
- `IMBALNGC|TOTAL|imbalance` = **9697** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=196, 2026-09-19T05:50:34.942583Z)
- `INDGEN|TOTAL|generation` = **26887** (n=196, 2026-09-19T05:50:50.449260Z)
- `MELNGC|TOTAL|margin` = **38235** (n=196, 2026-09-19T05:49:46.009897Z)
- `NDF|TOTAL|demand` = **16550** (n=200, 2026-09-19T05:47:37.564895Z)
- `TSDF|TOTAL|demand` = **17190** (n=200, 2026-09-19T05:47:37.564895Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T06:16:21.494162Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:19.564897Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:17.754094Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:15.925733Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:14.368474Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:12.609821Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:11.043804Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:09.494352Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:07.241323Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:05.154127Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:03.124753Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:16:01.556016Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:15:59.908739Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:15:58.345549Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T06:15:56.780644Z` — **MID**: 0 rows; marker `2026-09-19T06:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
