# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T19:53:59.382920Z`  
Current process started UTC: `2026-09-18T19:49:58.654647Z`  
1-second metadata polls in this process: **228**  
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

- `FUELINST|fuelType=INTVKL|generation` = **943** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=NPSHYD|generation` = **487** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3336** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=OTHER|generation` = **926** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=PS|generation` = **412** (n=1085, 2026-09-18T19:50:30.538560Z)
- `FUELINST|fuelType=WIND|generation` = **16820** (n=1085, 2026-09-18T19:50:30.538560Z)
- `IMBALNGC|TOTAL|imbalance` = **9049** (n=179, 2026-09-18T19:52:38.744964Z)
- `INDDEM|TOTAL|demand` = **-10891** (n=179, 2026-09-18T19:52:38.744964Z)
- `INDGEN|TOTAL|generation` = **26243** (n=179, 2026-09-18T19:52:38.744964Z)
- `MELNGC|TOTAL|margin` = **37531** (n=179, 2026-09-18T19:49:58.654655Z)
- `NDF|TOTAL|demand` = **16550** (n=183, 2026-09-18T19:47:55.702271Z)
- `TSDF|TOTAL|demand` = **17194** (n=183, 2026-09-18T19:47:55.702271Z)
- `WINDFOR|TOTAL|generation` = **7313** (n=31, 2026-09-18T19:30:50.210772Z)

## Latest publication events

- `2026-09-18T19:53:58.435139Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:57.435039Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:56.434923Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:55.434806Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:54.434724Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:53.434608Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:52.434491Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:51.434375Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:50.434259Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:49.434148Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:48.434037Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:47.433927Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:46.433812Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:45.433695Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T19:53:43.949420Z` — **MID**: 0 rows; marker `2026-09-18T19:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
