# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T06:07:33.048300Z`  
Current process started UTC: `2026-09-18T06:03:32.275530Z`  
1-second metadata polls in this process: **221**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1306** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=NPSHYD|generation` = **459** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3342** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=OTHER|generation` = **636** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=PS|generation` = **527** (n=943, 2026-09-18T06:05:40.404525Z)
- `FUELINST|fuelType=WIND|generation` = **14322** (n=943, 2026-09-18T06:05:40.404525Z)
- `IMBALNGC|TOTAL|imbalance` = **10719** (n=156, 2026-09-18T05:50:16.495445Z)
- `INDDEM|TOTAL|demand` = **-11168** (n=156, 2026-09-18T05:50:16.495445Z)
- `INDGEN|TOTAL|generation` = **27533** (n=156, 2026-09-18T05:50:16.495445Z)
- `MELNGC|TOTAL|margin` = **38005** (n=156, 2026-09-18T05:49:12.578437Z)
- `NDF|TOTAL|demand` = **16314** (n=159, 2026-09-18T05:47:34.288045Z)
- `TSDF|TOTAL|demand` = **16814** (n=159, 2026-09-18T05:47:18.405461Z)
- `WINDFOR|TOTAL|generation` = **7773** (n=27, 2026-09-18T05:30:55.204522Z)

## Latest publication events

- `2026-09-18T06:07:32.065097Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:31.065024Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:30.064958Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:29.064883Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:28.064785Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:27.064679Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:26.064610Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:25.058804Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:24.058707Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:23.058600Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:22.058525Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:21.058430Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:20.058318Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:19.058247Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T06:07:18.058111Z` — **MID**: 0 rows; marker `2026-09-18T06:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
