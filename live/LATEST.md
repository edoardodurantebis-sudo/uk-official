# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T15:37:58.641008Z`  
Current process started UTC: `2026-09-18T15:33:57.008876Z`  
1-second metadata polls in this process: **130**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1051** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=NPSHYD|generation` = **344** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3334** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=OTHER|generation` = **160** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=PS|generation` = **226** (n=1057, 2026-09-18T15:35:33.701596Z)
- `FUELINST|fuelType=WIND|generation` = **16703** (n=1057, 2026-09-18T15:35:33.701596Z)
- `IMBALNGC|TOTAL|imbalance` = **8521** (n=174, 2026-09-18T15:23:28.385039Z)
- `INDDEM|TOTAL|demand` = **-10767** (n=174, 2026-09-18T15:23:10.555240Z)
- `INDGEN|TOTAL|generation` = **25571** (n=174, 2026-09-18T15:23:28.385039Z)
- `MELNGC|TOTAL|margin` = **38024** (n=174, 2026-09-18T15:20:56.613821Z)
- `NDF|TOTAL|demand` = **16550** (n=178, 2026-09-18T15:18:18.353381Z)
- `TSDF|TOTAL|demand` = **17050** (n=178, 2026-09-18T15:18:18.353381Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T15:37:56.893235Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:55.118662Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:53.424694Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:51.718478Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:49.980336Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:47.499660Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:45.773033Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:44.072152Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:42.383439Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:40.671651Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:38.977825Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:37.277651Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:35.531271Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:33.528218Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T15:37:31.171656Z` — **MID**: 0 rows; marker `2026-09-18T15:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
