# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T11:18:52.909713Z`  
Current process started UTC: `2026-09-20T11:14:51.241088Z`  
1-second metadata polls in this process: **160**  
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

- `FUELINST|fuelType=INTVKL|generation` = **0** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=NPSHYD|generation` = **287** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3331** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=OTHER|generation` = **481** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=PS|generation` = **-665** (n=1537, 2026-09-20T11:15:25.700283Z)
- `FUELINST|fuelType=WIND|generation` = **13378** (n=1537, 2026-09-20T11:15:25.700283Z)
- `IMBALNGC|TOTAL|imbalance` = **-5746** (n=252, 2026-09-20T10:54:42.018205Z)
- `INDDEM|TOTAL|demand` = **-11813** (n=252, 2026-09-20T10:54:26.628199Z)
- `INDGEN|TOTAL|generation` = **15358** (n=252, 2026-09-20T10:54:42.018205Z)
- `MELNGC|TOTAL|margin` = **35793** (n=252, 2026-09-20T10:51:04.511192Z)
- `NDF|TOTAL|demand` = **20604** (n=259, 2026-09-20T11:18:08.138348Z)
- `TSDF|TOTAL|demand` = **21104** (n=259, 2026-09-20T11:18:41.045360Z)
- `WINDFOR|TOTAL|generation` = **2360** (n=44, 2026-09-20T10:30:44.491768Z)

## Latest publication events

- `2026-09-20T11:18:51.173839Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:49.707462Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:48.157220Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:46.749733Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:45.317696Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:43.845104Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:41.045360Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:41.045360Z` — **TSDF**: 1458 rows; marker `2026-09-20T11:17:00Z`
- `2026-09-20T11:18:39.562457Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:38.144554Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:36.730523Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:35.299317Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:33.831215Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:32.115870Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T11:18:30.658625Z` — **MID**: 0 rows; marker `2026-09-20T11:12:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
