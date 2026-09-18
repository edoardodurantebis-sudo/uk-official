# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T05:08:39.340226Z`  
Current process started UTC: `2026-09-18T05:04:38.413765Z`  
1-second metadata polls in this process: **152**  
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

- `FUELINST|fuelType=INTVKL|generation` = **824** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=NPSHYD|generation` = **468** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=OTHER|generation` = **378** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=PS|generation` = **512** (n=931, 2026-09-18T05:05:35.237114Z)
- `FUELINST|fuelType=WIND|generation` = **13525** (n=931, 2026-09-18T05:05:35.237114Z)
- `IMBALNGC|TOTAL|imbalance` = **10765** (n=154, 2026-09-18T04:50:56.245036Z)
- `INDDEM|TOTAL|demand` = **-11169** (n=154, 2026-09-18T04:50:38.189613Z)
- `INDGEN|TOTAL|generation` = **27579** (n=154, 2026-09-18T04:50:56.245036Z)
- `MELNGC|TOTAL|margin` = **38056** (n=154, 2026-09-18T04:49:35.020770Z)
- `NDF|TOTAL|demand` = **16314** (n=157, 2026-09-18T04:47:22.036502Z)
- `TSDF|TOTAL|demand` = **16814** (n=157, 2026-09-18T04:47:22.036502Z)
- `WINDFOR|TOTAL|generation` = **7845** (n=26, 2026-09-18T03:30:37.036559Z)

## Latest publication events

- `2026-09-18T05:08:38.025209Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:36.684756Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:35.383048Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:34.089729Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:32.371804Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:31.042959Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:29.726519Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:28.351139Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:27.047312Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:25.737122Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:24.412169Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:23.120632Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:21.802642Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:20.496034Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T05:08:19.153383Z` — **MID**: 0 rows; marker `2026-09-18T05:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
