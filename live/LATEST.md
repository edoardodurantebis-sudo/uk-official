# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T10:11:42.852742Z`  
Current process started UTC: `2026-09-20T10:07:40.688113Z`  
1-second metadata polls in this process: **134**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=NPSHYD|generation` = **273** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3338** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=OTHER|generation` = **494** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=PS|generation` = **-474** (n=1524, 2026-09-20T10:10:36.275844Z)
- `FUELINST|fuelType=WIND|generation` = **14041** (n=1524, 2026-09-20T10:10:36.275844Z)
- `IMBALNGC|TOTAL|imbalance` = **-4154** (n=250, 2026-09-20T09:49:58.854824Z)
- `INDDEM|TOTAL|demand` = **-12359** (n=250, 2026-09-20T09:49:41.948249Z)
- `INDGEN|TOTAL|generation` = **16012** (n=250, 2026-09-20T09:49:41.948249Z)
- `MELNGC|TOTAL|margin` = **39288** (n=250, 2026-09-20T09:49:14.645349Z)
- `NDF|TOTAL|demand` = **19666** (n=256, 2026-09-20T09:47:20.517011Z)
- `TSDF|TOTAL|demand` = **20166** (n=256, 2026-09-20T09:47:20.517011Z)
- `WINDFOR|TOTAL|generation` = **2453** (n=43, 2026-09-20T08:30:44.975647Z)

## Latest publication events

- `2026-09-20T10:11:40.012828Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:38.303830Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:36.589228Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:34.886328Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:33.179585Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:31.428561Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:29.732790Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:28.003635Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:26.304060Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:24.164123Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:22.470073Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:20.764278Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:19.057910Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:17.173014Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T10:11:15.479395Z` — **MID**: 0 rows; marker `2026-09-20T10:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
