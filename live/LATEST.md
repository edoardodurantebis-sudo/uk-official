# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-19T10:29:47.180022Z`  
Current process started UTC: `2026-09-19T10:25:46.874769Z`  
1-second metadata polls in this process: **148**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=NPSHYD|generation` = **301** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=OCGT|generation` = **0** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=OTHER|generation` = **388** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=PS|generation` = **-693** (n=1239, 2026-09-19T10:25:46.874777Z)
- `FUELINST|fuelType=WIND|generation` = **15814** (n=1239, 2026-09-19T10:25:46.874777Z)
- `IMBALNGC|TOTAL|imbalance` = **7134** (n=204, 2026-09-19T10:19:28.234788Z)
- `INDDEM|TOTAL|demand` = **-13222** (n=204, 2026-09-19T10:19:28.234788Z)
- `INDGEN|TOTAL|generation` = **26065** (n=204, 2026-09-19T10:19:28.234788Z)
- `MELNGC|TOTAL|margin` = **36510** (n=204, 2026-09-19T10:18:55.427991Z)
- `NDF|TOTAL|demand` = **15940** (n=209, 2026-09-19T10:16:50.751867Z)
- `TSDF|TOTAL|demand` = **18932** (n=209, 2026-09-19T10:16:50.751867Z)
- `WINDFOR|TOTAL|generation` = **6987** (n=35, 2026-09-19T08:30:39.402179Z)

## Latest publication events

- `2026-09-19T10:29:45.652218Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:44.139151Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:42.618851Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:41.096981Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:39.590708Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:38.072296Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:36.548648Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:35.021537Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:33.480316Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:31.515535Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:29.989912Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:28.149131Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:26.632473Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:25.109776Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-19T10:29:23.587299Z` — **MID**: 0 rows; marker `2026-09-19T10:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
