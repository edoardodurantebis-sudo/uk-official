# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:57:55.937309Z`  
Current process started UTC: `2026-09-20T10:53:54.965441Z`  
1-second metadata polls in this process: **178**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=NPSHYD|generation` = **270** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=OTHER|generation` = **598** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=PS|generation` = **-890** (n=1533, 2026-09-20T10:55:30.340668Z)
- `FUELINST|fuelType=WIND|generation` = **13757** (n=1533, 2026-09-20T10:55:30.340668Z)
- `IMBALNGC|TOTAL|imbalance` = **-5746** (n=252, 2026-09-20T10:54:42.018205Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=252, 2026-09-20T10:54:26.628199Z)
- `INDGEN|TOTAL|generation` = **15358** (n=252, 2026-09-20T10:54:42.018205Z)
- `MELNGC|TOTAL|margin` = **35793** (n=252, 2026-09-20T10:51:04.511192Z)
- `NDF|TOTAL|demand` = **20604** (n=258, 2026-09-20T10:48:26.920343Z)
- `TSDF|TOTAL|demand` = **21104** (n=258, 2026-09-20T10:48:42.282443Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T10:57:54.652352Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:53.031898Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:51.760383Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:50.445934Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:49.162966Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:47.860496Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:46.553647Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:45.244589Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:43.916730Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:42.653260Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:41.368768Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:40.090892Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:38.841573Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:37.270318Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:57:35.982735Z` — **MID**: 0 rows; marker `2026-09-20T10:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
