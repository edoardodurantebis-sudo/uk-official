# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T19:31:37.695721Z`  
Current process started UTC: `2026-09-17T19:27:37.373948Z`  
1-second metadata polls in this process: **186**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=79, delta=-2, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=81, delta=-2, z=4.34 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=82, delta=45, z=5.06 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1407** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=NPSHYD|generation` = **633** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=OCGT|generation` = **118** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=OTHER|generation` = **621** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=PS|generation` = **427** (n=816, 2026-09-17T19:30:38.284217Z)
- `FUELINST|fuelType=WIND|generation` = **15583** (n=816, 2026-09-17T19:30:38.284217Z)
- `IMBALNGC|TOTAL|imbalance` = **9684** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDDEM|TOTAL|demand` = **-11160** (n=135, 2026-09-17T19:23:43.864314Z)
- `INDGEN|TOTAL|generation` = **26498** (n=135, 2026-09-17T19:23:43.864314Z)
- `MELNGC|TOTAL|margin` = **36493** (n=135, 2026-09-17T19:20:53.732823Z)
- `NDF|TOTAL|demand` = **16314** (n=138, 2026-09-17T19:18:38.940808Z)
- `TSDF|TOTAL|demand` = **16814** (n=138, 2026-09-17T19:18:38.940808Z)
- `WINDFOR|TOTAL|generation` = **18713** (n=24, 2026-09-17T19:30:38.284217Z)

## Latest publication events

- `2026-09-17T19:31:36.432642Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:35.219574Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:34.047996Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:32.800380Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:31.587100Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:30.361699Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:28.647209Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:27.403740Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:26.172520Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:24.907157Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:23.635230Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:22.417668Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:21.215397Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:19.985446Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T19:31:18.756245Z` — **MID**: 0 rows; marker `2026-09-17T19:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
