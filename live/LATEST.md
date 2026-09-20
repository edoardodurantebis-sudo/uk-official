# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T11:10:29.819780Z`  
Current process started UTC: `2026-09-20T11:06:29.390870Z`  
1-second metadata polls in this process: **229**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=NPSHYD|generation` = **285** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=OTHER|generation` = **402** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=PS|generation` = **-674** (n=1536, 2026-09-20T11:10:23.022441Z)
- `FUELINST|fuelType=WIND|generation` = **13515** (n=1536, 2026-09-20T11:10:23.022441Z)
- `IMBALNGC|TOTAL|imbalance` = **-5746** (n=252, 2026-09-20T10:54:42.018205Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=252, 2026-09-20T10:54:26.628199Z)
- `INDGEN|TOTAL|generation` = **15358** (n=252, 2026-09-20T10:54:42.018205Z)
- `MELNGC|TOTAL|margin` = **35793** (n=252, 2026-09-20T10:51:04.511192Z)
- `NDF|TOTAL|demand` = **20604** (n=258, 2026-09-20T10:48:26.920343Z)
- `TSDF|TOTAL|demand` = **21104** (n=258, 2026-09-20T10:48:42.282443Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T11:10:28.807264Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:27.797738Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:26.769379Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:25.737600Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:24.732842Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:23.022441Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:23.022441Z` — **FUELINST**: 80 rows; marker `2026-09-20T11:10:00Z`
- `2026-09-20T11:10:22.016408Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:20.999456Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:19.989916Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:18.981873Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:17.944412Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:16.929986Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:15.890734Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:10:14.859604Z` — **MID**: 0 rows; marker `2026-09-20T11:05:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
