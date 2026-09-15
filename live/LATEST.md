# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T23:15:30.173099Z`  
Current process started UTC: `2026-09-15T23:11:30.421893Z`  
1-second metadata polls in this process: **236**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=2, delta=2, z=3.36 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=0, z=3.64 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=53, delta=-1, z=3.74 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.30 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=54, delta=-1, z=3.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.15 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.38 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.76 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=4.99 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=17, z=8.89 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.25 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.56 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=5.93 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=6.39 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **249** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=NPSHYD|generation` = **426** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3326** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=OTHER|generation` = **437** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=PS|generation` = **172** (n=315, 2026-09-15T23:10:29.671078Z)
- `FUELINST|fuelType=WIND|generation` = **10800** (n=315, 2026-09-15T23:10:29.671078Z)
- `IMBALNGC|TOTAL|imbalance` = **5801** (n=52, 2026-09-15T22:51:19.020642Z)
- `INDDEM|TOTAL|demand` = **-12081** (n=52, 2026-09-15T22:51:19.020642Z)
- `INDGEN|TOTAL|generation` = **24922** (n=52, 2026-09-15T22:51:19.020642Z)
- `MELNGC|TOTAL|margin` = **35740** (n=52, 2026-09-15T22:49:19.915312Z)
- `NDF|TOTAL|demand` = **18621** (n=53, 2026-09-15T22:47:44.804584Z)
- `TSDF|TOTAL|demand` = **19121** (n=53, 2026-09-15T22:47:44.804584Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T23:14:11.203596Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:13:45Z`
- `2026-09-15T23:12:18.428923Z` — **MID**: 0 rows; marker `2026-09-15T23:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T23:12:18.428923Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:11:45Z`
- `2026-09-15T23:10:29.671078Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:10:00Z`
- `2026-09-15T23:10:13.588575Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:09:45Z`
- `2026-09-15T23:08:21.113238Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:07:45Z`
- `2026-09-15T23:06:33.944806Z` — **MID**: 0 rows; marker `2026-09-15T23:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T23:06:33.944806Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:05:45Z`
- `2026-09-15T23:05:30.576182Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:05:00Z`
- `2026-09-15T23:04:10.591457Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:03:45Z`
- `2026-09-15T23:02:22.847297Z` — **FREQ**: 5761 rows; marker `2026-09-15T23:01:45Z`
- `2026-09-15T23:00:30.737417Z` — **FUELHH**: 20 rows; marker `2026-09-15T23:00:00Z`
- `2026-09-15T23:00:30.737417Z` — **FUELINST**: 80 rows; marker `2026-09-15T23:00:00Z`
- `2026-09-15T23:00:14.639724Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:59:45Z`
- `2026-09-15T22:58:14.901306Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:57:45Z`
