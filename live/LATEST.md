# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:37:47.235834Z`  
Current process started UTC: `2026-09-18T18:33:46.008930Z`  
1-second metadata polls in this process: **172**  
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

- `FUELINST|fuelType=INTVKL|generation` = **939** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=NPSHYD|generation` = **497** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=OCGT|generation` = **5** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=OTHER|generation` = **1591** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=PS|generation` = **403** (n=1070, 2026-09-18T18:35:42.366865Z)
- `FUELINST|fuelType=WIND|generation` = **16966** (n=1070, 2026-09-18T18:35:42.366865Z)
- `IMBALNGC|TOTAL|imbalance` = **9176** (n=176, 2026-09-18T18:24:19.444583Z)
- `INDDEM|TOTAL|demand` = **-10736** (n=176, 2026-09-18T18:24:03.813466Z)
- `INDGEN|TOTAL|generation` = **26226** (n=176, 2026-09-18T18:24:03.813466Z)
- `MELNGC|TOTAL|margin` = **37767** (n=176, 2026-09-18T18:21:20.209125Z)
- `NDF|TOTAL|demand` = **16550** (n=180, 2026-09-18T18:18:44.073570Z)
- `TSDF|TOTAL|demand` = **17050** (n=180, 2026-09-18T18:18:44.073570Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:37:45.853531Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:44.508441Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:43.130727Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:41.855110Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:40.539360Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:39.213372Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:37.293733Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:36.018899Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:34.711153Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:33.376731Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:32.040832Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:30.710447Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:29.402532Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:28.083477Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:37:26.756708Z` — **MID**: 0 rows; marker `2026-09-18T18:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
