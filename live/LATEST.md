# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T07:23:09.702028Z`  
Current process started UTC: `2026-09-18T07:19:09.419939Z`  
1-second metadata polls in this process: **153**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1425** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=NPSHYD|generation` = **379** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=OTHER|generation` = **1711** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=PS|generation` = **601** (n=958, 2026-09-18T07:20:31.586820Z)
- `FUELINST|fuelType=WIND|generation` = **12612** (n=958, 2026-09-18T07:20:31.586820Z)
- `IMBALNGC|TOTAL|imbalance` = **10218** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDDEM|TOTAL|demand` = **-11739** (n=159, 2026-09-18T07:19:58.374346Z)
- `INDGEN|TOTAL|generation` = **27722** (n=159, 2026-09-18T07:19:58.374346Z)
- `MELNGC|TOTAL|margin` = **37765** (n=159, 2026-09-18T07:19:09.419948Z)
- `NDF|TOTAL|demand` = **16314** (n=162, 2026-09-18T07:17:24.178373Z)
- `TSDF|TOTAL|demand` = **17504** (n=162, 2026-09-18T07:17:24.178373Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T07:23:08.240807Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:23:06.740339Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:23:05.262158Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:23:03.794936Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:23:02.325133Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:23:00.736621Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:58.740133Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:57.286438Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:55.842904Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:54.379440Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:52.933183Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:51.469443Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:50.014858Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:48.560028Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T07:22:47.059995Z` — **MID**: 0 rows; marker `2026-09-18T07:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
