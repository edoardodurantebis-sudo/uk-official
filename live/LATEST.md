# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T02:55:09.061108Z`  
Current process started UTC: `2026-09-20T02:51:08.955699Z`  
1-second metadata polls in this process: **231**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-5.29 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-5.35 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.40 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-5.46 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.90 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-5.53 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.58 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-5.65 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.71 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-5.78 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-5.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-6.39 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-5.93 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-6.00 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=1, z=-6.08 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **329** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=NPSHYD|generation` = **308** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3329** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=OTHER|generation` = **366** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=PS|generation` = **-695** (n=1436, 2026-09-20T02:50:40.289420Z)
- `FUELINST|fuelType=WIND|generation` = **15437** (n=1436, 2026-09-20T02:50:40.289420Z)
- `IMBALNGC|TOTAL|imbalance` = **-3749** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDDEM|TOTAL|demand` = **-12278** (n=237, 2026-09-20T02:51:25.319509Z)
- `INDGEN|TOTAL|generation` = **16203** (n=237, 2026-09-20T02:51:25.319509Z)
- `MELNGC|TOTAL|margin` = **37607** (n=237, 2026-09-20T02:49:53.425892Z)
- `NDF|TOTAL|demand` = **19452** (n=242, 2026-09-20T02:47:28.862306Z)
- `TSDF|TOTAL|demand` = **19952** (n=242, 2026-09-20T02:47:28.862306Z)
- `WINDFOR|TOTAL|generation` = **6511** (n=40, 2026-09-19T23:30:42.413783Z)

## Latest publication events

- `2026-09-20T02:55:08.109653Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:07.109534Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:06.109452Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:05.109331Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:04.109210Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:03.109086Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:02.108976Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:01.108862Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:55:00.108762Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:54:59.108650Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:54:57.920648Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:54:56.920526Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:54:55.920423Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:54:54.920308Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T02:54:53.920187Z` — **MID**: 0 rows; marker `2026-09-20T02:42:03Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
