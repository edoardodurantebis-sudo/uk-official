# GB Alien — live control room

Engine: `GB_ALIEN_CONTINUOUS_V1.1.0`  
Last heartbeat UTC: `2026-09-20T06:53:07.701722Z`  
Current process started UTC: `2026-09-20T06:49:06.621327Z`  
1-second metadata polls in this process: **134**  
HTTP/data errors in this process: **0**  

The one-second loop is event-driven: a statistical observation is added only when
the provider publishes a new marker. Categorical series are kept separate and
identifiers such as settlementPeriod are excluded from signal statistics.

## Watched Elexon feeds

`FREQ`, `FUELINST`, `FUELHH`, `WINDFOR`, `NDF`, `TSDF`, `IMBALNGC`, `INDDEM`, `INDGEN`, `MELNGC`, `LOLPDRM`, `MID`

## Latest statistically unusual observations

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
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1013, delta=2, z=-3.98 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1015, delta=-1, z=-4.01 -> generation-mix component moved
- **FUELINST** `fuelType=INTNED` `generation` — instantaneous generation mix [fuelType=INTNED] generation: value=-1014, delta=0, z=-4.03 -> generation-mix component moved

## Latest market values

- `FUELINST|fuelType=INTVKL|generation` = **1248** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=NPSHYD|generation` = **342** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=NUCLEAR|generation` = **3333** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=OCGT|generation` = **50** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=OIL|generation` = **0** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=OTHER|generation` = **732** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=PS|generation` = **-802** (n=1484, 2026-09-20T06:50:25.602645Z)
- `FUELINST|fuelType=WIND|generation` = **15826** (n=1484, 2026-09-20T06:50:25.602645Z)
- `IMBALNGC|TOTAL|imbalance` = **-6802** (n=245, 2026-09-20T06:51:13.366134Z)
- `INDDEM|TOTAL|demand` = **-12302** (n=245, 2026-09-20T06:50:57.374716Z)
- `INDGEN|TOTAL|generation` = **13150** (n=245, 2026-09-20T06:50:57.374716Z)
- `MELNGC|TOTAL|margin` = **37681** (n=245, 2026-09-20T06:49:53.401212Z)
- `NDF|TOTAL|demand` = **19452** (n=250, 2026-09-20T06:47:34.462781Z)
- `TSDF|TOTAL|demand` = **19952** (n=250, 2026-09-20T06:47:34.462781Z)
- `WINDFOR|TOTAL|generation` = **2654** (n=42, 2026-09-20T05:30:57.629113Z)

## Latest publication events

- `2026-09-20T06:53:05.763789Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:53:04.043346Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:53:02.357259Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:53:00.662286Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:58.982102Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:57.300931Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:55.612528Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:53.923356Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:52.255148Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:50.243484Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:48.537902Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:46.848143Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:45.146481Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:43.458983Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
- `2026-09-20T06:52:41.752204Z` — **MID**: 0 rows; marker `2026-09-20T06:42:04Z`; ERROR=RuntimeError: MID: HTTP Error 400: Bad Request
