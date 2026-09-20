# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:40:27.668450Z`  
Current process started UTC: `2026-09-20T06:36:26.635147Z`  
1-second metadata polls in this process: **158**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.72 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-988, delta=26, z=-3.87 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=0, z=-3.74 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-986, delta=1, z=-3.76 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.79 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=0, z=-3.81 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-987, delta=2, z=-3.83 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-989, delta=24, z=-3.85 -> generation-mix component moved
- **FUELHH** `fuelType=INTNED` `generation` — half-hour generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.13 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.01 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.03 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=2, z=-4.05 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1016, delta=-2, z=-4.08 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=1, z=-4.10 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=NPSHYD|generation` = **334** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3332** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=OTHER|generation` = **677** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=PS|generation` = **-804** (n=1481, 2026-09-20T06:35:45.177551Z)
- `FUELINST|fuelType=WIND|generation` = **15909** (n=1481, 2026-09-20T06:35:45.177551Z)
- `IMBALNGC|TOTAL|imbalance` = **-6854** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDDEM|TOTAL|demand` = **-12306** (n=244, 2026-09-20T06:21:02.514900Z)
- `INDGEN|TOTAL|generation` = **13098** (n=244, 2026-09-20T06:21:02.514900Z)
- `MELNGC|TOTAL|margin` = **37476** (n=244, 2026-09-20T06:19:41.611361Z)
- `NDF|TOTAL|demand` = **19452** (n=249, 2026-09-20T06:17:25.387697Z)
- `TSDF|TOTAL|demand` = **19952** (n=249, 2026-09-20T06:17:42.365986Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:40:26.228008Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:24.745246Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:23.325520Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:21.841634Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:20.385148Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:18.895475Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:16.073044Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:16.073044Z` — **FREQ**: 5761 rows; marker `2026-09-20T06:39:45Z`
- `2026-09-20T06:40:14.616129Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:13.155852Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:11.690237Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:10.243987Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:08.807213Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:07.336211Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:40:05.892607Z` — **MID**: 0 rows; marker `2026-09-20T06:35:00Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
