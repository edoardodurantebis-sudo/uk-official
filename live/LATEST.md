# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T14:42:37.912809Z`  
Current process started UTC: `2026-09-18T14:38:36.410161Z`  
1-second metadata polls in this process: **146**  
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

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=NPSHYD|generation` = **317** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=OTHER|generation` = **226** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=PS|generation` = **-470** (n=1046, 2026-09-18T14:40:30.135465Z)
- `FUELINST|fuelType=WIND|generation` = **16746** (n=1046, 2026-09-18T14:40:30.135465Z)
- `IMBALNGC|TOTAL|imbalance` = **8550** (n=172, 2026-09-18T14:24:33.593094Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=172, 2026-09-18T14:24:17.122424Z)
- `INDGEN|TOTAL|generation` = **25600** (n=172, 2026-09-18T14:24:17.122424Z)
- `MELNGC|TOTAL|margin` = **38296** (n=172, 2026-09-18T14:21:10.291729Z)
- `NDF|TOTAL|demand` = **16550** (n=176, 2026-09-18T14:18:53.718876Z)
- `TSDF|TOTAL|demand` = **17050** (n=176, 2026-09-18T14:18:53.718876Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T14:42:36.385958Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:34.774111Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:33.217363Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:31.652741Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:30.079603Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:28.546955Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:27.031741Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:24.919543Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:23.352329Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:21.817305Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:20.299711Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:18.709004Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:17.193616Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:15.674970Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T14:42:14.035114Z` — **MID**: 0 rows; marker `2026-09-18T14:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
