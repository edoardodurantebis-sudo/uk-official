# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T09:21:22.242688Z`  
Current process started UTC: `2026-09-19T09:17:21.692479Z`  
1-second metadata polls in this process: **226**  
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

- `FUELINST|fuelType=INTVKL|generation` = **560** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=NPSHYD|generation` = **331** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=OTHER|generation` = **523** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=PS|generation` = **-422** (n=1226, 2026-09-19T09:20:32.965390Z)
- `FUELINST|fuelType=WIND|generation` = **15000** (n=1226, 2026-09-19T09:20:32.965390Z)
- `IMBALNGC|TOTAL|imbalance` = **7771** (n=202, 2026-09-19T09:19:44.569379Z)
- `INDDEM|TOTAL|demand` = **-13216** (n=202, 2026-09-19T09:19:44.569379Z)
- `INDGEN|TOTAL|generation` = **26702** (n=202, 2026-09-19T09:19:44.569379Z)
- `MELNGC|TOTAL|margin` = **36478** (n=202, 2026-09-19T09:18:55.905783Z)
- `NDF|TOTAL|demand` = **15940** (n=207, 2026-09-19T09:17:21.692487Z)
- `TSDF|TOTAL|demand` = **18932** (n=207, 2026-09-19T09:17:21.692487Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T09:21:20.780688Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:19.780574Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:18.780458Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:17.780378Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:16.780269Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:15.780146Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:14.780022Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:13.779953Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:12.775909Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:11.775797Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:10.775684Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:09.775571Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:08.775450Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:07.638014Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T09:21:06.637909Z` — **MID**: 0 rows; marker `2026-09-19T09:12:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
