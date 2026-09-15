# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-15T22:41:47.200887Z`  
Current process started UTC: `2026-09-15T22:37:46.973514Z`  
1-second metadata polls in this process: **237**  
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

- `FUELINST|fuelType=INTVKL|generation` = **354** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=NPSHYD|generation` = **435** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=OTHER|generation` = **299** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=PS|generation` = **-258** (n=309, 2026-09-15T22:40:41.901696Z)
- `FUELINST|fuelType=WIND|generation` = **11985** (n=309, 2026-09-15T22:40:41.901696Z)
- `IMBALNGC|TOTAL|imbalance` = **5815** (n=51, 2026-09-15T22:21:16.013291Z)
- `INDDEM|TOTAL|demand` = **-11915** (n=51, 2026-09-15T22:21:16.013291Z)
- `INDGEN|TOTAL|generation` = **24936** (n=51, 2026-09-15T22:21:16.013291Z)
- `MELNGC|TOTAL|margin` = **35753** (n=51, 2026-09-15T22:19:15.823893Z)
- `NDF|TOTAL|demand` = **18621** (n=52, 2026-09-15T22:17:24.476756Z)
- `TSDF|TOTAL|demand` = **19121** (n=52, 2026-09-15T22:17:24.476756Z)
- `WINDFOR|TOTAL|generation` = **17679** (n=8, 2026-09-15T19:30:46.768983Z)

## Latest publication events

- `2026-09-15T22:40:41.901696Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:40:00Z`
- `2026-09-15T22:40:26.374694Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:39:45Z`
- `2026-09-15T22:38:19.030678Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:37:45Z`
- `2026-09-15T22:37:21.721468Z` — **MID**: 0 rows; marker `2026-09-15T22:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 404: Resource Not Found
- `2026-09-15T22:36:17.840998Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:35:45Z`
- `2026-09-15T22:35:29.393030Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:35:00Z`
- `2026-09-15T22:34:25.203665Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:33:45Z`
- `2026-09-15T22:32:17.286491Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:31:45Z`
- `2026-09-15T22:30:41.379623Z` — **FUELHH**: 20 rows; marker `2026-09-15T22:30:00Z`
- `2026-09-15T22:30:41.379623Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:30:00Z`
- `2026-09-15T22:30:25.588814Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:29:45Z`
- `2026-09-15T22:28:10.516846Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:27:45Z`
- `2026-09-15T22:26:18.765715Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:25:45Z`
- `2026-09-15T22:25:30.505784Z` — **FUELINST**: 80 rows; marker `2026-09-15T22:25:00Z`
- `2026-09-15T22:24:11.115350Z` — **FREQ**: 5761 rows; marker `2026-09-15T22:23:45Z`
