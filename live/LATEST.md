# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-18T18:25:03.887551Z`  
Current process started UTC: `2026-09-18T18:21:03.491337Z`  
1-second metadata polls in this process: **170**  
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

- `FUELINST|fuelType=INTVKL|generation` = **939** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=NPSHYD|generation` = **495** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=OCGT|generation` = **7** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=OTHER|generation` = **1684** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=PS|generation` = **513** (n=1067, 2026-09-18T18:20:38.302082Z)
- `FUELINST|fuelType=WIND|generation` = **16830** (n=1067, 2026-09-18T18:20:38.302082Z)
- `IMBALNGC|TOTAL|imbalance` = **9176** (n=176, 2026-09-18T18:24:19.444583Z)
- `INDDEM|TOTAL|demand` = **-10736** (n=176, 2026-09-18T18:24:03.813466Z)
- `INDGEN|TOTAL|generation` = **26226** (n=176, 2026-09-18T18:24:03.813466Z)
- `MELNGC|TOTAL|margin` = **37767** (n=176, 2026-09-18T18:21:20.209125Z)
- `NDF|TOTAL|demand` = **16550** (n=180, 2026-09-18T18:18:44.073570Z)
- `TSDF|TOTAL|demand` = **17050** (n=180, 2026-09-18T18:18:44.073570Z)
- `WINDFOR|TOTAL|generation` = **6802** (n=30, 2026-09-18T12:30:56.000926Z)

## Latest publication events

- `2026-09-18T18:25:02.578236Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:25:01.249395Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:59.919543Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:58.582776Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:57.231458Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:55.928541Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:54.599516Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:53.285999Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:51.561716Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:50.249665Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:48.914630Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:47.613919Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:46.271111Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:44.956574Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-18T18:24:43.640933Z` — **MID**: 0 rows; marker `2026-09-18T18:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
