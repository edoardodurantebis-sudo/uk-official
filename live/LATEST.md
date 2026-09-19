# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T03:48:59.006275Z`  
Current process started UTC: `2026-09-19T03:44:58.105535Z`  
1-second metadata polls in this process: **221**  
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

- `FUELINST|fuelType=INTVKL|generation` = **-487** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=NPSHYD|generation` = **334** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3346** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=OTHER|generation` = **425** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=PS|generation` = **-543** (n=1159, 2026-09-19T03:45:29.820769Z)
- `FUELINST|fuelType=WIND|generation` = **15722** (n=1159, 2026-09-19T03:45:29.820769Z)
- `IMBALNGC|TOTAL|imbalance` = **9422** (n=191, 2026-09-19T03:21:05.977521Z)
- `INDDEM|TOTAL|demand` = **-10881** (n=191, 2026-09-19T03:21:05.977521Z)
- `INDGEN|TOTAL|generation` = **26617** (n=191, 2026-09-19T03:21:05.977521Z)
- `MELNGC|TOTAL|margin` = **38308** (n=191, 2026-09-19T03:19:22.215712Z)
- `NDF|TOTAL|demand` = **16550** (n=196, 2026-09-19T03:47:06.305878Z)
- `TSDF|TOTAL|demand` = **17194** (n=196, 2026-09-19T03:47:40.778261Z)
- `WINDFOR|TOTAL|generation` = **6714** (n=33, 2026-09-19T03:30:33.519312Z)

## Latest publication events

- `2026-09-19T03:48:58.055272Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:57.055167Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:56.055088Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:55.054963Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:54.054852Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:53.054731Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:52.054651Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:51.054553Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:50.054429Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:49.054314Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:48.054202Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:47.054117Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:44.868460Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:43.868343Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T03:48:42.868208Z` — **MID**: 0 rows; marker `2026-09-19T03:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
