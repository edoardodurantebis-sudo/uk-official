# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:34:16.822795Z`  
Current process started UTC: `2026-09-19T05:30:16.439963Z`  
1-second metadata polls in this process: **162**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=NPSHYD|generation` = **352** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=OTHER|generation` = **575** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=PS|generation` = **-541** (n=1180, 2026-09-19T05:30:34.205766Z)
- `FUELINST|fuelType=WIND|generation` = **15834** (n=1180, 2026-09-19T05:30:34.205766Z)
- `IMBALNGC|TOTAL|imbalance` = **9712** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDGEN|TOTAL|generation` = **26901** (n=195, 2026-09-19T05:21:11.032937Z)
- `MELNGC|TOTAL|margin` = **38254** (n=195, 2026-09-19T05:19:51.225658Z)
- `NDF|TOTAL|demand` = **16550** (n=199, 2026-09-19T05:17:24.210800Z)
- `TSDF|TOTAL|demand` = **17190** (n=199, 2026-09-19T05:17:24.210800Z)
- `WINDFOR|TOTAL|generation` = **6872** (n=34, 2026-09-19T05:30:34.205766Z)

## Latest publication events

- `2026-09-19T05:34:15.530658Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:14.254117Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:12.919030Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:11.624289Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:10.326094Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:09.005091Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:07.702502Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:05.983660Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:04.683679Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:03.327673Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:02.030013Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:34:00.735039Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:33:59.420806Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:33:58.092270Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:33:56.802014Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
