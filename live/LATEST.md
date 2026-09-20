# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T05:49:39.840811Z`  
Current process started UTC: `2026-09-20T05:45:39.386689Z`  
1-second metadata polls in this process: **141**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=2, z=-4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-4.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-4.10 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=-1, z=-4.15 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.17 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.20 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-2, z=-4.23 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.25 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.46 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.28 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=0, z=-4.31 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-4.34 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.38 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **716** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=NPSHYD|generation` = **296** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3335** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=OTHER|generation` = **466** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=PS|generation` = **-812** (n=1471, 2026-09-20T05:45:40.984181Z)
- `FUELINST|fuelType=WIND|generation` = **15581** (n=1471, 2026-09-20T05:45:40.984181Z)
- `IMBALNGC|TOTAL|imbalance` = **-6811** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDDEM|TOTAL|demand` = **-12319** (n=242, 2026-09-20T05:20:37.923780Z)
- `INDGEN|TOTAL|generation` = **13141** (n=242, 2026-09-20T05:20:37.923780Z)
- `MELNGC|TOTAL|margin` = **37465** (n=243, 2026-09-20T05:49:29.338975Z)
- `NDF|TOTAL|demand` = **19452** (n=248, 2026-09-20T05:47:19.313557Z)
- `TSDF|TOTAL|demand` = **19952** (n=248, 2026-09-20T05:47:19.313557Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T05:49:38.300752Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:36.770349Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:35.236533Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:33.682055Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:32.092795Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:29.338975Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:29.338975Z` — **MELNGC**: 792 rows; marker `2026-09-20T05:46:00Z`
- `2026-09-20T05:49:27.760238Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:26.118229Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:24.580674Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:23.028400Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:21.484845Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:19.944159Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:18.407237Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T05:49:16.799298Z` — **MID**: 0 rows; marker `2026-09-20T05:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
