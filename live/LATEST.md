# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:25:51.268387Z`  
Current process started UTC: `2026-09-19T05:21:50.945894Z`  
1-second metadata polls in this process: **178**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-454** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=NPSHYD|generation` = **351** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=OTHER|generation` = **461** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=PS|generation` = **-542** (n=1179, 2026-09-19T05:25:34.940229Z)
- `FUELINST|fuelType=WIND|generation` = **15856** (n=1179, 2026-09-19T05:25:34.940229Z)
- `IMBALNGC|TOTAL|imbalance` = **9712** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDDEM|TOTAL|demand` = **-10865** (n=195, 2026-09-19T05:21:11.032937Z)
- `INDGEN|TOTAL|generation` = **26901** (n=195, 2026-09-19T05:21:11.032937Z)
- `MELNGC|TOTAL|margin` = **38254** (n=195, 2026-09-19T05:19:51.225658Z)
- `NDF|TOTAL|demand` = **16550** (n=199, 2026-09-19T05:17:24.210800Z)
- `TSDF|TOTAL|demand` = **17190** (n=199, 2026-09-19T05:17:24.210800Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T05:25:49.980806Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:48.664024Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:47.424267Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:46.161413Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:44.882827Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:43.580613Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:42.289114Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:40.996688Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:39.707244Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:38.458266Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:37.163771Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:34.940229Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:34.940229Z` — **FUELINST**: 80 rows; marker `2026-09-19T05:25:00Z`
- `2026-09-19T05:25:33.653599Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:25:32.389279Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
