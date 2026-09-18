# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T23:44:07.146910Z`  
Current process started UTC: `2026-09-18T23:40:06.155506Z`  
1-second metadata polls in this process: **133**  
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

- `FUELINST|fuelType=INTVKL|generation` = **747** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=NPSHYD|generation` = **428** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3341** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=OTHER|generation` = **866** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=PS|generation` = **-422** (n=1110, 2026-09-18T23:40:38.037975Z)
- `FUELINST|fuelType=WIND|generation` = **15744** (n=1110, 2026-09-18T23:40:38.037975Z)
- `IMBALNGC|TOTAL|imbalance` = **9193** (n=183, 2026-09-18T23:24:12.299291Z)
- `INDDEM|TOTAL|demand` = **-10889** (n=183, 2026-09-18T23:23:56.569934Z)
- `INDGEN|TOTAL|generation` = **26388** (n=183, 2026-09-18T23:23:56.569934Z)
- `MELNGC|TOTAL|margin` = **37541** (n=183, 2026-09-18T23:22:33.697837Z)
- `NDF|TOTAL|demand` = **16550** (n=187, 2026-09-18T23:19:40.000667Z)
- `TSDF|TOTAL|demand` = **17194** (n=187, 2026-09-18T23:19:40.000667Z)
- `WINDFOR|TOTAL|generation` = **7462** (n=32, 2026-09-18T23:30:39.396995Z)

## Latest publication events

- `2026-09-18T23:44:05.431874Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:44:03.697939Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:44:01.910748Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:44:00.192393Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:58.458832Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:56.772070Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:54.996698Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:53.311519Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:51.288988Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:49.577877Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:47.832950Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:46.093035Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:44.380286Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:42.671032Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T23:43:40.962061Z` — **MID**: 0 rows; marker `2026-09-18T23:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
