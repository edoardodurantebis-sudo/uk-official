# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-17T18:11:41.795727Z`  
Current process started UTC: `2026-09-17T18:07:41.041702Z`  
1-second metadata polls in this process: **234**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELHH** `fuelType=OCGT` `generation` — half-hour generation mix [fuelType=OCGT] generation: value=56, delta=14, z=4.61 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1422** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=NPSHYD|generation` = **617** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3328** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=OCGT|generation` = **84** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=OTHER|generation` = **1263** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=PS|generation` = **331** (n=800, 2026-09-17T18:10:38.229294Z)
- `FUELINST|fuelType=WIND|generation` = **15019** (n=800, 2026-09-17T18:10:38.229294Z)
- `IMBALNGC|TOTAL|imbalance` = **9672** (n=132, 2026-09-17T17:53:48.152872Z)
- `INDDEM|TOTAL|demand` = **-11283** (n=132, 2026-09-17T17:53:16.406856Z)
- `INDGEN|TOTAL|generation` = **26486** (n=132, 2026-09-17T17:53:16.406856Z)
- `MELNGC|TOTAL|margin` = **36603** (n=132, 2026-09-17T17:50:54.490629Z)
- `NDF|TOTAL|demand` = **16314** (n=135, 2026-09-17T17:48:35.747451Z)
- `TSDF|TOTAL|demand` = **16814** (n=135, 2026-09-17T17:48:35.747451Z)
- `WINDFOR|TOTAL|generation` = **18904** (n=23, 2026-09-17T16:30:48.573176Z)

## Latest publication events

- `2026-09-17T18:11:40.837955Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:39.837847Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:38.837769Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:37.837653Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:36.837574Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:35.837443Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:34.823548Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:33.823434Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:32.823321Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:31.823208Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:30.823095Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:29.822982Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:28.822867Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:27.822753Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-17T18:11:26.519467Z` — **MID**: 0 rows; marker `2026-09-17T18:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
