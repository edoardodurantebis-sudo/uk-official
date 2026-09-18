# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T08:26:15.824215Z`  
Current process started UTC: `2026-09-18T08:22:15.099152Z`  
1-second metadata polls in this process: **170**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=NPSHYD|generation` = **376** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3337** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=OTHER|generation` = **1376** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=PS|generation` = **597** (n=971, 2026-09-18T08:25:32.808532Z)
- `FUELINST|fuelType=WIND|generation` = **12263** (n=971, 2026-09-18T08:25:32.808532Z)
- `IMBALNGC|TOTAL|imbalance` = **9625** (n=160, 2026-09-18T08:20:46.536994Z)
- `INDDEM|TOTAL|demand` = **-11736** (n=160, 2026-09-18T08:20:29.773738Z)
- `INDGEN|TOTAL|generation` = **27269** (n=160, 2026-09-18T08:20:29.773738Z)
- `MELNGC|TOTAL|margin` = **37653** (n=160, 2026-09-18T08:19:40.681819Z)
- `NDF|TOTAL|demand` = **16454** (n=164, 2026-09-18T08:17:38.545846Z)
- `TSDF|TOTAL|demand` = **17644** (n=164, 2026-09-18T08:17:38.545846Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T08:26:14.486616Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:13.177973Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:11.870318Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:10.531723Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:09.194627Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:07.856886Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:04.957248Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:03.626853Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:02.261560Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:26:00.953300Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:25:59.569505Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:25:58.248828Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:25:56.881248Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:25:55.481820Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T08:25:54.156974Z` — **MID**: 0 rows; marker `2026-09-18T08:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
