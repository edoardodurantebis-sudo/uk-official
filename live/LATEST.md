# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T02:41:32.657583Z`  
Current process started UTC: `2026-09-18T02:37:32.597852Z`  
1-second metadata polls in this process: **230**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=0, z=4.12 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **976** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=NPSHYD|generation` = **406** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=OTHER|generation` = **517** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=PS|generation` = **296** (n=902, 2026-09-18T02:40:29.719197Z)
- `FUELINST|fuelType=WIND|generation` = **14006** (n=902, 2026-09-18T02:40:29.719197Z)
- `IMBALNGC|TOTAL|imbalance` = **10176** (n=149, 2026-09-18T02:21:02.468684Z)
- `INDDEM|TOTAL|demand` = **-11204** (n=149, 2026-09-18T02:20:46.650594Z)
- `INDGEN|TOTAL|generation` = **26990** (n=149, 2026-09-18T02:21:02.468684Z)
- `MELNGC|TOTAL|margin` = **38212** (n=149, 2026-09-18T02:19:51.484596Z)
- `NDF|TOTAL|demand` = **16314** (n=152, 2026-09-18T02:17:25.911508Z)
- `TSDF|TOTAL|demand` = **16814** (n=152, 2026-09-18T02:17:25.911508Z)
- `WINDFOR|TOTAL|generation` = **18868** (n=25, 2026-09-17T23:30:47.122302Z)

## Latest publication events

- `2026-09-18T02:41:31.590183Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:30.590077Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:29.556794Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:28.556718Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:27.556596Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:26.556483Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:25.556358Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:24.556283Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:23.556147Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:22.556029Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:21.555917Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:20.368126Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:19.367997Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:17.593577Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T02:41:16.593457Z` — **MID**: 0 rows; marker `2026-09-18T02:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
