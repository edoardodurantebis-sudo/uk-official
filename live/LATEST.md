# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T23:13:49.012375Z`  
Current process started UTC: `2026-09-18T23:09:48.363634Z`  
1-second metadata polls in this process: **174**  
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

- `FUELINST|fuelType=INTVKL|generation` = **747** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=NPSHYD|generation` = **429** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=OTHER|generation` = **1093** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=PS|generation` = **-420** (n=1104, 2026-09-18T23:10:20.739641Z)
- `FUELINST|fuelType=WIND|generation` = **15821** (n=1104, 2026-09-18T23:10:20.739641Z)
- `IMBALNGC|TOTAL|imbalance` = **8975** (n=182, 2026-09-18T22:53:01.694251Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=182, 2026-09-18T22:53:01.694251Z)
- `INDGEN|TOTAL|generation` = **26170** (n=182, 2026-09-18T22:53:01.694251Z)
- `MELNGC|TOTAL|margin` = **37610** (n=182, 2026-09-18T22:50:10.642009Z)
- `NDF|TOTAL|demand` = **16550** (n=186, 2026-09-18T22:48:26.880797Z)
- `TSDF|TOTAL|demand` = **17194** (n=186, 2026-09-18T22:48:26.880797Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T23:13:47.696009Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:46.365786Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:45.057459Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:43.754680Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:42.432320Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:41.087506Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:39.786463Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:38.147830Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:36.798098Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:35.453928Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:34.149909Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:32.863821Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:31.594171Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:30.282074Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:13:28.962442Z` — **MID**: 0 rows; marker `2026-09-18T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
