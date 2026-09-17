# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:20:04.895359Z`  
Current process started UTC: `2026-09-17T18:16:04.184998Z`  
1-second metadata polls in this process: **225**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=83, delta=-1, z=4.71 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=84, delta=7, z=4.84 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=77, delta=66, z=4.46 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=58, delta=2, z=3.72 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.78 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.52 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.55 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=52, delta=-3, z=3.67 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=4, z=3.58 -> generation-mix component moved
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=55, delta=-1, z=4.17 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=-2, z=3.82 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=0, z=4.01 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=58, delta=1, z=4.05 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=57, delta=1, z=4.02 -> generation-mix component moved
- **FUELINST** `fuelType=OCGT` `generation` — instantaneous generation mix [fuelType=OCGT] generation: value=56, delta=0, z=3.99 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=NPSHYD|generation` = **620** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3327** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=OCGT|generation` = **83** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=OTHER|generation` = **1132** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=PS|generation` = **325** (n=801, 2026-09-17T18:15:34.630577Z)
- `FUELINST|fuelType=WIND|generation` = **14899** (n=801, 2026-09-17T18:15:34.630577Z)
- `IMBALNGC|TOTAL|imbalance` = **9672** (n=132, 2026-09-17T17:53:48.152872Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=132, 2026-09-17T17:53:16.406856Z)
- `INDGEN|TOTAL|generation` = **26486** (n=132, 2026-09-17T17:53:16.406856Z)
- `MELNGC|TOTAL|margin` = **36603** (n=132, 2026-09-17T17:50:54.490629Z)
- `NDF|TOTAL|demand` = **16314** (n=136, 2026-09-17T18:18:46.937615Z)
- `TSDF|TOTAL|demand` = **16814** (n=136, 2026-09-17T18:18:46.937615Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:20:03.947582Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:20:02.936984Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:20:01.907341Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:20:00.907240Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:59.907166Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:58.907057Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:57.906953Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:56.906865Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:55.906743Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:54.906638Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:53.906554Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:52.906454Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:51.906352Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:50.572631Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:19:49.572515Z` — **MID**: 0 rows; marker `2026-09-17T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
