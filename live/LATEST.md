# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T07:35:11.630014Z`  
Current process started UTC: `2026-09-20T07:31:09.615022Z`  
1-second metadata polls in this process: **137**  
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

- `FUELINST|fuelType=INTVKL|generation` = **1262** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=NPSHYD|generation` = **350** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3339** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=OTHER|generation` = **382** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=PS|generation` = **-841** (n=1492, 2026-09-20T07:30:39.318079Z)
- `FUELINST|fuelType=WIND|generation` = **15657** (n=1492, 2026-09-20T07:30:39.318079Z)
- `IMBALNGC|TOTAL|imbalance` = **-6364** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDDEM|TOTAL|demand` = **-12307** (n=246, 2026-09-20T07:20:39.619957Z)
- `INDGEN|TOTAL|generation` = **13588** (n=246, 2026-09-20T07:20:39.619957Z)
- `MELNGC|TOTAL|margin` = **38029** (n=246, 2026-09-20T07:19:35.864933Z)
- `NDF|TOTAL|demand` = **19452** (n=251, 2026-09-20T07:17:28.599471Z)
- `TSDF|TOTAL|demand` = **19952** (n=251, 2026-09-20T07:17:28.599471Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T07:35:09.610416Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:35:07.940002Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:35:06.210308Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:35:04.514182Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:35:02.817927Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:35:01.159880Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:59.441654Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:57.762235Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:56.091916Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:54.071767Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:52.410647Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:50.711921Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:49.032546Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:47.360978Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T07:34:45.694005Z` — **MID**: 0 rows; marker `2026-09-20T07:12:02Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
