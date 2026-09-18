# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T22:48:39.629632Z`  
Current process started UTC: `2026-09-18T22:44:38.861469Z`  
1-second metadata polls in this process: **187**  
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

- `FUELINST|fuelType=INTVKL|generation` = **443** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=NPSHYD|generation` = **444** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=OTHER|generation` = **1367** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=PS|generation` = **-708** (n=1099, 2026-09-18T22:45:43.127177Z)
- `FUELINST|fuelType=WIND|generation` = **15904** (n=1099, 2026-09-18T22:45:43.127177Z)
- `IMBALNGC|TOTAL|imbalance` = **8984** (n=181, 2026-09-18T22:23:06.697614Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=181, 2026-09-18T22:22:50.501799Z)
- `INDGEN|TOTAL|generation` = **26179** (n=181, 2026-09-18T22:23:06.697614Z)
- `MELNGC|TOTAL|margin` = **37591** (n=181, 2026-09-18T22:20:41.960616Z)
- `NDF|TOTAL|demand` = **16550** (n=186, 2026-09-18T22:48:26.880797Z)
- `TSDF|TOTAL|demand` = **17194** (n=186, 2026-09-18T22:48:26.880797Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T22:48:38.431964Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:36.890448Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:35.707658Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:34.531831Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:33.337632Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:32.130375Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:30.934127Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:26.880797Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:26.880797Z` — **TSDF**: 1044 rows; marker `2026-09-18T22:47:00Z`
- `2026-09-18T22:48:26.880797Z` — **NDF**: 58 rows; marker `2026-09-18T22:47:00Z`
- `2026-09-18T22:48:26.880797Z` — **FREQ**: 5761 rows; marker `2026-09-18T22:47:45Z`
- `2026-09-18T22:48:25.680133Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:24.484316Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:23.273542Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T22:48:22.083153Z` — **MID**: 0 rows; marker `2026-09-18T22:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
