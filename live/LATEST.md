# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T11:24:42.201686Z`  
Current process started UTC: `2026-09-19T11:20:40.864558Z`  
1-second metadata polls in this process: **146**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **INDGEN** `TOTAL` `generation` — indicated generation [TOTAL] generation: value=16752, delta=-9313, z=-3.94 -> state changed
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

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **333** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=NPSHYD|generation` = **307** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=OTHER|generation` = **536** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=PS|generation` = **-935** (n=1250, 2026-09-19T11:20:40.864567Z)
- `FUELINST|fuelType=WIND|generation` = **15694** (n=1250, 2026-09-19T11:20:40.864567Z)
- `IMBALNGC|TOTAL|imbalance` = **-3378** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDDEM|TOTAL|demand` = **-11780** (n=205, 2026-09-19T10:55:05.891910Z)
- `INDGEN|TOTAL|generation` = **16752** (n=205, 2026-09-19T10:55:05.891910Z)
- `MELNGC|TOTAL|margin` = **36659** (n=206, 2026-09-19T11:21:14.136124Z)
- `NDF|TOTAL|demand` = **19631** (n=211, 2026-09-19T11:18:50.597516Z)
- `TSDF|TOTAL|demand` = **20131** (n=211, 2026-09-19T11:18:50.597516Z)
- `WINDFOR|TOTAL|generation` = **6656** (n=36, 2026-09-19T10:30:47.910212Z)

## Latest publication events

- `2026-09-19T11:24:40.646340Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:39.107273Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:37.573749Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:36.008126Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:34.409471Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:32.892367Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:31.334750Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:28.442701Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:26.880989Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:25.347720Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:23.792897Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:22.279372Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:20.730459Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:19.188364Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T11:24:17.610738Z` — **MID**: 0 rows; marker `2026-09-19T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
