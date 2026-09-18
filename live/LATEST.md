# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T03:36:24.271303Z`  
Current process started UTC: `2026-09-18T03:32:22.882922Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **990** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=NPSHYD|generation` = **404** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=OTHER|generation` = **167** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=PS|generation` = **180** (n=913, 2026-09-18T03:35:42.575618Z)
- `FUELINST|fuelType=WIND|generation` = **13759** (n=913, 2026-09-18T03:35:42.575618Z)
- `IMBALNGC|TOTAL|imbalance` = **10169** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDDEM|TOTAL|demand` = **-11249** (n=151, 2026-09-18T03:21:23.504107Z)
- `INDGEN|TOTAL|generation` = **26983** (n=151, 2026-09-18T03:21:23.504107Z)
- `MELNGC|TOTAL|margin` = **38166** (n=151, 2026-09-18T03:19:45.452751Z)
- `NDF|TOTAL|demand` = **16314** (n=154, 2026-09-18T03:17:28.449836Z)
- `TSDF|TOTAL|demand` = **16814** (n=154, 2026-09-18T03:17:28.449836Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T03:36:22.626889Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:21.006743Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:19.370588Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:16.087833Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:16.087833Z` — **FREQ**: 5761 rows; marker `2026-09-18T03:35:45Z`
- `2026-09-18T03:36:14.285453Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:12.557035Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:10.894727Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:08.992776Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:07.211912Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:05.556360Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:03.766769Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:36:01.923830Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:35:59.630258Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T03:35:58.054072Z` — **MID**: 0 rows; marker `2026-09-18T03:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
