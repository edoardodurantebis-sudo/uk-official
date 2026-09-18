# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T23:39:16.835599Z`  
Current process started UTC: `2026-09-18T23:35:16.300719Z`  
1-second metadata polls in this process: **136**  
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

- `FUELINST|fuelType=INTVKL|generation` = **747** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=NPSHYD|generation` = **429** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=OTHER|generation` = **954** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=PS|generation` = **-422** (n=1109, 2026-09-18T23:35:35.100301Z)
- `FUELINST|fuelType=WIND|generation` = **15740** (n=1109, 2026-09-18T23:35:35.100301Z)
- `IMBALNGC|TOTAL|imbalance` = **9193** (n=183, 2026-09-18T23:24:12.299291Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=183, 2026-09-18T23:23:56.569934Z)
- `INDGEN|TOTAL|generation` = **26388** (n=183, 2026-09-18T23:23:56.569934Z)
- `MELNGC|TOTAL|margin` = **37541** (n=183, 2026-09-18T23:22:33.697837Z)
- `NDF|TOTAL|demand` = **16550** (n=187, 2026-09-18T23:19:40.000667Z)
- `TSDF|TOTAL|demand` = **17194** (n=187, 2026-09-18T23:19:40.000667Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-18T23:39:15.133189Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:13.496467Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:11.866844Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:10.183430Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:08.513047Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:06.297632Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:04.607607Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:02.961862Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:39:01.311796Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:38:59.680641Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:38:58.022468Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:38:56.286238Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:38:54.611510Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:38:52.749412Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:38:50.526107Z` — **MID**: 0 rows; marker `2026-09-18T23:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
