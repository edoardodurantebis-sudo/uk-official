# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T12:38:40.896605Z`  
Current process started UTC: `2026-09-20T12:34:40.000002Z`  
1-second metadata polls in this process: **163**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-986, delta=2, z=-3.75 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-983, delta=3, z=-3.62 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.67 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.69 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=-1, z=-3.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=NPSHYD|generation` = **263** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=OTHER|generation` = **486** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=PS|generation` = **-670** (n=1553, 2026-09-20T12:35:32.725803Z)
- `FUELINST|fuelType=WIND|generation` = **12230** (n=1553, 2026-09-20T12:35:32.725803Z)
- `IMBALNGC|TOTAL|imbalance` = **-5720** (n=255, 2026-09-20T12:23:23.217722Z)
- `INDDEM|TOTAL|demand` = **-11815** (n=255, 2026-09-20T12:23:23.217722Z)
- `INDGEN|TOTAL|generation` = **15384** (n=255, 2026-09-20T12:23:23.217722Z)
- `MELNGC|TOTAL|margin` = **35780** (n=255, 2026-09-20T12:20:29.957281Z)
- `NDF|TOTAL|demand` = **20604** (n=261, 2026-09-20T12:18:20.759778Z)
- `TSDF|TOTAL|demand` = **21104** (n=261, 2026-09-20T12:18:20.759778Z)
- `WINDFOR|TOTAL|generation` = **2287** (n=45, 2026-09-20T12:30:29.016530Z)

## Latest publication events

- `2026-09-20T12:38:39.466593Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:38.017570Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:36.598209Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:35.185664Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:33.732844Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:32.320124Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:30.880255Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:29.456918Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:27.733385Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:26.262700Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:24.846975Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:23.421433Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:22.015828Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:20.563814Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T12:38:19.124062Z` — **MID**: 0 rows; marker `2026-09-20T12:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
