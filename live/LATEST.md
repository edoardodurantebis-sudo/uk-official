# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T05:30:03.156527Z`  
Current process started UTC: `2026-09-19T05:26:02.950334Z`  
1-second metadata polls in this process: **134**  
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

- `2026-09-19T05:30:00.842273Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:59.122815Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:57.426129Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:55.707663Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:54.002311Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:52.240870Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:50.513232Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:48.783304Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:47.073720Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:44.886533Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:43.178060Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:41.481270Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:39.778494Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:38.045248Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T05:29:36.321630Z` — **MID**: 0 rows; marker `2026-09-19T05:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
